# Sistema de Calculadora de Notas
alunos = []


def exibir_menu():
    print("\n" + "="*30)
    print("   CALCULADORA DE NOTAS")
    print("="*30)
    print("1 - Cadastrar aluno")
    print("2 - Adicionar nota")
    print("3 - Ver situação dos alunos")
    print("4 - Sair")
    print("="*30)


def cadastrar_aluno():
    print("\n--- CADASTRAR ALUNO ---")
    nome = input("Digite o nome do aluno: ").strip()

    if not nome:
        print("Nome não pode estar vazio!")
        return

    # Verificar se já existe
    for aluno in alunos:
        if aluno['nome'].lower() == nome.lower():
            print("Aluno já cadastrado!")
            return

    aluno = {
        'nome': nome,
        'notas': []
    }

    alunos.append(aluno)
    print(f"✅ Aluno '{nome}' cadastrado com sucesso!")


def adicionar_nota():
    print("\n--- ADICIONAR NOTA ---")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    print("Alunos cadastrados:")
    for i, aluno in enumerate(alunos, 1):
        print(f"{i}. {aluno['nome']}")

    try:
        indice = int(input("\nEscolha o aluno: ")) - 1

        if 0 <= indice < len(alunos):
            nota = float(input("Digite a nota (0-10): "))

            if 0 <= nota <= 10:
                alunos[indice]['notas'].append(nota)
                print(
                    f"✅ Nota {nota} adicionada para {alunos[indice]['nome']}!")
            else:
                print("Nota deve estar entre 0 e 10!")
        else:
            print("Aluno inválido!")
    except ValueError:
        print("Digite apenas números!")


def calcular_media(notas):
    if not notas:
        return 0
    return sum(notas) / len(notas)


def determinar_situacao(media):
    if media >= 7:
        return "✅ APROVADO"
    elif media >= 5:
        return "⚠️  RECUPERAÇÃO"
    else:
        return "❌ REPROVADO"


def ver_situacao():
    print("\n--- SITUAÇÃO DOS ALUNOS ---")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos:
        media = calcular_media(aluno['notas'])
        situacao = determinar_situacao(media)

        print(f"\n{aluno['nome']}:")
        print(f"  Notas: {aluno['notas']}")
        print(f"  Média: {media:.1f}")
        print(f"  Situação: {situacao}")


def main():
    print("Bem-vindo à Calculadora de Notas!")

    while True:
        exibir_menu()

        try:
            opcao = int(input("\nEscolha uma opção: "))

            if opcao == 1:
                cadastrar_aluno()
            elif opcao == 2:
                adicionar_nota()
            elif opcao == 3:
                ver_situacao()
            elif opcao == 4:
                print("\n🎓 Obrigado por usar o sistema! 🎓")
                break
            else:
                print("⚠️  Opção inválida! Escolha entre 1 e 4.")

        except ValueError:
            print("⚠️  Por favor, digite apenas números!")

        input("\nPressione ENTER para continuar...")


if __name__ == "__main__":
    main()
