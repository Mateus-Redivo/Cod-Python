# Menor e maior valor

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| Intermediário | 15 min | lista, comparação em laço, valor inicial |

## O que fazer

Leia 10 números inteiros e exiba o menor e o maior valor da lista.

**Restrição:** encontre os dois percorrendo a lista com um laço e comparando, sem usar `min()` e
`max()`. O objetivo aqui é entender o algoritmo que essas funções escondem.

## Exemplo de saída

```text
Digite um número: 15
Digite um número: -3
Digite um número: 42
Digite um número: 7
Digite um número: 0
Digite um número: 28
Digite um número: -11
Digite um número: 5
Digite um número: 19
Digite um número: 33
Menor valor: -11, Maior valor: 42
```

## Critérios de aceitação

- [ ] `min()` e `max()` não são usados
- [ ] Uma lista só com números negativos devolve o menor e o maior corretos
- [ ] Uma lista com todos os números iguais devolve esse valor nos dois

## Armadilha conhecida

Não comece `menor` e `maior` em zero. Se todos os números forem negativos, o maior sairia como 0,
que nem foi digitado. Comece os dois com o **primeiro elemento da lista**: é um valor que
comprovadamente existe nos dados.

---

Gabarito: [gabaritos/banco-de-exercicios/nivel-2-intermediario/menor-maior-valor/](../../gabaritos/banco-de-exercicios/nivel-2-intermediario/menor-maior-valor/),
depois de tentar, não antes.

Pré-requisito: [Módulo 06 — Listas](../../modulo-06-listas/).
