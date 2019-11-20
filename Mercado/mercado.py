import yfinance as yf
import pandas as pd
import json

class Mercado:

    @classmethod
    def get_data(cls, symbol, start, end, rounding=True):
        """
        Obtener datos financieros de un mercado
        :param symbol: símbolo del mercado en yahoo finance
        :param start: fecha inicial desde donde se empezarán a obtener datos
        .param end: fecha final hasta donde se obtendrán los datos
        :param rounding: True si se desea redondear las cifras numéricas
        :return: datos en formato JSON
        """
        df = yf.download(symbol, start=start, end=end, rounding=rounding)
        df.index = df.index.strftime('%Y-%m-%d')
        return json.loads(df.to_json(orient='index',date_format='iso'))

    @classmethod
    def get_data_in_realtime(cls, symbol):
        """
        Obtener información en tiempo real de un mercado
        :param symbol: símbolo del mercado en yahoo finance
        :return: datos en tiempo real en formato JSON
        """
        ticker = yf.Ticker(symbol)
        info = ticker.info
        key = {'_id': symbol}
        data = {
            '_id': symbol,
            'shortName': info['shortName'],
            'regularMarketOpen': info['regularMarketOpen'],
            'regularMarketDayHigh': info['regularMarketDayHigh'],
            'regularMarketDayLow': info['regularMarketDayLow'],
            'regularMarketVolume': info['regularMarketVolume'],
        }
        return data
