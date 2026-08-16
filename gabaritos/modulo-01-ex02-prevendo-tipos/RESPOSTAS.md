# Gabarito — Módulo 01, Exercício 02: Prevendo tipos e resultados

Enunciado: [EXERCICIO-02-prevendo-tipos.md](../../modulo-01-tipos-e-variaveis/exercicios/EXERCICIO-02-prevendo-tipos.md)

> Se você chegou aqui sem ter preenchido a tabela primeiro, feche. O exercício mede onde o seu
> modelo mental de tipos falha: ler a resposta antes apaga exatamente a informação que ele
> produziria.

---

## Parte 1 — Tabela completa

| # | Expressão | Resultado | Tipo |
| --- | --- | --- | --- |
| 1 | `7 + 3` | `10` | `int` |
| 2 | `7 / 2` | `3.5` | `float` |
| 3 | `7 // 2` | `3` | `int` |
| 4 | `"7" + "3"` | `'73'` | `str` |
| 5 | `"7" * 3` | `'777'` | `str` |
| 6 | `7 + 3.0` | `10.0` | `float` |
| 7 | `"7" + 3` | **erro** | `TypeError` |
| 8 | `int("7") + 3` | `10` | `int` |
| 9 | `float("7") + 3` | `10.0` | `float` |
| 10 | `int("7.5")` | **erro** | `ValueError` |
| 11 | `str(7) + "3"` | `'73'` | `str` |
| 12 | `True + True` | `2` | `int` |

Mensagens exatas dos dois erros:

```text
TypeError: can only concatenate str (not "int") to str
ValueError: invalid literal for int() with base 10: '7.5'
```

---

## Parte 2 — Explicações

**a) Por que `7 / 2` devolve `float`?**

Porque em Python 3 o operador `/` é **sempre** divisão real: ele devolve `float` mesmo quando a
conta dá exata. `4 / 2` resulta em `2.0`, não `2`.

Isso é uma decisão de projeto da linguagem: o resultado de uma divisão não deveria mudar de tipo
conforme os números escolhidos. Se você quer o inteiro, o operador é `//`, como na linha 3.

**b) Diferença entre a linha 4 e a linha 8**

As duas partem de `"7"`, mas fazem perguntas diferentes:

- Linha 4 (`"7" + "3"`) trata os dois como **texto**: o `+` gruda, e o resultado é `'73'`. Ninguém
  somou nada: é o mesmo mecanismo de `"bom" + "dia"`.
- Linha 8 (`int("7") + 3`) **converte** o texto para número antes. Aí o `+` soma de verdade, e o
  resultado é `10`.

A lição: o `+` não tem um significado só. Quem decide o que ele faz é o **tipo dos operandos**.

**c) Por que a linha 10 quebra e a 9 não?**

O nome da função é a resposta. `int()` converte para **inteiro**, e `"7.5"` não é a escrita de um
inteiro. O Python não arredonda por conta própria: arredondar seria adivinhar sua intenção
(7? 8?), e ele prefere reclamar.

`float()` converte para **decimal**, e `"7"` é uma escrita perfeitamente válida de decimal, vira
`7.0`. Converter "para mais preciso" funciona; "para menos preciso" exige que você diga como.

Se você quisesse mesmo o inteiro a partir de `"7.5"`, a conversão é em duas etapas:

```python
int(float("7.5"))       # 7 — descarta a parte decimal
```

**d) O que a linha 12 revela sobre `bool`?**

Que `bool` é um `int` disfarçado. Em Python, `True` vale 1 e `False` vale 0: literalmente, a ponto
de `True + True` dar `2` e `type(True + True)` ser `int`.

Isso não é curiosidade inútil: a partir do módulo 05 é um atalho comum para contar quantas vezes
uma condição foi verdadeira, somando os próprios booleanos.

---

## Parte 3 — O programa quebrado

**a)** A mensagem completa:

```text
Traceback (most recent call last):
  File "programa.py", line 3, in <module>
    total = primeiro_valor + segundo_valor
            ~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~
TypeError: can only concatenate str (not "int") to str
```

O problema é `primeiro_valor = "10"` estar entre aspas: é o texto `"10"`, não o número `10`.

**b) Duas correções**

Tratando como **números** (provavelmente o que se queria):

```python
primeiro_valor = "10"
segundo_valor = 5
total = int(primeiro_valor) + segundo_valor
print("Total:", total)          # Total: 15
```

Tratando como **texto**:

```python
primeiro_valor = "10"
segundo_valor = 5
total = primeiro_valor + str(segundo_valor)
print("Total:", total)          # Total: 105
```

**Quando cada uma faz sentido?**

A primeira, sempre que os valores representam **quantidades**: preços, notas, idades. É o caso
esmagadoramente mais comum, e é o que você vai fazer no módulo 03 com tudo que vier do `input()`.

A segunda, quando os valores são **rótulos que só parecem números**: código de produto, CPF, CEP,
número de telefone. Aí somar não faz sentido nenhum: ninguém quer o resultado de somar dois CEPs.
O sinal de alerta é: "faz sentido calcular a média disso?" Se não faz, é texto.

Repare que as duas versões rodam sem erro e dão respostas completamente diferentes: `15` e `105`.
O Python não tinha como escolher por você. Por isso ele parou e perguntou.

---

## O que rever, conforme onde você errou

| Errou em | Volte para |
| --- | --- |
| Linhas 2, 3, 6 | seção "Os quatro tipos básicos" do [README](../../modulo-01-tipos-e-variaveis/) |
| Linhas 4, 5, 7, 11 | [exemplos/04_somando_tipos.py](../../modulo-01-tipos-e-variaveis/exemplos/04_somando_tipos.py) |
| Linhas 8, 9, 10 | as conversões voltam com força no módulo 03: vale reler depois de estudá-lo |
| Linha 12 | Experimento 3 do [exemplos/04_somando_tipos.py](../../modulo-01-tipos-e-variaveis/exemplos/04_somando_tipos.py) |
| Parte 3 | seção "O mesmo `+` faz duas coisas diferentes" do [README](../../modulo-01-tipos-e-variaveis/) |
