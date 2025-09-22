insert into exchange (name, country) values
	('binance', 'usa');

insert into symbols (name, symbol) values
    ('bitcoin', 'BTC'),
    ('ethereum', 'ETH');


INSERT INTO tickers (symbols_id, exchange_id, ticker)
VALUES
    (
        (SELECT s.id FROM symbols s WHERE s.name = 'bitcoin'),
        (SELECT e.id FROM exchange e WHERE e.name = 'binance'),
        'BTCUSD'
    ),
    (
        (SELECT s.id FROM symbols s WHERE s.name = 'ethereum'),
        (SELECT e.id FROM exchange e WHERE e.name = 'binance'),
        'BTCUSD'
    );
