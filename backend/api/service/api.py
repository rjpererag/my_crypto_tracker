from flask import Flask,jsonify
from .utils.db_connection import *
from .utils.queries import *
from .utils.formatters import *

from typing import Callable

app = Flask(__name__)

def _get(query: str,
         formatter: Callable,
         *args):

    db_creds = build_db_creds()
    db_conn = get_db_connection(db_creds)

    try:
        with db_conn.cursor() as cursor:
            cursor.execute(query, args)
            results = cursor.fetchall()
            results_formatted = formatter(results=results)

            response = {"data": results_formatted}

            cursor.close()
            db_conn.close()

            return jsonify(response), 200

    except Exception as e:
        return {"error": str(e)}, 500


@app.route('/symbols', methods=['GET'])
def get_symbols():
    return _get(
        get_symbols_(),
        format_get_symbols_response,
    )

@app.route('/exchanges', methods=['GET'])
def get_exchanges():
    return _get(
        get_exchanges_(),
        format_get_exchanges_response,
    )

@app.route('/tickers/<string:symbol_name>/<string:exchange_name>', methods=['GET'])
def get_tickers(symbol_name: str, exchange_name: str):
    return _get(
        get_tickers_(),
        format_get_tickers_response,
        symbol_name,
        exchange_name,
    )

@app.route('/price-history-minutes/<string:minutes>/<string:ticker>', methods=['GET'])
def get_price_history_minutes(minutes: str, ticker: str):
    return _get(
        get_price_history(),
        format_price_history,
        minutes,
        ticker,
        10
    )




