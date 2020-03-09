from unittest.mock import Mock,patch,call
from unittest import TestCase
from exercicios_testes_unitarios.app.api_cep import ApiCep,_get_somente_numeros


class TestMock_api_cep(TestCase):

    @patch('exercicios_testes_unitarios.app.api_cep.re.sub')
    def test_get_somente_numeros(self, mock_sub):
        caracteres = '@33425%392036'
        mock_sub.return_value = '33425392036'

        resultado = _get_somente_numeros(caracteres)

        self.assertEqual(resultado,'33425392036')
        mock_sub.assert_called_once_with('[^0-9]', '', caracteres)

