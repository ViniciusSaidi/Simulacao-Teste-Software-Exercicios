from task_manager.task import Status


class TaskService:
    """
    Camada de serviço: orquestra as operações de negócio.
    Usa o repositório para persistir dados e aplica regras
    como validação antes de salvar.
    """

    def __init__(self, repository):
        self.repository = repository

    def criar_tarefa(self, titulo, descricao, prioridade, prazo):
        """
        Cria uma nova Task, valida e salva.
        Lança ValueError se a task for inválida.
        """
        from task_manager.task import Task
        task = Task(None, titulo, descricao, prioridade, prazo)
        task.validar()  # lança ValueError se inválida
        return self.repository.save(task)

    def listar_todas(self):
        """Retorna todas as tasks salvas."""
        return self.repository.find_all()

    def atualizar_status(self, id, novo_status):
        """
        Atualiza o status de uma task existente.
        Lança ValueError se o status for inválido ou a task não existir.
        """
        if not isinstance(novo_status, Status):
            raise ValueError(f"Status inválido: {novo_status}")

        task = self.repository.find_by_id(id)
        if task is None:
            raise ValueError(f"Task com id={id} não encontrada.")

        task.status = novo_status
        return task