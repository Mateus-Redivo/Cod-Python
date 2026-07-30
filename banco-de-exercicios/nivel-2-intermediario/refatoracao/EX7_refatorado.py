# Refatoracao de EX7 — Controle de Vendas Concessionaria
# Problemas originais: bloco de venda copiado 5 vezes, calculos repetidos,
# validacoes sem try/except.

COMISSAO_PERCENTUAL = 0.03


def obter_texto(mensagem, minimo=2):
    while True:
        valor = input(mensagem).strip()
        if len(valor) >= minimo:
            return valor
        print(f"Digite pelo menos {minimo} caracteres.")


def obter_preco(mensagem):
    while True:
        try:
            preco = float(input(mensagem))
            if preco > 0:
                return preco
            print("O preco deve ser positivo.")
        except ValueError:
            print("Digite um numero valido.")


def obter_desconto(mensagem):
    while True:
        try:
            desconto = float(input(mensagem))
            if 0 <= desconto <= 30:
                return desconto
            print("O desconto deve estar entre 0% e 30%.")
        except ValueError:
            print("Digite um numero valido.")


def registrar_venda(numero):
    print(f"\n--- Venda {numero} ---")
    modelo = obter_texto("Modelo do carro: ")
    cor = obter_texto("Cor: ")
    preco = obter_preco("Preco de tabela: R$ ")
    vendedor = obter_texto("Nome do vendedor: ")
    desconto = obter_desconto("Desconto (%): ")

    preco_final = preco * (1 - desconto / 100)
    comissao = preco_final * COMISSAO_PERCENTUAL

    return {
        "modelo": modelo, "cor": cor, "vendedor": vendedor,
        "preco": preco, "desconto": desconto,
        "preco_final": preco_final, "comissao": comissao,
    }


def exibir_resumo(vendas):
    print("\n=== Resumo de Vendas ===")
    for v in vendas:
        print(f"{v['modelo']} ({v['cor']}) | Vendedor: {v['vendedor']} | "
              f"R${v['preco']:.2f} -{v['desconto']:.0f}% = R${v['preco_final']:.2f} | "
              f"Comissao: R${v['comissao']:.2f}")
    total = sum(v["preco_final"] for v in vendas)
    total_comissao = sum(v["comissao"] for v in vendas)
    print(f"\nTotal de vendas: R$ {total:.2f}")
    print(f"Total de comissoes: R$ {total_comissao:.2f}")


vendas = [registrar_venda(i) for i in range(1, 6)]
exibir_resumo(vendas)
