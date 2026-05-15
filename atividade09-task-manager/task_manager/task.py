from enum import Enum, IntEnum
from datetime import datetime


class Priority(IntEnum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3


class Status(Enum):
    PENDENTE = "pendente"
    EM_PROGRESSO = "em_progresso"
    CONCLUIDA = "concluida"


class Task:
    def __init__(self, id, titulo, descricao, prioridade, prazo, status=Status.PENDENTE):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.prazo = prazo
        self.status = status

    def validar(self):
        if len(self.titulo) < 3:
            raise ValueError(f"Título deve ter pelo menos 3 caracteres. Recebido: '{self.titulo}'")

        if self.prazo < datetime.now():
            raise ValueError(f"O prazo não pode ser uma data no passado. Recebido: {self.prazo}")

    def __repr__(self):
        return f"Task(id={self.id}, titulo='{self.titulo}', status={self.status.value})"