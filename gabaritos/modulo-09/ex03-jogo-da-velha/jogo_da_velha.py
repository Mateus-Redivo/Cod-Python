"""
Gabarito — Módulo 09, Exercício 03: Jogo da velha

Enunciado:
  modulo-09-matrizes/exercicios/EXERCICIO-03-jogo-da-velha.md

Como executar:
  python jogo_da_velha.py
"""

TAMANHO = 3
VAZIO = " "


def criar_tabuleiro():
    """Matriz TAMANHO x TAMANHO com listas independentes."""
    tabuleiro = []
    for i in range(TAMANHO):
        linha = []
        for j in range(TAMANHO):
            linha.append(VAZIO)
        tabuleiro.append(linha)
    return tabuleiro


def mostrar_tabuleiro(tabuleiro):
    print()
    print("   " + "   ".join(str(c + 1) for c in range(TAMANHO)))
    for i in range(TAMANHO):
        print(f"{i + 1}  " + " | ".join(tabuleiro[i]))
        if i < TAMANHO - 1:
            print("  " + "---+" * (TAMANHO - 1) + "---")
    print()


def posicao_valida(tabuleiro, linha, coluna):
    """Dentro do tabuleiro E ainda livre."""
    dentro = 0 <= linha < TAMANHO and 0 <= coluna < TAMANHO
    if not dentro:
        return False
    return tabuleiro[linha][coluna] == VAZIO


def venceu_em_alguma_linha(tabuleiro, simbolo):
    for i in range(TAMANHO):
        completou = True
        for j in range(TAMANHO):
            if tabuleiro[i][j] != simbolo:
                completou = False
        if completou:
            return True
    return False


def venceu_em_alguma_coluna(tabuleiro, simbolo):
    for j in range(TAMANHO):
        completou = True
        for i in range(TAMANHO):
            if tabuleiro[i][j] != simbolo:
                completou = False
        if completou:
            return True
    return False


def venceu_em_alguma_diagonal(tabuleiro, simbolo):
    principal = True
    secundaria = True
    for i in range(TAMANHO):
        if tabuleiro[i][i] != simbolo:
            principal = False
        if tabuleiro[i][TAMANHO - 1 - i] != simbolo:
            secundaria = False
    return principal or secundaria


def verificar_vitoria(tabuleiro, simbolo):
    return (venceu_em_alguma_linha(tabuleiro, simbolo)
            or venceu_em_alguma_coluna(tabuleiro, simbolo)
            or venceu_em_alguma_diagonal(tabuleiro, simbolo))


def tabuleiro_cheio(tabuleiro):
    for linha in tabuleiro:
        for casa in linha:
            if casa == VAZIO:
                return False
    return True


def ler_jogada(tabuleiro, simbolo):
    """Insiste até a jogada ser válida. Devolve linha e coluna internas."""
    while True:
        # A conversão -1 acontece AQUI, num lugar só. O usuário digita
        # 1 a 3; a matriz usa 0 a 2.
        linha = int(input(f"Jogador {simbolo} - linha: ")) - 1
        coluna = int(input(f"Jogador {simbolo} - coluna: ")) - 1

        if posicao_valida(tabuleiro, linha, coluna):
            return linha, coluna

        print("Posição inválida! Tente de novo.")


# --- Programa principal ----------------------------------------------
tabuleiro = criar_tabuleiro()
jogador = "X"

mostrar_tabuleiro(tabuleiro)

while True:
    linha, coluna = ler_jogada(tabuleiro, jogador)
    tabuleiro[linha][coluna] = jogador
    mostrar_tabuleiro(tabuleiro)

    if verificar_vitoria(tabuleiro, jogador):
        print(f"Jogador {jogador} venceu!")
        break

    if tabuleiro_cheio(tabuleiro):
        print("Deu velha!")
        break

    # Alterna o jogador
    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"


# --- Por que assim -------------------------------------------------
# 1. A conversão "-1" acontece em UM lugar só: dentro de ler_jogada.
#    Todo o resto do programa pensa em 0, 1, 2. Espalhar o -1 por
#    várias funções é o caminho mais curto para um bug que só aparece
#    numa jogada específica.
#
# 2. ler_jogada usa "while True" com return, não com break. O return
#    faz as duas coisas: entrega os valores e encerra o laço. É o
#    padrão do módulo 05 num caso em que ele lê melhor.
#
# 3. A vitória foi quebrada em três funções (linha, coluna, diagonal)
#    em vez de oito ifs. Cada uma percorre a matriz numa direção — as
#    mesmas três direções do exemplo 03 do módulo.
#
# 4. Repare no padrão dentro de venceu_em_alguma_linha: começa
#    supondo "completou = True" e procura um CONTRAEXEMPLO. É a mesma
#    flag do exercício do número primo, no módulo 05.
#
# 5. TAMANHO é constante, e nenhuma função tem o número 3 escrito.
#    Por isso a resposta ao desafio é curta — veja abaixo.
#
# 6. posicao_valida testa duas coisas em ordem: primeiro se está
#    DENTRO, depois se está LIVRE. A ordem importa: testar
#    tabuleiro[linha][coluna] antes de saber se o índice existe daria
#    IndexError.


# --- Solução do desafio dentro do desafio ----------------------------
# Para virar um 4x4, muda-se UMA linha:
#
#   TAMANHO = 4
#
# O tabuleiro, o desenho, as três verificações de vitória e a
# checagem de tabuleiro cheio já usam TAMANHO. Rode e confira.
#
# (Um jogo 4x4 de verdade costuma pedir "quatro em linha" num
# tabuleiro maior, o que já é outra regra — mas a estrutura de
# percorrer linhas, colunas e diagonais continua a mesma.)
#
# Se no SEU código a resposta foi "muitas linhas", procure onde o 3
# aparece escrito: em range(3), em len() que você não usou, no desenho
# do tabuleiro. Cada 3 fixo é um lugar a mais para lembrar de mudar.
