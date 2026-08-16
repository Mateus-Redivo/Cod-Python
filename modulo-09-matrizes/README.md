# Módulo 09 — Matrizes

No módulo 08 você terminou com um incômodo: três listas paralelas (`produtos`, `precos`,
`estoque`) que precisavam ficar sempre na mesma ordem. Basta alguém acrescentar um item e esquecer
o preço para tudo desalinhar.

A matriz resolve isso. Ela é o que você usa quando os dados têm **duas dimensões**: uma tabela, um
tabuleiro, uma planilha, as notas de vários alunos em vários bimestres.

## Objetivos de aprendizagem

Ao final deste módulo você será capaz de:

- [ ] Criar uma matriz como lista de listas
- [ ] Acessar e alterar um elemento com `matriz[linha][coluna]`
- [ ] Percorrer uma matriz com laços aninhados
- [ ] Explicar por que o laço de fora é a linha e o de dentro a coluna
- [ ] Somar linhas, colunas e diagonais
- [ ] Criar uma matriz do tamanho que o programa precisar
- [ ] Reconhecer a armadilha do `[[0] * 3] * 3`

## Pré-requisitos

[Módulo 08 — Funções](../modulo-08-funcoes/) concluído. E os módulos 05 e 06 bem assentados: uma
matriz é uma lista de listas percorrida com laços dentro de laços. Se `for` e índice ainda te
confundem, volte antes: aqui tudo dobra.

## Conceito

### O problema: listas paralelas desalinham

```python
produtos = ["caneta", "caderno", "mochila"]
precos = [2.50, 18.90, 129.99]
estoque = [40, 12, 3]
```

O preço da mochila é `precos[2]` porque a mochila é `produtos[2]`. Essa correspondência não está
escrita em lugar nenhum: é uma **combinação** que só existe na cabeça de quem escreveu. Acrescente
um produto sem acrescentar o preço e o programa passa a mentir, ou quebra com `IndexError`.

```python
produtos = [
    ["caneta",  2.50,   40],
    ["caderno", 18.90,  12],
    ["mochila", 129.99,  3],
]
```

Agora nome, preço e quantidade viajam juntos. É impossível desalinhar.

### Uma matriz é uma lista de listas

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
```

```text
            col 0   col 1   col 2
  linha 0 [   1  ,    2  ,    3   ]
  linha 1 [   4  ,    5  ,    6   ]
  linha 2 [   7  ,    8  ,    9   ]
```

O acesso usa **dois** índices, nesta ordem:

```python
matriz[0][0]    # 1  — linha 0, coluna 0
matriz[1][2]    # 6  — linha 1, coluna 2
matriz[2][1]    # 8  — linha 2, coluna 1
```

Leia da esquerda para a direita: `matriz[1]` devolve a lista `[4, 5, 6]`; o `[2]` seguinte pega o
elemento 2 **dessa** lista. Não há mágica nova: é o índice do módulo 06 aplicado duas vezes.

**Linha primeiro, coluna depois.** Trocar a ordem não dá erro; dá o elemento errado.

### Dimensões

```python
len(matriz)         # 3  — quantas LINHAS
len(matriz[0])      # 3  — quantas COLUNAS (o tamanho da primeira linha)
```

Repare que `len(matriz)` conta linhas, não elementos. Uma matriz 3x3 tem `len` igual a 3, não 9.

### Percorrer: laços aninhados

```python
for linha in range(len(matriz)):
    for coluna in range(len(matriz[0])):
        print(matriz[linha][coluna], end=" ")
    print()        # quebra a linha ao terminar cada faixa
```

O laço de **fora** anda pelas linhas; o de **dentro**, pelas colunas de cada linha. O `print()`
vazio, entre os dois, é o que faz a saída sair em formato de tabela. Ele pertence ao laço externo.

Esse desenho é o mesmo do exemplo de laço aninhado que você analisou no módulo 05. Agora ele tem um
propósito.

Quando os índices não interessam, dá para percorrer direto:

```python
for linha in matriz:
    for valor in linha:
        print(valor, end=" ")
    print()
```

Prefira esta quando você só precisa dos valores.

### Criar uma matriz do tamanho certo

Para uma matriz cujo tamanho o programa descobre em execução:

```python
matriz = []
for i in range(linhas):
    nova_linha = []
    for j in range(colunas):
        nova_linha.append(0)
    matriz.append(nova_linha)
```

### A armadilha do `* 3`

Esta merece cuidado, porque o código parece certo e o erro é assustador:

```python
matriz = [[0] * 3] * 3      # PARECE uma matriz 3x3 de zeros
matriz[0][0] = 9
print(matriz)               # [[9, 0, 0], [9, 0, 0], [9, 0, 0]]
```

Mudou **as três linhas** de uma vez. O motivo: `* 3` não faz três cópias da lista: faz três
referências **à mesma** lista. Alterar uma altera todas, porque são a mesma.

A forma segura é a do bloco anterior, criando uma lista nova a cada volta.

### Somar linhas, colunas e diagonais

```python
soma_da_linha_1 = sum(matriz[1])            # a linha JÁ é uma lista

soma_da_coluna_1 = 0                        # a coluna não existe como lista
for linha in range(len(matriz)):
    soma_da_coluna_1 += matriz[linha][1]

soma_da_diagonal = 0                        # onde linha == coluna
for i in range(len(matriz)):
    soma_da_diagonal += matriz[i][i]
```

Repare na assimetria: somar uma **linha** é fácil porque ela é uma lista de verdade. Somar uma
**coluna** exige um laço, porque a coluna está espalhada por todas as linhas.

## Exemplos guiados

| Arquivo | O que mostra |
| --- | --- |
| [exemplos/01_criando_e_acessando.py](exemplos/01_criando_e_acessando.py) | lista de listas, dois índices, dimensões |
| [exemplos/02_percorrendo.py](exemplos/02_percorrendo.py) | laços aninhados e a saída em formato de tabela |
| [exemplos/03_somas.py](exemplos/03_somas.py) | linha, coluna, diagonais e o total |
| [exemplos/04_criando_dinamicamente.py](exemplos/04_criando_dinamicamente.py) | montar do tamanho certo e a armadilha do `* 3` |

Para rodar qualquer um deles:

```bash
cd modulo-09-matrizes/exemplos
python 01_criando_e_acessando.py
```

## Exercícios

1. [EXERCICIO-01-operacoes-com-matrizes.md](exercicios/EXERCICIO-01-operacoes-com-matrizes.md)
   (nível 1): soma, transposta e multiplicação por escalar.
2. [EXERCICIO-02-boletim-bimestral.md](exercicios/EXERCICIO-02-boletim-bimestral.md)
   (nível 2): notas de vários alunos em vários bimestres.
3. [EXERCICIO-03-jogo-da-velha.md](exercicios/EXERCICIO-03-jogo-da-velha.md)
   (nível 3): tabuleiro, jogadas e detecção de vitória.

## Para ir além

Estes assuntos ficam fora da trilha, mas o material existe e vale a curiosidade:

- **Matriz espelhada e valores extremos**: variações dos exercícios acima.
- **NumPy**: a biblioteca que faz tudo isto em uma linha, e que profissionais usam para valer.
  Fora do escopo porque o objetivo aqui é entender o mecanismo, não terceirizá-lo. Depois do módulo
  14, olhe.

## Auto-avaliação

- [ ] Sei dizer o que `matriz[2][0]` significa sem contar nos dedos
- [ ] Sei por que `len(matriz)` de uma matriz 3x3 dá 3, e não 9
- [ ] Escrevo laços aninhados e sei onde vai o `print()` que quebra a linha
- [ ] Sei somar uma coluna e explicar por que é mais trabalhoso que somar uma linha
- [ ] Já vi o `[[0] * 3] * 3` falhar e sei explicar o motivo
- [ ] Consigo criar uma matriz do tamanho que o usuário pedir

## Erros comuns

| Erro | O que está acontecendo |
| --- | --- |
| `IndexError` ao percorrer | trocou linha por coluna; o primeiro índice é sempre a linha |
| Todas as linhas mudam juntas | usou `[[0] * n] * m`; são referências à mesma lista |
| A tabela sai numa linha só | faltou o `print()` vazio no fim do laço externo |
| `TypeError: 'int' object is not subscriptable` | usou dois índices onde só havia um nível de lista |
| `len(matriz)` não é o total de elementos | ele conta linhas; o total é `len(matriz) * len(matriz[0])` |
| Soma da coluna dá errado | o índice fixo tem que ser o segundo: `matriz[linha][COLUNA]` |
| Matriz com linhas de tamanhos diferentes | `len(matriz[0])` deixa de valer para todas; confira ao criar |

---

Anterior: [Módulo 08 — Funções](../modulo-08-funcoes/) | Próximo: [Módulo 10 — Tratamento de erros](../modulo-10-tratamento-de-erros/)
