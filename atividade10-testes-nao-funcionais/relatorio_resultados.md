# 📊 Relatório de Testes Não Funcionais - E-commerce Black Friday

## 📖 Contexto

Este relatório apresenta os resultados dos testes não funcionais realizados para um sistema de e-commerce simulado, considerando o cenário de Black Friday com alta carga de usuários.

### 🎯 Requisitos do sistema

* 10.000 usuários simultâneos esperados
* Tempo de resposta P95 < 500ms
* Throughput > 2000 req/s
* Ponto de quebra > 15.000 usuários
* Eficiência horizontal > 80%
* Rate limiting: 100 req/min/IP

---

# 🚀 1. Teste de Desempenho

* Endpoint: `/posts/1`
* Total de requisições: 50

### 📊 Resultados

* Tempo médio: **33.14 ms**
* P95: **37.81 ms**
* Meta: **< 500 ms**

### ✅ Resultado: APROVADO

### 🔎 Análise

O sistema apresentou excelente desempenho, com tempo de resposta muito abaixo da meta estabelecida. Isso indica baixa latência e boa responsividade para requisições individuais.

---

# ⚡ 2. Teste de Carga

* Total de requisições: 500
* Concorrência: 50

### 📊 Resultados (aproximado)

* Throughput: **~200–300 req/s**
* Taxa de sucesso: **> 95%**
* Meta: **> 2000 req/s**

### ❌ Resultado: REPROVADO

### 🔎 Análise

O sistema não atingiu o throughput esperado. Possíveis causas:

* Limitações do ambiente local de teste
* Uso de biblioteca síncrona (`requests`)
* API pública não otimizada para alta carga

Apesar disso, a alta taxa de sucesso indica estabilidade sob carga moderada.

---

# 💥 3. Teste de Estresse

### 📊 Resultados

* Ponto de quebra: **~500 usuários simultâneos**
* Taxa de erro: **> 5% a partir desse ponto**
* Meta: **> 15.000 usuários**

### ❌ Resultado: REPROVADO

### 🔎 Análise

O sistema apresentou degradação significativa a partir de 500 usuários simultâneos, com aumento de erros e queda de throughput.

Isso indica que o sistema não está preparado para cenários extremos como Black Friday.

---

# 📈 4. Teste de Escalabilidade

### 📊 Resultados

| Servidores | Eficiência |
| ---------- | ---------- |
| 1          | 100%       |
| 2          | 95%        |
| 4          | 90%        |
| 8          | 80%        |

* Meta: **> 80%**

### ❌ Resultado: REPROVADO

### 🔎 Análise

A eficiência diminui conforme o número de servidores aumenta, indicando overhead de distribuição e possíveis gargalos de rede ou balanceamento.

O cenário com 8 servidores atingiu exatamente 80%, ficando abaixo da meta exigida (> 80%).

---

# 🔐 5. Teste de Segurança

### 📊 Resultados

* Total de requisições: 120
* Respostas 429: **0**
* Meta: **Rate limiting ativo (>100 req/min/IP)**

### ❌ Resultado: REPROVADO

### 🔎 Análise

A API não apresentou mecanismos de rate limiting, permitindo múltiplas requisições sem restrição.

Isso representa um risco de segurança, pois possibilita ataques como:

* DDoS
* Abuso de recursos
* scraping em larga escala

---

# 📌 Conclusão Geral

| Tipo de Teste  | Resultado   |
| -------------- | ----------- |
| Desempenho     | ✅ Aprovado  |
| Carga          | ❌ Reprovado |
| Estresse       | ❌ Reprovado |
| Escalabilidade | ❌ Reprovado |
| Segurança      | ❌ Reprovado |

---

## 🧠 Considerações Finais

* O sistema apresenta bom desempenho em baixa carga
* Não suporta cenários de alta concorrência
* Não atende aos requisitos de escalabilidade
* Não possui mecanismos adequados de proteção contra abuso

### 🔧 Recomendações

* Implementar cache e otimização de queries
* Utilizar arquitetura distribuída (load balancer)
* Adotar ferramentas como Locust para testes mais realistas
* Implementar rate limiting e autenticação
