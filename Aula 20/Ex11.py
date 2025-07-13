# Função que implementa o algoritmo Insertion Sort (ordenação por inserção)
def insertion_sort(lista):
    # Percorre a lista a partir do segundo elemento (índice 1)
    for i in range(1, len(lista)):
        # Guarda o elemento atual que será comparado e inserido na posição correta
        chave = lista[i]
        # j é o índice do elemento anterior ao elemento atual
        j = i - 1

        # Move os elementos maiores que a chave uma posição para frente
        # até encontrar a posição correta para inserir a chave
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]  # Desloca o elemento maior para a direita
            j -= 1  # Move para o próximo elemento à esquerda

        # Insere a chave na posição correta encontrada
        lista[j + 1] = chave


# Cria uma lista com 5 números inseridos pelo usuário
# Usa list comprehension para solicitar cada número
numeros = [int(input("Digite um número: ")) for _ in range(5)]

# Chama a função insertion_sort para ordenar a lista
insertion_sort(numeros)

# Exibe a lista após a ordenação
print("Lista ordenada:", numeros)
