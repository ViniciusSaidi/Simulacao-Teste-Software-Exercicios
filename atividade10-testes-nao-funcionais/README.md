# 🧪 Testes Não Funcionais - E-commerce Black Friday

## 📖 Descrição

Este projeto implementa um conjunto de testes não funcionais para um sistema de e-commerce, simulando o cenário de alta demanda da Black Friday.

Foram desenvolvidos testes em Python para avaliar diferentes aspectos de qualidade do sistema, incluindo desempenho, carga, estresse, escalabilidade e segurança.

---

## 🎯 Objetivo

Validar se o sistema atende aos requisitos de qualidade definidos para o evento de Black Friday, considerando:

* Alto volume de usuários simultâneos
* Baixo tempo de resposta
* Alta capacidade de processamento
* Escalabilidade eficiente
* Proteção contra abusos e ataques

---

## 📊 Tipos de testes implementados

### 🚀 Desempenho

* Métrica: Tempo de resposta (P95)
* Meta: < 500 ms

### ⚡ Carga

* Métrica: Throughput (requisições por segundo)
* Meta: > 2000 req/s

### 💥 Estresse

* Métrica: Ponto de quebra
* Meta: > 15.000 usuários

### 📈 Escalabilidade

* Métrica: Eficiência horizontal
* Meta: > 80%

### 🔐 Segurança

* Métrica: Rate limiting
* Meta: 100 requisições por minuto por IP

---

## ⚙️ Como instalar

Instale as dependências com:

```bash
pip install -r requirements.txt
```

---

## 🧪 Como executar

Execute os testes individualmente:

```bash
python performance_test.py
python load_test.py
python stress_test.py
python scalability_test.py
python security_test.py
```

---

## 📁 Estrutura do projeto

```bash
atividade10-testes-nao-funcionais/
│
├── performance_test.py     # Teste de desempenho (tempo de resposta)
├── load_test.py            # Teste de carga (throughput)
├── stress_test.py          # Teste de estresse (ponto de quebra)
├── scalability_test.py     # Teste de escalabilidade
├── security_test.py        # Teste de segurança (rate limiting)
│
├── relatorio_resultados.md # Análise dos resultados obtidos
├── requirements.txt
└── README.md
```

---

## 📌 Observações

* Os testes utilizam uma API pública (`JSONPlaceholder`) para simulação.
* Algumas metas não foram atingidas devido a limitações do ambiente de teste e da própria API utilizada.
* Os resultados obtidos são utilizados para análise e não representam um sistema real de produção.

---

## 📊 Resultados

Os resultados detalhados e a análise de aprovação/reprovação estão disponíveis em:

```txt
relatorio_resultados.md
```
