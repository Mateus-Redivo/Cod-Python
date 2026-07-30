"""
Módulo 11 — Algoritmos de ordenação
Exemplo 02: Selection Sort e Insertion Sort

Este arquivo mostra:
  - Selection: acha o menor e traz para a frente
  - Insertion: encaixa cada elemento no lugar, como cartas na mão
  - por que o Insertion brilha em lista quase ordenada

Como executar:
  python 02_selection_e_insertion.py
"""


def selection_sort_mostrando(lista):
    """A cada passagem, o menor do resto vai para a posição i."""
    for i in range(len(lista)):
        # Guarda o ÍNDICE do menor, não o valor — é o índice que
        # permite a troca depois.
        indice_do_menor = i

        for j in range(i + 1, len(lista)):
            if lista[j] < lista[indice_do_menor]:
                indice_do_menor = j

        lista[i], lista[indice_do_menor] = lista[indice_do_menor], lista[i]
        print(f"  passagem {i + 1}: {lista}   (menor encontrado: {lista[i]})")

    return lista


def insertion_sort_mostrando(lista):
    """Cada elemento é empurrado para trás até achar seu lugar."""
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1

        # Empurra para a direita todo mundo que for maior que "atual".
        while j >= 0 and lista[j] > atual:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = atual        # encaixa
        print(f"  inserindo {atual}: {lista}")

    return lista


numeros = [64, 34, 25, 12, 22, 11]

print("=== SELECTION SORT ===")
print(f"Original: {numeros}")
selection_sort_mostrando(numeros[:])
print()

print("=== INSERTION SORT ===")
print(f"Original: {numeros}")
insertion_sort_mostrando(numeros[:])
print()


# --- Onde o Insertion brilha -----------------------------------------
print("=== INSERTION com lista QUASE ordenada ===")
quase = [1, 2, 3, 5, 4, 6]
print(f"Original: {quase}")
insertion_sort_mostrando(quase[:])
print()
print("Repare: quase nada se moveu. O while para assim que acha o")
print("lugar certo, sem varrer o resto. É o melhor dos três quando a")
print("lista já está quase pronta — situação comum na vida real.")


# --- Experimento ---------------------------------------------------
# 1. No Selection, troque "indice_do_menor = j" por
#    "menor = lista[j]". Agora você tem o valor, mas não o índice —
#    e a troca da linha seguinte fica impossível. Entenda por quê.
#
# 2. No Insertion, apague o "j -= 1". Loop infinito. Ctrl + C.
#
# 3. Rode o Insertion com [6, 5, 4, 3, 2, 1] (o pior caso possível).
#    Compare a quantidade de linhas impressas com o caso quase
#    ordenado.
