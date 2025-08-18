# Sistema de Biblioteca Simples
# Gerencia livros com funcionalidades de adicionar, listar, emprestar e devolver
livros = []  # Lista para armazenar os livros cadastrados


def exibir_menu():
    """Exibe o menu principal com as opções disponíveis"""
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
    """Adiciona um novo livro à biblioteca"""
    print("\n--- ADICIONAR LIVRO ---")
    titulo = input("Digite o título do livro: ").strip()
    autor = input("Digite o autor: ").strip()

    # Valida se título e autor foram preenchidos
    if not titulo or not autor:
        print("Título e autor não podem estar vazios!")
        return

    # Cria dicionário com dados do livro
    livro = {
        'titulo': titulo,
        'autor': autor,
        'disponivel': True  # Livro inicia como disponível
    }

    livros.append(livro)
    print(f"Livro '{titulo}' adicionado com sucesso!")


def listar_livros():
    """Lista todos os livros cadastrados com seu status"""
    print("\n--- LISTA DE LIVROS ---")
    if not livros:
        print("Nenhum livro cadastrado.")
        return

    # Exibe cada livro com numeração e status
    for i, livro in enumerate(livros, 1):
        status = "Disponível" if livro['disponivel'] else "Emprestado"
        print(f"{i}. {livro['titulo']} - {livro['autor']} ({status})")


def emprestar_livro():
    """Realiza o empréstimo de um livro disponível"""
    print("\n--- EMPRESTAR LIVRO ---")
    if not livros:
        print("Nenhum livro cadastrado.")
        return

    listar_livros()
    try:
        indice = int(input("\nDigite o número do livro: ")) - 1

        # Verifica se o índice é válido
        if 0 <= indice < len(livros):
            if livros[indice]['disponivel']:
                livros[indice]['disponivel'] = False  # Marca como emprestado
                print(f"Livro '{livros[indice]['titulo']}' emprestado!")
            else:
                print("Este livro já está emprestado!")
        else:
            print("Número inválido!")
    except ValueError:
        print("Digite apenas números!")


def devolver_livro():
    """Processa a devolução de um livro emprestado"""
    print("\n--- DEVOLVER LIVRO ---")
    # Filtra apenas livros emprestados
    emprestados = [livro for livro in livros if not livro['disponivel']]

    if not emprestados:
        print("Nenhum livro emprestado.")
        return

    # Lista apenas os livros emprestados
    print("Livros emprestados:")
    for i, livro in enumerate(emprestados, 1):
        print(f"{i}. {livro['titulo']} - {livro['autor']}")

    try:
        indice = int(input("\nDigite o número do livro: ")) - 1

        if 0 <= indice < len(emprestados):
            emprestados[indice]['disponivel'] = True  # Marca como disponível
            print(f"Livro '{emprestados[indice]['titulo']}' devolvido!")
        else:
            print("Número inválido!")
    except ValueError:
        print("Digite apenas números!")


def main():
    """Função principal que executa o sistema da biblioteca"""
    print("Bem-vindo ao Sistema de Biblioteca!")

    while True:
        exibir_menu()

        try:
            opcao = int(input("\nEscolha uma opção: "))

            # Processa a opção escolhida pelo usuário
            if opcao == 1:
                adicionar_livro()
            elif opcao == 2:
                listar_livros()
            elif opcao == 3:
                emprestar_livro()
            elif opcao == 4:
                devolver_livro()
            elif opcao == 5:
                print("\nObrigado por usar a biblioteca!")
                break
            else:
                print("Opção inválida! Escolha entre 1 e 5.")

        except ValueError:
            print("Por favor, digite apenas números!")

        input("\nPressione ENTER para continuar...")


# Executa o programa principal
if __name__ == "__main__":
    main()
