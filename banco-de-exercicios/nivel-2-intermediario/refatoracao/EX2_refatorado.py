# Refatoracao de EX2 — Cadastro de Alunos
# Problemas originais: variaveis nome1/nome2/nome3, blocos copiados, sem funcoes.

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
            print("Digite um numero inteiro valido.")


def obter_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Digite um numero valido.")


def cadastrar_aluno(numero):
    print(f"\n--- Aluno {numero} ---")
    nome = obter_nome("Nome: ")
    idade = obter_inteiro("Idade: ", 5, 100)
    nota = obter_nota("Nota: ")
    return {"nome": nome, "idade": idade, "nota": nota}


def exibir_relatorio(alunos):
    print("\n=== Relatorio da Turma ===")
    for aluno in alunos:
        print(f"{aluno['nome']} | Idade: {aluno['idade']} | Nota: {aluno['nota']:.1f}")
    media = sum(a["nota"] for a in alunos) / len(alunos)
    print(f"\nMedia da turma: {media:.2f}")


alunos = [cadastrar_aluno(i) for i in range(1, 4)]
exibir_relatorio(alunos)
