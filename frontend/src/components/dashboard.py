import pandas as pd
import streamlit as st
from requests.exceptions import *
from time import sleep

from ..utils.fetch_data import DataFetcher


class Dashboard:

    def __init__(self, settings: dict):
        self.settings = settings

        self.fetcher = DataFetcher(host=self.settings["host"])

    @staticmethod
    def _format_price_history_df(price_history_df: pd.DataFrame) -> pd.DataFrame:
        price_history_df['date'] = pd.to_datetime(price_history_df['date'])
        price_history_df.set_index('date', inplace=True)
        return price_history_df

    def _get_price_history_df(self) -> pd.DataFrame:
        price_history = self.fetcher.fetch_price_history(
            ticker=self.settings["ticker"],
            time_interval=self.settings["time_interval"],
        )

        if price_history:
            price_history_df = pd.DataFrame(price_history, columns=['date', 'price', 'ticker'])
            price_history_df_formatted = self._format_price_history_df(price_history_df)

            return price_history_df_formatted

        return pd.DataFrame()

    @staticmethod
    def create_price_history_chart(price_history_df: pd.DataFrame, placeholder):

        if not price_history_df.empty:
            with placeholder.container():
                st.subheader(f"Price Evolution")
                st.line_chart(price_history_df['price'])
                st.write(price_history_df.tail(1))
        else:
            with placeholder.container():
                st.warning("No data available for the specified parameters.")

    def show_price_history_chart(self, placeholder = None):
        try:
            if not placeholder:
                placeholder = st.empty()

            price_history_df = self._get_price_history_df()
            self.create_price_history_chart(price_history_df=price_history_df,
                                            placeholder=placeholder
                                            )

        except RequestException:
            st.warning("Could not fetch price history data.")

        except Exception as e:
            st.warning(f"Other error. {str(e)}")


    def stream_price_history_chart(self):
        chart_placeholder = st.empty()
        while True:
            self.show_price_history_chart(placeholder=chart_placeholder)
            sleep(self.settings['refresh_rate'])
