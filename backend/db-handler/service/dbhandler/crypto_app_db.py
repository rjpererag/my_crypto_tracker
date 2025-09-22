from datetime import datetime

from .handler import DBHandler
from .settings import DBCredentials


class CryptoAppDBHandler(DBHandler):

    def __init__(self, creds: DBCredentials, **kwargs) -> None:
        super().__init__(creds=creds)
        self.available_exchanges = kwargs.get('available_exchanges', [])
        self.cache_data = self._create_cache_data()

        self._handle_cache_data()


    def _create_cache_data(self) -> dict:
        return {'auxiliary_tables': {'status': 'INVALID',
                                     'tables': {'tickers': {},
                                                'exchange': {},
                                                'symbols': {}
                                                }
                                     },
                'exchange_tickers': {exchange: {} for exchange in self.available_exchanges},
                }

    @staticmethod
    def _get_auxiliary_table(table_name: str) -> tuple[dict, list]:

        table = {}
        if table_name == 'tickers':
            table = {
                "id": None,
                "symbols_id": None,
                "exchange_id": None,
                "ticker": None
            }

        elif table_name == 'exchange':
            table = {
                "id": None,
                "name": None,
                "country": None
            }

        elif table_name == 'symbols':
            table = {
                "id": None,
                "name": None,
                "symbol": None
            }

        return table, list(table.keys())

    def _map_auxiliary_table(self, table_name: str, records: list[tuple]) -> list:
        if records:
            table_schema, table_keys = self._get_auxiliary_table(table_name=table_name)
            table_records = [dict(zip(table_keys, record)) for record in records]
            return table_records
        return []

    def _handle_auxiliary_tables(self):

        if self.cache_data.get('auxiliary_tables', {}).get('status') == 'INVALID':
            auxiliary_tables = self.cache_data.get('auxiliary_tables', {}).get('tables', {})
            for table_name, mapping in auxiliary_tables.items():
                query = f"SELECT * FROM {table_name}"
                records = self.select(query)
                mapped_records = self._map_auxiliary_table(table_name=table_name, records=records)

                self.cache_data['auxiliary_tables']['tables'][table_name] = mapped_records

            self.cache_data['auxiliary_tables']['status'] = 'VALID'

    def _handle_exchange_tickers(self):

        for exchange in self.available_exchanges:
            query = f"""
            SELECT t.ticker, t.id
            FROM tickers t 
            JOIN exchange e on e.id = t.exchange_id
            WHERE e."name" = '{exchange}';
            """

            records = self.select(query)
            self.cache_data['exchange_tickers'][exchange] = {record[0] : record[1] for record in records}

    def _handle_cache_data(self):
        self._handle_auxiliary_tables()
        self._handle_exchange_tickers()
    
    def insert_price(self, price_data: dict):
        self._handle_cache_data()
        query = f"""
            INSERT INTO prices (ticker_id, price, timestamp)
            VALUES (%s, %s, %s)
            """

        params = (
            self.cache_data['exchange_tickers'][price_data['exchange_name']][price_data['ticker']],
            price_data["price"],
            datetime.strptime(price_data["timestamp"], '%Y%m%d%H%M%S')
        )

        self.execute_query(query=query, params=params)

    def process_message(self, msg: dict):
        ...
