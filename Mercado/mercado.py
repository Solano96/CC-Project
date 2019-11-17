import yfinance as yf
import pandas as pd
import json

class Mercado:

    @classmethod
    def get_data(cls, symbol, start, end, rounding=True):
        """
        Get finance data from symbol
        :param symbol: company symbol in yahoo finance
        :return: data in json format
        """
        df = yf.download(symbol, start=start, end=end, rounding=rounding)
        df.index = df.index.strftime('%Y-%m-%d')
        return json.loads(df.to_json(orient='index',date_format='iso'))

    @classmethod
    def get_data_in_realtime(cls, symbol):
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
