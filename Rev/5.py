def formatar_numeros():
    """
    Demonstração de formatação de números com diferentes precisões decimais usando f-strings.
    """
    valor = 123.456789
    
    print("Exemplos de formatação com f-strings:")
    print(f"Valor original: {valor}")
    print(f"Com 2 casas decimais: {valor:.2f}")
    print(f"Com 4 casas decimais: {valor:.4f}")
    print(f"Notação científica: {valor:.2e}")
    print(f"Preenchimento com zeros (total 10 dígitos): {valor:010.2f}")
    print(f"Com separador de milhar: {1234567.89:,.2f}")
    print(f"Porcentagem: {0.7251:.2%}")
    
    # Alinhamento e espaçamento
    print(f"{'Alinhado à direita':>20}")
    print(f"{'Centralizado':^20}")
    print(f"{'Alinhado à esquerda':<20}")


def entrada_segura(mensagem, tipo=float):
    """
    Solicita entrada numérica do usuário com tratamento de exceções.
    """
    while True:
        try:
            valor = tipo(input(mensagem))
            return valor
        except ValueError:
            print(f"Erro: Por favor, digite um valor {tipo.__name__} válido.")
        except KeyboardInterrupt:
            print("\nOperação cancelada pelo usuário.")
            return None


def exibir_matriz_formatada(matriz):
    """
    Exibe uma matriz formatada com alinhamento e espaçamento adequados.
    """
    if not matriz:
        print("Matriz vazia.")
        return
    
    # Determinar a largura máxima para cada coluna
    num_colunas = len(matriz[0])
    larguras = [0] * num_colunas
    
    for linha in matriz:
        for i, valor in enumerate(linha):
            larguras[i] = max(larguras[i], len(str(valor)))
    
    # Imprimir a matriz formatada
    print("Matriz formatada:")
    for linha in matriz:
        linha_str = " | ".join(f"{str(valor):^{larguras[i]}}" for i, valor in enumerate(linha))
        print(f"| {linha_str} |")


def demonstrar_todos():
    """Demonstra todas as funções de tratamento de entrada/saída."""
    
    # 1. Formatação de saída
    formatar_numeros()
    print("\n" + "-" * 50 + "\n")
    
    # 2. Entrada segura
    print("Demonstração de entrada segura:")
    idade = entrada_segura("Digite sua idade (número inteiro): ", int)
    if idade is not None:
        print(f"Idade registrada: {idade}")
    
    altura = entrada_segura("Digite sua altura em metros: ")
    if altura is not None:
        print(f"Altura registrada: {altura:.2f} metros")
    
    print("\n" + "-" * 50 + "\n")
    
    # 3. Exibição formatada
    print("Demonstração de exibição formatada de matriz:")
    matriz_exemplo = [
        [10, 25, 8, 100],
        [5, 12345, 7, 9],
        [42, 98, 1000, 3]
    ]
    exibir_matriz_formatada(matriz_exemplo)


if __name__ == "__main__":
    demonstrar_todos()