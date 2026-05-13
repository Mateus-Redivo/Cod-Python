# Refatoracao de EX4 — Controle de Estoque Farmacia
# Problemas originais: validacao repetida 3 vezes, logica de desconto inconsistente,
# variavel 'd' nao usada, importacao invalida de narwhals.

CATEGORIAS = ["antibiotico", "analgesico", "vitamina"]
DESCONTOS = {"antibiotico": 0.05, "analgesico": 0.10, "vitamina": 0.15}


def obter_nome(mensagem):
    while True:
        nome = input(mensagem).strip()
        if len(nome) >= 2:
            return nome
        print("Nome deve ter pelo menos 2 caracteres.")


def obter_preco(mensagem):
    while True:
        try:
            preco = float(input(mensagem))
            if preco > 0:
                return preco
            print("O preco deve ser positivo.")
        except ValueError:
            print("Digite um numero valido.")


def obter_estoque(mensagem):
    while True:
        try:
            qtd = int(input(mensagem))
            if qtd >= 0:
                return qtd
            print("O estoque nao pode ser negativo.")
        except ValueError:
            print("Digite um numero inteiro.")


def obter_categoria(mensagem):
    while True:
        cat = input(mensagem).lower().strip()
        if cat in CATEGORIAS:
            return cat
        print(f"Categoria invalida. Opcoes: {', '.join(CATEGORIAS)}")


def cadastrar_medicamento(numero):
    print(f"\n--- Medicamento {numero} ---")
    nome = obter_nome("Nome: ")
    preco = obter_preco("Preco: R$ ")
    estoque = obter_estoque("Quantidade em estoque: ")
    categoria = obter_categoria("Categoria (antibiotico/analgesico/vitamina): ")
    desconto = DESCONTOS[categoria]
    preco_final = preco * (1 - desconto)
    return {
        "nome": nome,
        "preco": preco,
        "estoque": estoque,
        "categoria": categoria,
        "desconto": desconto,
        "preco_final": preco_final,
        "valor_estoque": preco_final * estoque,
    }


def exibir_relatorio(medicamentos):
    print("\n=== Relatorio de Estoque ===")
    for m in medicamentos:
        print(f"{m['nome']} | {m['categoria']} | "
              f"R${m['preco']:.2f} -> R${m['preco_final']:.2f} "
              f"({m['desconto']*100:.0f}% desconto) | "
              f"Estoque: {m['estoque']}")
    total = sum(m["valor_estoque"] for m in medicamentos)
    print(f"\nValor total do estoque: R$ {total:.2f}")


medicamentos = [cadastrar_medicamento(i) for i in range(1, 4)]
exibir_relatorio(medicamentos)
