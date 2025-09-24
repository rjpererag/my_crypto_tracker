from src.dashboard import Dashboard


if __name__ == "__main__":
    dashboard_settings = {
        "host": "http://localhost:5001",
        "ticker": "BTCUSDT",
        "time_interval": "2880 minutes",
        "refresh_rate": 60,
    }


    dashboard = Dashboard(settings=dashboard_settings)
    chart = dashboard.create_chart()