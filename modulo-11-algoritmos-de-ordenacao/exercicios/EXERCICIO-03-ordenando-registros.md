# Exercício 03 — Ordenando registros (desafio)

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 3 de 3 | 55 min | matriz, ordenação, funções, estabilidade |

## Objetivo

Ordenar uma tabela de registros por **qualquer coluna** que o usuário escolher, e descobrir, no
caminho, um conceito que ninguém explica no começo: **estabilidade**.

## Os dados

```python
# nome, idade, nota
alunos = [
    ["Carla",  22, 9.5],
    ["Bruno",  19, 7.0],
    ["Ana",    22, 8.0],
    ["Diego",  20, 7.0],
    ["Elena",  19, 9.5],
]
```

É a lista de listas do módulo 09: cada linha é um aluno, cada coluna um campo.

## Requisitos

1. Crie `ordenando_registros.py`.
2. Escreva `ordenar_por(registros, coluna, crescente=True)`, que ordena a matriz **por uma coluna**,
   usando um dos algoritmos do exercício 01. Não use `sort()` nem `sorted()`.
3. Escreva `mostrar_tabela(registros)`, com colunas alinhadas.
4. Faça um menu que pergunte por qual coluna ordenar e em qual sentido, e mostre o resultado.
5. O menu repete até o usuário sair, e usa as funções de leitura segura do módulo 10.

## Exemplo de saída

```text
Nome         Idade   Nota
Carla           22    9.5
Bruno           19    7.0
Ana             22    8.0
Diego           20    7.0
Elena           19    9.5

Ordenar por: (0) Nome (1) Idade (2) Nota  -> 1
Sentido: (1) crescente (2) decrescente -> 1

Nome         Idade   Nota
Bruno           19    7.0
Elena           19    9.5
Diego           20    7.0
Carla           22    9.5
Ana             22    8.0
```

## A descoberta: estabilidade

Olhe o resultado acima com atenção. Bruno e Elena têm a **mesma idade** (19). Qual dos dois veio
primeiro?

Na lista original, Bruno aparece antes de Elena. Se o seu algoritmo preservar essa ordem relativa
entre valores empatados, ele é chamado de **estável**. Se embaralhar os empatados, é **instável**.

Isso importa de verdade: é o que permite ordenar por nota e **depois** por idade, mantendo a nota
como critério de desempate. Sem estabilidade, a primeira ordenação é perdida.

**Descubra experimentalmente:** ordene os alunos por idade usando os três algoritmos do exercício 01
e compare a ordem de Bruno e Elena em cada um. Anote qual é estável e qual não é.

> Dica: dois dos três costumam ser estáveis; um não é. Não confie na minha palavra: meça.

## Critérios de aceitação

- [ ] `ordenar_por` funciona para as três colunas, nos dois sentidos
- [ ] Nenhum `sort()` ou `sorted()` dentro das funções de ordenação
- [ ] A tabela fica alinhada, com qualquer nome de até 12 caracteres
- [ ] O menu não quebra com entrada inválida
- [ ] Os registros continuam íntegros: nenhum aluno fica com a nota de outro
- [ ] A investigação de estabilidade está registrada em comentários, com o resultado medido

## O erro que este exercício previne

Ao ordenar, você troca **linhas inteiras**, não valores soltos:

```python
registros[i], registros[j] = registros[j], registros[i]      # certo
registros[i][coluna], registros[j][coluna] = ...             # ERRADO
```

A segunda forma troca só o campo comparado e deixa o resto no lugar: o aluno fica com a nota de
outro. É exatamente o problema das listas paralelas do módulo 08, reaparecendo por outro caminho.

## Desafio dentro do desafio

Ordene por **dois critérios**: nota decrescente e, em caso de empate, nome crescente. Com um
algoritmo estável, isso se resolve ordenando duas vezes, mas em qual ordem? Descubra e explique.

---

Gabarito: [gabaritos/modulo-11-ex03-ordenando-registros/](../../gabaritos/modulo-11-ex03-ordenando-registros/), depois de tentar, não antes.
