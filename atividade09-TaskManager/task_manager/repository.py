class TaskRepository:
    """
    Responsável por salvar e recuperar Tasks usando um storage.
    O storage é injetado no construtor (injeção de dependência),
    o que facilita substituí-lo por um mock nos testes.
    """

    def __init__(self, storage):
        self.storage = storage
        self._next_id = 1  # contador de IDs automático

    def save(self, task):
        """
        Atribui um ID único à tarefa e a salva no storage.
        Retorna a task já com o ID preenchido.
        """
        task.id = self._next_id
        self._next_id += 1
        self.storage.add(task.id, task)
        return task

    def find_by_id(self, id):
        """Busca e retorna uma task pelo ID, ou None se não encontrar."""
        return self.storage.get(id)

    def find_all(self):
        """Retorna todas as tasks salvas."""
        return self.storage.get_all()

    def delete(self, id):
        """Remove a task com aquele ID. Retorna True/False."""
        return self.storage.delete(id)