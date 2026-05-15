# 🌐 Testes de API REST - JSONPlaceholder

## 📖 Descrição

Este projeto implementa uma suíte de testes automatizados para a API pública **JSONPlaceholder**, utilizando Python com as bibliotecas **requests**, **pytest** e **jsonschema**.

O objetivo é validar o comportamento da API por meio de testes de sistema, cobrindo cenários como requisições HTTP, validação de dados, operações CRUD, uso de fixtures e verificação de tempo de resposta.

---

## 🔗 API utilizada

* Nome: JSONPlaceholder
* URL: https://jsonplaceholder.typicode.com/
* Documentação: https://jsonplaceholder.typicode.com/guide/

---

## 🤔 Justificativa da escolha

A API JSONPlaceholder foi escolhida por ser pública, estável e amplamente utilizada para testes de aplicações REST.
Ela permite realizar operações CRUD completas, atendendo aos requisitos da atividade sem necessidade de autenticação.

---

## ⚙️ Como instalar

Instale as dependências com:

```bash
pip install -r requirements.txt
```

---

## 🧪 Como executar

Execute os testes com:

```bash
pytest -v
```

---

## 📁 Estrutura do projeto

```bash
atividade08-testes-api-rest/
│
├── test_api.py        # Suíte de testes com pytest
└── README.md
```

---

## 🧪 Testes implementados

A suíte de testes cobre os seguintes cenários:

* ✅ GET em coleção → status 200 e lista não vazia
* ✅ GET em recurso existente → validação de schema com jsonschema
* ✅ GET em recurso inexistente → status 404
* ✅ POST criando recurso → status 201 e retorno com ID
* ✅ PATCH atualizando recurso → campo alterado corretamente
* ✅ DELETE de recurso → status 200 ou 204
* ✅ Envio de dados inválidos → retorno de erro (4xx)
* ✅ Simulação de autenticação → requisições com e sem credencial
* ✅ Uso de fixture → criação e reutilização de recurso
* ✅ Tempo de resposta → inferior a 2 segundos

---

## 📌 Observações

* A API utilizada não possui autenticação real, portanto o teste foi simulado para fins de validação do comportamento esperado.
* Os testes foram desenvolvidos sem uso de ferramentas gráficas, conforme exigido pela atividade.
* Não foi utilizado `time.sleep()`, sendo priorizadas boas práticas de testes automatizados.
