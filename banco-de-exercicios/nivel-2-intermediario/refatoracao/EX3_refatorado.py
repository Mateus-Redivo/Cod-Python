# Refatoracao de EX3 — Sistema de Vendas Lanchonete
# Problemas originais: bloco de produto copiado 4 vezes, validacao incorreta com isdigit() em float.

def obter_nome(mensagem):
    while True:
        nome = input(mensagem).strip()
        if len(nome) >= 2:
            return nome
        print("Nome deve ter pelo menos 2 caracteres.")


def obter_positivo(mensagem, tipo=float):
    while True:
        try:
            valor = tipo(input(mensagem))
            if valor > 0:
                return valor
            print("O valor deve ser maior que zero.")
        except ValueError:
            print("Digite um numero valido.")


def registrar_produto(numero):
    print(f"\n--- Produto {numero} ---")
    nome = obter_nome("Nome do produto: ")
    preco = obter_positivo("Preco unitario: R$ ")
    quantidade = obter_positivo("Quantidade vendida: ", tipo=int)
    subtotal = preco * quantidade
    return {"nome": nome, "preco": preco, "quantidade": quantidade, "subtotal": subtotal}


def exibir_relatorio(produtos):
    print("\n=== Relatorio de Vendas ===")
    for p in produtos:
        print(f"{p['nome']}: {p['quantidade']} x R${p['preco']:.2f} = R${p['subtotal']:.2f}")

    total = sum(p["subtotal"] for p in produtos)
    mais_vendido = max(produtos, key=lambda p: p["quantidade"])
    print(f"\nTotal arrecadado: R$ {total:.2f}")
    print(f"Produto mais vendido: {mais_vendido['nome']} ({mais_vendido['quantidade']} unidades)")


produtos = [registrar_produto(i) for i in range(1, 5)]
exibir_relatorio(produtos)
