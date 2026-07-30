# Exercício 01 — Lendo código alheio

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 1 de 3 | 35 min | leitura de código, rastreio manual |

## Objetivo

Descrever o que um código faz **sem executá-lo**. É a habilidade que você usa toda vez que abre um
arquivo que não escreveu.

## Como fazer

Abra [exemplos/01_calculo_precos_antes.py](../exemplos/01_calculo_precos_antes.py) e **não rode**.
Leia com papel ao lado.

## Parte 1 — Traduza os nomes

A função se chama `p` e recebe `d`, `f` e `t`. Descubra, pela leitura, o que cada um guarda e
proponha um nome melhor:

| Nome atual | O que guarda | Nome proposto |
| --- | --- | --- |
| `p` | | |
| `d` | | |
| `f` | | |
| `t` | | |
| `r` | | |
| `v` | | |
| `tx` | | |

## Parte 2 — Rastreie na mão

A última linha chama `p([30, 60, 100])`. Sem rodar, percorra o código e responda:

**a)** Quantas voltas o laço dá?
**b)** Para cada item da lista, qual ramo do `if` é usado — o do `isinstance` ou o `else`?
**c)** Qual o valor de cada item no resultado final?
**d)** Escreva a lista que será impressa.

Só depois rode e compare com a sua previsão.

## Parte 3 — Aponte os problemas

Liste **cinco** características que tornam esse código difícil de ler. Para cada uma, diga qual
sinal da tabela do README ela representa.

## Parte 4 — A pergunta difícil

O parâmetro `t` começa em 10 e diminui a cada chamada recursiva. Ele nunca é usado para calcular
nada — só para decidir quando parar.

**Para que ele serve?** E o que aconteceria se ele não existisse?

## Critérios de aceitação

- [ ] Os sete nomes têm proposta de substituição
- [ ] A previsão da Parte 2 foi escrita **antes** de rodar
- [ ] A lista prevista bate com a real (ou a diferença está explicada)
- [ ] Os cinco problemas estão ligados aos sinais do README
- [ ] A resposta da Parte 4 explica o mecanismo, não só o efeito

## Depois de terminar

Abra o [_depois.py](../exemplos/01_calculo_precos_depois.py) e compare com os nomes que você
propôs. Onde você acertou? Onde a versão oficial escolheu diferente — e qual das duas você acha
melhor?

---

Gabarito: [gabaritos/modulo-12-ex01-lendo-codigo-alheio/](../../gabaritos/modulo-12-ex01-lendo-codigo-alheio/) —
depois de tentar, não antes.
