from flask import Flask,jsonify
from .utils.db_connection import *
from .utils.queries import *
from .utils.formatters import *


app = Flask(__name__)


@app.route('/symbols', methods=['GET'])
def get_symbols():
    db_creds = build_db_creds()
    db_conn = get_db_connection(db_creds)

    try:
        with db_conn.cursor() as cursor:
            query = get_symbols_()
            cursor.execute(query=query)
            results = cursor.fetchall()
            results_formatted = format_get_symbols_response(results=results)

            response = {"data": results_formatted}

            cursor.close()
            db_conn.close()

            return jsonify(response), 200

    except Exception as e:
        return {"error": str(e)}, 500

@app.route('/exchanges', methods=['GET'])
def get_exchanges():
    db_creds = build_db_creds()
    db_conn = get_db_connection(db_creds)

    try:
        with db_conn.cursor() as cursor:
            query = get_exchanges_()
            cursor.execute(query=query)
            results = cursor.fetchall()

            results_formatted = format_get_exchanges_response(results=results)
            response = {"data": results_formatted}

            cursor.close()
            db_conn.close()

            return jsonify(response), 200

    except Exception as e:
        return {"error": str(e)}, 500


@app.route('/tickers/<string:symbol_name>/<string:exchange_name>', methods=['GET'])
def get_tickers(symbol_name: str, exchange_name: str):
    db_creds = build_db_creds()
    db_conn = get_db_connection(db_creds)

    try:
        with db_conn.cursor() as cursor:
            query = get_tickers_()
            cursor.execute(query, (symbol_name, exchange_name))
            results = cursor.fetchall()

            results_formatted = format_get_tickers_response(results=results)
            response = {"data": results_formatted}

            cursor.close()
            db_conn.close()

            return jsonify(response), 200

    except Exception as e:
        return {"error": str(e)}, 500





