# Exercício 01 — Operações com matrizes

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 1 de 3 | 35 min | laços aninhados, `[linha][coluna]`, funções |

## Objetivo

Implementar as três operações básicas de matriz (soma, transposta e multiplicação por escalar),
cada uma como uma função.

## Requisitos

1. Crie um arquivo `operacoes_com_matrizes.py`.
2. Escreva as funções abaixo. Todas devem **devolver uma matriz nova**, sem alterar as recebidas.

| Função | Recebe | Devolve |
| --- | --- | --- |
| `somar_matrizes(a, b)` | duas matrizes de mesmo tamanho | a soma, elemento a elemento |
| `transpor(matriz)` | uma matriz | linhas viram colunas |
| `multiplicar_por_escalar(matriz, numero)` | matriz e número | cada elemento multiplicado |
| `mostrar_matriz(matriz)` | uma matriz | nada: imprime formatado |

3. Use as matrizes de teste abaixo e mostre o resultado de cada operação.
4. Nenhuma função pode alterar a matriz que recebeu (confira imprimindo a original no fim).

```python
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[10, 20, 30],
     [40, 50, 60]]
```

## Exemplo de saída

```text
Matriz A:
     1   2   3
     4   5   6

Matriz B:
    10  20  30
    40  50  60

A + B:
    11  22  33
    44  55  66

Transposta de A:
     1   4
     2   5
     3   6

A x 3:
     3   6   9
    12  15  18

A continua intacta:
     1   2   3
     4   5   6
```

## A parte que exige atenção

Na **transposta**, o resultado tem dimensões trocadas: uma matriz 2x3 vira 3x2. Isso significa que
você não pode criar a matriz de saída com o mesmo tamanho da entrada.

```python
linhas_da_saida = len(matriz[0])      # colunas da entrada
colunas_da_saida = len(matriz)        # linhas da entrada
```

E o elemento: `transposta[j][i] = matriz[i][j]`.

## Critérios de aceitação

- [ ] As quatro funções existem, e três delas devolvem matriz nova
- [ ] `A` continua intacta depois de todas as operações
- [ ] A transposta de uma 2x3 é uma 3x2
- [ ] Nenhuma matriz foi criada com `[[0] * n] * m`
- [ ] As funções usam `len()`, e não os números 2 e 3 fixos
- [ ] Testei com uma matriz 1x1 e com uma 3x3

## Desafio opcional

Escreva `somar_matrizes` de forma que ela recuse matrizes de tamanhos diferentes, avisando em vez de
produzir resultado errado ou quebrar. O que ela deveria devolver nesse caso?

---

Gabarito: [gabaritos/modulo-09/ex01-operacoes-com-matrizes/](../../gabaritos/modulo-09/ex01-operacoes-com-matrizes/), depois de tentar, não antes.
