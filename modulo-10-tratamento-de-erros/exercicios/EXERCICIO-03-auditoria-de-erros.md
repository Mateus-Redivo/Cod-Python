# Exercício 03 — Auditoria de erros (desafio)

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 3 de 3 | 50 min | julgamento sobre tratar, prevenir ou deixar quebrar |

## Objetivo

O exercício mais difícil do módulo, e o único sem resposta única: decidir, para cada situação, se o
certo é **capturar**, **prevenir com `if`** ou **deixar quebrar**.

Escrever `try` é fácil. Saber quando não escrever é o que separa código robusto de código que
esconde defeitos.

## Parte 1 — Julgue cada caso

Para cada situação, escolha uma das três respostas e **justifique em duas frases**:

- **T** — capturar com `try`/`except`
- **P** — prevenir com `if`, sem `try`
- **D** — deixar quebrar

| # | Situação |
| --- | --- |
| 1 | O usuário digita a idade e você converte com `int()` |
| 2 | Você vai dividir a soma pela quantidade de itens de uma lista que você mesmo montou |
| 3 | Você acessa `lista[0]` de uma lista que veio de outra função |
| 4 | Você chama uma função com o nome errado (erro de digitação seu) |
| 5 | O programa lê um arquivo cujo nome o usuário informou |
| 6 | Você acessa `matriz[i][j]` dentro de laços que você mesmo escreveu com `range(len(...))` |
| 7 | O usuário escolhe uma opção de menu de 1 a 4 |
| 8 | Você converte para `float` um valor que acabou de ler de uma lista de números |

## Parte 2 — Conserte três programas

Cada um tem um problema de tratamento de erro. Diga qual é e reescreva.

### Programa A

```python
try:
    idade = int(input("Idade: "))
    ano_nascimento = 2026 - idade
    print(f"Você nasceu em {ano_nascimento}")
except:
    print("Erro")
```

### Programa B

```python
notas = []
try:
    media = sum(notas) / len(notas)
except ZeroDivisionError:
    media = 0
print(f"Média da turma: {media}")
```

### Programa C

```python
while True:
    try:
        numero = int(input("Número: "))
        break
    except ValueError:
        pass
```

## Parte 3 — A pergunta final

O programa abaixo funciona e nunca quebra:

```python
def calcular_media(notas):
    try:
        return sum(notas) / len(notas)
    except:
        return 0
```

Escreva um parágrafo respondendo: **por que este código é perigoso, apesar de nunca quebrar?**
Cite pelo menos duas coisas diferentes que podem dar errado e que ele esconderia.

## Critérios de aceitação

- [ ] As 8 situações têm resposta **e** justificativa de duas frases
- [ ] Os três programas foram reescritos e rodam
- [ ] A correção do Programa A mantém o `try` curto
- [ ] A correção do Programa B **não** inventa um valor
- [ ] A correção do Programa C avisa o usuário
- [ ] O parágrafo final cita dois problemas distintos

---

Gabarito: [gabaritos/modulo-10-ex03-auditoria-de-erros/](../../gabaritos/modulo-10-ex03-auditoria-de-erros/) —
depois de tentar, não antes. Este exercício é sobre julgamento; ler a resposta antes de formar a sua
não ensina nada.
