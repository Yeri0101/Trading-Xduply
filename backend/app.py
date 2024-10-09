
from flask import Flask, jsonify, request
from utils import get_klines_data  # Importa la función desde utils.py
import ccxt

app = Flask(__name__)

# Configuración de la API de Binance
exchange = ccxt.binance({
    'apiKey': 'OG0ewpBSOhKmmCIZy62Jrx4qxODxA3CC6wsSbblu0KdvRddmkeTONrcW4fwnXDGa',
    'secret': '5KuND8PhyDsyWe4XPibkmuglBY3n8k4pnLdDPIN9BfwKXoM7a9sOQV1ZA9BJJyTM'
})

@app.route('/api/klines')
def get_klines():
    """
    Obtiene los datos de klines (velas japonesas) de Binance.
    """
    symbol = request.args.get('symbol', 'BTCUSDT')  # Símbolo del par de trading (por defecto BTCUSDT)
    timeframe = request.args.get('timeframe', '15m')  # Intervalo de tiempo (por defecto 1 minuto)
    limit = int(request.args.get('limit', 300))  # Número de velas (por defecto 100)

    # Obtiene los datos de klines usando la función get_klines_data de utils.py
    klines = get_klines_data(exchange, symbol, timeframe, limit)
    return jsonify(klines)  # Devuelve los datos en formato JSON

@app.route('/api/drawings', methods=['POST'])
def save_drawing():
    """
    Guarda los datos del dibujo en un archivo o base de datos.
    """
    drawing_data = request.get_json()
    # ... (lógica para guardar drawing_data) ...
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
