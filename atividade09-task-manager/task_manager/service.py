from task_manager.task import Status


class TaskService:

    def __init__(self, repository):
        self.repository = repository

    def criar_tarefa(self, titulo, descricao, prioridade, prazo):
        from task_manager.task import Task
        task = Task(None, titulo, descricao, prioridade, prazo)
        task.validar()  # lança ValueError se inválida
        return self.repository.save(task)

    def listar_todas(self):
        return self.repository.find_all()

    def atualizar_status(self, id, novo_status):
        if not isinstance(novo_status, Status):
            raise ValueError(f"Status inválido: {novo_status}")

        task = self.repository.find_by_id(id)
        if task is None:
            raise ValueError(f"Task com id={id} não encontrada.")

        task.status = novo_status
        return task