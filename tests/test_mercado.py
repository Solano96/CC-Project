import pytest
import sys
sys.path.append('src')

from Mercado.mercado import Mercado

def test_get_data_1():
    data = Mercado.get_data('AAPL', '2019-11-04', '2019-11-16')
    assert data['2019-11-04']['Open'] == 64.33
    assert data['2019-11-15']['Close'] == 66.44


def test_get_data_in_realtime():
    data = Mercado.get_realtime_data('GOOGL')
    assert data['shortName'] == "Alphabet Inc."
