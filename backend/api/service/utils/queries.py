def get_symbols_() -> str:
    return """
    SELECT s."name", s.symbol 
    FROM symbols s
    ORDER BY s."name";
    """

def get_exchanges_() -> str:
    return """
    SELECT e."name", e.country 
    FROM exchange e
    ORDER BY e."name";
    """

def get_tickers_() -> str:
    return """
    SELECT t.ticker, e."name", s."name"
    FROM tickers t
    JOIN exchange e ON e.id = t.exchange_id 
    JOIN symbols s  ON s.id  = t.symbols_id
    WHERE s."name" = %s AND e."name" = %s
    ORDER BY s."name";
    """

def get_price_history() -> str:
    return """
    SELECT t.ticker, AVG(p.price) AS price, DATE_TRUNC('minute', MAX(p."timestamp")) as timestamp
    FROM prices p
    JOIN tickers t ON t.id = p.ticker_id
    WHERE p."timestamp" >= NOW() - INTERVAL '24 hours' AND t.ticker = 'BTCUSDT'
    GROUP by t.ticker, FLOOR(EXTRACT(EPOCH FROM p."timestamp") / (1*60))
    ORDER by timestamp DESC
    limit 100;
    """

