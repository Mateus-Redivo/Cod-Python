"""
Exercício 23 - Valores Extremos em Matriz
Desenvolva um programa em Python que:

Crie uma matriz 3x3 com valores inteiros digitados pelo usuário
Encontre o valor mínimo e o valor máximo presentes na matriz, bem como suas respectivas posições
Exiba a matriz formatada na tela
Mostre o menor e o maior valor encontrados, junto com suas posições na matriz no formato (linha, coluna)
Observação: Implemente a busca pelos valores mínimos e máximos sem utilizar as funções prontas min() e max() do Python.
"""

def encontrar_min_max_matriz(matriz):
    """
    Encontra os valores mínimos e máximos da matriz manualmente,
    sem usar funções prontas como min() e max()
    """
    # Inicializa com o primeiro elemento da matriz
    menor = matriz[0][0]
    maior = matriz[0][0]
    pos_menor = (0, 0)
    pos_maior = (0, 0)
    
    # Percorre a matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            # Verifica se encontrou um valor menor
            if matriz[i][j] < menor:
                menor = matriz[i][j]
                pos_menor = (i, j)
            # Verifica se encontrou um valor maior    
            if matriz[i][j] > maior:
                maior = matriz[i][j]
                pos_maior = (i, j)
    
    return menor, pos_menor, maior, pos_maior

def criar_matriz():
    """Cria uma matriz 3x3 com valores digitados pelo usuário"""
    matriz = []
    for i in range(3):
        linha = []
        for j in range(3):
            valor = int(input(f"Digite o valor para posição [{i}][{j}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def exibir_matriz(matriz):
    """Exibe a matriz de forma organizada"""
    print("\nMatriz:")
    for linha in matriz:
        for valor in linha:
            print(f"{valor:4}", end="")
        print()

def main():
    # Cria a matriz
    print("Digite os valores para a matriz 3x3:")
    matriz = criar_matriz()
    
    # Exibe a matriz
    exibir_matriz(matriz)
    
    # Encontra os valores mínimos e máximos
    menor, pos_menor, maior, pos_maior = encontrar_min_max_matriz(matriz)
    
    # Exibe os resultados
    print(f"\nMenor valor: {menor} na posição {pos_menor}")
    print(f"Maior valor: {maior} na posição {pos_maior}")

if __name__ == "__main__":
    main()