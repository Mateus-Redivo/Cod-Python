"""
Módulo 11 — Algoritmos de ordenação
Exemplo 04: contando comparações e trocas

Este arquivo mostra:
  - os três algoritmos instrumentados, contando operações
  - a mesma lista nos três, para comparar de verdade
  - o abismo que aparece quando a lista cresce

Como executar:
  python 04_comparando_custos.py
"""

import random
import time


def bubble_sort(lista):
    lista = lista[:]
    comparacoes = trocas = 0
    n = len(lista)
    for i in range(n):
        for j in range(n - i - 1):
            comparacoes += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1
    return comparacoes, trocas


def selection_sort(lista):
    lista = lista[:]
    comparacoes = trocas = 0
    for i in range(len(lista)):
        menor = i
        for j in range(i + 1, len(lista)):
            comparacoes += 1
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
        trocas += 1
    return comparacoes, trocas


def insertion_sort(lista):
    lista = lista[:]
    comparacoes = movimentacoes = 0
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > atual:
            comparacoes += 1
            lista[j + 1] = lista[j]
            movimentacoes += 1
            j -= 1
        if j >= 0:
            comparacoes += 1        # a comparação que fez o while parar
        lista[j + 1] = atual
    return comparacoes, movimentacoes


# --- A mesma lista nos três ------------------------------------------
lista = [64, 34, 25, 12, 22, 11, 90, 45, 78, 3]

print(f"Lista: {lista}")
print(f"{len(lista)} elementos")
print()
print(f"{'Algoritmo':<12}{'Comparações':>13}{'Trocas/mov.':>13}")
print("-" * 38)

for nome, funcao in [("Bubble", bubble_sort),
                     ("Selection", selection_sort),
                     ("Insertion", insertion_sort)]:
    comparacoes, trocas = funcao(lista)
    print(f"{nome:<12}{comparacoes:>13}{trocas:>13}")

print()
print("Bubble e Selection comparam igual — os dois olham todos os pares.")
print("A diferença está nas trocas: Selection faz uma por passagem.")
print("Insertion compara menos: o while para assim que acha o lugar.")
print()


# --- O abismo quando a lista cresce ----------------------------------
print("=" * 52)
print("O que acontece quando a lista cresce")
print("=" * 52)
print(f"{'Tamanho':>9}{'Comparações (Bubble)':>22}{'sort() (s)':>14}")
print("-" * 52)

for tamanho in [10, 100, 500, 2000]:
    aleatoria = [random.randint(1, 10000) for _ in range(tamanho)]

    comparacoes, _ = bubble_sort(aleatoria)

    inicio = time.perf_counter()
    sorted(aleatoria)
    duracao = time.perf_counter() - inicio

    print(f"{tamanho:>9}{comparacoes:>22,}{duracao:>14.6f}")

print()
print("As comparações do Bubble crescem com o QUADRADO do tamanho:")
print("dobrar a lista quadruplica o trabalho. O sort() do Python")
print("continua instantâneo — é Timsort, escrito em C.")
print()
print("Moral: entenda os algoritmos, use o sort().")


# --- Experimento ---------------------------------------------------
# 1. Acrescente 5000 na lista de tamanhos e rode. Ainda é rápido?
#    (Cuidado: 10000 pode demorar bastante.)
#
# 2. Troque a lista aleatória por uma já ordenada,
#    "aleatoria = list(range(tamanho))". As comparações do Bubble
#    mudam? E se fosse a versão com a flag do exemplo 01?
#
# 3. Instrumente o quick_sort do exemplo 03 do mesmo jeito e compare.
