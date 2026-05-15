import pytest

from sistema_notas import (
    validar_nota,
    calcular_media,
    obter_situacao,
    calcular_estatisticas,
    normalizar_notas
)


class TestValidarNota:

    def test_nota_valida_inteira(self):
        assert validar_nota(0) is True
        assert validar_nota(5) is True
        assert validar_nota(10) is True

    def test_nota_valida_decimal(self):
        assert validar_nota(7.5) is True
        assert validar_nota(9.9) is True

    def test_nota_invalida_negativa(self):
        assert validar_nota(-1) is False

    def test_nota_invalida_acima_de_dez(self):
        assert validar_nota(11) is False

    def test_nota_invalida_texto(self):
        assert validar_nota("dez") is False


class TestCalcularMedia:

    def test_calcular_media_notas_validas(self):
        notas = [7, 8, 9]
        assert calcular_media(notas) == pytest.approx(8.0)

    def test_calcular_media_com_notas_invalidas(self):
        notas = [7, 8, 11, -1]
        assert calcular_media(notas) == pytest.approx(7.5)

    def test_calcular_media_com_decimais(self):
        notas = [7.5, 8.5, 9.0]
        assert calcular_media(notas) == pytest.approx(8.333333, rel=1e-5)

    def test_calcular_media_lista_vazia(self):
        with pytest.raises(ValueError):
            calcular_media([])

    def test_calcular_media_sem_notas_validas(self):
        with pytest.raises(ValueError):
            calcular_media([-1, 11, 20])


class TestObterSituacao:

    def test_situacao_aprovado(self):
        assert obter_situacao(7.0) == "Aprovado"
        assert obter_situacao(10.0) == "Aprovado"

    def test_situacao_recuperacao(self):
        assert obter_situacao(5.0) == "Recuperação"
        assert obter_situacao(6.9) == "Recuperação"

    def test_situacao_reprovado(self):
        assert obter_situacao(0.0) == "Reprovado"
        assert obter_situacao(4.9) == "Reprovado"

    def test_situacao_media_invalida_negativa(self):
        with pytest.raises(ValueError):
            obter_situacao(-1)

    def test_situacao_media_invalida_acima_de_dez(self):
        with pytest.raises(ValueError):
            obter_situacao(11)


class TestCalcularEstatisticas:

    def test_calcular_estatisticas_basico(self):
        notas = [3, 5, 7, 9]

        resultado = calcular_estatisticas(notas)

        assert resultado["media"] == pytest.approx(6.0)
        assert resultado["maior"] == 9
        assert resultado["menor"] == 3
        assert resultado["aprovados"] == 2
        assert resultado["recuperacao"] == 1
        assert resultado["reprovados"] == 1

    def test_calcular_estatisticas_ignora_invalidas(self):
        notas = [4, 6, 8, 11, -2]

        resultado = calcular_estatisticas(notas)

        assert resultado["media"] == pytest.approx(6.0)
        assert resultado["maior"] == 8
        assert resultado["menor"] == 4
        assert resultado["aprovados"] == 1
        assert resultado["recuperacao"] == 1
        assert resultado["reprovados"] == 1

    def test_calcular_estatisticas_todos_aprovados(self):
        notas = [7, 8, 9, 10]

        resultado = calcular_estatisticas(notas)

        assert resultado["aprovados"] == 4
        assert resultado["recuperacao"] == 0
        assert resultado["reprovados"] == 0

    def test_calcular_estatisticas_lista_vazia(self):
        with pytest.raises(ValueError):
            calcular_estatisticas([])

    def test_calcular_estatisticas_sem_notas_validas(self):
        with pytest.raises(ValueError):
            calcular_estatisticas([-5, 15, 20])


class TestNormalizarNotas:

    def test_normalizar_notas_escala_vinte(self):
        notas = [10, 20]
        assert normalizar_notas(notas, 20) == [5.0, 10.0]

    def test_normalizar_notas_escala_cem(self):
        notas = [50, 75, 100]
        assert normalizar_notas(notas, 100) == [5.0, 7.5, 10.0]

    def test_normalizar_notas_escala_dez(self):
        notas = [5, 7, 10]
        assert normalizar_notas(notas) == [5.0, 7.0, 10.0]

    def test_normalizar_notas_lista_vazia(self):
        assert normalizar_notas([], 20) == []

    def test_normalizar_notas_maxima_invalida_zero(self):
        with pytest.raises(ValueError):
            normalizar_notas([10, 20], 0)

    def test_normalizar_notas_maxima_invalida_negativa(self):
        with pytest.raises(ValueError):
            normalizar_notas([10, 20], -10)