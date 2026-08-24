# Exercício 02 — Regras de acesso

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 2 de 3 | 35 min | `and`, `or`, `not`, comparação, precedência |

## Objetivo

Traduzir regras escritas em português para expressões lógicas em Python. É a habilidade que o
módulo 04 vai cobrar em cada `if` que você escrever.

## Parte 1 — Traduza

Para cada regra, escreva **uma linha** de Python que guarde `True` ou `False` numa variável de nome
descritivo. Use as variáveis dadas; não invente `input()`.

```python
idade = 20
eh_socio = True
tem_convite = False
eh_fim_de_semana = True
saldo = 150.00
nota_prova = 7.5
frequencia = 85
trabalho_entregue = True
```

| # | Regra em português |
| --- | --- |
| 1 | Pode entrar se for maior de idade **e** sócio |
| 2 | Pode entrar se for sócio **ou** tiver convite |
| 3 | Paga meia-entrada se **não** for sócio |
| 4 | Pode comprar se o saldo for maior que 100 **e** menor que 1000 |
| 5 | Está aprovado se a nota for pelo menos 6, a frequência pelo menos 75 **e** o trabalho tiver sido entregue |
| 6 | Precisa de convite se **não** for sócio **e** for fim de semana |
| 7 | Está reprovado se a nota for menor que 6 **ou** a frequência for menor que 75 |
| 8 | O saldo está **fora** da faixa de 100 a 1000 |

Repare nas regras 4 e 8: elas descrevem a mesma faixa, uma por dentro e outra por fora. Os
operadores têm que ser diferentes.

## Parte 2 — Preveja

Sem rodar, diga o valor de cada expressão. Depois confira.

| # | Expressão | Previsão |
| --- | --- | --- |
| 1 | `True or False and False` | |
| 2 | `(True or False) and False` | |
| 3 | `not True and False` | |
| 4 | `not (True and False)` | |
| 5 | `5 > 3 or 10 / 0 > 1` | |

A número 5 é uma pegadinha: dividir por zero dá erro. Ela dá erro? Rode e explique o que viu.

## Parte 3 — Encontre o bug

Este código deveria aceitar apenas notas entre 0 e 10, mas aceita qualquer coisa:

```python
nota = 50
nota_valida = nota >= 0 or nota <= 10
print("Nota válida?", nota_valida)
```

**a)** Por que ele diz que 50 é válida?
**b)** Teste com `-30`. O que acontece? Existe algum número que ele recuse?
**c)** Corrija, e reescreva também usando o atalho de intervalo do Python.

## Critérios de aceitação

- [ ] As 8 traduções cabem em uma linha cada e guardam o resultado em variável nomeada
- [ ] Nenhum nome de variável tem uma letra só
- [ ] As regras 4 e 8 usam operadores diferentes entre si
- [ ] As 5 previsões da Parte 2 foram escritas antes de rodar
- [ ] A explicação da Parte 3 diz **por que** o `or` aceita tudo, não só que estava errado

---

Gabarito: [gabaritos/modulo-02/ex02-regras-de-acesso/](../../gabaritos/modulo-02/ex02-regras-de-acesso/), depois de tentar, não antes.
