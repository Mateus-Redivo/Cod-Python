# Exercício 04 — Análise de código

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 2 de 3 | 40 min | leitura de código, previsão de saída, depuração |

## Objetivo

Ler código escrito por outra pessoa, prever o que ele faz **sem rodar** e consertar o que estiver
quebrado. Essa é a habilidade que separa quem escreve código de quem entende código.

## Como fazer

Responda cada questão **antes** de executar qualquer coisa. Escreva sua previsão, depois rode e
compare. Onde você errou é exatamente onde está o aprendizado — anote esses pontos.

Entregue as respostas em um arquivo `respostas.md` (ou no formato que o professor pedir), com o
código das questões que pedem implementação.

---

## Questão 1 — Prever a saída

```python
total = 0
for i in range(1, 11):
    if i % 2 == 0:
        continue
    total += i
print(total)
```

**a)** Qual é o valor impresso ao final?
**b)** O que o `continue` faz nesse contexto? Quais números realmente entram na soma?
**c)** Reescreva sem usar `continue`, mantendo exatamente o mesmo resultado.

---

## Questão 2 — Prever a saída

```python
resultado = 1
for i in range(1, 6):
    resultado *= i
print(resultado)
```

**a)** Qual é o valor impresso?
**b)** Que operação matemática isso representa?
**c)** Por que `resultado` começa em 1, e não em 0?
**d)** Modifique para o usuário informar N, validando que N seja um inteiro entre 1 e 10. Use
`while` para a validação, sem `try/except`.

---

## Questão 3 — Encontre o bug

Este código deveria pedir uma senha numérica entre 1000 e 9999 e só aceitar quando ela for válida.
Mas ele não faz isso.

```python
senha = int(input("Digite a senha (1000-9999): "))
if senha < 1000 or senha > 9999:
    print("Senha inválida!")
    senha = int(input("Digite novamente: "))
print("Senha aceita:", senha)
```

**a)** Qual é o bug? Descreva a sequência de digitações que expõe o problema.
**b)** Corrija o código para que ele insista até o usuário digitar um valor válido. Use `while`.

---

## Questão 4 — Encontre o bug

```python
numero = int(input("Digite um número entre 1 e 5: "))
while numero < 1 and numero > 5:
    print("Fora do intervalo!")
    numero = int(input("Digite novamente: "))
print("Número válido:", numero)
```

**a)** Digite 99 e observe. O que aconteceu, e por quê?
**b)** Qual operador lógico está errado? Explique com suas palavras por que o outro é o correto.
**c)** Corrija o código.

---

## Questão 5 — Laço dentro de laço

```python
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(i * j, end="  ")
        j += 1
    print()
    i += 1
```

**a)** Quantas vezes o `print` interno é executado?
**b)** Escreva a saída completa do programa, linha por linha.
**c)** O que esse código gera visualmente?
**d)** Por que `j = 1` está **dentro** do laço externo? O que mudaria se estivesse fora?

---

## Questão 6 — Flag e `break`

```python
numero = int(input("Digite um número: "))
primo = True
for i in range(2, numero):
    if numero % i == 0:
        primo = False
        break
if primo and numero > 1:
    print(f"{numero} é primo")
else:
    print(f"{numero} não é primo")
```

**a)** O que a variável `primo` representa? Por que ela começa como `True`?
**b)** Por que o `range` começa em 2, e não em 1?
**c)** Por que existe a condição `numero > 1` no `if` final?
**d)** O que acontece se o usuário digitar 1? E se digitar 2? Rastreie o laço nos dois casos.
**e)** Acrescente validação: o número deve ser inteiro positivo. Use `while`, sem `try/except`.

---

## Critérios de aceitação

- [ ] Todas as previsões de saída foram escritas **antes** de rodar o código
- [ ] As respostas de "por quê" explicam o mecanismo, não só repetem o resultado
- [ ] Os códigos corrigidos rodam e resolvem de fato o problema descrito
- [ ] As validações usam `while` e não deixam passar valor inválido
- [ ] Cada previsão errada está anotada com o motivo do erro

---

Gabarito: [gabaritos/modulo-05-ex04-analise-de-codigo/](../../gabaritos/modulo-05-ex04-analise-de-codigo/) —
depois de tentar, não antes. Este exercício em particular perde todo o valor se você ler a resposta
primeiro: o objetivo é justamente descobrir onde a sua leitura de código falha.
