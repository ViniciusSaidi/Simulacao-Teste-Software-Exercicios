"""
test_task.py — Testes UNITÁRIOS da classe Task

Testes unitários = testam UMA classe isolada, sem dependências externas.
Task não depende de nada externo, então não precisamos de mocks aqui.

Foco: estado dos atributos e ciclo de vida (transições de status).
"""
import pytest
from datetime import datetime, timedelta
from task_manager.task import Task, Priority, Status


# ──────────────────────────────────────────────
# FIXTURE: cria uma task válida reutilizável
# O pytest chama esta função antes de cada teste
# que pede 'task_valida' como parâmetro.
# ──────────────────────────────────────────────
@pytest.fixture
def task_valida():
    prazo = datetime.now() + timedelta(days=1)
    return Task(None, "Estudar", "Python", Priority.ALTA, prazo)


# ──────────────────────────────────────────────
# TESTE 1 — Estado inicial
# Verifica que todos os atributos foram atribuídos
# corretamente e que o status padrão é PENDENTE.
# ──────────────────────────────────────────────
def test_estado_inicial(task_valida):
    task_valida.validar()  # não deve lançar erro

    assert task_valida.titulo == "Estudar"
    assert task_valida.descricao == "Python"
    assert task_valida.prioridade == Priority.ALTA
    assert task_valida.id is None          # ainda sem ID
    assert task_valida.status == Status.PENDENTE  # padrão!


# ──────────────────────────────────────────────
# TESTE 2 — Título inválido (menos de 3 chars)
# pytest.raises verifica que a exceção foi lançada.
# ──────────────────────────────────────────────
def test_titulo_curto_invalido():
    prazo = datetime.now() + timedelta(days=1)
    task = Task(None, "AB", "Descrição", Priority.BAIXA, prazo)

    with pytest.raises(ValueError):
        task.validar()


# ──────────────────────────────────────────────
# TESTE 3 — Prazo no passado
# Qualquer data anterior a agora deve ser rejeitada.
# ──────────────────────────────────────────────
def test_prazo_no_passado_invalido():
    prazo_passado = datetime.now() - timedelta(days=1)
    task = Task(None, "Tarefa", "Descrição", Priority.MEDIA, prazo_passado)

    with pytest.raises(ValueError):
        task.validar()


# ──────────────────────────────────────────────
# TESTE 4 — Ciclo de vida: transição VÁLIDA
# Muda o status de PENDENTE para EM_PROGRESSO
# e verifica que o atributo mudou de fato.
# ──────────────────────────────────────────────
def test_ciclo_vida_transicao_valida(task_valida):
    assert task_valida.status == Status.PENDENTE  # estado inicial

    task_valida.status = Status.EM_PROGRESSO

    assert task_valida.status == Status.EM_PROGRESSO  # estado mudou!


# ──────────────────────────────────────────────
# TESTE 5 — Ciclo de vida: transição INVÁLIDA
# Tentar atribuir um valor que não pertence ao enum
# deve lançar ValueError.
# ──────────────────────────────────────────────
def test_ciclo_vida_status_invalido(task_valida):
    with pytest.raises(ValueError):
        task_valida.status = Status("valor_que_nao_existe")


# ──────────────────────────────────────────────
# TESTE 6 — Título com exatamente 3 chars (borda)
# Deve ser válido (limite mínimo aceito).
# ──────────────────────────────────────────────
def test_titulo_com_tres_caracteres_valido():
    prazo = datetime.now() + timedelta(days=1)
    task = Task(None, "ABC", "Descrição", Priority.BAIXA, prazo)

    task.validar()  # não deve lançar erro


# ──────────────────────────────────────────────
# TESTE 7 — Transição completa do ciclo de vida
# PENDENTE → EM_PROGRESSO → CONCLUIDA
# ──────────────────────────────────────────────
def test_ciclo_vida_completo(task_valida):
    assert task_valida.status == Status.PENDENTE

    task_valida.status = Status.EM_PROGRESSO
    assert task_valida.status == Status.EM_PROGRESSO

    task_valida.status = Status.CONCLUIDA
    assert task_valida.status == Status.CONCLUIDA