import streamlit as st
from .components import Dashboard, SideBar


def app():

    st.set_page_config(
        page_title=f"my-crypto-app",
        layout="wide",
    )

    (
        selected_symbol,
        selected_ticker,
        selected_refresh_rate
    ) = SideBar().create_sidebar()

    dashboard_settings = {
        "ticker": selected_ticker,
        "time_interval": "2880 minutes",
        "refresh_rate": selected_refresh_rate,
        "symbol": selected_symbol,
    }

    dashboard = Dashboard(settings=dashboard_settings)
    dashboard.stream_price_history_chart()

