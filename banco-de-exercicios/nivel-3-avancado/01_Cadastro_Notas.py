def registrar_aluno(banco_de_dados, nome, nota1, nota2, nota3):
    """Registra um aluno e suas 3 notas"""
    try:
        # Converte as notas para números
        notas = [float(nota1), float(nota2), float(nota3)]
        banco_de_dados[nome] = notas
        return True
    except ValueError:
        print("Erro: As notas devem ser números válidos.")
        return False

def calcular_media(notas):
    """Calcula a média das notas"""
    return sum(notas) / len(notas)

def exibir_alunos(banco_de_dados):
    """Exibe todos os alunos, suas notas e médias"""
    print("\n===== REGISTROS DE ALUNOS =====")
    print("Nome            Nota 1  Nota 2  Nota 3  Média")
    print("---------------------------------------")
    for nome, notas in banco_de_dados.items():
        media = calcular_media(notas)
        print(
            f"{nome:<15} {notas[0]:>6.1f} {notas[1]:>7.1f} {notas[2]:>7.1f} {media:>7.1f}")

def menu():
    """Exibe o menu de opções"""
    print("\n===== SISTEMA DE NOTAS =====")
    print("1 - Registrar novo aluno")
    print("2 - Ver todos os alunos")
    print("3 - Calcular média de um aluno")
    print("4 - Sair")
    return input("Escolha uma opção: ")

def registrar_novo_aluno(banco_de_dados):
    nome = input("Nome do aluno: ")
    nota1 = input("Nota 1: ")
    nota2 = input("Nota 2: ")
    nota3 = input("Nota 3: ")
    if registrar_aluno(banco_de_dados, nome, nota1, nota2, nota3):
        print(f"Aluno {nome} registrado com sucesso!")

def ver_todos_alunos(banco_de_dados):
    if banco_de_dados:
        exibir_alunos(banco_de_dados)
    else:
        print("Nenhum aluno registrado.")

def calcular_media_aluno(banco_de_dados):
    nome = input("Nome do aluno: ")
    if nome in banco_de_dados:
        media = calcular_media(banco_de_dados[nome])
        print(f"A média de {nome} é {media:.1f}")
    else:
        print(f"Aluno {nome} não encontrado.")

def main():
    """Função principal do programa"""
    banco_de_dados = {}

    while True:
        opcao = menu()

        if opcao == '1':
            registrar_novo_aluno(banco_de_dados)
        elif opcao == '2':
            ver_todos_alunos(banco_de_dados)
        elif opcao == '3':
            calcular_media_aluno(banco_de_dados)
        elif opcao == '4':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
