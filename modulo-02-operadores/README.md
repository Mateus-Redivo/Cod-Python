# Módulo 02 — Operadores

Seu programa já guarda valores. Agora ele vai **fazer contas** com eles, **compará-los** e
**combinar** essas comparações. Os operadores deste módulo são a matéria-prima das decisões que
você vai escrever no módulo 04: sem eles, o `if` não teria o que testar.

## Objetivos de aprendizagem

Ao final deste módulo você será capaz de:

- [ ] Usar os sete operadores aritméticos, incluindo `//`, `%` e `**`
- [ ] Explicar para que serve o resto da divisão em problemas do dia a dia
- [ ] Prever o resultado de uma expressão respeitando a ordem de precedência
- [ ] Escrever comparações que resultam em `True` ou `False`
- [ ] Combinar condições com `and`, `or` e `not`
- [ ] Explicar por que comparar decimais com `==` às vezes dá errado

## Pré-requisitos

[Módulo 01 — Tipos e variáveis](../modulo-01-tipos-e-variaveis/) concluído. Você precisa saber a
diferença entre `int`, `float` e `str`: o mesmo operador se comporta de um jeito com cada tipo.

## Conceito

### Aritméticos: os quatro conhecidos e os três novos

Os quatro primeiros você já usa desde a escola: `+`, `-`, `*` e `/`. Os outros três são os que
resolvem problemas que a matemática do papel resolve de outro jeito.

| Operador | Nome | `10 op 3` dá |
| --- | --- | --- |
| `+` | soma | `13` |
| `-` | subtração | `7` |
| `*` | multiplicação | `30` |
| `/` | divisão | `3.3333333333333335` |
| `//` | divisão inteira | `3` |
| `%` | resto da divisão | `1` |
| `**` | potência | `1000` |

**`/` sempre devolve `float`**, mesmo quando a conta é exata: `4 / 2` dá `2.0`. Se você quer o
inteiro, o operador é `//`.

### O `%` é mais útil do que parece

O resto da divisão parece curiosidade escolar, mas resolve três problemas que aparecem o tempo todo:

```python
numero % 2 == 0        # o número é par?
numero % 3 == 0        # é múltiplo de 3?
segundos % 60          # quantos segundos sobram depois dos minutos inteiros
```

Guarde o primeiro: "par ou ímpar" é `% 2` e vai aparecer em quase todo módulo daqui para frente.

### Precedência: a conta não é da esquerda para a direita

```python
2 + 3 * 4       # 14, não 20
```

Python segue a ordem da matemática:

1. `()`: parênteses
2. `**`: potência
3. `*`, `/`, `//`, `%`
4. `+`, `-`

Você não precisa decorar isso. Precisa de um hábito melhor: **na dúvida, use parênteses.** Eles não
custam nada, não deixam o programa mais lento e poupam quem for ler o código depois (inclusive
você).

```python
media = nota1 + nota2 / 2       # ERRADO: divide só a nota2
media = (nota1 + nota2) / 2     # certo
```

Esse erro específico derruba muita gente na primeira lista de exercícios.

### Comparação: perguntas que só têm duas respostas

| Operador | Pergunta |
| --- | --- |
| `==` | são iguais? |
| `!=` | são diferentes? |
| `>` | maior? |
| `<` | menor? |
| `>=` | maior ou igual? |
| `<=` | menor ou igual? |

Toda comparação devolve `True` ou `False`: um `bool`, o tipo do módulo 01. E isso significa que
você pode guardá-la numa variável:

```python
idade = 20
eh_maior_de_idade = idade >= 18     # guarda True
print(eh_maior_de_idade)
```

Essa variável de nome descritivo é o que vai deixar seu `if` legível no módulo 04.

> **`=` guarda, `==` pergunta.** É o erro mais frequente do módulo. Em Python, escrever
> `if idade = 18:` nem roda: dá `SyntaxError`. É uma gentileza da linguagem. Em outras, isso
> compila e produz um bug silencioso.

### Comparação também funciona com texto

```python
"Ana" == "Ana"      # True
"Ana" < "Bruno"     # True — ordem alfabética
```

Cuidado: a comparação usa a tabela de caracteres, e nela **maiúsculas vêm antes das minúsculas**.
Por isso `"Zebra" < "ana"` dá `True`, o que não é a ordem do dicionário. O módulo 07 mostra como
resolver isso comparando tudo em minúsculas.

### Lógicos: combinando perguntas

| Operador | Devolve `True` quando |
| --- | --- |
| `and` | **as duas** condições são verdadeiras |
| `or` | **pelo menos uma** é verdadeira |
| `not` | inverte: `not True` vira `False` |

```python
pode_dirigir = idade >= 18 and tem_carteira
tem_desconto = eh_vip or valor_compra > 100
precisa_login = not usuario_logado
```

A precedência entre eles é `not` > `and` > `or`. Mesma recomendação de antes: **parênteses**.

### A armadilha do intervalo

Esta merece seção própria, porque custa horas a quem não conhece:

```python
# "número entre 1 e 5"  -> intervalo PERMITIDO -> and
numero >= 1 and numero <= 5

# "número FORA de 1 a 5" -> intervalo PROIBIDO -> or
numero < 1 or numero > 5
```

Trocar um pelo outro produz um programa que **roda sem erro e faz a coisa errada**: o pior tipo
de bug. `numero < 1 and numero > 5` é impossível de satisfazer: nada é menor que 1 e maior que 5 ao
mesmo tempo.

Regra de bolso: **dentro de um intervalo é `and`; fora dele é `or`**.

Python ainda oferece um atalho que outras linguagens não têm:

```python
1 <= numero <= 5        # idêntico ao and, e lê melhor
```

### Por que `0.1 + 0.2` não dá `0.3`

```python
print(0.1 + 0.2)            # 0.30000000000000004
print(0.1 + 0.2 == 0.3)     # False
```

Isso não é bug do Python: é como todo computador guarda números decimais, em binário. Alguns
valores não têm representação exata, e sobra uma poeirinha no fim.

A consequência prática: **não compare `float` com `==`**. Compare a diferença:

```python
abs((0.1 + 0.2) - 0.3) < 0.0001     # True
```

Para dinheiro e notas, arredondar na hora de exibir (`{valor:.2f}`) resolve na prática.

## Exemplos guiados

| Arquivo | O que mostra |
| --- | --- |
| [exemplos/01_aritmeticos.py](exemplos/01_aritmeticos.py) | os sete operadores e para que serve o `%` |
| [exemplos/02_precedencia.py](exemplos/02_precedencia.py) | a ordem das contas e o erro da média |
| [exemplos/03_comparacao.py](exemplos/03_comparacao.py) | comparações, o `bool` guardado e a cilada dos decimais |
| [exemplos/04_logicos.py](exemplos/04_logicos.py) | `and`, `or`, `not` e a armadilha do intervalo |

Para rodar qualquer um deles:

```bash
cd modulo-02-operadores/exemplos
python 01_aritmeticos.py
```

## Exercícios

1. [EXERCICIO-01-calculadora-de-tempo.md](exercicios/EXERCICIO-01-calculadora-de-tempo.md) (nível 1): `//` e `%` resolvendo um problema real.
2. [EXERCICIO-02-regras-de-acesso.md](exercicios/EXERCICIO-02-regras-de-acesso.md) (nível 2): traduzir regras em português para expressões lógicas.
3. [EXERCICIO-03-anatomia-de-um-numero.md](exercicios/EXERCICIO-03-anatomia-de-um-numero.md) (nível 3): desmontar um número só com aritmética.

## Auto-avaliação

- [ ] Sei quando usar `/` e quando usar `//`
- [ ] Sei testar se um número é par sem pensar duas vezes
- [ ] Calculo `2 + 3 * 4` de cabeça e acerto
- [ ] Sei por que `media = a + b / 2` está errado
- [ ] Escolho entre `and` e `or` olhando se o intervalo é permitido ou proibido
- [ ] Sei explicar por que `0.1 + 0.2 == 0.3` é `False`

## Erros comuns

| Erro | O que está acontecendo |
| --- | --- |
| `media = a + b / 2` | precedência: só o `b` foi dividido; use `(a + b) / 2` |
| `if nota = 10:` | `=` atribui, `==` compara; isso dá `SyntaxError` |
| `numero < 1 and numero > 5` | intervalo proibido pede `or`; com `and` a condição nunca é verdadeira |
| `numero >= 1 or numero <= 5` | intervalo permitido pede `and`; com `or` tudo passa |
| Esperar `2` de `4 / 2` | `/` sempre devolve `float`; o resultado é `2.0` |
| `0.1 + 0.2 == 0.3` dá `False` | decimais não têm representação exata; compare a diferença |
| `"Zebra" < "ana"` dá `True` | maiúsculas vêm antes das minúsculas na tabela de caracteres |
| `2 ** 3 ** 2` dá `512`, não `64` | a potência resolve da direita para a esquerda |

---

Anterior: [Módulo 01 — Tipos e variáveis](../modulo-01-tipos-e-variaveis/) | Próximo: [Módulo 03 — Entrada e saída](../modulo-03-entrada-e-saida/)
