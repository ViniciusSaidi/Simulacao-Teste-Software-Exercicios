# Atividade 01 - Testes Automatizados com Pytest

Esta atividade tem como objetivo praticar a criação de testes automatizados utilizando o framework Pytest.

O projeto implementa um sistema simples de notas, contendo funções para validação, cálculo de média, classificação da situação do aluno, estatísticas e normalização de notas.

## Funções implementadas

### 1. validar_nota(nota)

Verifica se uma nota está dentro do intervalo válido de 0 a 10.

### 2. calcular_media(notas)

Calcula a média das notas válidas de uma lista, ignorando valores inválidos.

### 3. obter_situacao(media)

Retorna a situação do aluno com base na média:

- Aprovado: média maior ou igual a 7.0
- Recuperação: média maior ou igual a 5.0 e menor que 7.0
- Reprovado: média menor que 5.0

### 4. calcular_estatisticas(notas)

Retorna um dicionário com:

- média
- maior nota
- menor nota
- quantidade de aprovados
- quantidade de alunos em recuperação
- quantidade de reprovados

### 5. normalizar_notas(notas, nota_maxima=10)

Converte notas de uma escala original para a escala de 0 a 10.

## Estrutura do projeto

```text
atividade01-pytest/
├── sistema_notas.py
├── test_sistema_notas.py
├── requirements.txt
└── README.md