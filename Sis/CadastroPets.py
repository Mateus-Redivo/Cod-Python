# Sistema de Cadastro de Pets
pets = []


def exibir_menu():
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
    print("\n--- CADASTRAR PET ---")
    nome = input("Nome do pet: ").strip()
    especie = input("Espécie (cão, gato, etc.): ").strip()

    if not nome:
        print("Nome não pode estar vazio!")
        return

    try:
        idade = int(input("Idade (em anos): "))

        if idade < 0:
            print("Idade deve ser positiva!")
            return

        pet = {
            'nome': nome,
            'especie': especie if especie else 'Não informado',
            'idade': idade,
            'vacinas': []
        }

        pets.append(pet)
        print(f"✅ Pet '{nome}' cadastrado com sucesso!")

    except ValueError:
        print("Digite uma idade válida!")


def listar_pets():
    print("\n--- LISTA DE PETS ---")
    if not pets:
        print("Nenhum pet cadastrado.")
        return

    for i, pet in enumerate(pets, 1):
        vacinas_count = len(pet['vacinas'])
        print(f"{i}. {pet['nome']} ({pet['especie']}) - {pet['idade']} anos")
        print(f"   Vacinas: {vacinas_count}")


def vacinar_pet():
    print("\n--- VACINAR PET ---")
    if not pets:
        print("Nenhum pet cadastrado.")
        return

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

            pets[indice]['vacinas'].append(vacina)
            print(f"💉 {pets[indice]['nome']} foi vacinado com {vacina}!")

        else:
            print("Pet inválido!")
    except ValueError:
        print("Digite apenas números!")


def ver_vacinas():
    print("\n--- VACINAS DOS PETS ---")
    if not pets:
        print("Nenhum pet cadastrado.")
        return

    for pet in pets:
        print(f"\n🐾 {pet['nome']} ({pet['especie']}):")
        if pet['vacinas']:
            for i, vacina in enumerate(pet['vacinas'], 1):
                print(f"  {i}. {vacina}")
        else:
            print("  Nenhuma vacina aplicada")


def main():
    print("Bem-vindo ao Sistema de Pets!")

    while True:
        exibir_menu()

        try:
            opcao = int(input("\nEscolha uma opção: "))

            if opcao == 1:
                cadastrar_pet()
            elif opcao == 2:
                listar_pets()
            elif opcao == 3:
                vacinar_pet()
            elif opcao == 4:
                ver_vacinas()
            elif opcao == 5:
                print("\n🐾 Obrigado por cuidar dos pets! 🐾")
                break
            else:
                print("⚠️  Opção inválida! Escolha entre 1 e 5.")

        except ValueError:
            print("⚠️  Por favor, digite apenas números!")

        input("\nPressione ENTER para continuar...")


if __name__ == "__main__":
    main()
