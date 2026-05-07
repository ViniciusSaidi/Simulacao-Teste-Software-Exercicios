import pytest
from datetime import datetime, timedelta
from unittest.mock import Mock
from task_manager.task import Task, Priority, Status
from task_manager.repository import TaskRepository

@pytest.fixture
def mock_storage():
    return Mock()


@pytest.fixture
def repo(mock_storage):
    return TaskRepository(mock_storage)


@pytest.fixture
def task():
    prazo = datetime.now() + timedelta(days=1)
    return Task(None, "Teste", "Descrição", Priority.BAIXA, prazo)


def test_save_atribui_id(repo, task):
    assert task.id is None

    resultado = repo.save(task)

    assert resultado.id == 1


def test_save_chama_storage_add(repo, task, mock_storage):
    repo.save(task)
    mock_storage.add.assert_called_once_with(1, task)


def test_find_by_id_usa_storage(repo, task, mock_storage):
    mock_storage.get.return_value = task
    resultado = repo.find_by_id(1)
    assert resultado == task


def test_sequencia_save_e_find_by_id(repo, task, mock_storage):
    mock_storage.get.return_value = task

    repo.save(task)
    encontrada = repo.find_by_id(task.id)

    assert encontrada == task
    mock_storage.add.assert_called_once()  
    mock_storage.get.assert_called_once_with(task.id)


def test_find_all_retorna_lista_vazia(repo, mock_storage):
    mock_storage.get_all.return_value = []

    resultado = repo.find_all()

    assert resultado == []


def test_save_ids_incrementais(repo, mock_storage):
    prazo = datetime.now() + timedelta(days=1)
    task1 = Task(None, "Tarefa 1", "Desc", Priority.BAIXA, prazo)
    task2 = Task(None, "Tarefa 2", "Desc", Priority.ALTA, prazo)

    repo.save(task1)
    repo.save(task2)

    assert task1.id == 1
    assert task2.id == 2


def test_delete_chama_storage_delete(repo, mock_storage):
    mock_storage.delete.return_value = True

    resultado = repo.delete(1)

    mock_storage.delete.assert_called_once_with(1)
    assert resultado is True