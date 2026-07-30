# Gabarito — Módulo 00, Exercício 02: Decifrando erros

Enunciado: [EXERCICIO-02-decifrando-erros.md](../../modulo-00-preparacao/exercicios/EXERCICIO-02-decifrando-erros.md)

> Escreva suas previsões antes de abrir. Aqui o objetivo não é acertar — é descobrir onde a sua
> leitura de mensagem de erro falha.

---

## Programa A — aspas não fechadas

```text
  File "A.py", line 1
    print("Bem-vindo ao sistema)
          ^
SyntaxError: unterminated string literal (detected at line 1)
```

| | |
| --- | --- |
| Linha | 1 |
| Tipo | `SyntaxError` |
| Significa | "você abriu aspas e não fechou" — o Python leu até o fim da linha procurando a segunda aspa e não achou |
| Conserto | `print("Bem-vindo ao sistema")` |

O `^` aponta exatamente onde a string começou, não onde ela deveria terminar. Faz sentido: o Python
sabe onde o problema **nasceu**, não onde você esqueceu de fechar.

---

## Programa B — texto somado com número

```text
  File "B.py", line 3, in <module>
    print("Você tem " + 25 + " anos")
          ~~~~~~~~~~~~^~~~
TypeError: can only concatenate str (not "int") to str
```

| | |
| --- | --- |
| Linha | 3 |
| Tipo | `TypeError` |
| Significa | "só sei grudar texto com texto" — o `+` não sabe o que fazer entre `"Você tem "` e `25` |
| Conserto | `print(f"Você tem {25} anos")` ou `print("Você tem " + str(25) + " anos")` |

Repare no `~~~~^~~~`: o Python marca **os dois lados** da operação que falhou, com o `^` no operador.
Isso é ajuda de verdade, e é a razão de ler a mensagem inteira.

A linha 2 (`print("Olá, " + nome)`) funciona porque `nome` **também** é texto. O erro só aparece
quando um dos lados é número.

---

## Programa C — nome que não existe

```text
  File "C.py", line 2, in <module>
    print(totall)
          ^^^^^^
NameError: name 'totall' is not defined
```

| | |
| --- | --- |
| Linha | 2 |
| Tipo | `NameError` |
| Significa | "esse nome não existe" — nenhuma variável chamada `totall` foi criada |
| Conserto | criar a variável antes: `totall = 100`, ou corrigir o nome se era outra coisa |

---

## Programa D — indentação inesperada

```text
  File "D.py", line 2
    print("Linha 2")
IndentationError: unexpected indent
```

| | |
| --- | --- |
| Linha | 2 |
| Tipo | `IndentationError` |
| Significa | "essa linha está recuada e não deveria estar" — não há nada antes que justifique o recuo |
| Conserto | alinhar `print("Linha 2")` com as outras duas |

Este é o erro que assusta quem vem de outras linguagens, onde recuo é só estética. Em Python, o
espaço no começo da linha **tem significado**, e um recuo sem motivo é erro de escrita.

---

## Programa E — a função que não existe

```text
  File "E.py", line 1, in <module>
    primt("Olá!")
    ^^^^^
NameError: name 'primt' is not defined. Did you mean: 'print'?
```

| | |
| --- | --- |
| Linha | 1 |
| Tipo | `NameError` |
| Significa | "não conheço nada chamado `primt`" — e o Python ainda arrisca um palpite |
| Conserto | `print("Olá!")` |

O `Did you mean: 'print'?` no fim é o Python comparando o nome errado com os que ele conhece e
sugerindo o mais parecido. Muita gente lê só a primeira linha da mensagem e perde essa ajuda.

Repare também que é o **mesmo tipo** de erro do Programa C: `NameError`. Para o Python, o nome de
uma função é só mais um nome — e um nome que não existe é sempre a mesma queixa.

---

## A pergunta que amarra o exercício

**Os dois programas em que nenhuma linha roda são o A e o D.**

A prova está na tela. Rodando cada um e olhando o que aparece **antes** do erro:

| Programa | Imprimiu antes de falhar? | Erro |
| --- | --- | --- |
| A | nada | `SyntaxError` |
| B | `Olá, Maria` | `TypeError` |
| C | `Calculando...` | `NameError` |
| D | nada | `IndentationError` |
| E | nada (não havia linha antes) | `NameError` |

**Por que isso acontece?**

Porque existem dois momentos diferentes:

1. **Antes de executar**, o Python **lê o arquivo inteiro** para entender o que está escrito. Se a
   escrita estiver quebrada — aspa faltando, recuo sem motivo, parêntese aberto —, ele nem começa.
   São os erros de escrita: `SyntaxError` e `IndentationError`.

2. **Durante a execução**, linha por linha, aparecem os problemas que só existem no momento em que
   a linha roda: somar texto com número, usar um nome inexistente. O programa já andou até ali, e
   tudo que veio antes já aconteceu.

Essa distinção é útil na prática: se você rodou um programa e **nada** apareceu na tela, procure um
erro de escrita — provavelmente numa linha que você nem estava mexendo. Se apareceu parte da saída
e depois quebrou, o problema está logo depois do último `print` que você viu.

> Cuidado com o Programa E: ele não imprimiu nada, mas **não** é erro de escrita. Ele simplesmente
> não tinha nenhuma linha antes para imprimir. Por isso a tabela sozinha engana — é preciso olhar
> também o **tipo** do erro. Se você respondeu "A, D e E", a observação estava certa e faltou só
> esse detalhe.

---

## O que rever

| Errou em | Volte para |
| --- | --- |
| A, D | seção "O erro não é o inimigo" do [README](../../modulo-00-preparacao/) |
| B | tabela de tipos do [módulo 01](../../modulo-01-tipos-e-variaveis/) — o `+` ambíguo |
| C, E | [exemplos/03_lendo_o_erro.py](../../modulo-00-preparacao/exemplos/03_lendo_o_erro.py) |
| A pergunta final | [exemplos/02_ordem_de_execucao.py](../../modulo-00-preparacao/exemplos/02_ordem_de_execucao.py) |
