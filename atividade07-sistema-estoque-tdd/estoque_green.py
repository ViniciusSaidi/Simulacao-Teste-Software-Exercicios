class Estoque:
    def __init__(self):
        self._produtos = {}

    def adicionar_produto(self, nome, quantidade):
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser positiva")
        if nome in self._produtos:
            self._produtos[nome] = self._produtos[nome] + quantidade
        else:
            self._produtos[nome] = quantidade

    def consultar_quantidade(self, nome):
        if nome in self._produtos:
            return self._produtos[nome]
        else:
            return 0

    def remover_produto(self, nome, quantidade):
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser positiva")

        if nome not in self._produtos:
            raise ValueError("Produto nao encontrado no estoque")

        if quantidade > self._produtos[nome]:
            raise ValueError("Estoque insuficiente")

        self._produtos[nome] = self._produtos[nome] - quantidade

    def listar_produtos(self):
        resultado = []
        for nome in self._produtos:
            if self._produtos[nome] > 0:
                resultado.append(nome)
        return resultado

    def produto_mais_estocado(self):
        if len(self._produtos) == 0:
            return None

        maior_nome = None
        maior_quantidade = -1
        for nome in self._produtos:
            if self._produtos[nome] > maior_quantidade:
                maior_quantidade = self._produtos[nome]
                maior_nome = nome

        if maior_quantidade == 0:
            return None

        return maior_nome