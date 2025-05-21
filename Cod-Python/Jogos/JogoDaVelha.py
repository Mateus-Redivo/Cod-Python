# Estrutura para um jogo da velha usando matriz

def jogar_velha():
    # Inicializa um tabuleiro 3x3 vazio
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    jogo_ativo = True

    def mostrar_tabuleiro():
        print("  1 2 3")  # Índices das colunas
        for i in range(3):
            print(
                f"{i+1} {tabuleiro[i][0]}|{tabuleiro[i][1]}|{tabuleiro[i][2]}")
            if i < 2:
                print("  -+-+-")

    def verificar_vitoria():
        # Verificar linhas
        for i in range(3):
            if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != " ":
                return True

        # Verificar colunas
        for j in range(3):
            if tabuleiro[0][j] == tabuleiro[1][j] == tabuleiro[2][j] != " ":
                return True

        # Verificar diagonais
        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
            return True
        if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
            return True

        return False

    def verificar_empate():
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == " ":
                    return False
        return True

    print("Jogo da Velha")
    print("Digite a linha (1-3) e coluna (1-3)")

    while jogo_ativo:
        mostrar_tabuleiro()
        try:
            linha = int(
                input(f"Jogador {jogador_atual}, escolha a linha (1-3): ")) - 1
            coluna = int(
                input(f"Jogador {jogador_atual}, escolha a coluna (1-3): ")) - 1

            if 0 <= linha <= 2 and 0 <= coluna <= 2 and tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = jogador_atual

                if verificar_vitoria():
                    mostrar_tabuleiro()
                    print(f"Jogador {jogador_atual} venceu!")
                    jogo_ativo = False
                elif verificar_empate():
                    mostrar_tabuleiro()
                    print("Empate!")
                    jogo_ativo = False
                else:
                    jogador_atual = "O" if jogador_atual == "X" else "X"
            else:
                print("Posição inválida ou já ocupada!")
        except ValueError:
            print("Digite apenas números!")


# Inicia o jogo quando o arquivo é executado diretamente
if __name__ == "__main__":
    jogar_velha()
