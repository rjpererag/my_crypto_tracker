def format_get_symbols_response(results: list[tuple]) -> list[dict]:

    formatted_result = []
    if results:
        formatted_result = [
            {"coin": item[0],
             "symbol": item[1]}
            for item in results if isinstance(item, tuple) and len(item) == 2]

    return formatted_result


def format_get_exchanges_response(results: list[tuple]) -> list[dict]:

    formatted_result = []
    if results:
        formatted_result = [
            {"exchange": item[0],
             "country": item[1]}
            for item in results if isinstance(item, tuple) and len(item) == 2]

    return formatted_result

def format_get_tickers_response(results: list[tuple]) -> list[dict]:

    formatted_result = []
    if results:
        formatted_result = [
            {"ticker": item[0],
             "exchange": item[1],
             "coin": item[2]}
            for item in results if isinstance(item, tuple) and len(item) == 3]

    return formatted_result

def format_price_history(results: list[tuple]) -> list[dict]:
    formatted_result = []
    if results:
        formatted_result = [
            {"ticker": item[0],
             "price": item[1],
             "date": item[2]}
            for item in results if isinstance(item, tuple) and len(item) == 3]

    return formatted_result