# Inicia os vetores para armazenar os dados dos produtos
nomes = []  # Lista para armazenar os nomes dos produtos
precos = []  # Lista para armazenar os preços dos produtos
quantidades = []  # Lista para armazenar as quantidades dos produtos

# Função para exibir o menu principal do sistema


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

# Funçoes reutilizáveis


def verifica_lista_vazia():
    if not nomes:
        print("Nenhum produto cadastrado")
        return True
    return False


def receber_produto():
    try:
        idx = int(input("Digite o número do produto que deseja atualizar: ")) - 1
        if idx < 0 or idx >= len(nomes):
            print("Produto inválido!")
            return None
        return idx
    except ValueError:
        print("Digite um valor numérico válido!")
        return None


def receber_op_valida():
    try:
        opcao = int(input("Escolha uma opção: "))
        return opcao
    except ValueError:
        return -1


def listar_produtos():
    print("\n--- LISTA DE PRODUTOS ---")

    if verifica_lista_vazia():
        return

    for i in range(len(nomes)):
        print(
            f"{i + 1}. Nome: {nomes[i]}, Preço: R$ {precos[i]:.2f}, Quantidade: {quantidades[i]}")

# Implementação das funcionalidades do sistema


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
    if not nome or not nome.replace(" ", "").isalpha():
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


def listar_produtos_status():
    print("\n--- LISTA DE PRODUTOS ---")

    if verifica_lista_vazia():
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


def atualizar_produto():

    if verifica_lista_vazia():
        return

    listar_produtos()

    id_produto = receber_produto()

    if id_produto is None:  
        print("Operação cancelada.") 
        return

    print("--- Atualizar Produto--- ")
    print("1. Atualizar nome")
    print("2. Atualizar preço")
    print("3. Atualizar quantidade")

    op = receber_op_valida()

    match op:

        case 1:
            novo_nome = input("Digite o novo nome do produto: ").strip()
            if not novo_nome or not novo_nome.replace(" ", "").isalpha():
                print("Erro: Nome inválido!")
                return
            nomes[id_produto] = novo_nome
            print(f"Nome do produto atualizado para '{novo_nome}'.")

        case 2:
            try:
                novo_preco = float(
                    input("Digite o novo preço do produto: R$ "))
                if novo_preco < 0:
                    print("Erro: Preço não pode ser negativo!")
                    return
                precos[id_produto] = novo_preco
                print(
                    f"Preço do produto {nomes[id_produto]} atualizado para R$ {novo_preco:.2f}.")
            except ValueError:
                print("Erro: Digite um valor numérico válido!")

        case 3:
            try:
                nova_quantidade = int(
                    input("Digite a nova quantidade do produto: "))
                if nova_quantidade < 0:
                    print("Erro: Quantidade não pode ser negativa!")
                    return
                quantidades[id_produto] = nova_quantidade
                print(
                    f"Quantidade do produto {nomes[id_produto]} atualizada para {nova_quantidade}.")
            except ValueError:
                print("Erro: Digite um valor numérico válido!")

        case _:
            print("Opção inválida! Tente novamente.")


def entrada_estoque():
    print("Entrada em estoque")

    if verifica_lista_vazia():
        return

    listar_produtos()

    id_produto = receber_produto()
    
    if id_produto is None:  
        print("Operação cancelada.") 
        return

    try:
        quantidade_entrada = int(input("Digite a quantidade da entrada: "))
        if quantidade_entrada < 0:
            print("Erro: Quantidade não pode ser negativa!")
            return
    except ValueError:
        print("Informe um valor válido")
        return

    quantidades[id_produto] += quantidade_entrada

    print(
        f"Quantidade {quantidade_entrada} adicionada ao produto {nomes[id_produto]}")


def saida_estoque():
    pass  # Função ainda não implementada


def remover_produto():
    pass  # Função ainda não implementada


def relatorio_inventario():
    pass  # Função ainda não implementada

# Implementação da função principal do sistema(A função main() é o ponto de entrada do programa)


def main():
    # Implementação da função principal do sistema
    while True:
        menu()

        opcao = receber_op_valida()
        match opcao:
            case 1:
                cadastrar_produto()
            case 2:
                listar_produtos_status()
            case 3:
                atualizar_produto()
            case 4:
                entrada_estoque()
            case 5:
                saida_estoque()
            case 6:
                remover_produto()
            case 7:
                relatorio_inventario()
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
