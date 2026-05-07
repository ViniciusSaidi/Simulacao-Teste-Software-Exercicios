import requests
import pytest
import jsonschema

BASE_URL = "https://jsonplaceholder.typicode.com"

POST_SCHEMA = {
    "type": "object",
    "required": ["userId", "id", "title", "body"],
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"},
    },
}


@pytest.fixture
def novo_post():
    return {
        "title": "Post de teste",
        "body": "Conteúdo do post de teste",
        "userId": 1,
    }


@pytest.fixture
def post_criado(novo_post):
    response = requests.post(f"{BASE_URL}/posts", json=novo_post)

    assert response.status_code == 201

    post = response.json()

    yield post

    requests.delete(f"{BASE_URL}/posts/{post['id']}")


def test_get_colecao_status_200_lista_nao_vazia():
    response = requests.get(f"{BASE_URL}/posts")

    assert response.status_code == 200

    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) > 0


def test_get_recurso_existente_valida_schema():
    response = requests.get(f"{BASE_URL}/posts/1")

    assert response.status_code == 200

    data = response.json()
    jsonschema.validate(instance=data, schema=POST_SCHEMA)


def test_get_recurso_inexistente_status_404():
    response = requests.get(f"{BASE_URL}/posts/999999")

    assert response.status_code == 404


def test_post_criando_recurso_status_201_id_no_retorno(novo_post):
    response = requests.post(f"{BASE_URL}/posts", json=novo_post)

    assert response.status_code == 201

    data = response.json()
    assert "id" in data
    assert data["title"] == novo_post["title"]
    assert data["body"] == novo_post["body"]
    assert data["userId"] == novo_post["userId"]


def test_patch_atualizando_recurso_campo_alterado():
    payload = {"title": "Título atualizado"}

    response = requests.patch(f"{BASE_URL}/posts/1", json=payload)

    assert response.status_code == 200

    data = response.json()
    assert data["title"] == "Título atualizado"


def test_delete_recurso_status_200_ou_204():
    response = requests.delete(f"{BASE_URL}/posts/1")

    assert response.status_code in [200, 204]


def test_envio_dados_invalidos_endpoint_inexistente_status_4xx():
    payload = {"title": "", "body": "", "userId": "invalido"}

    response = requests.post(f"{BASE_URL}/posts-invalidos", json=payload)

    assert 400 <= response.status_code < 500


def test_endpoint_com_e_sem_credencial_simulado():
    response_sem_credencial = requests.get(f"{BASE_URL}/posts/1")

    headers = {"Authorization": "Bearer token_simulado"}
    response_com_credencial = requests.get(f"{BASE_URL}/posts/1", headers=headers)

    assert response_sem_credencial.status_code == 200
    assert response_com_credencial.status_code == 200


def test_criar_recurso_com_fixture(post_criado):
    assert "id" in post_criado
    assert post_criado["title"] == "Post de teste"
    assert post_criado["body"] == "Conteúdo do post de teste"


def test_tempo_resposta_menor_que_2_segundos():
    response = requests.get(f"{BASE_URL}/posts/1")

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2.0