# Sistema de Controle de Gastos
# Gerencia receitas e despesas pessoais com relatórios financeiros
receitas = []  # Lista de receitas registradas
despesas = []  # Lista de despesas registradas


def exibir_menu():
    """Exibe o menu principal do sistema financeiro"""
    print("\n" + "="*30)
    print("   CONTROLE DE GASTOS")
    print("="*30)
    print("1 - Adicionar receita")
    print("2 - Adicionar despesa")
    print("3 - Ver relatório")
    print("4 - Listar receitas")
    print("5 - Listar despesas")
    print("6 - Sair")
    print("="*30)


def adicionar_receita():
    """Registra uma nova receita no sistema"""
    print("\n--- ADICIONAR RECEITA ---")
    descricao = input("Descrição da receita: ").strip()

    if not descricao:
        print("Descrição não pode estar vazia!")
        return

    try:
        valor = float(input("Valor: R$ "))

        if valor <= 0:
            print("Valor deve ser positivo!")
            return

        receita = {
            'descricao': descricao,
            'valor': valor
        }

        receitas.append(receita)
        print(f"Receita '{descricao}' de R$ {valor:.2f} adicionada!")

    except ValueError:
        print("Digite um valor válido!")


def adicionar_despesa():
    """Registra uma nova despesa no sistema"""
    print("\n--- ADICIONAR DESPESA ---")
    descricao = input("Descrição da despesa: ").strip()
    categoria = input("Categoria (alimentação, transporte, etc.): ").strip()

    if not descricao:
        print("Descrição não pode estar vazia!")
        return

    try:
        valor = float(input("Valor: R$ "))

        if valor <= 0:
            print("Valor deve ser positivo!")
            return

        despesa = {
            'descricao': descricao,
            'categoria': categoria if categoria else 'Geral',
            'valor': valor
        }

        despesas.append(despesa)
        print(f"Despesa '{descricao}' de R$ {valor:.2f} adicionada!")

    except ValueError:
        print("Digite um valor válido!")


def calcular_totais():
    total_receitas = sum(r['valor'] for r in receitas)
    total_despesas = sum(d['valor'] for d in despesas)
    saldo = total_receitas - total_despesas

    return total_receitas, total_despesas, saldo


def ver_relatorio():
    """Gera relatório completo das finanças"""
    print("\n--- RELATÓRIO FINANCEIRO ---")

    total_receitas, total_despesas, saldo = calcular_totais()

    print(f"Total de receitas: R$ {total_receitas:.2f}")
    print(f"Total de despesas: R$ {total_despesas:.2f}")
    print("-" * 30)

    if saldo > 0:
        print(f"Saldo positivo: R$ {saldo:.2f}")
    elif saldo < 0:
        print(f"Saldo negativo: R$ {saldo:.2f}")
    else:
        print("Saldo zerado: R$ 0.00")

    # Despesas por categoria
    if despesas:
        print("\n--- DESPESAS POR CATEGORIA ---")
        categorias = {}
        for despesa in despesas:
            cat = despesa['categoria']
            if cat in categorias:
                categorias[cat] += despesa['valor']
            else:
                categorias[cat] = despesa['valor']

        for categoria, valor in categorias.items():
            print(f"  {categoria}: R$ {valor:.2f}")


def listar_receitas():
    print("\n--- LISTA DE RECEITAS ---")
    if not receitas:
        print("Nenhuma receita cadastrada.")
        return

    for i, receita in enumerate(receitas, 1):
        print(f"{i}. {receita['descricao']} - R$ {receita['valor']:.2f}")

    total = sum(r['valor'] for r in receitas)
    print(f"\nTotal: R$ {total:.2f}")


def listar_despesas():
    print("\n--- LISTA DE DESPESAS ---")
    if not despesas:
        print("Nenhuma despesa cadastrada.")
        return

    for i, despesa in enumerate(despesas, 1):
        print(
            f"{i}. {despesa['descricao']} ({despesa['categoria']}) - R$ {despesa['valor']:.2f}")

    total = sum(d['valor'] for d in despesas)
    print(f"\nTotal: R$ {total:.2f}")


def main():
    print("Bem-vindo ao Controle de Gastos!")

    while True:
        exibir_menu()

        try:
            opcao = int(input("\nEscolha uma opção: "))

            if opcao == 1:
                adicionar_receita()
            elif opcao == 2:
                adicionar_despesa()
            elif opcao == 3:
                ver_relatorio()
            elif opcao == 4:
                listar_receitas()
            elif opcao == 5:
                listar_despesas()
            elif opcao == 6:
                print("\nObrigado por usar o sistema!")
                break
            else:
                print("Opção inválida! Escolha entre 1 e 6.")

        except ValueError:
            print("Por favor, digite apenas números!")

        input("\nPressione ENTER para continuar...")


if __name__ == "__main__":
    main()
