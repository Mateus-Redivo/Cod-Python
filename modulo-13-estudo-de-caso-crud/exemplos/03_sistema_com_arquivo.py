# Nome do arquivo para armazenar os produtos
ARQUIVO_PRODUTOS = "produtos.txt"


# Funções para manipulação do arquivo TXT
def carregar_produtos():
    """Carrega os produtos do arquivo txt e retorna as listas de dados"""
    nomes = []
    precos = []
    quantidades = []

    try:
        with open(ARQUIVO_PRODUTOS, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",")
                if len(dados) == 3:  # Verifica se a linha tem os 3 campos esperados
                    nomes.append(dados[0])
                    precos.append(float(dados[1]))
                    quantidades.append(int(dados[2]))
    except FileNotFoundError:
        # Se o arquivo não existir, retorna listas vazias
        pass

    return nomes, precos, quantidades


def salvar_produtos(nomes, precos, quantidades):
    """Salva os produtos no arquivo txt"""
    with open(ARQUIVO_PRODUTOS, "w", encoding="utf-8") as arquivo:
        for i in range(len(nomes)):
            arquivo.write(f"{nomes[i]},{precos[i]},{quantidades[i]}\n")


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

    nomes, precos, quantidades = [], [], []
    for nome, preco, quantidade in produtos_exemplo:
        nomes.append(nome)
        precos.append(preco)
        quantidades.append(quantidade)

    salvar_produtos(nomes, precos, quantidades)


def cadastrar_produto():
    print("\n" + "=" * 50)
    print(" " * 12 + "CADASTRAR PRODUTO")
    print("=" * 50)

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

        # Carrega produtos existentes
        nomes, precos, quantidades = carregar_produtos()

        # Adiciona o novo produto
        nomes.append(nome)
        precos.append(preco)
        quantidades.append(quantidade)

        # Salva todos os produtos no arquivo
        salvar_produtos(nomes, precos, quantidades)

        print(f"\nProduto '{nome}' cadastrado com sucesso!")

    except ValueError:
        print("Erro: Digite valores numéricos válidos!")


def listar_produtos_status():
    print("\n" + "=" * 50)
    print(" " * 12 + "LISTA DE PRODUTOS")
    print("=" * 50)

    if verifica_lista_vazia():
        return

    nomes, precos, quantidades = carregar_produtos()
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
    print("\n" + "=" * 50)
    print(" " * 12 + "ALTERAÇÃO DE PRODUTOS")
    print("=" * 50)

    if verifica_lista_vazia():
        return

    listar_produtos()

    id_produto = receber_produto()

    if id_produto is None:
        print("Alteração cancelada.")
        return

    print("--- Atualizar Produto--- ")
    print("1. Atualizar nome")
    print("2. Atualizar preço")
    print("3. Atualizar quantidade")

    op = receber_op_valida()

    # Carrega os produtos atuais
    nomes, precos, quantidades = carregar_produtos()

    match op:
        case 1:
            novo_nome = input("Digite o novo nome do produto: ").strip()
            if not novo_nome or not novo_nome.replace(" ", "").isalpha():
                print("Erro: Nome inválido!")
                return
            nomes[id_produto] = novo_nome
            print(f"Nome do produto atualizado para '{novo_nome}'.")
            salvar_produtos(nomes, precos, quantidades)

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
                salvar_produtos(nomes, precos, quantidades)
            except ValueError:
                print("Erro: Digite um valor numérico válido!")

        case 3:
            try:
                nova_quantidade = int(
                    input("Digite a nova quantidade do produto: "))
                if nova_quantidade < 0:
                    print("Quantidade não pode ser negativa!")
                    return
                quantidades[id_produto] = nova_quantidade
                print(
                    f"Quantidade do produto {nomes[id_produto]} atualizada para {nova_quantidade}.")
                salvar_produtos(nomes, precos, quantidades)
            except ValueError:
                print("Erro: Digite um valor numérico válido!")

        case _:
            print("Opção inválida! Tente novamente.")


def entrada_estoque():
    print("\n" + "=" * 50)
    print(" " * 12 + "ENTRADA DE PRODUTOS")
    print("=" * 50)

    if verifica_lista_vazia():
        return

    listar_produtos()

    id_produto = receber_produto()

    if id_produto is None:
        print("Entrada cancelada.")
        return

    try:
        quantidade_entrada = int(input("Digite a quantidade da entrada: "))
        if quantidade_entrada < 0:
            print("Erro: Quantidade não pode ser negativa!")
            return
    except ValueError:
        print("Informe um valor válido")
        return

    # Carrega os produtos atuais
    nomes, precos, quantidades = carregar_produtos()

    quantidades[id_produto] += quantidade_entrada
    salvar_produtos(nomes, precos, quantidades)

    print(
        f"Quantidade {quantidade_entrada} adicionada ao produto {nomes[id_produto]}")


def saida_estoque():
    print("\n" + "=" * 50)
    print(" " * 12 + "SAÍDA DE PRODUTOS")
    print("=" * 50)

    if verifica_lista_vazia():
        return

    listar_produtos()

    id_produto = receber_produto()

    if id_produto is None:
        print("Saída cancelada.")
        return

    try:
        quantidade_saida = int(input("Digite a quantidade de saida: "))
        if quantidade_saida < 0:
            print("Erro: Quantidade não pode ser negativa!")
            return
    except ValueError:
        print("Informe um valor válido")
        return

    # Carrega os produtos atuais
    nomes, precos, quantidades = carregar_produtos()

    if quantidade_saida > quantidades[id_produto]:
        print("Quantidade insuficiente em estoque!")
        return

    quantidades[id_produto] -= quantidade_saida
    salvar_produtos(nomes, precos, quantidades)

    print(
        f"Quantidade {quantidade_saida} removida do produto {nomes[id_produto]}")


def remover_produto():
    print("\n" + "=" * 50)
    print(" " * 12 + "REMOVER PRODUTO")
    print("=" * 50)

    if verifica_lista_vazia():
        return

    listar_produtos()

    id_produto = receber_produto()

    if id_produto is None:
        print("Remoção cancelada.")
        return

    # Carrega os produtos atuais
    nomes, precos, quantidades = carregar_produtos()

    # Armazena o nome do produto que será removido para ser impresso pos remoção
    nome_removido = nomes[id_produto]

    # Remove o produto da lista
    del nomes[id_produto]
    del precos[id_produto]
    del quantidades[id_produto]

    # Salva os produtos atualizados
    salvar_produtos(nomes, precos, quantidades)

    print(f"Produto '{nome_removido}' removido com sucesso!")


def relatorio_inventario():
    print("\n" + "=" * 50)
    print(" " * 12 + "RELATÓRIO DO INVENTÁRIO")
    print("=" * 50)

    if verifica_lista_vazia():
        return

    nomes, precos, quantidades = carregar_produtos()

    print(f"\nTotal de produtos cadastrados: {len(nomes)}")
    print(
        f"Valor total do inventário: R$ {sum(precos[i] * quantidades[i] for i in range(len(nomes))):.2f}")
    print(f"Produtos em estoque: {sum(1 for q in quantidades if q > 0)}")
    print(f"Produtos esgotados: {sum(1 for q in quantidades if q == 0)}")
    print(
        f"Produtos com estoque baixo: {sum(1 for q in quantidades if 0 < q < 5)}")

    listar_produtos_status()


# Implementação da função principal do sistema(A função main() é o ponto de entrada do programa)
def main():
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
