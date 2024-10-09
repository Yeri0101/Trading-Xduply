import ccxt

def get_klines_data(exchange, symbol, timeframe, limit):
    """
    Obtiene los datos de klines de Binance y los formatea.
    """
    klines = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    # Formatea los datos para que sean compatibles con la librería de gráficos
    formatted_klines = [{
        'time': int(kline[0]),  # Timestamp en milisegundos
        'open': float(kline[1]),
        'high': float(kline[2]),
        'low': float(kline[3]),
        'close': float(kline[4]),
        'volume': float(kline[5])
    } for kline in klines]
    return

    formatted_klines
