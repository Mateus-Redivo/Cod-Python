"""
Módulo 11 — Algoritmos de ordenação
Exemplo 01: Bubble Sort passo a passo

Este arquivo mostra:
  - a lista depois de cada passagem
  - por que o laço interno usa n - i - 1
  - o maior valor "borbulhando" para o fim

Como executar:
  python 01_bubble_sort.py
"""


def bubble_sort_mostrando(lista):
    """Ordena mostrando o estado a cada passagem."""
    n = len(lista)

    for i in range(n):
        trocou_nesta_passagem = False

        # n - i - 1: os i últimos JÁ estão no lugar certo.
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                # A troca do módulo 01, que voltou.
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou_nesta_passagem = True

        ja_ordenados = lista[n - i - 1:]
        print(f"  passagem {i + 1}: {lista}   (fim garantido: {ja_ordenados})")

        if not trocou_nesta_passagem:
            print("  nenhuma troca: a lista já está ordenada, posso parar")
            break

    return lista


numeros = [64, 34, 25, 12, 22, 11]
print(f"Lista original: {numeros}")
print()
bubble_sort_mostrando(numeros)
print()
print(f"Lista ordenada: {numeros}")
print()


# --- Com uma lista já ordenada ---------------------------------------
print("Com a lista já ordenada:")
ja_ordenada = [1, 2, 3, 4, 5]
print(f"Lista original: {ja_ordenada}")
bubble_sort_mostrando(ja_ordenada)


# --- Experimento ---------------------------------------------------
# 1. Troque "range(n - i - 1)" por "range(n - 1)" e rode. Funciona
#    igual — só que comparando de novo posições que já estavam certas.
#    O -i é o que evita trabalho desperdiçado.
#
# 2. Troque por "range(n)" e rode. Agora dá IndexError: o j + 1
#    estourou o fim da lista.
#
# 3. Apague a "flag" trocou_nesta_passagem e o break. Rode com a lista
#    já ordenada: ele faz todas as passagens à toa. Essa flag é uma
#    otimização barata que quase ninguém lembra de escrever.
