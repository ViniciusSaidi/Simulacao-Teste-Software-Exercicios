import pytest
#from estoque_red import Estoque
#from estoque_green import Estoque
#from estoque_refactor import Estoque
from estoque import Estoque

def test_adicionar_produto_novo():
    estoque = Estoque()
    estoque.adicionar_produto("Arroz", 10)
    assert estoque.consultar_quantidade("Arroz") == 10

def test_adicionar_produto_existente_incrementa():
    estoque = Estoque()
    estoque.adicionar_produto("Arroz", 10)
    estoque.adicionar_produto("Arroz", 5)
    assert estoque.consultar_quantidade("Arroz") == 15

def test_adicionar_quantidade_zero_levanta_erro():
    estoque = Estoque()
    with pytest.raises(ValueError):
        estoque.adicionar_produto("Arroz", 0)

def test_adicionar_quantidade_negativa_levanta_erro():
    estoque = Estoque()
    with pytest.raises(ValueError):
        estoque.adicionar_produto("Arroz", -5)


def test_consultar_produto_inexistente_retorna_zero():
    estoque = Estoque()
    assert estoque.consultar_quantidade("Feijão") == 0


def test_remover_produto_diminui_quantidade():
    estoque = Estoque()
    estoque.adicionar_produto("Macarrão", 20)
    estoque.remover_produto("Macarrão", 8)
    assert estoque.consultar_quantidade("Macarrão") == 12

def test_remover_mais_que_disponivel_levanta_erro():
    estoque = Estoque()
    estoque.adicionar_produto("Macarrão", 5)
    with pytest.raises(ValueError):
        estoque.remover_produto("Macarrão", 10)

def test_remover_quantidade_zero_levanta_erro():
    estoque = Estoque()
    estoque.adicionar_produto("Macarrão", 10)
    with pytest.raises(ValueError):
        estoque.remover_produto("Macarrão", 0)

def test_remover_produto_inexistente_levanta_erro():
    estoque = Estoque()
    with pytest.raises(ValueError):
        estoque.remover_produto("Feijão", 5)


def test_listar_produtos_retorna_com_quantidade_positiva():
    estoque = Estoque()
    estoque.adicionar_produto("Arroz", 10)
    estoque.adicionar_produto("Feijão", 5)
    produtos = estoque.listar_produtos()
    assert "Arroz" in produtos
    assert "Feijão" in produtos

def test_listar_produtos_nao_inclui_zerados():
    estoque = Estoque()
    estoque.adicionar_produto("Arroz", 5)
    estoque.remover_produto("Arroz", 5)
    produtos = estoque.listar_produtos()
    assert "Arroz" not in produtos

def test_listar_produtos_estoque_vazio_retorna_lista_vazia():
    estoque = Estoque()
    assert estoque.listar_produtos() == []


def test_produto_mais_estocado_retorna_nome_correto():
    estoque = Estoque()
    estoque.adicionar_produto("Arroz", 10)
    estoque.adicionar_produto("Feijão", 50)
    estoque.adicionar_produto("Macarrão", 25)
    assert estoque.produto_mais_estocado() == "Feijão"

def test_produto_mais_estocado_estoque_vazio_retorna_none():
    estoque = Estoque()
    assert estoque.produto_mais_estocado() is None