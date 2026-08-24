# Segundo maior número

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| Intermediário | 20 min | função com retorno, lista, duplicatas, ordenação |

## O que fazer

Escreva uma função que receba uma lista e devolva o **segundo maior** valor dela. No programa
principal, leia 8 números inteiros do usuário e exiba o resultado da função.

## Requisitos

1. A lógica fica dentro de uma função que **retorna** o valor, sem imprimir nada.
2. Valores repetidos contam uma vez só: em `[9, 9, 4]`, o segundo maior é `4`, não `9`.
3. Se não houver um segundo valor distinto (todos os números iguais), a função devolve `None`.

## Exemplo de saída

```text
Digite um número: 10
Digite um número: 25
Digite um número: 3
Digite um número: 25
Digite um número: 8
Digite um número: 17
Digite um número: 1
Digite um número: 25
Segundo maior número: 17
```

Repare: o 25 aparece três vezes, e mesmo assim o segundo maior é 17, não 25.

## Critérios de aceitação

- [ ] A função retorna o valor em vez de imprimir
- [ ] Duplicatas do maior valor não viram a resposta
- [ ] Lista com todos os elementos iguais devolve `None` em vez de quebrar

---

Gabarito: [gabaritos/banco-de-exercicios/nivel-2-intermediario/segundo-maior-numero/](../../gabaritos/banco-de-exercicios/nivel-2-intermediario/segundo-maior-numero/),
depois de tentar, não antes.

Pré-requisito: [Módulo 08 — Funções](../../modulo-08-funcoes/).
