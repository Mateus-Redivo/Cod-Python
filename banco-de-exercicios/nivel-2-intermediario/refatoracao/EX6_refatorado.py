# Refatoracao de EX6 — Cadastro de Livros Biblioteca
# Problemas originais: 4 blocos identicos, 20 variaveis numeradas (titulo1..4),
# soma manual de precos no final.

def obter_texto(mensagem, minimo=2):
    while True:
        valor = input(mensagem).strip()
        if len(valor) >= minimo:
            return valor
        print(f"Digite pelo menos {minimo} caracteres.")


def obter_inteiro(mensagem, minimo, maximo):
    while True:
        try:
            valor = int(input(mensagem))
            if minimo <= valor <= maximo:
                return valor
            print(f"Digite um valor entre {minimo} e {maximo}.")
        except ValueError:
            print("Digite um numero inteiro.")


def obter_preco(mensagem):
    while True:
        try:
            preco = float(input(mensagem))
            if preco > 0:
                return preco
            print("O preco deve ser positivo.")
        except ValueError:
            print("Digite um numero valido.")


def cadastrar_livro(numero):
    print(f"\n--- Livro {numero} ---")
    titulo = obter_texto("Titulo: ")
    autor = obter_texto("Autor: ")
    paginas = obter_inteiro("Numero de paginas: ", 1, 10000)
    preco = obter_preco("Preco: R$ ")
    ano = obter_inteiro("Ano de publicacao: ", 1000, 2025)
    return {"titulo": titulo, "autor": autor, "paginas": paginas, "preco": preco, "ano": ano}


def exibir_relatorio(livros):
    print("\n=== Acervo da Biblioteca ===")
    for livro in livros:
        print(f"{livro['titulo']} — {livro['autor']} "
              f"({livro['ano']}) | {livro['paginas']} pag | R$ {livro['preco']:.2f}")
    total = sum(l["preco"] for l in livros)
    media_paginas = sum(l["paginas"] for l in livros) / len(livros)
    mais_caro = max(livros, key=lambda l: l["preco"])
    print(f"\nTotal do acervo: R$ {total:.2f}")
    print(f"Media de paginas: {media_paginas:.0f}")
    print(f"Livro mais caro: {mais_caro['titulo']} (R$ {mais_caro['preco']:.2f})")


livros = [cadastrar_livro(i) for i in range(1, 5)]
exibir_relatorio(livros)
