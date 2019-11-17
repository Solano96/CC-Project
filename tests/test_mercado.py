import pytest
import sys
sys.path.append('Mercado')

from mercado import Mercado

def test_get_data_1():
    data = Mercado.get_data('AAPL', '2019-11-04', '2019-11-16')
    assert data['2019-11-04']['Open'] == 257.33
    assert data['2019-11-15']['Close'] == 265.76


def test_get_data_in_realtime():
    data = Mercado.get_data_in_realtime('GOOGL')
    assert data['_id'] == 'GOOGL'
    assert data['shortName'] == "Alphabet Inc."
    assert type(data['regularMarketOpen']) is float
