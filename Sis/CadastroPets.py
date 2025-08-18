# Sistema de Cadastro de Pets
# Gerencia informações de pets incluindo vacinação
pets = []  # Lista para armazenar os pets cadastrados


def exibir_menu():
    """Exibe o menu principal do sistema de pets"""
    print("\n" + "="*30)
    print("    CADASTRO DE PETS")
    print("="*30)
    print("1 - Cadastrar pet")
    print("2 - Listar pets")
    print("3 - Vacinar pet")
    print("4 - Ver vacinas")
    print("5 - Sair")
    print("="*30)


def cadastrar_pet():
    """Cadastra um novo pet no sistema"""
    print("\n--- CADASTRAR PET ---")
    nome = input("Nome do pet: ").strip()
    especie = input("Espécie (cão, gato, etc.): ").strip()

    # Valida se o nome foi preenchido
    if not nome:
        print("Nome não pode estar vazio!")
        return

    try:
        idade = int(input("Idade (em anos): "))

        # Valida se a idade é positiva
        if idade < 0:
            print("Idade deve ser positiva!")
            return

        # Cria dicionário com dados do pet
        pet = {
            'nome': nome,
            'especie': especie if especie else 'Não informado',
            'idade': idade,
            'vacinas': []  # Lista de vacinas aplicadas
        }

        pets.append(pet)
        print(f"Pet '{nome}' cadastrado com sucesso!")

    except ValueError:
        print("Digite uma idade válida!")


def listar_pets():
    """Lista todos os pets cadastrados"""
    print("\n--- LISTA DE PETS ---")
    if not pets:
        print("Nenhum pet cadastrado.")
        return

    # Exibe informações de cada pet
    for i, pet in enumerate(pets, 1):
        vacinas_count = len(pet['vacinas'])
        print(f"{i}. {pet['nome']} ({pet['especie']}) - {pet['idade']} anos")
        print(f"   Vacinas: {vacinas_count}")


def vacinar_pet():
    """Registra uma nova vacina para um pet"""
    print("\n--- VACINAR PET ---")
    if not pets:
        print("Nenhum pet cadastrado.")
        return

    # Lista pets disponíveis para vacinação
    print("Pets cadastrados:")
    for i, pet in enumerate(pets, 1):
        print(f"{i}. {pet['nome']}")

    try:
        indice = int(input("\nEscolha o pet: ")) - 1

        if 0 <= indice < len(pets):
            vacina = input("Nome da vacina: ").strip()

            if not vacina:
                print("Nome da vacina não pode estar vazio!")
                return

            # Adiciona vacina ao histórico do pet
            pets[indice]['vacinas'].append(vacina)
            print(f"{pets[indice]['nome']} foi vacinado com {vacina}!")

        else:
            print("Pet inválido!")
    except ValueError:
        print("Digite apenas números!")


def ver_vacinas():
    """Exibe o histórico de vacinas de todos os pets"""
    print("\n--- VACINAS DOS PETS ---")
    if not pets:
        print("Nenhum pet cadastrado.")
        return

    # Exibe histórico de vacinas para cada pet
    for pet in pets:
        print(f"\n{pet['nome']} ({pet['especie']}):")
        if pet['vacinas']:
            for i, vacina in enumerate(pet['vacinas'], 1):
                print(f"  {i}. {vacina}")
        else:
            print("  Nenhuma vacina aplicada")


def main():
    """Função principal que executa o sistema de pets"""
    print("Bem-vindo ao Sistema de Pets!")

    while True:
        exibir_menu()

        try:
            opcao = int(input("\nEscolha uma opção: "))

            # Processa a opção escolhida pelo usuário
            if opcao == 1:
                cadastrar_pet()
            elif opcao == 2:
                listar_pets()
            elif opcao == 3:
                vacinar_pet()
            elif opcao == 4:
                ver_vacinas()
            elif opcao == 5:
                print("\nObrigado por cuidar dos pets!")
                break
            else:
                print("Opção inválida! Escolha entre 1 e 5.")

        except ValueError:
            print("Por favor, digite apenas números!")

        input("\nPressione ENTER para continuar...")


# Executa o programa principal
if __name__ == "__main__":
    main()
