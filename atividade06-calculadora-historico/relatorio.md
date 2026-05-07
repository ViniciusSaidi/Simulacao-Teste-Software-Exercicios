# 📊 Relatório - Testes de Unidade e Integração

## 📖 Descrição

Este projeto implementa testes de unidade, integração e uso de test doubles (stub e mock) para uma calculadora com persistência de histórico.

O objetivo foi validar o comportamento do sistema, garantir cobertura completa e identificar defeitos por meio de testes automatizados.

---

# 🧪 1. Testes de Unidade

Foram implementados testes para todos os métodos da classe `Calculadora`, cobrindo:

* Entrada e saída
* Tipagem
* Limites (valores extremos)
* Valores fora do intervalo
* Mensagens de erro
* Fluxos de controle

Os testes foram executados utilizando `MagicMock` como stub do repositório, garantindo isolamento da lógica da calculadora.

---

# 🔗 2. Testes de Integração

Os testes de integração validaram a comunicação entre:

* `Calculadora`
* `HistoricoRepositorio`

Foram testados cenários como:

* Execução de múltiplas operações sequenciais
* Consistência do histórico
* Limpeza do histórico
* Formato correto das operações registradas

---

# 🧪 3. Test Doubles

## Stub

O stub foi utilizado para simular o repositório, permitindo testar a calculadora sem depender da implementação real.

Isso possibilitou:

* Isolamento dos testes
* Controle do comportamento do repositório

## Mock

O mock foi utilizado para verificar interações entre componentes.

Foram validados:

* Se `salvar()` foi chamado
* Quantas vezes foi chamado
* Com quais argumentos foi chamado
* Se NÃO foi chamado em casos de erro

---

# 🐛 4. Bug Encontrado e Correção

Foi identificado um defeito no método `potencia`.

## ❌ Problema

O histórico estava sendo registrado incorretamente:

```python
"{base} * {expoente} = {resultado}"
```

Ou seja, utilizava o operador de multiplicação (`*`) em vez do operador de potência.

## ✅ Correção

Foi ajustado para:

```python
"{base} ** {expoente} = {resultado}"
```

Os testes com mock permitiram detectar esse erro ao validar o argumento passado ao método `salvar()`.

---

# 📈 5. Cobertura de Testes

Resultados obtidos com `coverage.py`:

```txt
calculadora.py → 100%
repositorio.py → 100%
TOTAL → 99%
```

* Todas as linhas de `calculadora.py` foram cobertas
* Algumas linhas dos testes não foram executadas, o que não impacta a avaliação do código principal

---

# 🧠 6. Reflexão: Stub vs Mock

* **Stub**: utilizado para fornecer respostas controladas e isolar o comportamento da calculadora
* **Mock**: utilizado para verificar interações e garantir que chamadas externas ocorreram corretamente

Na prática:

* Stub foca no **estado**
* Mock foca no **comportamento**

---

# 🎯 Conclusão

* O sistema apresentou comportamento correto em todos os cenários testados
* O bug foi identificado e corrigido com sucesso
* A cobertura de testes atingiu o objetivo proposto
* Os testes garantem confiabilidade e manutenção futura do sistema
