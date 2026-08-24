# Acumulador com sentinela

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| Intermediário | 30 min | `while`, valor sentinela, acumulador, contador |

## Objetivo

Ler números do usuário por tempo indeterminado (quem decide quando parar é ele) e resumir o que
foi digitado.

## Requisitos

1. Peça números inteiros ao usuário, repetidamente.
2. Encerre quando o usuário digitar **0**. Esse é o valor *sentinela*: o combinado de "acabou".
3. O 0 sinaliza o fim e **não** entra na soma nem na contagem.
4. Ao final, exiba a soma, a quantidade de números digitados e a média com duas casas decimais.
5. Se o usuário digitar 0 logo de cara, exiba `Nenhum número informado.` e nada mais.

**Restrições:** use `while`. Não use listas (elas só chegam no módulo 06) e não use `try/except`
(módulo 10).

## Exemplo de saída

```text
Digite números inteiros. Digite 0 para encerrar.
Número: 4
Número: 7
Número: 2
Número: 0
Soma = 13
Quantidade = 3
Média = 4.33
```

E no caso vazio:

```text
Digite números inteiros. Digite 0 para encerrar.
Número: 0
Nenhum número informado.
```

## Critérios de aceitação

- [ ] O 0 encerra o programa e não é contado nem somado
- [ ] Números negativos são aceitos normalmente (só o 0 é especial)
- [ ] Digitar 0 na primeira pergunta não gera `ZeroDivisionError`
- [ ] A média sai com duas casas decimais
- [ ] Existe apenas um acumulador para a soma e um contador para a quantidade

## Armadilha conhecida

A média é `soma / quantidade`. Se a quantidade for zero, o Python levanta `ZeroDivisionError` e o
programa morre. Teste a contagem **antes** de dividir: é exatamente o que o quinto requisito está
pedindo.

## Desafio opcional

Mostre também o maior e o menor número digitado. Pense bem no valor inicial dessas duas variáveis:
começar ambas em zero dá resposta errada se o usuário digitar só negativos.

---

Gabarito: [gabaritos/banco-de-exercicios/nivel-2-intermediario/acumulador-com-sentinela/](../../gabaritos/banco-de-exercicios/nivel-2-intermediario/acumulador-com-sentinela/),
depois de tentar, não antes.

Pré-requisito: [Módulo 05 — Laços de repetição](../../modulo-05-lacos-de-repeticao/).
