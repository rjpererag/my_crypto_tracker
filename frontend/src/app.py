import streamlit as st
from .components import Dashboard, SideBar


def app():

    dashboard_settings = {
        "host": "http://localhost:5001",
        "ticker": "BTCUSDT",
        "time_interval": "2880 minutes",
        "refresh_rate": 10,
    }

    st.set_page_config(
        page_title=f"Real-Time Dashboard",
        layout="wide",
    )

    st.title(f"Real-Time Price Dashboard")

    sidebar = SideBar()

    dashboard = Dashboard(settings=dashboard_settings)
    dashboard.show_price_history_chart()
    # dashboard.stream_price_history_chart()
