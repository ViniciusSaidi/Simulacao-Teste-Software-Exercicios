import pytest
from datetime import datetime, timedelta
from task_manager.task import Task, Priority, Status


@pytest.fixture
def task_valida():
    prazo = datetime.now() + timedelta(days=1)
    return Task(None, "Estudar", "Python", Priority.ALTA, prazo)


def test_estado_inicial(task_valida):
    task_valida.validar()

    assert task_valida.titulo == "Estudar"
    assert task_valida.descricao == "Python"
    assert task_valida.prioridade == Priority.ALTA
    assert task_valida.id is None
    assert task_valida.status == Status.PENDENTE


def test_titulo_curto_invalido():
    prazo = datetime.now() + timedelta(days=1)
    task = Task(None, "AB", "Descrição", Priority.BAIXA, prazo)

    with pytest.raises(ValueError):
        task.validar()


def test_prazo_no_passado_invalido():
    prazo_passado = datetime.now() - timedelta(days=1)
    task = Task(None, "Tarefa", "Descrição", Priority.MEDIA, prazo_passado)

    with pytest.raises(ValueError):
        task.validar()


def test_ciclo_vida_transicao_valida(task_valida):
    assert task_valida.status == Status.PENDENTE

    task_valida.status = Status.EM_PROGRESSO

    assert task_valida.status == Status.EM_PROGRESSO


def test_ciclo_vida_status_invalido(task_valida):
    with pytest.raises(ValueError):
        task_valida.status = Status("valor_que_nao_existe")


def test_titulo_com_tres_caracteres_valido():
    prazo = datetime.now() + timedelta(days=1)
    task = Task(None, "ABC", "Descrição", Priority.BAIXA, prazo)

    task.validar()


def test_ciclo_vida_completo(task_valida):
    assert task_valida.status == Status.PENDENTE

    task_valida.status = Status.EM_PROGRESSO
    assert task_valida.status == Status.EM_PROGRESSO

    task_valida.status = Status.CONCLUIDA
    assert task_valida.status == Status.CONCLUIDA