# Exercício 02 — Contando operações

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 2 de 3 | 45 min | instrumentação, comparação de algoritmos, análise |

## Objetivo

Instrumentar os três algoritmos para contar comparações e trocas, e então **medir** em vez de
supor. É a primeira vez neste curso que você responde "qual é melhor?" com números.

## Requisitos

1. Parta do seu `tres_ordenacoes.py` do exercício 01.
2. Faça cada função devolver `(comparacoes, trocas)` além de ordenar.
3. Rode os três sobre **a mesma lista**, nos três cenários:
   - lista embaralhada
   - lista já ordenada
   - lista em ordem inversa
4. Monte uma tabela comparativa para cada cenário.
5. Repita com listas de 10, 50 e 100 elementos aleatórios e mostre como os números crescem.

## Exemplo de saída

```text
=== LISTA EMBARALHADA (10 elementos) ===
Algoritmo      Comparações  Trocas
Bubble                  45      26
Selection               45      10
Insertion               30      26

=== JÁ ORDENADA (10 elementos) ===
Algoritmo      Comparações  Trocas
Bubble                  45       0
Selection               45      10
Insertion                9       0

=== ORDEM INVERSA (10 elementos) ===
...

=== CRESCIMENTO (Bubble, embaralhada) ===
Tamanho    Comparações
     10             45
     50          1,225
    100          4,950
```

## Parte escrita

Depois de rodar, responda em comentários no próprio arquivo:

**a)** Por que Bubble e Selection fazem exatamente o mesmo número de comparações, sempre?

**b)** Com a lista **já ordenada**, o Insertion faz muito menos comparações que os outros dois.
Explique o mecanismo: o que exatamente ele deixa de fazer?

**c)** O Selection faz 10 trocas mesmo na lista já ordenada. Por quê? Como você evitaria essas
trocas inúteis?

**d)** Passando de 50 para 100 elementos, as comparações do Bubble mais ou menos **quadruplicam**.
Explique por que o fator é 4 e não 2.

**e)** Em qual cenário cada algoritmo é o melhor? Existe um que nunca ganha?

## Critérios de aceitação

- [ ] As três funções devolvem as contagens e continuam ordenando corretamente
- [ ] Os três cenários foram medidos com **a mesma** lista de partida
- [ ] A tabela de crescimento mostra pelo menos três tamanhos
- [ ] As cinco perguntas estão respondidas com base nos números que você mediu
- [ ] A resposta de (d) fala de `n²`, não só "porque cresce muito"

## Cuidado com a medição

Se você passar a mesma lista para os três algoritmos sem copiá-la, o primeiro a rodar deixa a lista
ordenada, e os outros dois vão medir o cenário errado. Use `lista[:]` para trabalhar com uma cópia.

Esse é um erro clássico de medição, e ele produz números que parecem plausíveis.

---

Gabarito: [gabaritos/modulo-11/ex02-contando-operacoes/](../../gabaritos/modulo-11/ex02-contando-operacoes/), depois de tentar, não antes.
