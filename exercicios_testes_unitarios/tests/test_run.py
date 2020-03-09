from unittest import TestCase
from unittest.mock import Mock, patch,call
from exercicios_testes_unitarios.run import consulta_api_viacep, ApiCep


class TestMock_run(TestCase):

    @patch('exercicios_testes_unitarios.run.print')
    @patch('exercicios_testes_unitarios.run.input')
    def test_consulta_api_viacep(self, mock_input, mock_print):
        mock_input.return_value = '89070550'
        mock_print.return_value = {'cep': '89070-550', 'logradouro': 'Rua Ângelo Bressanini',
                                   'complemento': '', 'bairro': 'Salto do Norte', 'localidade': 'Blumenau',
                                   'uf': 'SC', 'unidade': '', 'ibge': '4202404', 'gia': ''}
        consulta = consulta_api_viacep()
        mock_input.assert_called_once_with('Informe o cep para consulta: ')
        self.assertEqual(consulta, 'Cep consultado com sucesso!')



        mock_print.assert_called_once_with({'cep': '89070-550', 'logradouro': 'Rua Ângelo Bressanini',
                                   'complemento': '', 'bairro': 'Salto do Norte', 'localidade': 'Blumenau',
                                   'uf': 'SC', 'unidade': '', 'ibge': '4202404', 'gia': ''})

        self.assertEqual(consulta,'Cep consultado com sucesso!')

    @patch('exercicios_testes_unitarios.app.api_cep.ApiCep.execute')
    def test_ApiCep_execute(self,mock_execute):
        cep = '89070-550'

        cep_end = {'cep': '89070-550', 'logradouro': 'Rua Ângelo Bressanini',
         'complemento': '', 'bairro': 'Salto do Norte', 'localidade': 'Blumenau',
         'uf': 'SC', 'unidade': '', 'ibge': '4202404', 'gia': ''}

        mock_execute.return_value = cep_end
        novo_execute = ApiCep.execute(cep)
        mock_execute.assert_called_once_with(cep)
        self.assertEqual(novo_execute,cep_end)
