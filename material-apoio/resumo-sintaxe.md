# Resumo de sintaxe Python

Cola de consulta rápida. Não é material de estudo. É o que você abre no meio de um exercício
quando esqueceu **como se escreve**. Para saber *o que significa*, use o [Glossário](../GLOSSARIO.md).

---

## Variáveis e tipos

```python
nome = "Maria"          # str   - texto, entre aspas
idade = 20              # int   - inteiro
altura = 1.75           # float - decimal, com PONTO
aprovado = True         # bool  - True ou False

type(idade)             # <class 'int'> - descobre o tipo
NOTA_MINIMA = 6.0       # constante: por convenção, MAIÚSCULA
```

## Entrada e saída

```python
print("Olá")
print("Nota:", 8.5)                 # separa com espaço automaticamente
print("sem quebra de linha", end="")

nome = input("Digite seu nome: ")   # devolve SEMPRE string
idade = int(input("Idade: "))       # converte para inteiro
preco = float(input("Preço: "))     # converte para decimal
```

### f-strings

```python
print(f"Olá, {nome}! Você tem {idade} anos.")
print(f"Média: {media:.2f}")        # 2 casas decimais
print(f"{7} x {3} = {7 * 3}")       # aceita expressão dentro das chaves
```

## Operadores

| Aritméticos | | Comparação | | Lógicos |
| --- | --- | --- | --- | --- |
| `+` soma | | `==` igual a | | `and` e |
| `-` subtração | | `!=` diferente de | | `or` ou |
| `*` multiplicação | | `>` maior | | `not` não |
| `/` divisão (dá float) | | `<` menor | | |
| `//` divisão inteira | | `>=` maior ou igual | | |
| `%` resto da divisão | | `<=` menor ou igual | | |
| `**` potência | | | | |

```python
7 / 2       # 3.5
7 // 2      # 3
7 % 2       # 1     <- resto: use para testar par/ímpar e múltiplos
2 ** 10     # 1024

contador += 1       # atalho para: contador = contador + 1
soma += nota        # funciona com -=, *=, /= também
```

## Condicionais

```python
if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")

if idade >= 18 and possui_carteira:
    print("Pode dirigir")
```

### match / case (Python 3.10+)

```python
match opcao:
    case 1:
        print("Somar")
    case 2 | 3:
        print("Subtrair ou multiplicar")
    case _:
        print("Opção inválida")
```

## Laços

```python
# while - repete ENQUANTO a condição for verdadeira
contador = 1
while contador <= 5:
    print(contador)
    contador += 1

# for + range - repete um número conhecido de vezes
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 11):      # 1 até 10 (o 11 NÃO entra)
    print(i)

for i in range(0, 11, 2):   # 0, 2, 4, 6, 8, 10
    print(i)

for i in range(10, 0, -1):  # contagem regressiva: 10 até 1
    print(i)

# for direto na lista
for nota in notas:
    print(nota)
```

```python
break       # sai do laço imediatamente
continue    # pula o resto desta volta e vai para a próxima
```

### Padrão acumulador

```python
soma = 0                    # ANTES do laço, sempre
for numero in numeros:
    soma += numero
media = soma / len(numeros)
```

## Listas

```python
notas = [8, 7, 10, 6]
vazia = []

notas[0]            # 8      - primeiro item (índice começa em ZERO)
notas[-1]           # 6      - último item
notas[1:3]          # [7, 10] - fatia: do 1 até antes do 3
len(notas)          # 4      - quantidade de itens

notas.append(9)             # adiciona no fim
notas.insert(0, 5)          # insere na posição 0
notas.remove(7)             # remove o primeiro 7 encontrado
notas.pop()                 # remove e devolve o último
notas.sort()                # ordena no lugar
notas.reverse()             # inverte no lugar

sum(notas)  max(notas)  min(notas)  sorted(notas)

if 8 in notas:              # testa se existe
    print("achou")
```

## Strings

```python
nome = "Maria Silva"

len(nome)               # 11
nome.upper()            # "MARIA SILVA"
nome.lower()            # "maria silva"
nome.strip()            # remove espaços das pontas
nome.replace("a", "@")  # troca todas as ocorrências
nome.split(" ")         # ["Maria", "Silva"]
nome[0]                 # "M"
nome[-1]                # "a"
"Silva" in nome         # True
```

## Matrizes (listas de listas)

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
]

matriz[0][2]        # 3 - linha 0, coluna 2
len(matriz)         # 2 - número de linhas
len(matriz[0])      # 3 - número de colunas

for linha in range(len(matriz)):
    for coluna in range(len(matriz[0])):
        print(matriz[linha][coluna], end=" ")
    print()
```

## Funções

```python
def calcular_media(nota1, nota2):
    """Devolve a média de duas notas."""
    return (nota1 + nota2) / 2

media = calcular_media(8, 6)        # 7.0


def saudar(nome, saudacao="Olá"):   # parâmetro com valor padrão
    print(f"{saudacao}, {nome}!")

saudar("Maria")                     # Olá, Maria!
saudar("João", "Bom dia")           # Bom dia, João!
```

## Tratamento de erros

```python
try:
    idade = int(input("Idade: "))
except ValueError:
    print("Isso não é um número inteiro.")
```

| Exceção | Acontece quando |
| --- | --- |
| `ValueError` | `int("abc")`: o texto não vira número |
| `ZeroDivisionError` | divisão por zero |
| `IndexError` | `lista[10]` numa lista de 3 itens |
| `TypeError` | `"3" + 5`: tipos incompatíveis |
| `NameError` | usou uma variável que não existe (quase sempre erro de digitação) |

## Comentários

```python
# comentário de uma linha

"""
Docstring: usada no topo de arquivos e funções
para explicar o que aquilo faz.
"""
```

---

Convenções de escrita de código (marcadores `TODO`, `FIXME`, `NOTE`…) estão no
[guia de comentários](guia-de-comentarios.md).
