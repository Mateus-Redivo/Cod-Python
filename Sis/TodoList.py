# Sistema de To-Do List (Lista de Tarefas)
# Gerencia tarefas pessoais com controle de status
tarefas = []  # Lista de tarefas cadastradas


def exibir_menu():
    """Exibe o menu principal do sistema de tarefas"""
    print("\n" + "="*30)
    print("     LISTA DE TAREFAS")
    print("="*30)
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Marcar como concluída")
    print("4 - Remover tarefa")
    print("5 - Sair")
    print("="*30)


def adicionar_tarefa():
    """Adiciona uma nova tarefa à lista"""
    print("\n--- ADICIONAR TAREFA ---")
    descricao = input("Digite a descrição da tarefa: ").strip()

    if not descricao:
        print("Descrição não pode estar vazia!")
        return

    tarefa = {
        'descricao': descricao,
        'concluida': False
    }

    tarefas.append(tarefa)
    print(f"Tarefa '{descricao}' adicionada com sucesso!")


def listar_tarefas():
    """Lista todas as tarefas com seus status"""
    print("\n--- LISTA DE TAREFAS ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    pendentes = 0
    concluidas = 0

    for i, tarefa in enumerate(tarefas, 1):
        if tarefa['concluida']:
            print(f"{i}. {tarefa['descricao']} (CONCLUÍDA)")
            concluidas += 1
        else:
            print(f"{i}. {tarefa['descricao']} (PENDENTE)")
            pendentes += 1

    print(f"\nResumo: {pendentes} pendente(s), {concluidas} concluída(s)")


def marcar_concluida():
    """Marca uma tarefa como concluída"""
    print("\n--- MARCAR COMO CONCLUÍDA ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    # Mostrar apenas tarefas pendentes
    pendentes = [t for t in tarefas if not t['concluida']]

    if not pendentes:
        print("Todas as tarefas já estão concluídas!")
        return

    print("Tarefas pendentes:")
    for i, tarefa in enumerate(pendentes, 1):
        print(f"{i}. {tarefa['descricao']}")

    try:
        indice = int(input("\nDigite o número da tarefa: ")) - 1

        if 0 <= indice < len(pendentes):
            pendentes[indice]['concluida'] = True
            print(
                f"Tarefa '{pendentes[indice]['descricao']}' marcada como concluída!")
        else:
            print("Número inválido!")
    except ValueError:
        print("Digite apenas números!")


def remover_tarefa():
    """Remove uma tarefa da lista"""
    print("\n--- REMOVER TAREFA ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    listar_tarefas()

    try:
        indice = int(input("\nDigite o número da tarefa para remover: ")) - 1

        if 0 <= indice < len(tarefas):
            tarefa_removida = tarefas.pop(indice)
            print(f"Tarefa '{tarefa_removida['descricao']}' removida!")
        else:
            print("Número inválido!")
    except ValueError:
        print("Digite apenas números!")


def main():
    """Função principal que executa o sistema de tarefas"""
    print("Bem-vindo ao Sistema de Tarefas!")

    while True:
        exibir_menu()

        try:
            opcao = int(input("\nEscolha uma opção: "))

            if opcao == 1:
                adicionar_tarefa()
            elif opcao == 2:
                listar_tarefas()
            elif opcao == 3:
                marcar_concluida()
            elif opcao == 4:
                remover_tarefa()
            elif opcao == 5:
                print("\nObrigado por usar o sistema!")
                break
            else:
                print("Opção inválida! Escolha entre 1 e 5.")

        except ValueError:
            print("Por favor, digite apenas números!")

        input("\nPressione ENTER para continuar...")


if __name__ == "__main__":
    main()
