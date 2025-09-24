import streamlit as st
from decouple import config

from ..utils.fetch_data import DataFetcher

class SideBar:

    def __init__(self,):
        self.fetcher = DataFetcher(host=config('API_HOST'))
        self.cache = {
            "exchanges": [],
            "symbols": [],
        }
        self._get_available_options()

    def _get_exchanges(self):
        exchanges = self.fetcher.fetch_exchanges()
        available_exchanges = [
            exchange.get('exchange').title()
            for exchange in exchanges
        ]

        self.cache['exchanges'] = available_exchanges

    def _get_symbols(self):
        symbols = self.fetcher.fetch_symbols()
        available_symbols = [
            symbol.get('coin').title()
            for symbol in symbols
        ]

        self.cache['symbols'] = available_symbols

    def _get_tickers(self, exchange, symbol) -> list:
        if exchange and symbol:
            tickers = self.fetcher.fetch_tickers(symbol=symbol, exchange=exchange)
            return [
                ticker.get("ticker").upper()
                for ticker in tickers
            ]
        return []

    def _get_available_options(self):
        self._get_exchanges()
        self._get_symbols()

    def create_sidebar(self):
        with st.sidebar:
            st.header("Settings")

            selected_exchange = st.selectbox(
                "Select Exchange",
                options=self.cache["exchanges"],
                help="Choose the exchange",
            )

            selected_symbol = st.selectbox(
                "Select Symbol",
                options=self.cache["symbols"],
                help="Choose the symbol",
            )

            available_tickers = self._get_tickers(exchange=selected_exchange,
                                                  symbol=selected_symbol)

            selected_ticker = st.selectbox(
                "Select Ticker",
                options=available_tickers,
                help="Choose the cryptocurrency ticker to display.",
            )

            selected_refresh_rate = st.slider(
                "Refresh Rate (seconds)",
                min_value=1,
                max_value=60,
                value=10,
                help="Set how often the data should refresh.",
            )

        return selected_symbol, selected_ticker, selected_refresh_rate