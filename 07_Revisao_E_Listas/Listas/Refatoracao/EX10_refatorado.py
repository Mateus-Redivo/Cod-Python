# Refatoracao de EX10 — Analise de Desempenho Academia
# Problemas originais: 3 blocos identicos, calculos de IMC e frequencia cardiaca
# repetidos, arrays manuais no final (objetivo1, objetivo2, objetivo3).

OBJETIVOS = ["emagrecimento", "hipertrofia", "condicionamento", "saude"]
EXPERIENCIAS = ["iniciante", "intermediario", "avancado"]
TREINOS_POR_EXPERIENCIA = {"iniciante": 3, "intermediario": 4, "avancado": 5}
FAIXAS_IMC = [
    (18.5, "Abaixo do peso"),
    (24.9, "Peso normal"),
    (29.9, "Sobrepeso"),
    (float("inf"), "Obesidade"),
]


def obter_nome(mensagem):
    while True:
        nome = input(mensagem).strip()
        if len(nome) >= 2:
            return nome
        print("Nome deve ter pelo menos 2 caracteres.")


def obter_inteiro(mensagem, minimo, maximo):
    while True:
        try:
            valor = int(input(mensagem))
            if minimo <= valor <= maximo:
                return valor
            print(f"Digite um valor entre {minimo} e {maximo}.")
        except ValueError:
            print("Digite um numero inteiro.")


def obter_decimal(mensagem, minimo, maximo):
    while True:
        try:
            valor = float(input(mensagem))
            if minimo <= valor <= maximo:
                return valor
            print(f"Digite um valor entre {minimo} e {maximo}.")
        except ValueError:
            print("Digite um numero valido.")


def obter_opcao(mensagem, opcoes):
    while True:
        valor = input(mensagem).lower().strip()
        if valor in opcoes:
            return valor
        print(f"Opcao invalida. Escolha: {', '.join(opcoes)}")


def calcular_imc(peso, altura):
    return peso / (altura ** 2)


def classificar_imc(imc):
    for limite, classificacao in FAIXAS_IMC:
        if imc <= limite:
            return classificacao
    return "Obesidade"


def cadastrar_aluno(numero):
    print(f"\n--- Aluno {numero} ---")
    nome = obter_nome("Nome: ")
    idade = obter_inteiro("Idade: ", 16, 80)
    peso = obter_decimal("Peso (kg): ", 30.0, 300.0)
    altura = obter_decimal("Altura (m): ", 1.0, 2.5)
    objetivo = obter_opcao(f"Objetivo ({'/'.join(OBJETIVOS)}): ", OBJETIVOS)
    experiencia = obter_opcao(f"Experiencia ({'/'.join(EXPERIENCIAS)}): ", EXPERIENCIAS)

    imc = calcular_imc(peso, altura)
    freq_cardiaca_max = 220 - idade
    treinos_semana = TREINOS_POR_EXPERIENCIA[experiencia]

    return {
        "nome": nome, "idade": idade, "peso": peso, "altura": altura,
        "objetivo": objetivo, "experiencia": experiencia,
        "imc": imc, "classificacao_imc": classificar_imc(imc),
        "freq_cardiaca_max": freq_cardiaca_max, "treinos_semana": treinos_semana,
    }


def exibir_relatorio(alunos):
    print("\n=== Relatorio da Academia ===")
    for a in alunos:
        print(f"\n{a['nome']} | {a['idade']} anos | {a['experiencia']}")
        print(f"  IMC: {a['imc']:.1f} ({a['classificacao_imc']})")
        print(f"  FC maxima: {a['freq_cardiaca_max']} bpm")
        print(f"  Objetivo: {a['objetivo']} | Treinos/semana: {a['treinos_semana']}")

    for objetivo in OBJETIVOS:
        count = sum(1 for a in alunos if a["objetivo"] == objetivo)
        if count:
            print(f"\nAlunos com objetivo '{objetivo}': {count}")


alunos = [cadastrar_aluno(i) for i in range(1, 4)]
exibir_relatorio(alunos)
