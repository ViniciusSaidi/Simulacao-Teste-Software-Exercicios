class InMemoryStorage:
    """
    Simula um banco de dados usando um dicionário Python em memória.
    Cada item é guardado com uma chave (o ID da tarefa).
    """

    def __init__(self):
        self._data = {}  # dicionário vazio no início

    def add(self, id, item):
        """Adiciona ou sobrescreve um item com a chave 'id'."""
        self._data[id] = item

    def get(self, id):
        """Retorna o item com aquele id, ou None se não existir."""
        return self._data.get(id)

    def get_all(self):
        """Retorna uma lista com todos os itens armazenados."""
        return list(self._data.values())

    def delete(self, id):
        """
        Remove o item com aquele id.
        Retorna True se removeu, False se não existia.
        """
        if id in self._data:
            del self._data[id]
            return True
        return False

    def clear(self):
        """Apaga todos os dados armazenados."""
        self._data = {}