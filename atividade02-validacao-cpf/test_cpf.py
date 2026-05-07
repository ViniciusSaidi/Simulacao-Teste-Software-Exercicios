import pytest
from cpf import validar_cpf, formatar_cpf


def test_validar_cpf_valido_padrao():
    # Arrange
    cpf = "52998224725"

    # Act
    resultado = validar_cpf(cpf)

    # Assert
    assert resultado is True


def test_validar_cpf_valido_com_formatacao():
    # Arrange
    cpf = "529.982.247-25"

    # Act
    resultado = validar_cpf(cpf)

    # Assert
    assert resultado is True


@pytest.mark.parametrize("cpf", [
    "52998224725",
    "16899535009",
    "11144477735",
])
def test_validar_multiplos_cpfs_validos(cpf):
    # Arrange

    # Act
    resultado = validar_cpf(cpf)

    # Assert
    assert resultado is True


@pytest.mark.parametrize("cpf", [
    "52998224724",
    "11111111111",
    "123456789",
    "123456789012",
    "abc12345678",
    "",
    None,
])
def test_validar_multiplos_cpfs_invalidos(cpf):
    # Arrange

    # Act
    resultado = validar_cpf(cpf)

    # Assert
    assert resultado is False


def test_cpf_invalido_digitos_verificadores_errados():
    # Arrange
    cpf = "52998224724"

    # Act
    resultado = validar_cpf(cpf)

    # Assert
    assert resultado is False


def test_cpf_com_todos_digitos_iguais_invalido():
    # Arrange
    cpf = "11111111111"

    # Act
    resultado = validar_cpf(cpf)

    # Assert
    assert resultado is False


def test_cpf_com_menos_de_11_digitos_invalido():
    # Arrange
    cpf = "123456789"

    # Act
    resultado = validar_cpf(cpf)

    # Assert
    assert resultado is False


def test_cpf_com_mais_de_11_digitos_invalido():
    # Arrange
    cpf = "123456789012"

    # Act
    resultado = validar_cpf(cpf)

    # Assert
    assert resultado is False


def test_cpf_com_letras_invalido():
    # Arrange
    cpf = "abc12345678"

    # Act
    resultado = validar_cpf(cpf)

    # Assert
    assert resultado is False


def test_formatar_cpf_valido():
    # Arrange
    cpf = "52998224725"

    # Act
    resultado = formatar_cpf(cpf)

    # Assert
    assert resultado == "529.982.247-25"


def test_formatar_cpf_invalido_levanta_excecao():
    # Arrange
    cpf = "12345678900"

    # Act / Assert
    with pytest.raises(ValueError):
        formatar_cpf(cpf)


def test_cpf_none_invalido():
    # Arrange
    cpf = None

    # Act
    resultado = validar_cpf(cpf)

    # Assert
    assert resultado is False