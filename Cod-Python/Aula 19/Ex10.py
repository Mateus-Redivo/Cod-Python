# Enunciado 2: Ordene uma lista de 6 números inteiros digitados pelo usuário utilizando Selection Sort.

def selection_sort(lista):
    # Percorre toda a lista do início até o penúltimo elemento
    for i in range(len(lista)):
        # Assume que o elemento atual é o mínimo
        min_idx = i

        # Procura o menor elemento no resto da lista (parte não ordenada)
        for j in range(i + 1, len(lista)):
            # Se encontrar um elemento menor que o atual mínimo
            if lista[j] < lista[min_idx]:
                # Atualiza o índice do menor elemento
                min_idx = j

        # Troca o elemento atual com o menor elemento encontrado
        # Isso coloca o menor elemento na posição correta
        lista[i], lista[min_idx] = lista[min_idx], lista[i]


# Cria uma lista com 6 números inteiros fornecidos pelo usuário
# usando list comprehension para solicitar cada entrada
numeros = [int(input("Digite um número: ")) for _ in range(6)]

# Aplica o algoritmo de ordenação Selection Sort na lista
selection_sort(numeros)

# Exibe a lista após a ordenação
print("Lista ordenada:", numeros)
