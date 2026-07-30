# Exercício 03 — Auditoria de refatoração (desafio)

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 3 de 3 | 55 min | julgamento crítico, medição, honestidade técnica |

## Objetivo

Julgar refatorações feitas por outras pessoas — inclusive as deste próprio módulo. É o exercício em
que você para de aplicar regras e começa a avaliá-las.

## Parte 1 — Audite os cinco pares

Para cada par em [exemplos/](../exemplos/), rode as duas versões e compare:

```bash
python 0N_nome_antes.py > a.txt
python 0N_nome_depois.py > b.txt
diff a.txt b.txt
```

Preencha:

| Par | `diff` vazio? | Se não, o que mudou? | Foi refatoração legítima? |
| --- | --- | --- | --- |
| 01 cálculo de preços | | | |
| 02 processamento de clientes | | | |
| 03 cálculo de seguro | | | |
| 04 status de pets | | | |
| 05 notas de estudantes | | | |

**Três dos cinco não passam no `diff`.** Para cada um, decida: a mudança foi no **cálculo** ou só na
**apresentação**? Justifique olhando o código, não só a saída.

> Para comparar só o cálculo, chame a função diretamente das duas versões com os mesmos argumentos e
> compare os valores devolvidos.

## Parte 2 — A pergunta conceitual

O README afirma que refatorar é "mudar a estrutura sem mudar o que o código faz".

**O que exatamente conta como "o que o código faz"?**

Considere os três casos e escreva um parágrafo para cada:

**a)** Uma função devolve `50.0` antes e depois, mas o `print` passou de `50.0` para `50.00`. Mudou
o comportamento?

**b)** Uma função devolve os mesmos valores, mas ficou 40% mais lenta. Mudou o comportamento?

**c)** Uma função devolve os mesmos valores para todas as entradas testadas, mas ninguém testou
lista vazia — e nela as duas versões divergem. Foi refatoração?

## Parte 3 — Refatore uma refatoração

Escolha o par que você achou **menos** bem resolvido. Escreva uma terceira versão, `_depois2.py`,
melhorando o que a versão oficial deixou passar.

Regras:
- a saída tem que continuar idêntica à do `_depois.py`
- justifique cada mudança em comentário
- se você achar que a versão oficial já está boa e não há o que melhorar, **diga isso** e
  justifique — é uma resposta legítima, e mais difícil de defender que a outra

## Parte 4 — O limite

Escreva um parágrafo respondendo: **existe código que não vale a pena refatorar?**

Dê um exemplo concreto — pode ser de um dos exemplos deste módulo, de um exercício seu de módulos
anteriores, ou inventado. Explique o critério que você usou para decidir.

## Critérios de aceitação

- [ ] Os cinco pares foram rodados e a tabela está preenchida com resultados reais
- [ ] Para os três que divergem, a análise distingue cálculo de apresentação
- [ ] As três perguntas da Parte 2 têm resposta com justificativa
- [ ] A Parte 3 tem código rodando e `diff` vazio contra o `_depois.py`
- [ ] A Parte 4 dá um exemplo concreto, não uma resposta genérica

## Uma observação honesta

Este módulo apresenta cinco pares como material de aula e, ao auditá-los, você descobre que três
deles não passam no critério que o próprio módulo ensina.

Isso não é pegadinha. É como o código real se parece: material antigo, escrito com um objetivo,
reaproveitado com outro. Perceber a inconsistência e conseguir descrevê-la com precisão vale mais
que qualquer exercício em que tudo fecha certinho.

---

Gabarito: [gabaritos/modulo-12-ex03-auditoria-de-refatoracao/](../../gabaritos/modulo-12-ex03-auditoria-de-refatoracao/) —
depois de tentar, não antes.
