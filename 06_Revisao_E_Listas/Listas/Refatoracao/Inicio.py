# Refatorem o código em funções para evitar repetição, consistência de validações e melhorar a organização.

def cadastrar():
    try:
        nome = input("Nome do produto: ").strip().replace(" ", "")
        if not nome.isalpha() or len(nome) < 2:
            raise ValueError(
                "Nome inválido! Deve conter apenas letras e ter pelo menos 2 caracteres.")

        preco = float(input("Preço do produto: R$ "))
        if preco <= 0 or preco > 1000:
            raise ValueError(
                "Preço inválido! Deve ser entre R$ 0,01 e R$ 1000,00.")
    except ValueError as e:
        print(e)
        return None, None
    return nome, preco


def alterar():
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: R$ "))
    return nome, preco


def listar(nome, preco):
    if nome and preco:
        print(f"O produto {nome} foi cadastrado com o preço de R$ {preco:.2f}.")
    else:
        print("Produto não cadastrado devido a erros.")
