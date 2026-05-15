import unittest
from unittest.mock import MagicMock

from src.calculadora import Calculadora


class TestComStub(unittest.TestCase):
    def setUp(self):
        self.stub_repo = MagicMock()
        self.calc = Calculadora(self.stub_repo)

    def test_soma_stub_repositorio(self):
        resultado = self.calc.somar(10, 5)

        self.assertEqual(resultado, 15)

    def test_stub_repositorio_nao_precisa_estar_pronto(self):
        self.stub_repo.total.return_value = 0

        resultado = self.calc.multiplicar(3, 7)

        self.assertEqual(resultado, 21)

    def test_stub_total_retorna_valor_controlado(self):
        self.stub_repo.total.return_value = 5

        total = self.stub_repo.total()

        self.assertEqual(total, 5)


class TestComMock(unittest.TestCase):
    def setUp(self):
        self.mock_repo = MagicMock()
        self.calc = Calculadora(self.mock_repo)

    def test_mock_salvar_chamado_apos_soma(self):
        self.calc.somar(4, 6)

        self.mock_repo.salvar.assert_called_once()

    def test_mock_salvar_chamado_com_argumento_correto_soma(self):
        self.calc.somar(4, 6)

        self.mock_repo.salvar.assert_called_once_with("4 + 6 = 10")

    def test_mock_salvar_chamado_com_argumento_correto_subtracao(self):
        self.calc.subtrair(10, 4)

        self.mock_repo.salvar.assert_called_once_with("10 - 4 = 6")

    def test_mock_salvar_chamado_com_argumento_correto_multiplicacao(self):
        self.calc.multiplicar(3, 5)

        self.mock_repo.salvar.assert_called_once_with("3 * 5 = 15")

    def test_mock_salvar_chamado_com_argumento_correto_divisao(self):
        self.calc.dividir(10, 2)

        self.mock_repo.salvar.assert_called_once_with("10 / 2 = 5.0")

    def test_mock_salvar_chamado_com_argumento_correto_potencia(self):
        self.calc.potencia(2, 3)

        self.mock_repo.salvar.assert_called_once_with("2 ** 3 = 8")

    def test_mock_salvar_nao_chamado_em_type_error(self):
        with self.assertRaises(TypeError):
            self.calc.somar("x", 1)

        self.mock_repo.salvar.assert_not_called()

    def test_mock_salvar_nao_chamado_em_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

        self.mock_repo.salvar.assert_not_called()


if __name__ == "__main__":
    unittest.main()