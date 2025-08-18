# Sistema de Biblioteca Simples
livros = []


def exibir_menu():
    print("\n" + "="*30)
    print("   SISTEMA DE BIBLIOTECA")
    print("="*30)
    print("1 - Adicionar livro")
    print("2 - Listar livros")
    print("3 - Emprestar livro")
    print("4 - Devolver livro")
    print("5 - Sair")
    print("="*30)


def adicionar_livro():
    print("\n--- ADICIONAR LIVRO ---")
    titulo = input("Digite o título do livro: ").strip()
    autor = input("Digite o autor: ").strip()

    if not titulo or not autor:
        print("Título e autor não podem estar vazios!")
        return

    livro = {
        'titulo': titulo,
        'autor': autor,
        'disponivel': True
    }

    livros.append(livro)
    print(f"✅ Livro '{titulo}' adicionado com sucesso!")


def listar_livros():
    print("\n--- LISTA DE LIVROS ---")
    if not livros:
        print("Nenhum livro cadastrado.")
        return

    for i, livro in enumerate(livros, 1):
        status = "📗 Disponível" if livro['disponivel'] else "📕 Emprestado"
        print(f"{i}. {livro['titulo']} - {livro['autor']} ({status})")


def emprestar_livro():
    print("\n--- EMPRESTAR LIVRO ---")
    if not livros:
        print("Nenhum livro cadastrado.")
        return

    listar_livros()
    try:
        indice = int(input("\nDigite o número do livro: ")) - 1

        if 0 <= indice < len(livros):
            if livros[indice]['disponivel']:
                livros[indice]['disponivel'] = False
                print(f"📕 Livro '{livros[indice]['titulo']}' emprestado!")
            else:
                print("Este livro já está emprestado!")
        else:
            print("Número inválido!")
    except ValueError:
        print("Digite apenas números!")


def devolver_livro():
    print("\n--- DEVOLVER LIVRO ---")
    emprestados = [l for l in livros if not l['disponivel']]

    if not emprestados:
        print("Nenhum livro emprestado.")
        return

    print("Livros emprestados:")
    for i, livro in enumerate(emprestados, 1):
        print(f"{i}. {livro['titulo']} - {livro['autor']}")

    try:
        indice = int(input("\nDigite o número do livro: ")) - 1

        if 0 <= indice < len(emprestados):
            emprestados[indice]['disponivel'] = True
            print(f"📗 Livro '{emprestados[indice]['titulo']}' devolvido!")
        else:
            print("Número inválido!")
    except ValueError:
        print("Digite apenas números!")


def main():
    print("Bem-vindo ao Sistema de Biblioteca!")

    while True:
        exibir_menu()

        try:
            opcao = int(input("\nEscolha uma opção: "))

            if opcao == 1:
                adicionar_livro()
            elif opcao == 2:
                listar_livros()
            elif opcao == 3:
                emprestar_livro()
            elif opcao == 4:
                devolver_livro()
            elif opcao == 5:
                print("\n📚 Obrigado por usar a biblioteca! 📚")
                break
            else:
                print("⚠️  Opção inválida! Escolha entre 1 e 5.")

        except ValueError:
            print("⚠️  Por favor, digite apenas números!")

        input("\nPressione ENTER para continuar...")


if __name__ == "__main__":
    main()
