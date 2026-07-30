# Refatoracao de EX1 — Cadastro de Pratos
# Problemas originais: bloco de entrada copiado 4 vezes, sem funcoes, validacao incorreta.

def obter_nome(mensagem):
    while True:
        nome = input(mensagem).strip()
        if len(nome) >= 2:
            return nome
        print("O nome deve ter pelo menos 2 caracteres.")


def obter_preco(mensagem):
    while True:
        try:
            preco = float(input(mensagem))
            if preco > 0:
                return preco
            print("O preco deve ser maior que zero.")
        except ValueError:
            print("Digite um numero valido.")


def cadastrar_prato(numero):
    print(f"\n--- Prato {numero} ---")
    nome = obter_nome("Nome do prato: ")
    preco = obter_preco("Preco: R$ ")
    return {"nome": nome, "preco": preco}


def exibir_cardapio(pratos):
    print("\n=== Cardapio ===")
    for i, prato in enumerate(pratos, 1):
        print(f"{i}. {prato['nome']} — R$ {prato['preco']:.2f}")


pratos = [cadastrar_prato(i) for i in range(1, 5)]
exibir_cardapio(pratos)
