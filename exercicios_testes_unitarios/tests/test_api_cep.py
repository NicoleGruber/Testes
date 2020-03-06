from unittest.mock import Mock,patch,call
from unittest import TestCase
from app.api_cep import ApiCep


class TestMock_api_cep(TestCase):

    @patch('app.api_cep.execute')
    def test_ApiCep_execute(self,mock_execute):
        mock_execute.return_value ={'cep': '89070-550', 'logradouro': 'Rua Ângelo Bressanini',
                                   'complemento': '', 'bairro': 'Salto do Norte', 'localidade': 'Blumenau',
                                   'uf': 'SC', 'unidade': '', 'ibge': '4202404', 'gia': ''}
        novo_mock = ApiCep.execute()


