# Enunciado 2: Implemente uma função que encontre o segundo maior número de um vetor de 8 elementos digitados pelo usuário.

def segundo_maior(lista):
    # Remove números duplicados usando set e converte de volta para lista
    lista = list(set(lista))
    # Ordena a lista em ordem crescente
    lista.sort()
    # Retorna o penúltimo elemento se a lista tiver mais de 1 elemento, senão retorna None
    return lista[-2] if len(lista) > 1 else None


# Cria uma lista com 8 números fornecidos pelo usuário usando list comprehension
numeros = [int(input("Digite um número: ")) for _ in range(8)]
# Exibe o segundo maior número encontrado
print("Segundo maior número:", segundo_maior(numeros))
