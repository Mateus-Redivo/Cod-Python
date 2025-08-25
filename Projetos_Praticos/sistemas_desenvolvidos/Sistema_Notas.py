alunos = []  # Lista para armazenar os nomes dos alunos
# Lista para armazenar as notas dos alunos (cada elemento é uma lista de notas)
notas = []


def menu():
    pass # Função de menu (a ser implementada)


def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ").strip()

    # Verifica se o nome não está vazio
    if not nome:
        print("Nome não pode estar vazio!")
        return

    # Verifica se o aluno já existe
    if nome in alunos:
        print(f"Aluno '{nome}' já está cadastrado!")
        return

    # Cadastra o aluno
    alunos.append(nome)
    notas.append([])  # Inicia com lista vazia de notas
    print(f"Aluno '{nome}' cadastrado com sucesso!")


def atualizar_nota():
    if not alunos:
        print("Nenhum aluno cadastrado!")
        return

    # Exibe os alunos cadastrados
    print("\nAlunos cadastrados:")
    for i in range(len(alunos)):
        aluno = alunos[i]
        # Calcula a média das notas do aluno
        if notas[i]:  # Se o aluno tem notas
            total_notas = sum(notas[i])
            quantidade_notas = len(notas[i])
            media = total_notas / quantidade_notas
        else:  # Se o aluno não tem notas ainda
            media = 0

        print(f"{i+1}. {aluno} - Notas: {notas[i]} - Média: {media:.2f}")

    try:
        # Recebe a escolha do usuário
        escolha = int(input("\nEscolha o número do aluno: ")) - 1

        # Verifica se a escolha é válida
        if escolha < 0 or escolha >= len(alunos):
            print("Opção inválida!")
            return

        # Recebe a nova nota
        nova_nota = float(
            input(f"Digite uma nova nota para {alunos[escolha]}: "))

        # Verifica se a nota está no intervalo válido
        if nova_nota < 0 or nova_nota > 10:
            print("Nota deve estar entre 0 e 10!")
            return

        # Adiciona a nova nota à lista de notas do aluno
        notas[escolha].append(nova_nota)
        media = sum(notas[escolha]) / len(notas[escolha])
        print(f"Nota {nova_nota} adicionada para '{alunos[escolha]}'!")
        print(f"Notas: {notas[escolha]} - Nova média: {media:.2f}")

    except ValueError:
        print("Por favor, digite um número válido!")


def main():
    pass # Função principal (a ser implementada)


if __name__ == "__main__":
    main()
