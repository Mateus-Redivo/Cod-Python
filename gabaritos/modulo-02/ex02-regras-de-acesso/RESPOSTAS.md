# Gabarito — Módulo 02, Exercício 02: Regras de acesso

Enunciado: [EXERCICIO-02-regras-de-acesso.md](../../modulo-02-operadores/exercicios/EXERCICIO-02-regras-de-acesso.md)

> Preencha as três partes antes de abrir. A Parte 2 em especial só ensina se a previsão vier
> primeiro.

---

## Parte 1 — Traduções

```python
idade = 20
eh_socio = True
tem_convite = False
eh_fim_de_semana = True
saldo = 150.00
nota_prova = 7.5
frequencia = 85
trabalho_entregue = True

# 1. Maior de idade E sócio
pode_entrar_por_socio = idade >= 18 and eh_socio                    # True

# 2. Sócio OU tem convite
pode_entrar_por_convite = eh_socio or tem_convite                   # True

# 3. NÃO é sócio
paga_meia_entrada = not eh_socio                                    # False

# 4. Saldo DENTRO da faixa: > 100 e < 1000
pode_comprar = saldo > 100 and saldo < 1000                         # True

# 5. Três condições, todas obrigatórias
esta_aprovado = nota_prova >= 6 and frequencia >= 75 and trabalho_entregue   # True

# 6. Não é sócio E é fim de semana
precisa_de_convite = not eh_socio and eh_fim_de_semana               # False

# 7. Basta uma das duas falhar
esta_reprovado = nota_prova < 6 or frequencia < 75                   # False

# 8. Saldo FORA da faixa de 100 a 1000
saldo_fora_da_faixa = saldo < 100 or saldo > 1000                    # False
```

**O par 4 e 8 é o ponto do exercício.** As duas descrevem a mesma faixa:

- A 4 pergunta "está **dentro**?": precisa das duas condições ao mesmo tempo, então é `and`.
- A 8 pergunta "está **fora**?": basta furar por um lado, então é `or`.

E repare que uma é exatamente a negação da outra. Dá para escrever a 8 assim:

```python
saldo_fora_da_faixa = not (saldo > 100 and saldo < 1000)
```

Isso não é coincidência: é a **lei de De Morgan**. Negar um `and` vira um `or` com as partes
negadas. Você não precisa decorar o nome, mas vale reconhecer o padrão: ele explica por que trocar
`and` por `or` sem inverter as comparações produz um programa que aceita tudo.

**Sobre a regra 5:** `trabalho_entregue` entra sozinho, sem `== True`. Escrever
`trabalho_entregue == True` funciona, mas é redundante: a variável **já é** um `bool`. Comparar um
booleano com `True` é como perguntar "é verdade que é verdade?".

---

## Parte 2 — Previsões

| # | Expressão | Resultado | Por quê |
| --- | --- | --- | --- |
| 1 | `True or False and False` | `True` | `and` tem precedência: vira `True or (False and False)` = `True or False` |
| 2 | `(True or False) and False` | `False` | os parênteses forçam a outra ordem: `True and False` |
| 3 | `not True and False` | `False` | `not` vem primeiro: `(not True) and False` = `False and False` |
| 4 | `not (True and False)` | `True` | o parêntese resolve antes: `not False` |
| 5 | `5 > 3 or 10 / 0 > 1` | `True` | **não dá erro** (veja abaixo) |

**A pegadinha da 5.** A divisão por zero nunca acontece.

Python avalia expressões lógicas em **curto-circuito**: assim que o resultado já está decidido, ele
para. Como `5 > 3` é `True` e basta um lado verdadeiro para o `or` inteiro ser verdadeiro, a
segunda parte nem chega a ser calculada.

Confirme invertendo a ordem:

```python
10 / 0 > 1 or 5 > 3     # ZeroDivisionError: division by zero
```

Agora quebra, porque a parte perigosa vem primeiro.

Isso tem uso prático, e você vai reencontrá-lo no módulo 06:

```python
if quantidade > 0 and soma / quantidade > 7:    # seguro
```

Se `quantidade` for zero, o `and` para na primeira condição e a divisão nunca acontece. A ordem das
condições deixa de ser estética e passa a ser proteção.

---

## Parte 3 — O bug do `or`

```python
nota = 50
nota_valida = nota >= 0 or nota <= 10
```

**a) Por que 50 é considerada válida?**

Porque `50 >= 0` é `True`, e para o `or` basta isso. A segunda condição (`50 <= 10`, que é `False`)
nem importa mais (inclusive nem é avaliada, pelo curto-circuito da Parte 2).

**b) Testando com -30**

`-30 >= 0` é `False`, mas `-30 <= 10` é `True`. O `or` devolve `True` de novo.

**Não existe número que esse código recuse.** Todo número real ou é maior ou igual a 0, ou é menor
ou igual a 10. Muitos são as duas coisas, e nenhum não é nenhuma das duas. A condição é sempre
verdadeira, o que a torna inútil.

É o espelho exato do erro `numero < 1 and numero > 5` visto no README: lá o `and` tornava a
condição sempre falsa; aqui o `or` a torna sempre verdadeira. Os dois rodam sem erro e fazem a
coisa errada em silêncio.

**c) Correções**

Com `and`, porque o intervalo é permitido:

```python
nota = 50
nota_valida = nota >= 0 and nota <= 10
print("Nota válida?", nota_valida)          # False
```

Com o atalho de intervalo do Python, que lê melhor:

```python
nota = 50
nota_valida = 0 <= nota <= 10
print("Nota válida?", nota_valida)          # False
```

A segunda forma é preferível sempre que houver um intervalo: ela se parece com a notação
matemática, e não dá margem para trocar o operador lógico, porque não há nenhum.

---

## O que rever, conforme onde você errou

| Errou em | Volte para |
| --- | --- |
| Parte 1, regras 4 e 8 | seção "A armadilha do intervalo" do [README](../../modulo-02-operadores/) |
| Parte 1, regra 5 (usou `== True`) | seção "Comparação" do [README](../../modulo-02-operadores/) |
| Parte 2, itens 1 a 4 | [exemplos/04_logicos.py](../../modulo-02-operadores/exemplos/04_logicos.py), bloco de precedência |
| Parte 2, item 5 | curto-circuito: está explicado só aqui; vale reler antes do módulo 06 |
| Parte 3 | [exemplos/04_logicos.py](../../modulo-02-operadores/exemplos/04_logicos.py), variável `nunca` |
