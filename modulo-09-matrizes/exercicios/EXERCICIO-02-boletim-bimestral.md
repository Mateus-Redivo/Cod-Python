# Exercício 02 — Boletim bimestral

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 2 de 3 | 45 min | matriz, laços aninhados, médias por linha e por coluna, funções |

## Objetivo

Guardar as notas de vários alunos em vários bimestres numa matriz, e produzir as duas médias que
importam: a de cada aluno e a da turma em cada bimestre.

É o exercício em que a matriz deixa de ser exercício de matemática e vira estrutura de dados de um
problema real.

## Requisitos

1. Crie um arquivo `boletim_bimestral.py`.
2. Use estes dados fixos (ainda sem `input()`):

```python
alunos = ["Ana", "Bruno", "Carla", "Diego"]
notas = [
    [8.0, 7.5, 9.0, 6.5],     # notas da Ana nos 4 bimestres
    [5.0, 6.0, 4.5, 7.0],     # Bruno
    [9.5, 9.0, 10.0, 8.5],    # Carla
    [3.0, 5.5, 6.0, 4.0],     # Diego
]
```

3. Escreva as funções:

| Função | Devolve |
| --- | --- |
| `media_do_aluno(notas, indice)` | a média de uma linha |
| `media_do_bimestre(notas, bimestre)` | a média de uma coluna |
| `situacao(media)` | `"Aprovado"` (>= 7), `"Recuperação"` (>= 5) ou `"Reprovado"` |
| `melhor_aluno(alunos, notas)` | o nome de quem tem a maior média |
| `mostrar_boletim(alunos, notas)` | nada: imprime a tabela |

4. A tabela deve mostrar, por aluno: as quatro notas, a média e a situação.
5. No rodapé, a média da turma em cada bimestre e o melhor aluno.

## Exemplo de saída

```text
========================================================
Aluno          1º B   2º B   3º B   4º B  Média  Situação
--------------------------------------------------------
Ana             8.0    7.5    9.0    6.5   7.75  Aprovado
Bruno           5.0    6.0    4.5    7.0   5.62  Recuperação
Carla           9.5    9.0   10.0    8.5   9.25  Aprovado
Diego           3.0    5.5    6.0    4.0   4.62  Reprovado
--------------------------------------------------------
Média turma     6.4    7.0    7.4    6.5
Melhor aluno: Carla (9.25)
========================================================
```

## A diferença que o exercício ensina

- A média de um **aluno** é a média de uma **linha**, e a linha já é uma lista, então `sum()`
  resolve.
- A média de um **bimestre** é a média de uma **coluna**, e a coluna não existe como lista, então
  é preciso um laço que colete `notas[linha][bimestre]` de cada linha.

Se as duas funções ficaram parecidas demais, releia: elas percorrem a matriz em direções diferentes.

## Critérios de aceitação

- [ ] As médias por aluno estão corretas (confira a da Ana na calculadora)
- [ ] As médias por bimestre estão corretas (confira a do 1º bimestre)
- [ ] As colunas ficam alinhadas na vertical
- [ ] Nenhuma função usa os números 4 ou 5 fixos; tudo com `len()`
- [ ] Acrescentar um quinto aluno funciona sem mudar nenhuma função
- [ ] `situacao` é uma função separada, não um `if` solto no meio da tabela

## Desafio opcional

Acrescente uma coluna "Faltas", mas note o problema: faltas não são notas, e misturá-las na mesma
matriz obrigaria a lembrar que "a última coluna é diferente". Escreva em um comentário como você
guardaria as faltas sem essa armadilha.

---

Gabarito: [gabaritos/modulo-09/ex02-boletim-bimestral/](../../gabaritos/modulo-09/ex02-boletim-bimestral/), depois de tentar, não antes.
