# Exercício 01 — Entrada à prova de tudo

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 1 de 3 | 30 min | `try`/`except`, `while`, funções |

## Objetivo

Escrever quatro funções de leitura que **não quebram**, aconteça o que acontecer com o teclado.
Elas viram a sua biblioteca pessoal — você vai copiá-las para todos os programas seguintes.

## Requisitos

1. Crie um arquivo `entrada_segura.py`.
2. Escreva as funções abaixo. Todas devem insistir até receber um valor aceitável.

| Função | Devolve |
| --- | --- |
| `ler_inteiro(mensagem)` | um `int`, qualquer valor |
| `ler_inteiro_na_faixa(mensagem, minimo, maximo)` | um `int` dentro do intervalo |
| `ler_decimal(mensagem)` | um `float` |
| `ler_sim_ou_nao(mensagem)` | `True` para sim, `False` para não |

3. Cada função captura o erro **específico** — nada de `except` pelado.
4. As mensagens de erro devem dizer ao usuário **o que fazer**, não só "erro".
5. `ler_sim_ou_nao` aceita `sim`, `s`, `nao`, `não`, `n`, em qualquer combinação de maiúsculas e com
   espaços sobrando (lembre da receita `.strip().lower()` do módulo 07).

## Exemplo de saída

```text
Idade: abc
  Digite um número inteiro.
Idade: 25.5
  Digite um número inteiro.
Idade: 25
Nota (0 a 10): 15
  O valor deve estar entre 0 e 10.
Nota (0 a 10): 7.5
  Digite um número inteiro.
Nota (0 a 10): 8
Altura: um metro
  Digite um número.
Altura: 1.75
Confirma? (s/n): TALVEZ
  Responda com s ou n.
Confirma? (s/n):   S
Confirmado!
```

## Critérios de aceitação

- [ ] Nenhuma função quebra com qualquer coisa que você digite — teste com letras, símbolos e vazio
- [ ] `ler_inteiro` recusa `25.5` (é decimal, não inteiro)
- [ ] `ler_decimal` aceita `1.75` **e** `7`
- [ ] `ler_inteiro_na_faixa` trata os dois problemas: tipo errado e valor fora da faixa
- [ ] `ler_sim_ou_nao` aceita `" S "` e `"SIM"`
- [ ] Nenhum `except` pelado no arquivo
- [ ] Cada mensagem diz o que o usuário deve fazer

## A pegadinha do vazio

Aperte Enter sem digitar nada. O `input()` devolve `""`, e `int("")` levanta `ValueError` — então
suas funções já tratam isso de graça. Confirme que sim.

## Desafio opcional

Acrescente `ler_texto_nao_vazio(mensagem)`, que insiste até receber algo além de espaços. Repare que
esta **não precisa de `try`**: não há conversão, então não há exceção. Um `if` resolve. Isso ilustra
a regra do módulo: nem todo problema de entrada é exceção.

---

Gabarito: [gabaritos/modulo-10-ex01-entrada-a-prova-de-tudo/](../../gabaritos/modulo-10-ex01-entrada-a-prova-de-tudo/) —
depois de tentar, não antes.
