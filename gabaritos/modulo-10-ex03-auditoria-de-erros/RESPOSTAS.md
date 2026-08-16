# Gabarito — Módulo 10, Exercício 03: Auditoria de erros

Enunciado: [EXERCICIO-03-auditoria-de-erros.md](../../modulo-10-tratamento-de-erros/exercicios/EXERCICIO-03-auditoria-de-erros.md)

> Forme a sua opinião antes de ler a minha. Este exercício é sobre julgamento, e julgamento não se
> aprende lendo: se aprende decidindo e depois conferindo.

---

## Parte 1 — As oito situações

A regra que organiza todas: **`try` para o que está fora do seu controle; `if` para o que está
dentro; deixar quebrar quando o erro é um bug seu.**

| # | Situação | Resposta | Por quê |
| --- | --- | --- | --- |
| 1 | `int()` na idade digitada | **T** | O que o usuário digita está fora do seu controle. Não há `if` que impeça `int("abc")` de explodir: a explosão é a própria detecção. |
| 2 | Dividir pela quantidade de uma lista que você montou | **P** | Você sabe se a lista está vazia: `if len(lista) > 0` responde antes de tentar. Prevenir declara a intenção; capturar sugere um imprevisto que não existe. |
| 3 | `lista[0]` de lista vinda de outra função | **P** | Também dá para checar antes com `if len(lista) > 0`. A lista vem de código seu, então o contrato é seu, e um `IndexError` aqui significa que você não conferiu. |
| 4 | Chamar função com nome errado | **D** | É bug de digitação. O `NameError` é o aviso, e escondê-lo com `try` transformaria um erro de dez segundos num mistério de duas horas. |
| 5 | Ler arquivo cujo nome o usuário informou | **T** | Clássico caso de "fora do controle": o arquivo pode não existir, estar sem permissão, ter sumido entre a checagem e a leitura. |
| 6 | `matriz[i][j]` em laços seus com `range(len(...))` | **D** | Se estourar, o `range` está errado: é bug seu. O `IndexError` aponta exatamente onde. Capturá-lo esconderia o defeito e produziria resultados incompletos em silêncio. |
| 7 | Opção de menu de 1 a 4 | **T e P** | As duas coisas, e é a lição do exercício: `try` para a conversão (pode vir letra), `if` para a faixa (o 9 é um inteiro perfeitamente válido, só não serve). |
| 8 | `float()` de valor lido de uma lista de números | **D** | Se a lista é de números, a conversão não falha. Se falhar, a lista não era o que você pensava, e isso é um problema de origem dos dados, que você quer descobrir agora, não mascarar. |

**Sobre o caso 3**, uma ressalva honesta: se a outra função é de terceiros e o contrato dela não é
claro, `try` passa a ser defensável. A resposta muda conforme o quanto você controla o código
vizinho, e isso é normal em decisões de projeto.

---

## Parte 2 — Os três programas

### Programa A — o `except` pelado e o `try` inchado

**Problemas, dois:**

1. `except:` sem tipo captura **tudo**, inclusive um erro de digitação seu na linha do `print`.
2. O `try` engloba três linhas, mas só a primeira pode falhar. Se o `print` tivesse um bug, a
   mensagem seria "Erro", como se o usuário tivesse digitado errado.

E um terceiro, menor: a mensagem "Erro" não diz nada a quem está do outro lado.

**Correção:**

```python
try:
    idade = int(input("Idade: "))
except ValueError:
    print("Digite um número inteiro.")
else:
    ano_nascimento = 2026 - idade
    print(f"Você nasceu em {ano_nascimento}")
```

O `try` ficou com uma linha só; o resto foi para o `else`. Agora um bug no cálculo aparece como bug,
não como "erro do usuário".

### Programa B — inventar um valor

**O problema:** `media = 0` para uma turma vazia é **mentira**. Uma turma sem notas e uma turma que
tirou zero em tudo passam a ser indistinguíveis no relatório.

Além disso, dava para prevenir: você montou a lista, então sabe se ela está vazia.

**Correção:**

```python
notas = []

if len(notas) > 0:
    media = sum(notas) / len(notas)
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhuma nota informada.")
```

Sem `try` nenhum. A situação era conhecida, e conhecida se resolve com `if`.

### Programa C — o `except: pass`

**O problema:** o `pass` engole o erro sem dizer nada. O usuário digita "abc", nada acontece, o
programa pergunta de novo, e ele não faz ideia do que fez de errado. Parece um programa travado.

**Correção:**

```python
while True:
    try:
        numero = int(input("Número: "))
        break
    except ValueError:
        print("Digite um número inteiro.")
```

Uma linha a mais, e o programa passa a ser utilizável. **Um `except` que só faz `pass` quase sempre
é um erro**: se não vale nem avisar, provavelmente não valia capturar.

---

## Parte 3 — Por que o `calcular_media` "seguro" é perigoso

```python
def calcular_media(notas):
    try:
        return sum(notas) / len(notas)
    except:
        return 0
```

Ele nunca quebra, e é justamente esse o problema: **ele transformou todo defeito possível no número
zero**, que é um valor plausível e por isso não levanta suspeita.

Pelo menos quatro coisas diferentes acabam viradas em `0`:

1. **Lista vazia** (`ZeroDivisionError`): não há média, mas o relatório dirá que ela é zero.
2. **Lista com texto dentro** (`TypeError` no `sum`): os dados estão corrompidos, e ninguém vai
   saber. Uma nota digitada como `"8"` em vez de `8` some sem rastro.
3. **`notas` sendo `None`** (`TypeError` no `len`): a função anterior falhou e devolveu `None`, e
   este `except` apaga a evidência.
4. **Erro de digitação dentro da própria função**: se você escrevesse `sum(nota)` no singular, o
   `NameError` seria capturado e a função devolveria zero para sempre, silenciosamente.

O agravante é o **valor escolhido**. `0` é um número legítimo de média: ninguém olha um relatório
com média zero e pensa "isto deve ser um bug". Se a função devolvesse `None`, ao menos quebraria
adiante, apontando para o problema.

E há o efeito de longo prazo: **este código não pode ser corrigido, porque não pode ser
diagnosticado**. Seis meses depois, alguém nota que as médias estão erradas em alguns casos, e não
há mensagem, log ou rastro para investigar. O bug foi construído para ser invisível.

**A versão honesta:**

```python
def calcular_media(notas):
    if len(notas) == 0:
        return None            # "não há média" é diferente de "a média é 0"
    return sum(notas) / len(notas)
```

Nenhum `try`. O único caso previsível é a lista vazia, e ele é tratado com `if`. Qualquer outro
problema (texto na lista, `None` no lugar da lista) continua explodindo, que é exatamente o que
você quer que aconteça enquanto ainda dá tempo de consertar.

---

## A regra para levar

> Capturar um erro é assumir a responsabilidade de resolvê-lo. Se você não sabe o que fazer com
> ele, não o capture: deixe que alguém que saiba o veja.
