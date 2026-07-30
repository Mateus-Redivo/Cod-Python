# Exercício 02 — Calculadora robusta

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 2 de 3 | 40 min | `try`/`except`, `while`, `match/case`, funções |

## Objetivo

Pegar a calculadora do módulo 04 — que morria com qualquer digitação estranha — e torná-la
inquebrável. É a mesma ideia do exercício de refatoração do módulo 08: mesmo programa, agora sem os
buracos.

## Ponto de partida

Sua solução do
[EXERCICIO-02 do módulo 04](../../modulo-04-condicionais/exercicios/EXERCICIO-02-calculadora-com-menu.md).
O gabarito de lá também serve.

Ela tem três defeitos que você não tinha como resolver naquele momento:

1. Digitar letra na opção mata o programa.
2. Digitar letra num dos números mata o programa.
3. Depois de uma conta, o programa encerra — não dá para fazer outra.

## Requisitos

1. Crie `calculadora_robusta.py`.
2. Reaproveite as funções de leitura do exercício 01 deste módulo.
3. O menu deve repetir até o usuário escolher **sair**. Acrescente a opção `0 - Sair`.
4. Opção inválida, número inválido e divisão por zero: cada um com sua mensagem, e nenhum derruba o
   programa.
5. Continue usando `match/case` para escolher a operação.
6. Depois de cada conta, o menu aparece de novo.

## Exemplo de saída

```text
===== CALCULADORA =====
1 - Somar
2 - Subtrair
3 - Multiplicar
4 - Dividir
0 - Sair
=======================
Escolha: sete
  Digite um número inteiro.
Escolha: 9
  O valor deve estar entre 0 e 4.
Escolha: 4
Primeiro número: dez
  Digite um número.
Primeiro número: 10
Segundo número: 0
Não é possível dividir por zero.

===== CALCULADORA =====
...
Escolha: 1
Primeiro número: 2.5
Segundo número: 3.5
2.50 + 3.50 = 6.00

===== CALCULADORA =====
...
Escolha: 0
Até logo!
```

## Onde tratar o quê

Este é o ponto do exercício. Nem tudo é `try`:

| Problema | Como resolver | Por quê |
| --- | --- | --- |
| Letra na opção | `try` | o `int()` pode explodir |
| Opção fora de 0 a 4 | `if` | o valor é válido como número, só não serve |
| Letra no número | `try` | o `float()` pode explodir |
| Divisão por zero | `if` | você **sabe** que zero não serve; prevenir é melhor |

Se você usou `try` para a divisão por zero, funciona — mas releia a seção "Quando não capturar" do
README e decida se prefere.

## Critérios de aceitação

- [ ] Nenhuma sequência de digitação derruba o programa — teste com letras, vazio e símbolos
- [ ] O menu repete até a opção 0
- [ ] Cada erro tem mensagem própria, dizendo o que fazer
- [ ] A divisão por zero é **prevenida** com `if`, não capturada
- [ ] `2.5 + 3.5` funciona (os números são `float`)
- [ ] Nenhum `except` pelado
- [ ] O `try` engloba só a linha que pode falhar

## Desafio opcional

Guarde o resultado da última conta e ofereça a opção de usá-lo como primeiro número da próxima —
como fazem as calculadoras de verdade. O que acontece na primeira conta, quando ainda não há
resultado anterior?

---

Gabarito: [gabaritos/modulo-10-ex02-calculadora-robusta/](../../gabaritos/modulo-10-ex02-calculadora-robusta/) —
depois de tentar, não antes.
