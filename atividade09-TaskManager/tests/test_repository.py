"""
test_repository.py — Testes de COMPONENTE do TaskRepository

Testes de componente = testam uma classe com sua lógica interna REAL,
mas substituem dependências externas por mocks.

Aqui: a lógica do TaskRepository é real, mas o InMemoryStorage
é substituído por um Mock (objeto falso controlado pelo teste).

Diferença entre STUB e MOCK usada aqui:
- STUB: só configura um valor de retorno (mock.get.return_value = task)
  → usado quando só precisamos que o storage "devolva algo"
- MOCK: verifica SE e COMO o método foi chamado (assert_called_once_with)
  → usado quando o comportamento importante é a chamada em si
"""
import pytest
from datetime import datetime, timedelta
from unittest.mock import Mock
from task_manager.task import Task, Priority, Status
from task_manager.repository import TaskRepository


# ──────────────────────────────────────────────
# FIXTURES
# ──────────────────────────────────────────────

@pytest.fixture
def mock_storage():
    """
    Cria um objeto Mock no lugar do InMemoryStorage real.
    O Mock aceita qualquer chamada de método sem reclamar
    e registra tudo que foi chamado.
    """
    return Mock()


@pytest.fixture
def repo(mock_storage):
    """Cria o repositório injetando o storage falso."""
    return TaskRepository(mock_storage)


@pytest.fixture
def task():
    """Cria uma task simples para usar nos testes."""
    prazo = datetime.now() + timedelta(days=1)
    return Task(None, "Teste", "Descrição", Priority.BAIXA, prazo)


# ──────────────────────────────────────────────
# TESTE 1 — Estado: save() atribui ID à task
# Verifica que o atributo task.id foi modificado.
# ──────────────────────────────────────────────
def test_save_atribui_id(repo, task):
    assert task.id is None  # antes: sem ID

    resultado = repo.save(task)

    assert resultado.id == 1  # depois: ID foi atribuído!


# ──────────────────────────────────────────────
# TESTE 2 — Mock: save() chama storage.add corretamente
# Verifica que o repositório delegou a chamada ao storage
# com os argumentos certos (id=1 e o objeto task).
# ──────────────────────────────────────────────
def test_save_chama_storage_add(repo, task, mock_storage):
    repo.save(task)

    # MOCK com assert: verifica SE foi chamado e COM O QUÊ
    mock_storage.add.assert_called_once_with(1, task)


# ──────────────────────────────────────────────
# TESTE 3 — Stub: find_by_id() delega ao storage
# Configura o mock para retornar a task quando get() for chamado.
# Verifica que o repositório repassa o resultado corretamente.
# ──────────────────────────────────────────────
def test_find_by_id_usa_storage(repo, task, mock_storage):
    mock_storage.get.return_value = task  # STUB: resposta fixa configurada

    resultado = repo.find_by_id(1)

    assert resultado == task  # repositório retornou o que o storage deu


# ──────────────────────────────────────────────
# TESTE 4 — Sequência: save() seguido de find_by_id()
# Testa a colaboração entre métodos:
# salvar e depois recuperar deve funcionar em sequência.
# ──────────────────────────────────────────────
def test_sequencia_save_e_find_by_id(repo, task, mock_storage):
    # Configura o stub para simular que o storage "guarda" e "devolve"
    mock_storage.get.return_value = task

    repo.save(task)
    encontrada = repo.find_by_id(task.id)

    assert encontrada == task
    mock_storage.add.assert_called_once()  # save chamou add
    mock_storage.get.assert_called_once_with(task.id)  # find chamou get


# ──────────────────────────────────────────────
# TESTE 5 — Isolamento: find_all() retorna lista vazia
# Quando o storage não tem itens, find_all() deve retornar [].
# ──────────────────────────────────────────────
def test_find_all_retorna_lista_vazia(repo, mock_storage):
    mock_storage.get_all.return_value = []  # stub: storage vazio

    resultado = repo.find_all()

    assert resultado == []


# ──────────────────────────────────────────────
# TESTE 6 — IDs incrementais: cada save() usa ID diferente
# Verifica que o contador _next_id funciona corretamente.
# ──────────────────────────────────────────────
def test_save_ids_incrementais(repo, mock_storage):
    prazo = datetime.now() + timedelta(days=1)
    task1 = Task(None, "Tarefa 1", "Desc", Priority.BAIXA, prazo)
    task2 = Task(None, "Tarefa 2", "Desc", Priority.ALTA, prazo)

    repo.save(task1)
    repo.save(task2)

    assert task1.id == 1
    assert task2.id == 2


# ──────────────────────────────────────────────
# TESTE 7 — delete() delega ao storage
# Verifica que o repositório chama storage.delete com o ID correto.
# ──────────────────────────────────────────────
def test_delete_chama_storage_delete(repo, mock_storage):
    mock_storage.delete.return_value = True  # stub

    resultado = repo.delete(1)

    mock_storage.delete.assert_called_once_with(1)  # mock com assert
    assert resultado is True