import random


def escolher_palavra():
    palavras = [
        "python", "matriz", "codigo", "arcade", "banana", "caneta",
        "dormir", "escola", "folhas", "girafa", "hokage", "imagem",
        "janela", "kinder", "limpar", "manter", "navios", "objeto",
        "pacote", "quarto", "relevo", "senado", "triste", "urbano",
        "viagem", "xamego", "zeloso", "amores", "buscar", "cinema",
        "danado", "errado", "frente", "geladp", "humano", "indice",
        "jornal", "logica", "manual", "nitido", "operar", "plural",
        "quieto", "rapido", "sombra", "trator", "unicos", "vagoes",
        "widget", "xingar"
    ]
    # Filtrar apenas palavras com até 6 letras
    palavras_filtradas = [palavra for palavra in palavras if len(palavra) == 6]
    return random.choice(palavras_filtradas)


def analisar_palpite(palpite, palavra_secreta):
    if len(palpite) != len(palavra_secreta):
        return f"O palpite deve ter {len(palavra_secreta)} letras!"

    resultado = ""
    # Cria uma cópia da palavra secreta para marcar letras já utilizadas
    palavra_copia = list(palavra_secreta)

    # Primeiro, marca as letras na posição correta
    for i, letra in enumerate(palpite):
        if i < len(palavra_secreta) and letra == palavra_secreta[i]:
            resultado += f"[{letra}] "  # Letra na posição correta
            palavra_copia[i] = "*"  # Marca como utilizada
        else:
            resultado += "_ "

    # Depois, verifica as letras na posição errada
    resultado += "\nLetras na palavra, mas em posição errada: "
    encontradas = False

    for i, letra in enumerate(palpite):
        if i < len(palavra_secreta) and letra != palavra_secreta[i] and letra in palavra_copia:
            resultado += letra + " "
            # Marca a primeira ocorrência como utilizada
            palavra_copia[palavra_copia.index(letra)] = "*"
            encontradas = True

    if not encontradas:
        resultado += "nenhuma"

    return resultado


def exibir_palavra(palavra, palpites):
    if not palpites:
        return "_ " * len(palavra)

    # Retorna a análise do último palpite
    return analisar_palpite(palpites[-1], palavra)


def menu_principal():
    print("="*18)
    print("ADIVINHE A PALAVRA")
    print("="*18)
    print("- Letras na posição correta aparecem entre colchetes [A]")
    print("- Letras na palavra mas na posição errada são listadas separadamente")

    palavra_secreta = escolher_palavra()
    tentativas_maximas = 6
    tentativas = 0
    palpites = []

    print(f"\nA palavra tem {len(palavra_secreta)} letras")

    while tentativas < tentativas_maximas:
        print(f"\nTentativa {tentativas+1}/{tentativas_maximas}")

        if palpites:
            print("\nSeus palpites anteriores:")
            for i, p in enumerate(palpites):
                print(f"Tentativa {i+1}: {p}")
                print(analisar_palpite(p, palavra_secreta))
                print("----------------------------------------")

        palpite = input(
            f"Digite uma palavra com {len(palavra_secreta)} letras: ").lower()

        if len(palpite) != len(palavra_secreta):
            print(
                f"Por favor, digite exatamente {len(palavra_secreta)} letras!")
            continue

        palpites.append(palpite)
        tentativas += 1

        if palpite == palavra_secreta:
            print(f"\nPARABÉNS! Você acertou a palavra: {palavra_secreta}")
            break

        print("\nAnálise do seu palpite:")
        print(analisar_palpite(palpite, palavra_secreta))

    if tentativas == tentativas_maximas and palpites[-1] != palavra_secreta:
        print(f"\nVocê perdeu! A palavra era: {palavra_secreta}")

    jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()
    if jogar_novamente == "s":
        menu_principal()
    else:
        print("Obrigado por jogar!")


# Iniciar o jogo
if __name__ == "__main__":
    menu_principal()
