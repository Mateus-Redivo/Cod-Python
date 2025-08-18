# Sistema de Calculadora de Notas
# Gerencia notas de alunos e calcula médias e situação acadêmica
alunos = []  # Lista para armazenar os alunos cadastrados


def exibir_menu():
    """Exibe o menu principal do sistema de notas"""
    print("\n" + "="*30)
    print("   CALCULADORA DE NOTAS")
    print("="*30)
    print("1 - Cadastrar aluno")
    print("2 - Adicionar nota")
    print("3 - Ver situação dos alunos")
    print("4 - Sair")
    print("="*30)


def cadastrar_aluno():
    """Cadastra um novo aluno no sistema"""
    print("\n--- CADASTRAR ALUNO ---")
    nome = input("Digite o nome do aluno: ").strip()

    if not nome:
        print("Nome não pode estar vazio!")
        return

    # Verifica se o aluno já foi cadastrado
    for aluno in alunos:
        if aluno['nome'].lower() == nome.lower():
            print("Aluno já cadastrado!")
            return

    # Cria dicionário com dados do aluno
    # Cria dicionário com dados do aluno
    aluno = {
        'nome': nome,
        'notas': []  # Lista de notas do aluno
    }

    alunos.append(aluno)
    print(f"Aluno '{nome}' cadastrado com sucesso!")


def adicionar_nota():
    """Adiciona uma nota a um aluno específico"""
    print("\n--- ADICIONAR NOTA ---")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    # Lista alunos disponíveis
    print("Alunos cadastrados:")
    for i, aluno in enumerate(alunos, 1):
        print(f"{i}. {aluno['nome']}")

    try:
        indice = int(input("\nEscolha o aluno: ")) - 1

        if 0 <= indice < len(alunos):
            nota = float(input("Digite a nota (0-10): "))

            # Valida se a nota está no intervalo correto
            if 0 <= nota <= 10:
                alunos[indice]['notas'].append(nota)
                print(
                    f"Nota {nota} adicionada para {alunos[indice]['nome']}!")
            else:
                print("Nota deve estar entre 0 e 10!")
        else:
            print("Aluno inválido!")
    except ValueError:
        print("Digite apenas números!")


def calcular_media(notas):
    """Calcula a média aritmética das notas"""
    if not notas:
        return 0
    return sum(notas) / len(notas)


def determinar_situacao(media):
    """Determina a situação do aluno baseada na média"""
    if media >= 7:
        return "APROVADO"
    elif media >= 5:
        return "RECUPERAÇÃO"
    else:
        return "REPROVADO"


def ver_situacao():
    """Exibe a situação acadêmica de todos os alunos"""
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
    """Função principal que executa o sistema de notas"""
    print("Bem-vindo à Calculadora de Notas!")

    while True:
        exibir_menu()

        try:
            opcao = int(input("\nEscolha uma opção: "))

            # Processa a opção escolhida pelo usuário
            if opcao == 1:
                cadastrar_aluno()
            elif opcao == 2:
                adicionar_nota()
            elif opcao == 3:
                ver_situacao()
            elif opcao == 4:
                print("\nObrigado por usar o sistema!")
                break
            else:
                print("Opção inválida! Escolha entre 1 e 4.")

        except ValueError:
            print("Por favor, digite apenas números!")

        input("\nPressione ENTER para continuar...")


# Executa o programa principal
if __name__ == "__main__":
    main()
