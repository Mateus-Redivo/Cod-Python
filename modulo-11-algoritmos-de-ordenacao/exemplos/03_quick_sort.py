"""
Módulo 11 — Algoritmos de ordenação
Exemplo 03: Quick Sort e a ideia do pivô

Este arquivo mostra:
  - separar a lista em torno de um pivô
  - a função chamando a si mesma (recursão)
  - por que dividir sai mais barato

A recursão é conteúdo ALÉM desta trilha. Está aqui para você
reconhecer a ideia, não para dominar a técnica.

Como executar:
  python 03_quick_sort.py
"""


def quick_sort(lista, nivel=0):
    """Ordena separando em menores e maiores que o pivô."""
    recuo = "  " * nivel

    # Caso base: lista de 0 ou 1 elemento já está ordenada.
    # Sem isso, a função se chamaria para sempre.
    if len(lista) <= 1:
        print(f"{recuo}{lista} -> já ordenada")
        return lista

    pivo = lista[0]
    menores = [x for x in lista[1:] if x <= pivo]
    maiores = [x for x in lista[1:] if x > pivo]

    print(f"{recuo}{lista}")
    print(f"{recuo}  pivô = {pivo} | menores = {menores} | maiores = {maiores}")

    # A função chama A SI MESMA para cada metade.
    esquerda = quick_sort(menores, nivel + 1)
    direita = quick_sort(maiores, nivel + 1)

    resultado = esquerda + [pivo] + direita
    print(f"{recuo}junta: {esquerda} + [{pivo}] + {direita} = {resultado}")
    return resultado


numeros = [64, 34, 25, 12, 22, 11, 90]
print(f"Lista original: {numeros}")
print()
ordenada = quick_sort(numeros)
print()
print(f"Lista ordenada: {ordenada}")
print()

print("A ideia central: em vez de comparar todo mundo com todo mundo,")
print("divida o problema em dois menores e resolva cada um. É por isso")
print("que ele escala melhor — o custo cresce n*log(n), não n².")
print()
print("Repare também: este quick_sort devolve uma lista NOVA, ao")
print("contrário dos outros três, que ordenam no lugar.")


# --- Experimento ---------------------------------------------------
# 1. Apague o "if len(lista) <= 1: return lista" e rode.
#    RecursionError: a função se chama para sempre. Todo algoritmo
#    recursivo precisa de um caso base que o faça parar.
#
# 2. Rode com uma lista JÁ ordenada, como [1,2,3,4,5]. Observe os
#    recuos: as divisões ficam desbalanceadas (o pivô é sempre o
#    menor). Este é o pior caso do Quick Sort — e o motivo de
#    implementações reais escolherem o pivô com mais cuidado.
#
# 3. Troque "lista[0]" por "lista[len(lista) // 2]" como pivô e rode
#    de novo com a lista ordenada. Melhorou?
