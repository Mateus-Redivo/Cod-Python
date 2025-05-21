# Enunciado 2: Ordene um vetor de 7 números utilizando QuickSort.

def quicksort(lista):
    # Caso base: se a lista tiver 1 ou menos elementos, já está ordenada
    if len(lista) <= 1:
        return lista

    # Seleciona o elemento do meio como pivô para melhor performance em média
    pivo = lista[len(lista) // 2]

    # Divide a lista em três partes:
    # menores: todos os elementos menores que o pivô
    menores = [x for x in lista if x < pivo]
    # iguais: todos os elementos iguais ao pivô
    iguais = [x for x in lista if x == pivo]
    # maiores: todos os elementos maiores que o pivô
    maiores = [x for x in lista if x > pivo]

    # Recursivamente ordena as sublistas e concatena o resultado:
    # 1. Ordena a lista de elementos menores
    # 2. Adiciona os elementos iguais ao pivô
    # 3. Ordena a lista de elementos maiores
    return quicksort(menores) + iguais + quicksort(maiores)


# Cria uma lista com 7 números inseridos pelo usuário
numeros = [int(input("Digite um número: ")) for _ in range(7)]
# Aplica o algoritmo quicksort para ordenar a lista
numeros = quicksort(numeros)
# Exibe a lista ordenada
print("Lista ordenada:", numeros)
