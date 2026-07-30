# Refatoracao de EX9 — Sistema de Reservas Hotel
# Problemas originais: 4 blocos identicos (24 variaveis numeradas),
# logica de desconto por tipo de quarto repetida 4 vezes.

TIPOS_QUARTO = ["standard", "superior", "luxo", "suite"]
DESCONTOS_QUARTO = {"standard": 0.0, "superior": 0.05, "luxo": 0.10, "suite": 0.15}
PRECO_CAFE = 25.0


def obter_nome(mensagem):
    while True:
        nome = input(mensagem).strip()
        if len(nome) >= 2:
            return nome
        print("Nome deve ter pelo menos 2 caracteres.")


def obter_tipo_quarto(mensagem):
    while True:
        tipo = input(mensagem).lower().strip()
        if tipo in TIPOS_QUARTO:
            return tipo
        print(f"Tipo invalido. Opcoes: {', '.join(TIPOS_QUARTO)}")


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


def obter_sim_nao(mensagem):
    while True:
        resp = input(mensagem).lower().strip()
        if resp in ["s", "n"]:
            return resp == "s"
        print("Digite 's' para sim ou 'n' para nao.")


def registrar_reserva(numero):
    print(f"\n--- Reserva {numero} ---")
    hospede = obter_nome("Nome do hospede: ")
    tipo = obter_tipo_quarto(f"Tipo de quarto ({'/'.join(TIPOS_QUARTO)}): ")
    numero_quarto = obter_inteiro("Numero do quarto: ", 1, 999)
    dias = obter_inteiro("Dias de estadia: ", 1, 30)
    diaria = obter_preco("Valor da diaria: R$ ")
    cafe = obter_sim_nao("Incluir cafe da manha? (s/n): ")

    desconto = DESCONTOS_QUARTO[tipo]
    valor_base = diaria * dias
    valor_cafe = PRECO_CAFE * dias if cafe else 0
    valor_final = valor_base * (1 - desconto) + valor_cafe

    return {
        "hospede": hospede, "tipo": tipo, "numero": numero_quarto,
        "dias": dias, "diaria": diaria, "cafe": cafe,
        "desconto": desconto, "valor_final": valor_final,
    }


def exibir_relatorio(reservas):
    print("\n=== Relatorio de Reservas ===")
    for r in reservas:
        cafe_str = "com cafe" if r["cafe"] else "sem cafe"
        print(f"Quarto {r['numero']} ({r['tipo']}) | {r['hospede']} | "
              f"{r['dias']} dias | {cafe_str} | "
              f"Desconto: {r['desconto']*100:.0f}% | Total: R${r['valor_final']:.2f}")
    total_geral = sum(r["valor_final"] for r in reservas)
    print(f"\nReceita total: R$ {total_geral:.2f}")


reservas = [registrar_reserva(i) for i in range(1, 5)]
exibir_relatorio(reservas)
