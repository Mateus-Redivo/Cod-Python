# Módulo 06 — Listas

Você já sabe guardar um valor e já sabe repetir. Agora junte as duas coisas: e se você precisar
guardar **trinta notas**? Trinta variáveis? `nota1`, `nota2`, `nota3`… e um `input()` para cada uma?

A lista é a resposta: **um nome só para muitos valores**.

## Objetivos de aprendizagem

Ao final deste módulo você será capaz de:

- [ ] Criar listas e acessar seus elementos por índice
- [ ] Explicar por que o primeiro índice é 0 e o que faz o índice `-1`
- [ ] Percorrer uma lista com `for`, das duas formas: por valor e por índice
- [ ] Adicionar, alterar e remover elementos
- [ ] Usar `len()`, `sum()`, `max()`, `min()` e `in`
- [ ] Fatiar uma lista com `[inicio:fim]`
- [ ] Reconhecer e evitar o `IndexError`

## Pré-requisitos

[Módulo 05 — Laços de repetição](../modulo-05-lacos-de-repeticao/) concluído. Este módulo é a
aplicação natural do `for`: lista sem laço é quase inútil, e o padrão acumulador que você treinou
lá é exatamente o que vai usar aqui.

## Conceito

### O problema: uma variável por valor não escala

Para calcular a média de cinco notas, sem listas:

```python
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
nota4 = float(input("Nota 4: "))
nota5 = float(input("Nota 5: "))
media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
```

Funciona. Agora faça para trinta alunos. Ou para "quantos o usuário quiser", e aí simplesmente não
dá, porque você teria que escrever as variáveis antes de saber quantas serão.

**Quando você numera nomes de variáveis, é uma lista pedindo para nascer.**

```python
notas = [8.0, 7.5, 9.0, 6.5, 10.0]
media = sum(notas) / len(notas)
```

Duas linhas, e funciona para cinco ou cinco mil.

### Criar e acessar

```python
notas = [8, 7, 10, 6]
nomes = ["Ana", "Bruno", "Carlos"]
vazia = []
```

O acesso é por **índice**, entre colchetes:

```python
cores = ["vermelho", "azul", "verde", "amarelo"]
#           0          1       2          3
#          -4         -3      -2         -1

cores[0]      # "vermelho"  <- o PRIMEIRO é o zero
cores[2]      # "verde"
cores[-1]     # "amarelo"   <- o último, sem precisar saber o tamanho
cores[-2]     # "verde"
```

### O índice começa em zero

Esta é a fonte de metade dos erros do módulo, e vale entender em vez de decorar.

O índice não diz "qual elemento", diz **"quantos elementos pular"**. O primeiro não pula nenhum,
então é `0`. Numa lista de 4 itens, os índices válidos vão de `0` a `3`: **nunca** `4`.

```python
cores[4]      # IndexError: list index out of range
```

Por isso o último elemento é `lista[len(lista) - 1]`. Ou, muito melhor, `lista[-1]`.

### `len()` e as funções que economizam laço

```python
notas = [8, 7, 10, 6]

len(notas)      # 4     quantos elementos
sum(notas)      # 31    soma tudo
max(notas)      # 10    o maior
min(notas)      # 6     o menor
```

No módulo 05 você somou com um acumulador e um `for`. Continua valendo, e continua sendo o que
você vai escrever quando a soma tiver alguma condição. Mas para somar tudo, `sum()` resolve.

### `in`: está na lista?

```python
if "banana" in frutas:
    print("Tem banana")
```

Devolve `True` ou `False`, e serve direto num `if`. Bem mais legível que percorrer procurando.

### Percorrer: as duas formas

**Por valor**, quando você só precisa do conteúdo:

```python
for nota in notas:
    print(nota)
```

**Por índice**, quando você precisa saber a posição, ou vai alterar a lista:

```python
for i in range(len(notas)):
    print(f"Nota {i + 1}: {notas[i]}")
```

A primeira é mais limpa e deve ser sua escolha padrão. Use a segunda só quando a posição importar
de verdade.

> Repare no `range(len(notas))`: `len` dá 4, e `range(4)` produz 0, 1, 2, 3, exatamente os índices
> válidos. Não é coincidência; é o motivo de o índice começar em zero.

### Modificar a lista

```python
animais = ["gato", "cachorro", "peixe"]

animais[1] = "hamster"          # troca o da posição 1
animais.append("coelho")        # acrescenta no fim
animais.insert(1, "pássaro")    # insere na posição 1, empurrando o resto
animais.remove("peixe")         # remove pelo VALOR (o primeiro que achar)
ultimo = animais.pop()          # remove o último e devolve
animais.sort()                  # ordena a própria lista
animais.reverse()               # inverte a própria lista
```

Repare na diferença de escrita: `len(lista)` é uma **função** que recebe a lista;
`lista.append(x)` é um **método**, chamado com ponto, que pertence à lista. Você vai ver os dois
estilos a vida toda.

### O detalhe que pega: métodos que não devolvem nada

```python
notas.sort()                    # certo: ordena a própria lista
notas = notas.sort()            # ERRADO: notas vira None!
```

`sort()`, `reverse()` e `append()` modificam a lista **no lugar** e devolvem `None`. Atribuir o
resultado destrói sua lista, e o erro só aparece na linha seguinte.

Se você quer a lista ordenada **sem mexer na original**, a função é outra:

```python
ordenadas = sorted(notas)       # devolve uma nova, preserva a original
```

### Fatiar

```python
numeros = [10, 20, 30, 40, 50]

numeros[1:3]     # [20, 30]      do 1 até ANTES do 3
numeros[:3]      # [10, 20, 30]  do começo
numeros[2:]      # [30, 40, 50]  até o fim
numeros[-2:]     # [40, 50]      os dois últimos
```

O limite final é exclusivo: a mesma regra do `range()` do módulo 05. Não é coincidência: é a mesma
ideia de "vai até, sem incluir".

## Exemplos guiados

| Arquivo | O que mostra |
| --- | --- |
| [exemplos/01_criando_e_acessando.py](exemplos/01_criando_e_acessando.py) | criar, indexar, índice negativo e `IndexError` |
| [exemplos/02_percorrendo.py](exemplos/02_percorrendo.py) | `for` por valor e por índice, com acumulador |
| [exemplos/03_modificando.py](exemplos/03_modificando.py) | `append`, `insert`, `remove`, `pop`, `sort` e a cilada do `None` |
| [exemplos/04_fatiando.py](exemplos/04_fatiando.py) | fatias e as funções `len`, `sum`, `max`, `min` |

Para rodar qualquer um deles:

```bash
cd modulo-06-listas/exemplos
python 01_criando_e_acessando.py
```

## Exercícios

1. [EXERCICIO-01-manipulando-listas.md](exercicios/EXERCICIO-01-manipulando-listas.md)
   (nível 1): previsão de saída e caça ao bug.
2. [EXERCICIO-02-boletim.md](exercicios/EXERCICIO-02-boletim.md)
   (nível 2): ler notas para uma lista e resumi-las.
3. [EXERCICIO-03-apuracao-de-votos.md](exercicios/EXERCICIO-03-apuracao-de-votos.md)
   (nível 3): contar votos, achar o vencedor e detectar empate.

## Auto-avaliação

- [ ] Sei explicar por que o primeiro índice é 0, sem só repetir que "é assim"
- [ ] Sei pegar o último elemento de duas formas diferentes
- [ ] Percorro uma lista por valor e por índice, e sei quando cada uma serve
- [ ] Sei por que `notas = notas.sort()` destrói a lista
- [ ] Somo os elementos de uma lista com `sum()` e também com acumulador
- [ ] Já provoquei um `IndexError` de propósito

## Erros comuns

| Erro | O que está acontecendo |
| --- | --- |
| `IndexError: list index out of range` | usou um índice que não existe; o último é `len(lista) - 1` |
| `lista = lista.sort()` transforma em `None` | `sort()` modifica no lugar e devolve `None`; use só `lista.sort()` |
| `lista.remove(0)` não remove a posição 0 | `remove()` age pelo **valor**; para posição, use `pop(0)` ou `del` |
| `for i in notas:` e depois `notas[i]` | aqui `i` já é o valor, não o índice; escolha uma das duas formas |
| `range(len(lista))` gerando índice inválido | não gera; se deu erro, o `+1` está sobrando em algum lugar |
| Alterar a lista enquanto a percorre | o `for` se perde; monte outra lista ou percorra de trás para frente |
| `ZeroDivisionError` ao calcular média | a lista está vazia; teste `if len(lista) > 0` antes de dividir |
| `sum()` numa lista de textos | `sum` só soma números; texto não |

---

Anterior: [Módulo 05 — Laços de repetição](../modulo-05-lacos-de-repeticao/) | Próximo: [Módulo 07 — Strings](../modulo-07-strings/)
