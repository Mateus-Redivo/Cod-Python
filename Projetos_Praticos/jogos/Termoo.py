import random
import os



def limpar_console():
    """Limpa o console"""
    os.system('cls' if os.name == 'nt' else 'clear')


def escolher_palavra():
    palavras = [
        "abrir", "baixo", "carro", "disco", "elite", "forca",
        "grave", "hotel", "ideal", "juros", "largo", "major",
        "negro", "ordem", "prato", "quite", "radio", "super",
        "tempo", "uniao", "verde", "wafer", "zebra", "angel",
        "bravo", "cesta", "drama", "etapa", "festa", "grama",
        "humor", "indio", "jovem", "laser", "morte", "nivel",
        "ouvir", "pedra", "raiva", "salto", "texto", "usina",
        "vapor", "windy", "xerox", "youth", "arame", "belga",
        "calma", "doces", "escla", "fibra", "golpe", "harpa",
        "igloo", "jarra", "kyoto", "louco", "macio", "navio",
        "oasis", "papel", "queda", "risco", "sonho", "torre",
        "ursos", "vinho", "world", "xadre", "yogas", "zumbi",
        "aceno", "balde", "campo", "dente", "extra", "fruta",
        "ganso", "horta", "islas", "junto", "kappa", "limao",
        "mesas", "notas", "obras", "pasta", "quero", "robos",
        "santo", "treno", "ultimo", "vidro", "water", "xenon",
        "yelow", "zebra", "aguas", "banho", "claro", "doido"
    ]
    # Filtrar apenas palavras com exatamente 5 letras
    palavras_filtradas = [palavra for palavra in palavras if len(palavra) == 5]
    return random.choice(palavras_filtradas)


def analisar_palpite(palpite, palavra_secreta):
    if len(palpite) != len(palavra_secreta):
        return f"O palpite deve ter {len(palavra_secreta)} letras!"

    resultado = ""
    palavra_copia = list(palavra_secreta)
    letras_posicao_errada = []

    # Primeiro, marca as letras na posição correta
    for i, letra in enumerate(palpite):
        if letra == palavra_secreta[i]:
            resultado += f"[{letra}] "  # Letra na posição correta
            palavra_copia[i] = "*"  # Marca como utilizada
        else:
            resultado += "_ "

    # Depois, verifica as letras na posição errada
    for i, letra in enumerate(palpite):
        if letra != palavra_secreta[i] and letra in palavra_copia:
            letras_posicao_errada.append(letra)
            # Marca a primeira ocorrência como utilizada
            idx = palavra_copia.index(letra)
            palavra_copia[idx] = "*"

    resultado += "\nLetras na palavra, mas em posição errada: "
    if letras_posicao_errada:
        resultado += " ".join(letras_posicao_errada)
    else:
        resultado += "nenhuma"

    return resultado


def obter_letras_nao_na_palavra(palpites, palavra_secreta):
    """Retorna as letras que foram testadas mas não estão na palavra"""
    letras_nao_na_palavra = set()

    for palpite in palpites:
        for letra in palpite:
            if letra not in palavra_secreta:
                letras_nao_na_palavra.add(letra)

    return sorted(letras_nao_na_palavra)


def exibir_palavra(palavra, palpites):
    if not palpites:
        return "_ " * len(palavra)

    # Retorna a análise do último palpite
    return analisar_palpite(palpites[-1], palavra)


def mostrar_palpites_anteriores(palpites, palavra_secreta):
    letras_descartadas = obter_letras_nao_na_palavra(palpites, palavra_secreta)
    if letras_descartadas:
        print(f"Letras descartadas: {', '.join(letras_descartadas)}")

    print("\nSeus palpites anteriores:")
    for i, p in enumerate(palpites):
        print(f"Tentativa {i+1}: {p}")
        print(analisar_palpite(p, palavra_secreta))
        print("----------------------------------------")


def menu_principal():
    limpar_console()
    print("="*18)
    print("ADIVINHE A PALAVRA")
    print("="*18)
    print("- Letras na posição correta aparecem entre colchetes [A]")
    print("- Letras na palavra mas na posição errada são listadas separadamente")
    print("- Letras que não estão na palavra são mostradas em 'Letras descartadas'")

    palavra_secreta = escolher_palavra()
    tentativas_maximas = 6
    tentativas = 0
    palpites = []

    print(f"\nA palavra tem {len(palavra_secreta)} letras")

    while tentativas < tentativas_maximas:
        print(f"\nTentativa {tentativas+1}/{tentativas_maximas}")

        # Mostrar letras que não estão na palavra e palpites anteriores
        if palpites:
            mostrar_palpites_anteriores(palpites, palavra_secreta)

        palpite = input(
            f"Digite uma palavra com {len(palavra_secreta)} letras: ").lower()

        if len(palpite) != len(palavra_secreta):
            print(
                f"Por favor, digite exatamente {len(palavra_secreta)} letras!")
            input("Pressione Enter para continuar...")
            limpar_console()
            print("="*18)
            print("ADIVINHE A PALAVRA")
            print("="*18)
            print(f"A palavra tem {len(palavra_secreta)} letras")
            continue

        palpites.append(palpite)
        tentativas += 1

        if palpite == palavra_secreta:
            print(f"\nPARABÉNS! Você acertou a palavra: {palavra_secreta}")
            break

        print("\nAnálise do seu palpite:")
        print(analisar_palpite(palpite, palavra_secreta))

        # Pausa antes de limpar o console para o jogador ver o resultado
        if tentativas < tentativas_maximas:
            input("\nPressione Enter para continuar...")
            limpar_console()
            print("="*18)
            print("ADIVINHE A PALAVRA")
            print("="*18)
            print(f"A palavra tem {len(palavra_secreta)} letras")

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
