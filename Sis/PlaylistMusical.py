# Sistema de Playlist Musical
musicas = []


def exibir_menu():
    print("\n" + "="*30)
    print("    PLAYLIST MUSICAL")
    print("="*30)
    print("1 - Adicionar música")
    print("2 - Listar músicas")
    print("3 - Buscar por gênero")
    print("4 - Tocar música")
    print("5 - Remover música")
    print("6 - Sair")
    print("="*30)


def adicionar_musica():
    print("\n--- ADICIONAR MÚSICA ---")
    titulo = input("Título da música: ").strip()
    artista = input("Artista: ").strip()
    genero = input("Gênero: ").strip()

    if not titulo or not artista:
        print("Título e artista são obrigatórios!")
        return

    try:
        duracao = int(input("Duração (em segundos): "))

        if duracao <= 0:
            print("Duração deve ser positiva!")
            return

        musica = {
            'titulo': titulo,
            'artista': artista,
            'genero': genero if genero else 'Não informado',
            'duracao': duracao
        }

        musicas.append(musica)
        print(f"🎵 Música '{titulo}' adicionada à playlist!")

    except ValueError:
        print("Digite uma duração válida!")


def formatar_duracao(segundos):
    minutos = segundos // 60
    segundos_restantes = segundos % 60
    return f"{minutos}:{segundos_restantes:02d}"


def listar_musicas():
    print("\n--- PLAYLIST COMPLETA ---")
    if not musicas:
        print("Nenhuma música na playlist.")
        return

    duracao_total = 0

    for i, musica in enumerate(musicas, 1):
        duracao_formatada = formatar_duracao(musica['duracao'])
        print(f"{i}. {musica['titulo']} - {musica['artista']}")
        print(f"   Gênero: {musica['genero']} | Duração: {duracao_formatada}")
        duracao_total += musica['duracao']

    print(f"\nTotal: {len(musicas)} música(s)")
    print(f"Duração total: {formatar_duracao(duracao_total)}")


def buscar_por_genero():
    print("\n--- BUSCAR POR GÊNERO ---")
    if not musicas:
        print("Nenhuma música na playlist.")
        return

    genero_busca = input("Digite o gênero para buscar: ").strip().lower()

    if not genero_busca:
        print("Gênero não pode estar vazio!")
        return

    encontradas = []
    for musica in musicas:
        if genero_busca in musica['genero'].lower():
            encontradas.append(musica)

    if not encontradas:
        print(f"Nenhuma música encontrada do gênero '{genero_busca}'.")
        return

    print(f"\n🎵 Músicas do gênero '{genero_busca}':")
    for i, musica in enumerate(encontradas, 1):
        duracao_formatada = formatar_duracao(musica['duracao'])
        print(
            f"{i}. {musica['titulo']} - {musica['artista']} ({duracao_formatada})")


def tocar_musica():
    print("\n--- TOCAR MÚSICA ---")
    if not musicas:
        print("Nenhuma música na playlist.")
        return

    listar_musicas()

    try:
        indice = int(input("\nEscolha a música: ")) - 1

        if 0 <= indice < len(musicas):
            musica = musicas[indice]
            duracao_formatada = formatar_duracao(musica['duracao'])

            print(f"\n🎵 Tocando agora:")
            print(f"   Título: {musica['titulo']}")
            print(f"   Artista: {musica['artista']}")
            print(f"   Gênero: {musica['genero']}")
            print(f"   Duração: {duracao_formatada}")
            print("   ♪♪♪ Enjoy the music! ♪♪♪")

        else:
            print("Música inválida!")
    except ValueError:
        print("Digite apenas números!")


def remover_musica():
    print("\n--- REMOVER MÚSICA ---")
    if not musicas:
        print("Nenhuma música na playlist.")
        return

    listar_musicas()

    try:
        indice = int(input("\nEscolha a música para remover: ")) - 1

        if 0 <= indice < len(musicas):
            musica_removida = musicas.pop(indice)
            print(
                f"🗑️ Música '{musica_removida['titulo']}' removida da playlist!")
        else:
            print("Música inválida!")
    except ValueError:
        print("Digite apenas números!")


def main():
    print("Bem-vindo à sua Playlist Musical!")

    while True:
        exibir_menu()

        try:
            opcao = int(input("\nEscolha uma opção: "))

            if opcao == 1:
                adicionar_musica()
            elif opcao == 2:
                listar_musicas()
            elif opcao == 3:
                buscar_por_genero()
            elif opcao == 4:
                tocar_musica()
            elif opcao == 5:
                remover_musica()
            elif opcao == 6:
                print("\n🎵 Obrigado por usar a playlist! 🎵")
                break
            else:
                print("⚠️  Opção inválida! Escolha entre 1 e 6.")

        except ValueError:
            print("⚠️  Por favor, digite apenas números!")

        input("\nPressione ENTER para continuar...")


if __name__ == "__main__":
    main()
