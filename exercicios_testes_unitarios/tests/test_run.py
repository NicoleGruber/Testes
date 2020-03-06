from unittest import TestCase
from unittest.mock import Mock, patch,call
from run import consulta_api_viacep


class TestMock_run(TestCase):

    @patch('run.print')
    @patch('run.input')
    def test_consulta_api_viacep(self, mock_input, mock_print):
        mock_input.return_value = '89070550'
        mock_print.return_value = {'cep': '89070-550', 'logradouro': 'Rua Ângelo Bressanini',
                                   'complemento': '', 'bairro': 'Salto do Norte', 'localidade': 'Blumenau',
                                   'uf': 'SC', 'unidade': '', 'ibge': '4202404', 'gia': ''}
        novo_input = consulta_api_viacep()
        mock_input.assert_called_once_with('Informe o cep para consulta: ')
        self.assertEqual(novo_input, 'Cep consultado com sucesso!')


        novo_print = consulta_api_viacep()
        mock_print.assert_has_calls([call({'cep': '89070-550', 'logradouro': 'Rua Ângelo Bressanini',
                                   'complemento': '', 'bairro': 'Salto do Norte', 'localidade': 'Blumenau',
                                   'uf': 'SC', 'unidade': '', 'ibge': '4202404', 'gia': ''})])
        self.assertEqual(novo_print,'Cep consultado com sucesso!')

        self.assertEqual(mock_input,mock_print)

