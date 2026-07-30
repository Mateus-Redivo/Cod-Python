# Exercício 02 — Prevendo tipos e resultados

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 2 de 3 | 30 min | tipos, conversão, `TypeError`, leitura de código |

## Objetivo

Prever o que o Python faz **antes** de rodar. Aqui não se escreve programa: exercita-se o modelo
mental de tipos, que é o que evita metade dos erros dos próximos módulos.

## Como fazer

Para cada linha da tabela, escreva sua previsão: **o resultado** e **o tipo** dele. Se você achar
que dá erro, escreva qual erro. Só depois de preencher tudo, rode e compare.

Onde você errou é onde está o aprendizado — anote o motivo, não só a correção.

## Parte 1 — Preveja resultado e tipo

| # | Expressão | Resultado? | Tipo? |
| --- | --- | --- | --- |
| 1 | `7 + 3` | | |
| 2 | `7 / 2` | | |
| 3 | `7 // 2` | | |
| 4 | `"7" + "3"` | | |
| 5 | `"7" * 3` | | |
| 6 | `7 + 3.0` | | |
| 7 | `"7" + 3` | | |
| 8 | `int("7") + 3` | | |
| 9 | `float("7") + 3` | | |
| 10 | `int("7.5")` | | |
| 11 | `str(7) + "3"` | | |
| 12 | `True + True` | | |

Para conferir o tipo, use `type(...)`. Por exemplo:

```python
print(7 / 2, type(7 / 2))
```

## Parte 2 — Explique

**a)** Por que a linha 2 (`7 / 2`) devolve `float`, se os dois números são inteiros?

**b)** Qual a diferença prática entre a linha 4 e a linha 8? As duas partem de `"7"` e `3`.

**c)** Por que a linha 10 quebra e a linha 9 não? Leia o nome das duas funções.

**d)** A linha 12 devolve `2`. O que isso revela sobre o tipo `bool` em Python?

## Parte 3 — Conserte

Este programa deveria somar dois valores e mostrar o total, mas não funciona:

```python
primeiro_valor = "10"
segundo_valor = 5
total = primeiro_valor + segundo_valor
print("Total:", total)
```

**a)** Qual erro aparece? Copie a mensagem completa.
**b)** Conserte de duas formas diferentes: uma tratando os valores como números e outra tratando-os
como texto. Explique quando cada uma faria sentido.

## Critérios de aceitação

- [ ] As 12 previsões foram escritas **antes** de rodar qualquer coisa
- [ ] Cada previsão errada está anotada com o motivo do erro
- [ ] As quatro explicações da Parte 2 falam do mecanismo, não só do resultado
- [ ] As duas correções da Parte 3 rodam e produzem saídas diferentes entre si

---

Gabarito: [gabaritos/modulo-01-ex02-prevendo-tipos/](../../gabaritos/modulo-01-ex02-prevendo-tipos/) —
depois de tentar, não antes. Ler a resposta antes de prever esvazia o exercício por completo.
