class Estoque:
    def __init__(self):
        self._produtos = {}

    def adicionar_produto(self, nome: str, quantidade: int):
        if quantidade <= 0:
            raise ValueError(f"Quantidade deve ser positiva. Recebido: {quantidade}")

        if nome in self._produtos:
            self._produtos[nome] += quantidade
        else:
            self._produtos[nome] = quantidade

    def consultar_quantidade(self, nome: str) -> int:
        return self._produtos.get(nome, 0)

    def remover_produto(self, nome: str, quantidade: int):
        if quantidade <= 0:
            raise ValueError(f"Quantidade deve ser positiva. Recebido: {quantidade}")

        if nome not in self._produtos:
            raise ValueError(f"Produto '{nome}' não encontrado no estoque.")

        if quantidade > self._produtos[nome]:
            raise ValueError(
                f"Estoque insuficiente para '{nome}'. "
                f"Disponível: {self._produtos[nome]}, solicitado: {quantidade}"
            )

        self._produtos[nome] -= quantidade

    def listar_produtos(self) -> list:
        return [nome for nome, qtd in self._produtos.items() if qtd > 0]

    def produto_mais_estocado(self):
        produtos_ativos = {nome: qtd for nome, qtd in self._produtos.items() if qtd > 0}

        if not produtos_ativos:
            return None

        return max(produtos_ativos, key=produtos_ativos.get)