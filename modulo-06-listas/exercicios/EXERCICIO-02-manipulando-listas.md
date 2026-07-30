# Exercício 02 — Manipulando listas

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 2 de 3 | 35 min | índices, fatias, métodos de lista, leitura de código |

## Objetivo

Prever o efeito de cada operação **antes** de rodar, e caçar os dois bugs mais caros de quem está
começando com listas.

## Parte 1 — Preveja o resultado

Para cada linha, escreva o valor final de `lista`. Cada item continua de onde o anterior parou.

```python
lista = [10, 20, 30, 40, 50]
```

| # | Operação | `lista` fica? |
| --- | --- | --- |
| 1 | `lista.append(60)` | |
| 2 | `lista.insert(0, 5)` | |
| 3 | `lista.remove(30)` | |
| 4 | `lista.pop()` | |
| 5 | `lista.pop(0)` | |
| 6 | `lista.reverse()` | |
| 7 | `lista.sort()` | |

## Parte 2 — Preveja a saída

Com `numeros = [10, 20, 30, 40, 50]`, o que cada expressão devolve?

| # | Expressão | Resultado? |
| --- | --- | --- |
| 1 | `numeros[0]` | |
| 2 | `numeros[-1]` | |
| 3 | `numeros[1:3]` | |
| 4 | `numeros[:2]` | |
| 5 | `numeros[3:]` | |
| 6 | `numeros[1:10]` | |
| 7 | `numeros[3:1]` | |
| 8 | `numeros[5]` | |
| 9 | `len(numeros[1:3])` | |
| 10 | `sum(numeros[:2])` | |

Duas delas surpreendem: a 6 e a 7. Explique por que **fatia** não dá `IndexError`, mas **índice**
dá.

## Parte 3 — Encontre o bug (dois programas)

### Bug A

```python
notas = [7, 5, 9]
notas = notas.sort()
print("A maior nota é", notas[-1])
```

**a)** Qual erro aparece? Copie a mensagem.
**b)** Por que o erro fala em `None`, se `notas` era uma lista?
**c)** Corrija de duas formas: uma usando `sort()` e outra usando `sorted()`.

### Bug B

```python
numeros = [10, 20, 30, 40]
for i in range(len(numeros)):
    print(numeros[i + 1])
```

**a)** Qual erro aparece, e em qual iteração?
**b)** O que o programador provavelmente queria fazer?
**c)** Corrija.

## Critérios de aceitação

- [ ] As 7 previsões da Parte 1 foram escritas antes de rodar
- [ ] As 10 previsões da Parte 2 também
- [ ] A explicação sobre fatia vs. índice fala do mecanismo, não só do resultado
- [ ] As duas correções do Bug A produzem o mesmo resultado por caminhos diferentes
- [ ] A correção do Bug B foi testada e roda até o fim

---

Gabarito: [gabaritos/modulo-06-ex02-manipulando-listas/](../../gabaritos/modulo-06-ex02-manipulando-listas/) —
depois de tentar, não antes.
