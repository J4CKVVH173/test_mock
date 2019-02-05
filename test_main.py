import pytest
from . import mmm
from . import culc

from unittest.mock import patch, Mock


@pytest.fixture(scope='module')
def lol():
    kek = 10

    yield kek


def test_kek(lol):
    with patch.object(culc, 'sum') as mock_sum:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.lol = 'lol'
        mock_response.o = dict(o='o', a=123)
        mock_response.A = culc.Test('13333')
        print(mock_response.A.get_a())
        mock_sum.return_value = 100
        print(mmm.test())
    print('end')

