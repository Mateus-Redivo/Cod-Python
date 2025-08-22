nomes = []
precos = []
quantidades = []


def popular_exemplo():
    produtos_exemplo = [
        ("Arroz", 20.0, 10),
        ("Feijão", 7.5, 5),
        ("Macarrão", 4.0, 2),
        ("Açúcar", 3.5, 0),
        ("Sal", 2.0, 1),
        ("Óleo", 8.0, 4),
        ("Café", 15.0, 3),
        ("Leite", 5.0, 6),
        ("Pão", 1.5, 0),
        ("Manteiga", 6.0, 2)
    ]
    for nome, preco, quantidade in produtos_exemplo:
        nomes.append(nome)
        precos.append(preco)
        quantidades.append(quantidade)


def cadastrar_produto():
    print("\n--- CADASTRAR PRODUTO ---")

    nome = input("Nome do produto: ").strip()
    if not nome or not nome.isalpha():
        print("Erro: Nome do produto não pode estar vazio ou conter caracteres inválidos!")
        return

    try:
        preco = float(input("Preço do produto: R$ "))
        quantidade = int(input("Quantidade em estoque: "))

        if preco < 0 or quantidade < 0:
            print("Erro: Preço e quantidade não podem ser negativos!")
            return

        nomes.append(nome)
        precos.append(preco)
        quantidades.append(quantidade)

        print(f"\nProduto '{nome}' cadastrado com sucesso!")

    except ValueError:
        print("Erro: Digite valores numéricos válidos!")


def listar_produtos():
    print("\n--- LISTA DE PRODUTOS ---")
    if not nomes:
        print("Nenhum produto cadastrado.")
        return
    status = ""
    for i in range(len(nomes)):
        if quantidades[i] == 0:
            status = "Produto esgotado"
        elif quantidades[i] < 5:
            status = "Estoque baixo"
        else:
            status = "Em estoque"
        print(
            f"{i + 1}. Nome: {nomes[i]}, Preço: R$ {precos[i]:.2f}, Quantidade: {quantidades[i]}, {status}")


def menu():
    print("\n" + "=" * 40)
    print("SISTEMA DE CONTROLE DE PRODUTOS")
    print("=" * 40)
    print("1. Cadastrar produto")
    print("2. Listar produtos")
    print("3. Atualizar produto")
    print("4. Entrada de estoque")
    print("5. Saída de estoque")
    print("6. Remover produto")
    print("7. Relatório do inventário")
    print("8. Popular produtos de exemplo")
    print("0. Sair")
    print("=" * 40)


def main():
    while True:
        menu()
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida! Tente novamente.")

        match opcao:
            case 1:
                cadastrar_produto()
            case 2:
                listar_produtos()
            case 3:
                print("Função ainda não implementada.")
            case 4:
                print("Função ainda não implementada.")
            case 5:
                print("Função ainda não implementada.")
            case 6:
                print("Função ainda não implementada.")
            case 7:
                print("Função ainda não implementada.")
            case 8:
                popular_exemplo()
                print("Produtos de exemplo adicionados com sucesso!")
            case 0:
                print("Saindo do sistema...")
                break
            case _:
                print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
