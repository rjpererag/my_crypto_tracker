import pandas as pd
import streamlit as st
from decouple import config
from requests.exceptions import *
from time import sleep
import altair as alt


from ..utils.fetch_data import DataFetcher


class Dashboard:

    def __init__(self, settings: dict):
        self.settings = settings

        self.fetcher = DataFetcher(host=config('API_HOST'))

    @staticmethod
    def _format_price_history_df(price_history_df: pd.DataFrame) -> pd.DataFrame:
        price_history_df['date'] = pd.to_datetime(price_history_df['date'])
        price_history_df.set_index('date', inplace=False)
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


    def create_price_history_chart(self,
                                   price_history_df: pd.DataFrame,
                                   placeholder,
                                   **kwargs):

        subheader_ ="Price Evolution"
        if kwargs.get("symbol"):
            subheader_ += f" {kwargs['symbol']}"

        if not price_history_df.empty:
            with placeholder.container():
                st.subheader(subheader_)

                # --- The Altair Chart Code ---
                chart = alt.Chart(price_history_df).mark_line().encode(
                    x=alt.X('date', title='Timestamp', axis=alt.Axis(grid=True)),
                    y=alt.Y('price', title=self.settings["ticker"], axis=alt.Axis(grid=True)),
                    tooltip=['date', 'price']
                ).interactive()

                st.altair_chart(chart, use_container_width=True)
                # --- End of Altair Chart Code ---

                # st.line_chart(price_history_df['price'])
                # st.write(price_history_df.tail(1))
        else:
            with placeholder.container():
                st.warning("No data available for the specified parameters.")

    def show_price_history_chart(self, placeholder = None, **kwargs):
        try:
            if not placeholder:
                placeholder = st.empty()

            price_history_df = self._get_price_history_df()
            self.create_price_history_chart(price_history_df=price_history_df,
                                            placeholder=placeholder,
                                            symbol=kwargs.get("symbol")
                                            )

        except RequestException:
            st.warning("Could not fetch price history data.")

        except Exception as e:
            st.warning(f"Other error. {str(e)}")


    def stream_price_history_chart(self):
        chart_placeholder = st.empty()
        while True:
            self.show_price_history_chart(
                placeholder=chart_placeholder,
                symbol=self.settings["symbol"],
            )

            sleep(self.settings['refresh_rate'])
