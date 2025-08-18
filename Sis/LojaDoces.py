# Sistema de Loja de Doces
# Gerencia produtos, vendas e controle de estoque
produtos = []  # Lista de produtos cadastrados


def exibir_menu():
    """Exibe o menu principal da loja"""
    print("\n" + "="*30)
    print("     LOJA DE DOCES")
    print("="*30)
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Fazer venda")
    print("4 - Repor estoque")
    print("5 - Sair")
    print("="*30)


def cadastrar_produto():
    """Cadastra um novo produto na loja"""
    print("\n--- CADASTRAR PRODUTO ---")
    nome = input("Digite o nome do doce: ").strip()

    if not nome:
        print("Nome não pode estar vazio!")
        return

    # Verificar se já existe
    for produto in produtos:
        if produto['nome'].lower() == nome.lower():
            print("Produto já cadastrado!")
            return

    try:
        preco = float(input("Digite o preço: R$ "))
        estoque = int(input("Digite a quantidade em estoque: "))

        if preco < 0 or estoque < 0:
            print("Preço e estoque devem ser positivos!")
            return

        produto = {
            'nome': nome,
            'preco': preco,
            'estoque': estoque
        }

        produtos.append(produto)
        print(f"Produto '{nome}' cadastrado com sucesso!")

    except ValueError:
        print("Digite valores válidos!")


def listar_produtos():
    print("\n--- PRODUTOS DISPONÍVEIS ---")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print(f"{'Nº':<3} {'Nome':<20} {'Preço':<10} {'Estoque':<8}")
    print("-" * 45)

    for i, produto in enumerate(produtos, 1):
        status = "Disponível" if produto['estoque'] > 0 else "Indisponível"
        print(
            f"{i:<3} {produto['nome']:<20} R${produto['preco']:<9.2f} {produto['estoque']:<3} {status}")


def fazer_venda():
    """Processa uma venda e atualiza o estoque"""
    print("\n--- FAZER VENDA ---")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    listar_produtos()

    try:
        indice = int(input("\nEscolha o produto: ")) - 1

        if 0 <= indice < len(produtos):
            produto = produtos[indice]

            if produto['estoque'] == 0:
                print("Produto em falta!")
                return

            quantidade = int(input(f"Quantas unidades de {produto['nome']}? "))

            if quantidade <= 0:
                print("Quantidade deve ser positiva!")
                return

            if quantidade > produto['estoque']:
                print(
                    f"Estoque insuficiente! Disponível: {produto['estoque']}")
                return

            total = quantidade * produto['preco']
            produto['estoque'] -= quantidade

            print("\nVENDA REALIZADA:")
            print(f"   Produto: {produto['nome']}")
            print(f"   Quantidade: {quantidade}")
            print(f"   Valor unitário: R$ {produto['preco']:.2f}")
            print(f"   Total: R$ {total:.2f}")
            print(f"   Estoque restante: {produto['estoque']}")

        else:
            print("Produto inválido!")
    except ValueError:
        print("Digite apenas números!")


def repor_estoque():
    print("\n--- REPOR ESTOQUE ---")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    listar_produtos()

    try:
        indice = int(input("\nEscolha o produto: ")) - 1

        if 0 <= indice < len(produtos):
            quantidade = int(input("Quantidade a adicionar: "))

            if quantidade <= 0:
                print("Quantidade deve ser positiva!")
                return

            produtos[indice]['estoque'] += quantidade
            print(f"Estoque de '{produtos[indice]['nome']}' atualizado!")
            print(f"   Novo estoque: {produtos[indice]['estoque']}")

        else:
            print("Produto inválido!")
    except ValueError:
        print("Digite apenas números!")


def main():
    print("Bem-vindo à Loja de Doces!")

    while True:
        exibir_menu()

        try:
            opcao = int(input("\nEscolha uma opção: "))

            if opcao == 1:
                cadastrar_produto()
            elif opcao == 2:
                listar_produtos()
            elif opcao == 3:
                fazer_venda()
            elif opcao == 4:
                repor_estoque()
            elif opcao == 5:
                print("\nObrigado por usar a loja!")
                break
            else:
                print("Opção inválida! Escolha entre 1 e 5.")

        except ValueError:
            print("Por favor, digite apenas números!")

        input("\nPressione ENTER para continuar...")


if __name__ == "__main__":
    main()
