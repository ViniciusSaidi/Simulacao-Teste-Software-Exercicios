# 🧮 Calculadora com Histórico - Testes de Unidade e Integração

## 📖 Descrição

Este projeto implementa uma calculadora com persistência de histórico, juntamente com uma suíte completa de testes automatizados utilizando **unittest**.

O objetivo da atividade é aplicar na prática:

* Testes de unidade
* Testes de integração
* Uso de test doubles (stub e mock)
* Identificação e correção de defeitos
* Medição de cobertura de testes

---

## 🎯 Objetivo

Garantir o correto funcionamento da calculadora e validar a interação com o repositório de histórico, assegurando qualidade e confiabilidade do sistema.

---

## ⚙️ Como instalar

Instale as dependências com:

```bash
pip install -r requirements.txt
```

---

## 🧪 Como executar os testes

Execute todos os testes com:

```bash
python -m unittest discover tests -v
```

---

## 📊 Cobertura de testes

Execute:

```bash
python -m coverage run -m unittest discover tests
python -m coverage report -m
```

Para gerar relatório visual:

```bash
python -m coverage html
```

---

## 📁 Estrutura do projeto

```bash
atividade06-calculadora-historico/
│
├── src/
│   ├── calculadora.py      # Implementação da calculadora (bug corrigido)
│   └── repositorio.py      # Repositório de histórico
│
├── tests/
│   ├── test_unidade.py     # Testes de unidade
│   ├── test_integracao.py  # Testes de integração
│   └── test_doubles.py     # Testes com stub e mock
│
├── requirements.txt
├── README.md
└── relatorio.md
```

---

## 🧪 Tipos de testes implementados

### 🔹 Testes de Unidade

* Validação de operações matemáticas
* Testes de tipagem
* Testes de limites
* Testes de exceções
* Testes de fluxos de controle

### 🔹 Testes de Integração

* Execução de operações encadeadas
* Consistência do histórico
* Interação entre calculadora e repositório

### 🔹 Test Doubles

* **Stub**: simulação do repositório para isolar testes
* **Mock**: verificação de chamadas e argumentos

---

## 🐛 Bug corrigido

Foi identificado um defeito no método de potência:

* ❌ Registro incorreto: utilizava operador `*`
* ✅ Correção: uso correto do operador `**`

---

## 📌 Observações

* O projeto atingiu **100% de cobertura em calculadora.py**
* Os testes foram desenvolvidos seguindo boas práticas de isolamento e verificação de comportamento
* O uso de mocks permitiu detectar o bug de forma precisa
