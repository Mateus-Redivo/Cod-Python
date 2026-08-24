# Gabarito — Módulo 06, Exercício 01: Manipulando listas

Enunciado: [EXERCICIO-01-manipulando-listas.md](../../modulo-06-listas/exercicios/EXERCICIO-01-manipulando-listas.md)

> Escreva as previsões antes de abrir. Sem isso, o exercício vira leitura passiva.

---

## Parte 1 — Efeito de cada operação

Partindo de `lista = [10, 20, 30, 40, 50]`, cada linha continua da anterior:

| # | Operação | `lista` fica | O que aconteceu |
| --- | --- | --- | --- |
| 1 | `lista.append(60)` | `[10, 20, 30, 40, 50, 60]` | acrescenta no fim |
| 2 | `lista.insert(0, 5)` | `[5, 10, 20, 30, 40, 50, 60]` | insere na posição 0, empurra todo o resto |
| 3 | `lista.remove(30)` | `[5, 10, 20, 40, 50, 60]` | remove o **valor** 30 |
| 4 | `lista.pop()` | `[5, 10, 20, 40, 50]` | remove o último (60) |
| 5 | `lista.pop(0)` | `[10, 20, 40, 50]` | remove a **posição** 0 (o 5) |
| 6 | `lista.reverse()` | `[50, 40, 20, 10]` | inverte no lugar |
| 7 | `lista.sort()` | `[10, 20, 40, 50]` | ordena no lugar, desfazendo o reverse |

**O par 3 e 5 é o ponto da parte.** `remove(30)` procura o **valor** 30 e o elimina. `pop(0)`
elimina a **posição** 0, seja lá qual valor esteja nela.

O erro que isso previne: quem quer remover o primeiro elemento e escreve `lista.remove(0)` não
remove a posição 0: ele procura o **valor** `0`, não acha, e recebe
`ValueError: list.remove(x): x not in list`.

---

## Parte 2 — Índices e fatias

Com `numeros = [10, 20, 30, 40, 50]`:

| # | Expressão | Resultado |
| --- | --- | --- |
| 1 | `numeros[0]` | `10` |
| 2 | `numeros[-1]` | `50` |
| 3 | `numeros[1:3]` | `[20, 30]` |
| 4 | `numeros[:2]` | `[10, 20]` |
| 5 | `numeros[3:]` | `[40, 50]` |
| 6 | `numeros[1:10]` | `[20, 30, 40, 50]` |
| 7 | `numeros[3:1]` | `[]` |
| 8 | `numeros[5]` | **`IndexError: list index out of range`** |
| 9 | `len(numeros[1:3])` | `2` |
| 10 | `sum(numeros[:2])` | `30` |

### Por que a fatia não dá erro e o índice dá

As duas surpresas são a 6 e a 7, e a explicação é a mesma para as duas.

**Índice e fatia respondem perguntas diferentes.**

`numeros[5]` pergunta: *"me dê o elemento da posição 5"*. Ou esse elemento existe, ou não existe.
Não existindo, não há resposta possível, e devolver algo inventado seria pior que o erro. Daí o
`IndexError`.

`numeros[1:10]` pergunta: *"me dê os elementos das posições 1 até 9"*. Essa pergunta **sempre tem
resposta**, mesmo que parcial ou vazia: são os elementos que existem nessa faixa. A lista acaba no
índice 4, então a fatia entrega o que há (`[20, 30, 40, 50]`) e para.

Pela mesma lógica, `numeros[3:1]` pede "do 3 até antes do 1". Andando para frente a partir do 3,
nunca se chega ao 1. Não há nenhum elemento nessa faixa, e a resposta correta é a lista vazia `[]`,
não um erro.

Isso é útil na prática: `lista[:3]` pega "até três elementos" sem você precisar checar se a lista
tem três. Já `lista[2]` sempre exige a checagem.

---

## Parte 3 — Bug A: o `None`

```python
notas = [7, 5, 9]
notas = notas.sort()
print("A maior nota é", notas[-1])
```

**a) A mensagem:**

```text
TypeError: 'NoneType' object is not subscriptable
```

**b) Por que fala em `None`?**

Porque `notas.sort()` faz duas coisas: ordena a lista **no lugar** e devolve `None`. A linha
`notas = notas.sort()` joga fora a lista ordenada e guarda o `None` no lugar dela.

Na linha seguinte, `notas[-1]` tenta indexar um `None`. "Not subscriptable" quer dizer "não aceita
colchetes": `None` não é uma coleção, não tem posições.

O que torna esse bug caro é que **a linha do erro não é a linha do problema**. O estrago aconteceu
na linha 2; a reclamação sai na linha 3. Sempre que aparecer `NoneType` num erro, procure uma
atribuição que recebeu o retorno de um método que modifica no lugar.

**c) As duas correções:**

Com `sort()`, ordena a lista existente, sem atribuir:

```python
notas = [7, 5, 9]
notas.sort()                        # sem o "notas ="
print("A maior nota é", notas[-1])  # 9
```

Com `sorted()`, devolve uma lista nova e preserva a original:

```python
notas = [7, 5, 9]
ordenadas = sorted(notas)
print("A maior nota é", ordenadas[-1])   # 9
print("ordem original preservada:", notas)   # [7, 5, 9]
```

**Qual usar?** `sort()` quando a ordem original não importa mais. `sorted()` quando você ainda
precisa dela (por exemplo, para mostrar as notas na ordem em que foram digitadas **e** o ranking).

E vale notar: para achar a maior nota, nenhuma das duas era necessária. `max(notas)` responde
direto, sem ordenar nada.

---

## Parte 3 — Bug B: o `+ 1` no índice

```python
numeros = [10, 20, 30, 40]
for i in range(len(numeros)):
    print(numeros[i + 1])
```

**a) O erro:**

```text
IndexError: list index out of range
```

Ele acontece na **última** iteração. `len(numeros)` é 4, então `range(4)` produz 0, 1, 2, 3. Nas
três primeiras voltas, `i + 1` vale 1, 2 e 3, índices válidos, e o programa imprime 20, 30 e 40.
Na quarta, `i` vale 3 e `i + 1` vale 4, que não existe.

Repare que **o programa imprime três linhas antes de quebrar**. Um erro que aparece só no fim do
laço é fácil de não notar em teste rápido.

**b) O que se queria fazer**

Quase certamente, numerar as notas a partir de 1 na exibição, confundindo a numeração **mostrada**
com o índice **usado**. O `+ 1` pertence ao texto, não ao acesso.

**c) A correção**

```python
numeros = [10, 20, 30, 40]
for i in range(len(numeros)):
    print(f"Item {i + 1}: {numeros[i]}")
```

O `+ 1` saiu de dentro dos colchetes e foi para a f-string. O acesso usa `i` puro, que já percorre
exatamente os índices válidos.

E se a posição não importa, a forma preferida dispensa o índice inteiro:

```python
for numero in numeros:
    print(numero)
```

---

## O que rever, conforme onde você errou

| Errou em | Volte para |
| --- | --- |
| Parte 1, itens 3 e 5 | [exemplos/03_modificando.py](../../modulo-06-listas/exemplos/03_modificando.py), bloco "remove é por valor, pop é por posição" |
| Parte 2, itens 6 e 7 | [exemplos/04_fatiando.py](../../modulo-06-listas/exemplos/04_fatiando.py) e os Experimentos dele |
| Parte 2, item 8 | seção "O índice começa em zero" do [README](../../modulo-06-listas/) |
| Bug A | seção "Métodos que não devolvem nada" do [README](../../modulo-06-listas/) |
| Bug B | [exemplos/02_percorrendo.py](../../modulo-06-listas/exemplos/02_percorrendo.py), Experimento 1 |
