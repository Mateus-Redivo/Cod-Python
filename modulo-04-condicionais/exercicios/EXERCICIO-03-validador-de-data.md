# Exercício 03 — Validador de data (desafio)

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 3 de 3 | 50 min | `if/elif/else` aninhado, `and`/`or`, `match/case`, regras compostas |

## Objetivo

Dizer se uma data existe. Parece trivial e não é: o número de dias muda por mês, fevereiro muda por
ano, e a regra do ano bissexto tem três condições encadeadas que quase todo mundo escreve errado.

É o exercício que separa "sei escrever `if`" de "sei traduzir uma regra complicada em condições".

## Requisitos

1. Crie um arquivo `validador_de_data.py`.
2. Peça dia, mês e ano.
3. Determine se a data é **válida**, verificando nesta ordem:
   - o ano é positivo
   - o mês está entre 1 e 12
   - o dia é positivo e não passa do número de dias daquele mês, naquele ano
4. Descubra quantos dias tem o mês informado. Use `match/case` para agrupar os meses de 31 e de 30
   dias: este é o caso em que ele lê melhor que `elif`.
5. Implemente a regra do ano bissexto **corretamente** (ela está abaixo).
6. Exiba: se a data é válida, quantos dias tem o mês, se o ano é bissexto e o nome do mês.
7. Quando inválida, diga **qual** regra falhou: não basta "data inválida".

**Restrição:** sem laços, sem listas, sem `try`. Só condicionais.

## A regra do ano bissexto

Não é "divisível por 4". A regra completa tem três partes:

> Um ano é bissexto se for divisível por 4, **exceto** se for divisível por 100, **a menos que**
> também seja divisível por 400.

Consequências que servem de teste:

| Ano | Bissexto? | Por quê |
| --- | --- | --- |
| 2024 | Sim | divisível por 4, não por 100 |
| 1900 | **Não** | divisível por 100 e não por 400 |
| 2000 | **Sim** | divisível por 400 |
| 2023 | Não | não é divisível por 4 |

Se o seu código disser que 1900 foi bissexto, a regra está incompleta, e esse é o erro mais comum.

## Exemplo de saída

```text
Dia: 29
Mês: 2
Ano: 2024

Data: 29/02/2024
Mês: Fevereiro (29 dias)
Ano bissexto: Sim
Data VÁLIDA
```

E com data inválida:

```text
Dia: 29
Mês: 2
Ano: 1900

Data: 29/02/1900
Mês: Fevereiro (28 dias)
Ano bissexto: Não
Data INVÁLIDA: fevereiro de 1900 tem apenas 28 dias
```

## Critérios de aceitação

- [ ] `29/02/2024` é válida; `29/02/2023` e `29/02/1900` não são
- [ ] `29/02/2000` é válida (o caso do divisível por 400)
- [ ] `31/04/2024` é recusada (abril tem 30)
- [ ] `31/12/2024` é aceita
- [ ] Mês 13 e mês 0 são recusados com mensagem própria
- [ ] Dia 0 e dia negativo são recusados
- [ ] A escolha dos dias do mês usa `match/case`
- [ ] Cada tipo de erro tem sua própria mensagem
- [ ] Nenhum laço, lista ou `try` no arquivo

## A ordem dos testes importa

Antes de perguntar "o dia cabe no mês?", você precisa saber **qual mês**, e um mês 13 não tem
número de dias. Se você testar o dia antes de validar o mês, seu programa vai tentar decidir quantos
dias tem o mês 13.

Esse encadeamento (validar uma coisa antes de poder validar a próxima) é o mesmo padrão do
validador de e-mail do módulo 07, e vai reaparecer em todo formulário que você escrever.

## Desafio dentro do desafio

Acrescente: dado que a data é válida, diga em que **estação do ano** ela cai (hemisfério sul). As
fronteiras não são no dia 1º: o verão começa em 21 de dezembro, por exemplo. Repare que a condição
do verão é a mais difícil das quatro, porque ela **atravessa a virada do ano**. Escreva-a e explique
por que ela precisa de `or` onde as outras usam `and`.

---

Gabarito: [gabaritos/modulo-04-ex03-validador-de-data/](../../gabaritos/modulo-04-ex03-validador-de-data/), depois de tentar, não antes.
