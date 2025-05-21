# Desenvolva um programa que permita manipular um vetor de números inteiros com as seguintes funcionalidades:

# 1. O usuário deve poder especificar o tamanho do vetor e preencher seus valores
# 2. O programa deve oferecer um menu com as seguintes operações:
#     - Ordenar o vetor(usando Bubble Sort)
#     - Encontrar o valor máximo e mínimo
#     - Dobrar todos os elementos
#     - Inverter a ordem dos elementos
#     - Visualizar o vetor atual
#     - Restaurar o vetor ao estado original
# 3. Após cada operação que modifica o vetor, o usuário deve poder escolher se deseja manter as alterações
# 4. O programa deve continuar executando até que o usuário escolha sair
# 5. Todas as operações devem ser implementadas sem usar funções prontas do Python


def ordenar_vetor(vetor):
    """
    Ordena o vetor usando Bubble Sort e retorna um novo vetor
    Parâmetro: vetor - lista de números
    Retorno: novo_vetor - nova lista ordenada
    """
    # Cria uma cópia do vetor original para não modificá-lo
    novo_vetor = vetor.copy()
    # Implementação do algoritmo Bubble Sort - compara pares adjacentes
    for i in range(len(novo_vetor)):
        for j in range(i + 1, len(novo_vetor)):
            # Se o elemento atual for maior que o próximo, troca suas posições
            if novo_vetor[i] > novo_vetor[j]:
                novo_vetor[i], novo_vetor[j] = novo_vetor[j], novo_vetor[i]
    return novo_vetor


def encontrar_max_min(vetor):
    """
    Encontra valores máximo e mínimo sem modificar o vetor original
    Parâmetro: vetor - lista de números
    Retorno: tupla (máximo, mínimo)
    """
    # Inicializa máximo e mínimo com o primeiro elemento do vetor
    maximo = minimo = vetor[0]
    # Percorre o vetor a partir do segundo elemento para comparações
    for x in vetor[1:]:
        # Atualiza o máximo se encontrar um valor maior
        if x > maximo:
            maximo = x
        # Atualiza o mínimo se encontrar um valor menor
        if x < minimo:
            minimo = x
    return maximo, minimo


def dobrar_elementos(vetor):
    """
    Cria um novo vetor com elementos dobrados
    Parâmetro: vetor - lista de números
    Retorno: novo_vetor - nova lista com elementos dobrados
    """
    # Inicializa uma lista vazia para armazenar os elementos dobrados
    novo_vetor = []
    # Percorre cada elemento do vetor original
    for elemento in vetor:
        # Multiplica o elemento por 2 e adiciona ao novo vetor
        novo_vetor.append(elemento * 2)
    return novo_vetor


def inverter_vetor(vetor):
    """
    Cria um novo vetor com ordem invertida
    Parâmetro: vetor - lista de números
    Retorno: novo_vetor - nova lista invertida
    """
    novo_vetor = []
    # Percorre o vetor do último ao primeiro elemento
    for i in range(len(vetor) - 1, -1, -1):
        novo_vetor.append(vetor[i])
    return novo_vetor


def main():
    # Inicializa os vetores vazios
    vetor_original = []
    vetor_atual = []

    # Obtém o tamanho do vetor do usuário
    n = int(input("Digite o tamanho do vetor: "))

    # Preenche o vetor original com valores fornecidos pelo usuário
    for i in range(n):
        valor = int(input(f"Digite o {i + 1}º valor: "))
        vetor_original.append(valor)

    # Cria uma cópia do vetor original para manipulação
    vetor_atual = vetor_original.copy()

    # Loop principal do programa
    while True:
        # Exibe o menu de opções
        print("\n=== Menu de Operações ===")
        print("1 - Ordenar vetor")
        print("2 - Encontrar valor máximo e mínimo")
        print("3 - Dobrar elementos")
        print("4 - Inverter vetor")
        print("5 - Mostrar vetor atual")
        print("6 - Restaurar vetor original")
        print("0 - Sair")

        # Obtém a escolha do usuário
        opcao = input("\nEscolha uma opção: ")

        # Estrutura match-case para processar a escolha do usuário
        match opcao:
            case "1":
                # Ordena o vetor e mostra o resultado
                novo_vetor = ordenar_vetor(vetor_atual)
                print("Vetor original:", vetor_atual)
                print("Novo vetor ordenado:", novo_vetor)
                # Permite ao usuário manter ou descartar as alterações
                if input("Deseja manter o novo vetor? (s/n): ").lower() == 's':
                    vetor_atual = novo_vetor

            case "2":
                # Encontra e exibe os valores máximo e mínimo
                maximo, minimo = encontrar_max_min(vetor_atual)
                print(f"Valor máximo: {maximo}")
                print(f"Valor mínimo: {minimo}")

            case "3":
                # Dobra os elementos e mostra o resultado
                novo_vetor = dobrar_elementos(vetor_atual)
                print("Vetor original:", vetor_atual)
                print("Novo vetor com elementos dobrados:", novo_vetor)
                # Permite ao usuário manter ou descartar as alterações
                if input("Deseja manter o novo vetor? (s/n): ").lower() == 's':
                    vetor_atual = novo_vetor

            case "4":
                # Inverte o vetor e mostra o resultado
                novo_vetor = inverter_vetor(vetor_atual)
                print("Vetor original:", vetor_atual)
                print("Novo vetor invertido:", novo_vetor)
                # Permite ao usuário manter ou descartar as alterações
                if input("Deseja manter o novo vetor? (s/n): ").lower() == 's':
                    vetor_atual = novo_vetor

            case "5":
                # Exibe os vetores atual e original
                print("Vetor atual:", vetor_atual)
                print("Vetor original:", vetor_original)

            case "6":
                # Restaura o vetor para seu estado original
                vetor_atual = vetor_original.copy()
                print("Vetor restaurado ao original!")

            case "0":
                # Encerra o programa
                print("Programa encerrado!")
                break

            case _:
                # Trata opções inválidas
                print("Opção inválida!")


# Ponto de entrada do programa
if __name__ == "__main__":
    main()


# Exemplos das funções usando as ferramentas inclusas no python:


# def ordenar_vetor(vetor):
#    return sorted(vetor)  # Usa a ferramenta inclusa no python para ordenar o vetor


# def encontrar_max_min(vetor):
#    return max(vetor), min(vetor)  # Retorna uma tupla com os valores máximo e mínimo


# def dobrar_elementos(vetor):
#    return [elemento * 2 for elemento in vetor]


# def dobrar_elementos(vetor):
#    return [x * 2 for x in vetor]  # Compreensão de lista para multiplicar cada elemento por 2


# def inverter_vetor(vetor):
#    return vetor[::-1] # Utiliza slice com passo -1 para inverter a ordem dos elementos
