# Módulo 04 — Condicionais

Seu programa já pergunta e já calcula. Mas ele ainda faz **sempre a mesma coisa**: a sequência de
linhas é fixa, do começo ao fim. Agora ele vai aprender a **decidir** — a tomar um caminho ou outro
conforme o que encontrar.

É o módulo em que o código deixa de ser uma receita e vira um programa de verdade.

## Objetivos de aprendizagem

Ao final deste módulo você será capaz de:

- [ ] Escrever `if`, `if/else` e `if/elif/else` e saber quando cada um serve
- [ ] Explicar por que a indentação em Python é sintaxe, não estética
- [ ] Ordenar condições de `elif` para que nenhuma fique inalcançável
- [ ] Aninhar condicionais e reconhecer quando isso está ficando complicado demais
- [ ] Proteger o programa de operações inválidas, como a divisão por zero
- [ ] Usar `match/case` e dizer quando ele lê melhor que uma sequência de `elif`

## Pré-requisitos

[Módulo 03 — Entrada e saída](../modulo-03-entrada-e-saida/) concluído. E, principalmente, o
[módulo 02](../modulo-02-operadores/) bem assentado: um `if` sem comparação e sem `and`/`or` não
tem o que testar. Se a armadilha do intervalo (`and` vs `or`) ainda te confunde, volte lá antes.

## Conceito

### O problema: o programa que não sabe dizer não

No módulo anterior você escreveu um divisor de contas. Ele funciona — até alguém digitar `0` no
número de pessoas:

```python
valor_por_pessoa = total / numero_de_pessoas    # ZeroDivisionError
```

O programa morre. E não morre porque você errou: morre porque não havia como ele **verificar** nada
antes de agir. Todo programa útil precisa perguntar "posso?" antes de fazer.

### `if`: faça só se

```python
idade = 18

if idade >= 18:
    print("Você é maior de idade!")
```

Três detalhes de escrita que valem o módulo:

1. **Dois-pontos** no fim da linha do `if`. Esquecer dá `SyntaxError`.
2. **Indentação** de 4 espaços no bloco de dentro. É ela que diz o que está sujeito à condição.
3. A condição é uma expressão que dá `True` ou `False` — exatamente as do módulo 02.

### Indentação é sintaxe, não enfeite

Em quase toda linguagem, recuar o código é hábito. Em Python é **a regra**. Compare:

```python
if nota >= 6:
    print("Aprovado")
    print("Parabéns!")        # dentro do if: só sai se passou

if nota >= 6:
    print("Aprovado")
print("Parabéns!")            # FORA do if: sai sempre
```

Nenhum dos dois dá erro. Eles simplesmente fazem coisas diferentes, e o único sinal disso são
quatro espaços. É por isso que indentação errada é o bug mais silencioso do módulo.

### `if/else`: um caminho ou o outro

```python
if temperatura >= 25:
    print("Está quente!")
else:
    print("Está frio!")
```

O `else` não tem condição — ele é o "em todos os outros casos". Sempre exatamente um dos dois blocos
executa; nunca os dois, nunca nenhum.

### `if/elif/else`: várias faixas

```python
if nota >= 9:
    print("Conceito A")
elif nota >= 7:
    print("Conceito B")
elif nota >= 5:
    print("Conceito C")
else:
    print("Conceito D")
```

O Python testa **de cima para baixo e para no primeiro que der `True`**. Os demais nem são
avaliados.

Isso tem uma consequência que derruba muita gente: **a ordem importa**.

```python
# ERRADO
if nota >= 5:
    print("Conceito C")
elif nota >= 9:        # inalcançável! quem tem 9 já parou no primeiro
    print("Conceito A")
```

Com nota 10, o primeiro `if` já é verdadeiro e o programa imprime "Conceito C". O `elif` de baixo
nunca roda para valor nenhum.

**Regra prática: em faixas numéricas, comece pela ponta mais restritiva.** Da maior nota para a
menor, ou da menor para a maior — mas sempre em ordem.

Repare também que o segundo teste não precisa repetir a faixa anterior. Não é preciso escrever
`elif nota >= 7 and nota < 9:` — se o programa chegou no `elif`, é porque o `if` de cima já foi
falso. O `elif` já carrega esse "senão" embutido.

### Condicionais aninhadas

Um `if` pode morar dentro de outro:

```python
if numero > 0:
    print("Positivo")
    if numero % 2 == 0:
        print("E par")
    else:
        print("E ímpar")
elif numero < 0:
    print("Negativo")
else:
    print("Zero")
```

Aninhar funciona, mas cobra caro na leitura. **Se você chegou ao terceiro nível de indentação, pare
e pense**: normalmente dá para trocar por um `and`, ou para inverter a condição e sair mais cedo.

```python
# Aninhado
if tem_conta:
    if saldo > 0:
        print("Pode sacar")

# Achatado: mesma coisa, uma leitura só
if tem_conta and saldo > 0:
    print("Pode sacar")
```

### Proteger antes de agir

Este é o padrão que fecha a promessa aberta no módulo 03:

```python
if numero_de_pessoas == 0:
    print("Não dá para dividir a conta por zero pessoas.")
else:
    print(f"Cada um paga R$ {total / numero_de_pessoas:.2f}")
```

Repare que a divisão está **dentro do `else`**. Testar não basta — a operação perigosa precisa
ficar no caminho onde já se sabe que é segura.

### `match/case`: quando o teste é "qual das opções"

A partir do Python 3.10 existe uma segunda forma de decidir, feita para um caso específico:
comparar **uma variável** com **vários valores exatos**.

```python
match opcao:
    case 1:
        print("Somar")
    case 2:
        print("Subtrair")
    case 3 | 4:                 # o | significa "ou"
        print("Multiplicar ou dividir")
    case _:                     # o _ é o "qualquer outro caso"
        print("Opção inválida")
```

O `case _` faz o papel do `else`.

**Quando usar cada um:**

| Situação | Prefira |
| --- | --- |
| Comparar uma variável com valores exatos (menu, código, opção) | `match/case` |
| Testar **faixas** (`nota >= 7`) | `if/elif` |
| Combinar condições com `and`/`or` | `if/elif` |
| Testar variáveis diferentes em cada ramo | `if/elif` |

`match/case` não substitui o `if` — ele resolve melhor um caso só, que é o menu de opções. Tudo que
ele faz, o `if/elif` também faz; o argumento é de legibilidade.

## Exemplos guiados

| Arquivo | O que mostra |
| --- | --- |
| [exemplos/01_if_else.py](exemplos/01_if_else.py) | `if`, `if/else` e o peso da indentação |
| [exemplos/02_elif_e_ordem.py](exemplos/02_elif_e_ordem.py) | faixas de nota e o `elif` inalcançável |
| [exemplos/03_aninhadas_e_protecao.py](exemplos/03_aninhadas_e_protecao.py) | aninhar, achatar e proteger da divisão por zero |
| [exemplos/04_match_case.py](exemplos/04_match_case.py) | menu com `match/case` e o mesmo menu com `elif` |

Para rodar qualquer um deles:

```bash
cd modulo-04-condicionais/exemplos
python 01_if_else.py
```

## Exercícios

1. [EXERCICIO-01-classificador-de-imc.md](exercicios/EXERCICIO-01-classificador-de-imc.md) — faixas
   com `elif`, na ordem certa.
2. [EXERCICIO-02-calculadora-com-menu.md](exercicios/EXERCICIO-02-calculadora-com-menu.md) — menu com
   `match/case` e proteção contra divisão por zero.

## Auto-avaliação

- [ ] Sei explicar por que mover uma linha quatro espaços muda o programa
- [ ] Escrevo uma cadeia de `elif` sem deixar nenhum ramo inalcançável
- [ ] Sei por que não preciso escrever `elif nota >= 7 and nota < 9`
- [ ] Protejo uma divisão testando o divisor **antes** de dividir
- [ ] Sei transformar um `if` aninhado em um `if` com `and`
- [ ] Sei dizer quando `match/case` lê melhor que `elif`

## Erros comuns

| Erro | O que está acontecendo |
| --- | --- |
| `SyntaxError: expected ':'` | faltou o dois-pontos no fim da linha do `if` |
| `IndentationError: expected an indented block` | o bloco depois do `if` não foi recuado |
| Linha executa sempre, mesmo com condição falsa | ela ficou fora do bloco; confira a indentação |
| `elif` que nunca roda | a ordem das faixas está invertida; comece pela mais restritiva |
| `if nota = 10:` | `=` atribui, `==` compara; dá `SyntaxError` |
| `if 0 < nota or nota > 10:` | intervalo proibido pede a lógica do módulo 02; reveja `and`/`or` |
| `ZeroDivisionError` mesmo com `if` | a divisão ficou fora do `else`, no caminho inseguro |
| `match` dá `SyntaxError` | você está num Python anterior ao 3.10; confira com `python --version` |
| `case _:` nunca executa | algum `case` acima já cobre tudo |

---

Anterior: [Módulo 03 — Entrada e saída](../modulo-03-entrada-e-saida/) | Próximo: [Módulo 05 — Laços de repetição](../modulo-05-lacos-de-repeticao/)
