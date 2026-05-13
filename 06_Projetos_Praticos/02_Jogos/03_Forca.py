import random


def escolher_palavra():
    """Escolhe uma palavra aleatória de uma lista predefinida"""
    palavras = [
        'PYTHON', 'PROGRAMACAO', 'COMPUTADOR', 'JOGO', 'FORCA',
        'CODIGO', 'ALGORITMO', 'VARIAVEL', 'FUNCAO', 'CLASSE',
        'OBJETO', 'METODO', 'LISTA', 'DICIONARIO', 'STRING'
    ]
    return random.choice(palavras)


def mostrar_palavra(palavra, letras_certas):
    """Mostra a palavra com as letras descobertas"""
    resultado = ''
    for letra in palavra:
        if letra in letras_certas:
            resultado += letra + ' '
        else:
            resultado += '_ '
    return resultado.strip()


def pedir_letra(letras_certas, letras_erradas):
    """Solicita uma letra válida do usuário"""
    while True:
        tentativa = input("\nDigite uma letra: ").upper().strip()

        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Digite apenas uma letra!")
            continue

        if tentativa in letras_certas or tentativa in letras_erradas:
            print("Voce ja tentou essa letra!")
            continue

        return tentativa


def jogar_forca():
    """Função principal do jogo da forca"""
    print("=== JOGO DA FORCA ===")
    print("Adivinhe a palavra!\n")

    palavra = escolher_palavra()
    letras_certas = set()
    letras_erradas = set()
    max_tentativas = 6
    tentativas_restantes = max_tentativas

    while tentativas_restantes > 0:
        # Mostrar estado atual
        print(f"Palavra: {mostrar_palavra(palavra, letras_certas)}")
        print(f"Letras erradas: {' '.join(sorted(letras_erradas))}")
        print(f"Tentativas restantes: {tentativas_restantes}")

        # Verificar se ganhou
        if all(letra in letras_certas for letra in palavra):
            print("\nPARABENS! Voce ganhou!")
            print(f"A palavra era: {palavra}")
            return True

        # Pedir letra
        tentativa = pedir_letra(letras_certas, letras_erradas)

        # Verificar se a letra está na palavra
        if tentativa in palavra:
            letras_certas.add(tentativa)
            print(f"Boa! A letra '{tentativa}' esta na palavra!")
        else:
            letras_erradas.add(tentativa)
            tentativas_restantes -= 1
            print(f"A letra '{tentativa}' nao esta na palavra!")

        print("-" * 40)

    # Game Over
    print("GAME OVER!")
    print(f"A palavra era: {palavra}")
    return False


def main():
    """Função principal com menu do jogo"""
    while True:
        if jogar_forca():
            print("Resultado: vitoria")
        else:
            print("Resultado: derrota")

        while True:
            jogar_novamente = input(
                "\nDeseja jogar novamente? (s/n): ").lower().strip()
            if jogar_novamente in ['s', 'sim']:
                print("\n" + "="*50)
                break
            elif jogar_novamente in ['n', 'nao', 'não']:
                print("\nObrigado por jogar!")
                return
            else:
                print("Digite 's' para sim ou 'n' para nao.")


if __name__ == "__main__":
    main()
