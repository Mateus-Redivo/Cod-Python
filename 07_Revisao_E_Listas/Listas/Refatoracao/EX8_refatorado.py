# Refatoracao de EX8 — Cadastro de Produtos Supermercado
# Problemas originais: 3 blocos identicos, validacao de codigo de 6 digitos repetida 3 vezes,
# logica de desconto repetida, verificacao de categorias com if/or no final.

CATEGORIAS = ["alimentos", "limpeza", "higiene", "bebidas"]
DESCONTOS = {"alimentos": 0.05, "limpeza": 0.10, "higiene": 0.08, "bebidas": 0.03}


def obter_nome(mensagem):
    while True:
        nome = input(mensagem).strip()
        if len(nome) >= 2:
            return nome
        print("Nome deve ter pelo menos 2 caracteres.")


def obter_categoria(mensagem):
    while True:
        cat = input(mensagem).lower().strip()
        if cat in CATEGORIAS:
            return cat
        print(f"Categoria invalida. Opcoes: {', '.join(CATEGORIAS)}")


def obter_preco(mensagem):
    while True:
        try:
            preco = float(input(mensagem))
            if preco > 0:
                return preco
            print("O preco deve ser positivo.")
        except ValueError:
            print("Digite um numero valido.")


def obter_quantidade(mensagem):
    while True:
        try:
            qtd = int(input(mensagem))
            if qtd >= 0:
                return qtd
            print("A quantidade nao pode ser negativa.")
        except ValueError:
            print("Digite um numero inteiro.")


def obter_codigo(mensagem):
    while True:
        codigo = input(mensagem).strip()
        if len(codigo) == 6 and codigo.isdigit():
            return codigo
        print("O codigo deve ter exatamente 6 digitos numericos.")


def cadastrar_produto(numero):
    print(f"\n--- Produto {numero} ---")
    nome = obter_nome("Nome: ")
    categoria = obter_categoria(f"Categoria ({'/'.join(CATEGORIAS)}): ")
    preco = obter_preco("Preco: R$ ")
    quantidade = obter_quantidade("Quantidade em estoque: ")
    codigo = obter_codigo("Codigo (6 digitos): ")

    desconto = DESCONTOS[categoria]
    preco_final = preco * (1 - desconto)
    valor_estoque = preco_final * quantidade

    return {
        "nome": nome, "categoria": categoria, "preco": preco,
        "quantidade": quantidade, "codigo": codigo,
        "desconto": desconto, "preco_final": preco_final, "valor_estoque": valor_estoque,
    }


def exibir_relatorio(produtos):
    print("\n=== Relatorio do Estoque ===")
    for p in produtos:
        print(f"[{p['codigo']}] {p['nome']} ({p['categoria']}) | "
              f"R${p['preco']:.2f} -{p['desconto']*100:.0f}% = R${p['preco_final']:.2f} | "
              f"Qtd: {p['quantidade']} | Total: R${p['valor_estoque']:.2f}")
    for cat in CATEGORIAS:
        count = sum(1 for p in produtos if p["categoria"] == cat)
        if count:
            print(f"Produtos em '{cat}': {count}")


produtos = [cadastrar_produto(i) for i in range(1, 4)]
exibir_relatorio(produtos)
