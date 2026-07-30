"""
Gabarito — Módulo 11, Exercício 01: Implementando os três

Enunciado:
  modulo-11-algoritmos-de-ordenacao/exercicios/EXERCICIO-01-implementando-os-tres.md

Como executar:
  python tres_ordenacoes.py
"""


def bubble_sort(lista):
    """Empurra o maior para o fim, comparando vizinhos."""
    n = len(lista)
    for i in range(n):
        # n - i - 1: os i últimos JÁ estão no lugar.
        # Usar n daria IndexError no lista[j + 1].
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


def selection_sort(lista):
    """Acha o menor do resto e o traz para a posição i."""
    for i in range(len(lista)):
        # Guarda o ÍNDICE, não o valor: é o índice que permite trocar.
        indice_do_menor = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[indice_do_menor]:
                indice_do_menor = j
        lista[i], lista[indice_do_menor] = lista[indice_do_menor], lista[i]


def insertion_sort(lista):
    """Encaixa cada elemento entre os que já estão ordenados."""
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > atual:
            lista[j + 1] = lista[j]
            j -= 1                  # sem isto, loop infinito
        lista[j + 1] = atual


def bubble_sort_com_bandeira(lista):
    """Bubble que para assim que uma passagem não faz trocas."""
    n = len(lista)
    passagens = 0
    for i in range(n):
        passagens += 1
        trocou = False
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
        if not trocou:
            break
    return passagens


# --- Teste -----------------------------------------------------------
LISTAS_DE_TESTE = [
    [64, 34, 25, 12, 22, 11],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [7],
    [],                             # o caso que o enunciado pede para testar
]

for nome, funcao in [("BUBBLE SORT", bubble_sort),
                     ("SELECTION SORT", selection_sort),
                     ("INSERTION SORT", insertion_sort)]:
    print(f"=== {nome} ===")
    for original in LISTAS_DE_TESTE:
        copia = original[:]         # cópia: senão o 2º algoritmo mede errado
        funcao(copia)
        # sorted() só na CONFERÊNCIA, nunca dentro das funções.
        status = "OK" if copia == sorted(original) else "ERRO"
        print(f"{str(original):<26} -> {str(copia):<26} {status}")
    print()


# --- Desafio opcional: a bandeira ------------------------------------
print("=== BUBBLE COM BANDEIRA: passagens economizadas ===")
for original in [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [64, 34, 25, 12, 22, 11]]:
    copia = original[:]
    passagens = bubble_sort_com_bandeira(copia)
    print(f"{str(original):<26} {passagens} passagens (sem bandeira seriam {len(original)})")


# --- Por que assim -------------------------------------------------
# 1. As três ordenam NO LUGAR e não devolvem nada — como o sort() do
#    Python. Por isso são chamadas assim:
#
#      bubble_sort(minha_lista)      # certo
#      lista = bubble_sort(lista)    # ERRADO: vira None
#
#    É exatamente a cilada do módulo 06, agora do outro lado: aqui é
#    você quem escreve a função que devolve None.
#
# 2. O "copia = original[:]" no teste é obrigatório. Sem ele, o
#    primeiro algoritmo deixaria a lista ordenada e os outros dois
#    receberiam o cenário errado — medindo "já ordenada" sem saber.
#
# 3. Lista vazia funciona nas três sem tratamento especial:
#      - bubble: range(0) não executa
#      - selection: range(0) não executa
#      - insertion: range(1, 0) não executa
#    Um range vazio é um laço que roda zero vezes, não um erro. Foi o
#    que você viu no módulo 05, na questão do número primo.
#
# 4. A conferência usa "copia == sorted(original)". Comparar listas
#    com == compara elemento a elemento — é seguro.
