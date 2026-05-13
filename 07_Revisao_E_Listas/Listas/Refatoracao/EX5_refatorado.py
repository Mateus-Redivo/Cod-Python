# Refatoracao de EX5 — Gerenciamento RH Funcionarios
# Problemas originais: 165 linhas repetidas 3 vezes, bug na linha 218 (bonus_tempo_func3
# usado no lugar de func1), constantes magicas espalhadas.

BONUS_CARGO = {"gerente": 0.20, "supervisor": 0.15, "analista": 0.10, "assistente": 0.05}
CARGOS = list(BONUS_CARGO.keys())
VALOR_HORA_EXTRA = 50.0
ALIQUOTA_INSS = 0.11
FAIXAS_IR = [
    (1903.98, 0.0),
    (2826.65, 0.075),
    (3751.05, 0.15),
    (4664.68, 0.225),
    (float("inf"), 0.275),
]


def obter_nome(mensagem):
    while True:
        nome = input(mensagem).strip()
        if len(nome) >= 2:
            return nome
        print("Nome deve ter pelo menos 2 caracteres.")


def obter_cargo(mensagem):
    while True:
        cargo = input(mensagem).lower().strip()
        if cargo in CARGOS:
            return cargo
        print(f"Cargo invalido. Opcoes: {', '.join(CARGOS)}")


def obter_positivo(mensagem, tipo=float):
    while True:
        try:
            valor = tipo(input(mensagem))
            if valor >= 0:
                return valor
            print("O valor nao pode ser negativo.")
        except ValueError:
            print("Digite um numero valido.")


def calcular_ir(salario_bruto):
    for limite, aliquota in FAIXAS_IR:
        if salario_bruto <= limite:
            return salario_bruto * aliquota
    return salario_bruto * FAIXAS_IR[-1][1]


def cadastrar_funcionario(numero):
    print(f"\n--- Funcionario {numero} ---")
    nome = obter_nome("Nome: ")
    cargo = obter_cargo(f"Cargo ({'/'.join(CARGOS)}): ")
    salario_base = obter_positivo("Salario base: R$ ")
    horas_extras = obter_positivo("Horas extras no mes: ", tipo=int)
    anos = obter_positivo("Anos na empresa: ", tipo=int)

    bonus_cargo = salario_base * BONUS_CARGO[cargo]
    bonus_tempo = salario_base * 0.05 if anos >= 5 else 0
    valor_horas_extras = horas_extras * VALOR_HORA_EXTRA
    salario_bruto = salario_base + bonus_cargo + bonus_tempo + valor_horas_extras
    inss = salario_bruto * ALIQUOTA_INSS
    ir = calcular_ir(salario_bruto)
    salario_liquido = salario_bruto - inss - ir

    return {
        "nome": nome, "cargo": cargo, "salario_base": salario_base,
        "salario_bruto": salario_bruto, "inss": inss, "ir": ir,
        "salario_liquido": salario_liquido,
    }


def exibir_folha(funcionarios):
    print("\n=== Folha de Pagamento ===")
    for f in funcionarios:
        print(f"\n{f['nome']} ({f['cargo']})")
        print(f"  Bruto:   R$ {f['salario_bruto']:.2f}")
        print(f"  INSS:   -R$ {f['inss']:.2f}")
        print(f"  IR:     -R$ {f['ir']:.2f}")
        print(f"  Liquido: R$ {f['salario_liquido']:.2f}")
    total = sum(f["salario_liquido"] for f in funcionarios)
    print(f"\nTotal da folha: R$ {total:.2f}")


funcionarios = [cadastrar_funcionario(i) for i in range(1, 4)]
exibir_folha(funcionarios)
