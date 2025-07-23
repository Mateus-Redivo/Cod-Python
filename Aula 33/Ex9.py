# Enunciado 1: Implemente o algoritmo Bubble Sort para ordenar uma lista de números digitados pelo usuário.

def bubble_sort(lista):
    # Obtém o tamanho da lista
    n = len(lista)

    # Loop externo: controla o número de passagens pela lista
    # A cada passagem, o maior elemento "flutua" para o final
    for i in range(n):
        # Loop interno: compara elementos adjacentes
        # (n-i-1) porque após cada passagem i, os últimos i elementos já estão ordenados
        for j in range(n - i - 1):
            # Compara elementos adjacentes
            # Se o elemento atual for maior que o próximo, troca suas posições
            if lista[j] > lista[j + 1]:
                # Realiza a troca (swap) dos elementos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


# Cria uma lista com 5 números inteiros fornecidos pelo usuário
# usando list comprehension para solicitar cada entrada
numeros = [int(input("Digite um número: ")) for _ in range(5)]

# Aplica o algoritmo de ordenação Bubble Sort na lista
bubble_sort(numeros)

# Exibe a lista após a ordenação
print("Lista ordenada:", numeros)
