import sys
import unittest
from unittest.mock import MagicMock

from src.calculadora import Calculadora


class TestEntradaSaida(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock()
        self.calc = Calculadora(self.repo)

    def test_soma_retorna_valor_correto(self):
        self.assertEqual(self.calc.somar(5, 3), 8)

    def test_soma_atualiza_ultimo_resultado(self):
        self.calc.somar(5, 3)
        self.assertEqual(self.calc.obter_ultimo_resultado(), 8)

    def test_subtracao_retorna_valor_correto(self):
        self.assertEqual(self.calc.subtrair(10, 4), 6)

    def test_subtracao_com_resultado_negativo(self):
        self.assertEqual(self.calc.subtrair(4, 10), -6)

    def test_multiplicacao_retorna_valor_correto(self):
        self.assertEqual(self.calc.multiplicar(6, 7), 42)

    def test_multiplicacao_por_zero(self):
        self.assertEqual(self.calc.multiplicar(8, 0), 0)

    def test_divisao_retorna_valor_correto(self):
        self.assertEqual(self.calc.dividir(10, 2), 5.0)

    def test_divisao_resultado_decimal(self):
        self.assertEqual(self.calc.dividir(5, 2), 2.5)

    def test_potencia_retorna_valor_correto(self):
        self.assertEqual(self.calc.potencia(2, 3), 8)

    def test_potencia_com_expoente_zero(self):
        self.assertEqual(self.calc.potencia(5, 0), 1)


class TestTipagem(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock()
        self.calc = Calculadora(self.repo)

    def test_somar_rejeita_string(self):
        with self.assertRaises(TypeError):
            self.calc.somar("5", 3)

    def test_subtrair_rejeita_none(self):
        with self.assertRaises(TypeError):
            self.calc.subtrair(None, 3)

    def test_multiplicar_rejeita_lista(self):
        with self.assertRaises(TypeError):
            self.calc.multiplicar([2], 3)

    def test_dividir_rejeita_string(self):
        with self.assertRaises(TypeError):
            self.calc.dividir(10, "2")

    def test_potencia_rejeita_dicionario(self):
        with self.assertRaises(TypeError):
            self.calc.potencia({}, 2)

    def test_bool_e_aceito_por_ser_subclasse_de_int(self):
        resultado = self.calc.somar(True, 2)
        self.assertEqual(resultado, 3)


class TestLimites(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock()
        self.calc = Calculadora(self.repo)

    def test_limite_zero(self):
        self.assertEqual(self.calc.somar(0, 5), 5)

    def test_limite_float_pequeno(self):
        self.assertAlmostEqual(self.calc.multiplicar(-1e-10, 2), -2e-10)

    def test_limite_float_grande(self):
        grande = sys.float_info.max / 2
        resultado = self.calc.somar(grande, grande)
        self.assertFalse(resultado == float("inf"))

    def test_divisor_muito_pequeno_proximo_de_zero(self):
        resultado = self.calc.dividir(1, 1e-10)
        self.assertAlmostEqual(resultado, 10000000000.0)

    def test_potencia_expoente_negativo(self):
        resultado = self.calc.potencia(2, -2)
        self.assertEqual(resultado, 0.25)

    def test_potencia_expoente_fracionario(self):
        resultado = self.calc.potencia(9, 0.5)
        self.assertEqual(resultado, 3.0)


class TestValoresForaDoIntervalo(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock()
        self.calc = Calculadora(self.repo)

    def test_divisao_por_zero_levanta_excecao(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)


class TestMensagensDeErro(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock()
        self.calc = Calculadora(self.repo)

    def test_mensagem_divisao_por_zero(self):
        with self.assertRaisesRegex(ValueError, "Divisao por zero"):
            self.calc.dividir(5, 0)

    def test_mensagem_tipo_invalido(self):
        with self.assertRaisesRegex(TypeError, "Argumentos devem ser numeros"):
            self.calc.somar("x", 1)


class TestFluxosDeControle(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock()
        self.calc = Calculadora(self.repo)

    def test_caminho_divisao_normal(self):
        self.assertEqual(self.calc.dividir(10, 2), 5.0)

    def test_caminho_divisao_erro(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

    def test_caminho_tipo_valido_salva_no_repositorio(self):
        self.calc.somar(1, 2)
        self.repo.salvar.assert_called_once_with("1 + 2 = 3")

    def test_caminho_tipo_invalido_nao_salva_no_repositorio(self):
        with self.assertRaises(TypeError):
            self.calc.somar("1", 2)

        self.repo.salvar.assert_not_called()


if __name__ == "__main__":
    unittest.main()