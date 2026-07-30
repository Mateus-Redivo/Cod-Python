"""
Gabarito — Módulo 09, Exercício 01: Operações com matrizes

Enunciado:
  modulo-09-matrizes/exercicios/EXERCICIO-01-operacoes-com-matrizes.md

Como executar:
  python operacoes_com_matrizes.py
"""


def criar_matriz(linhas, colunas, valor=0):
    """Matriz nova, com listas independentes. Nunca use [[0]*n]*m."""
    matriz = []
    for i in range(linhas):
        nova_linha = []
        for j in range(colunas):
            nova_linha.append(valor)
        matriz.append(nova_linha)
    return matriz


def somar_matrizes(a, b):
    """Soma elemento a elemento. Devolve matriz nova."""
    resultado = criar_matriz(len(a), len(a[0]))
    for i in range(len(a)):
        for j in range(len(a[0])):
            resultado[i][j] = a[i][j] + b[i][j]
    return resultado


def transpor(matriz):
    """Linhas viram colunas. Uma 2x3 devolve uma 3x2."""
    # As dimensões da saída são TROCADAS em relação à entrada.
    resultado = criar_matriz(len(matriz[0]), len(matriz))
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            resultado[j][i] = matriz[i][j]      # j e i trocados
    return resultado


def multiplicar_por_escalar(matriz, numero):
    """Cada elemento vezes o número. Devolve matriz nova."""
    resultado = criar_matriz(len(matriz), len(matriz[0]))
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            resultado[i][j] = matriz[i][j] * numero
    return resultado


def mostrar_matriz(matriz):
    for linha in matriz:
        print("  " + "".join(f"{valor:4}" for valor in linha))


# --- Uso -------------------------------------------------------------
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[10, 20, 30],
     [40, 50, 60]]

print("Matriz A:")
mostrar_matriz(A)
print()

print("Matriz B:")
mostrar_matriz(B)
print()

print("A + B:")
mostrar_matriz(somar_matrizes(A, B))
print()

print("Transposta de A:")
mostrar_matriz(transpor(A))
print()

print("A x 3:")
mostrar_matriz(multiplicar_por_escalar(A, 3))
print()

print("A continua intacta:")
mostrar_matriz(A)


# --- Por que assim -------------------------------------------------
# 1. "criar_matriz" existe para não repetir o laço duplo de criação em
#    três funções — e, principalmente, para que a forma SEGURA de criar
#    esteja escrita em um lugar só. Se alguém for tentado a usar
#    [[0]*n]*m, tem que passar por aqui.
#
# 2. Toda função devolve matriz NOVA. Nenhuma altera o que recebeu —
#    por isso "A continua intacta" no fim. Função que modifica o
#    argumento surpreende quem chama: você passa uma matriz para somar
#    e ela volta diferente.
#
# 3. Na transposta, repare em duas coisas:
#      - a criação usa len(matriz[0]) linhas e len(matriz) colunas,
#        invertidas de propósito
#      - a atribuição é resultado[j][i] = matriz[i][j]
#    Trocar só um dos dois dá IndexError numa matriz não quadrada — e,
#    numa quadrada, dá resultado errado em silêncio. Teste sempre a
#    transposta com uma matriz retangular.
#
# 4. Tudo com len(), nada com 2 e 3 fixos. É o que permite trocar A por
#    uma 5x7 sem tocar em nenhuma função.


# --- Conferência ----------------------------------------------------
# A + B: 1+10=11, 2+20=22, 3+30=33 / 4+40=44, 5+50=55, 6+60=66
#
# Transposta de A (2x3 -> 3x2):
#   A[0][0]=1 vai para T[0][0]      A[0][1]=2 vai para T[1][0]
#   A[1][0]=4 vai para T[0][1]      A[1][1]=5 vai para T[1][1]
#   resultado: [[1,4],[2,5],[3,6]]
#
# A x 3: 3, 6, 9 / 12, 15, 18


# --- Solução do desafio opcional ------------------------------------
# Recusar matrizes de tamanhos diferentes:
#
#   def somar_matrizes(a, b):
#       if len(a) != len(b) or len(a[0]) != len(b[0]):
#           return None
#       ...
#
# Devolver None é a escolha honesta: "não existe soma para estas
# duas". É o mesmo raciocínio do gabarito do módulo 08 sobre a média
# de lista vazia — inventar um resultado seria pior.
#
# E quem chama precisa testar:
#
#   soma = somar_matrizes(A, C)
#   if soma is None:
#       print("Matrizes de tamanhos diferentes não podem ser somadas.")
#   else:
#       mostrar_matriz(soma)
#
# No módulo 10 você vai ver a alternativa: levantar uma exceção em vez
# de devolver None, o que impede quem chama de ignorar o problema.
