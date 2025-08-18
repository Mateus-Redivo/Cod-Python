# Sistema de Cadastro de Churrasco
participantes = []
carnes = []
bebidas = []

def exibir_menu():
    print("\n" + "="*40)
    print("       SISTEMA DE CHURRASCO")
    print("="*40)
    print("1 - Cadastrar participante")
    print("2 - Listar participantes")
    print("3 - Listar itens do churrasco")
    print("4 - Sair")
    print("="*40)

def cadastrar_participante():
    print("\n--- CADASTRO DE PARTICIPANTE ---")
    nome = input("Digite o nome do participante: ").strip()
    
    if not nome:
        print("Nome não pode estar vazio!")
        return
    
    # Verificar se já existe
    if nome.lower() in [p.lower() for p in participantes]:
        print(f"O participante {nome} já está cadastrado!")
        return
    
    print(f"\nOlá {nome}! Você precisa trazer 1 carne e 1 bebida.")
    
    # Cadastrar carne
    carne = input("Que tipo de carne você vai trazer? ").strip()
    if not carne:
        print("Tipo de carne não pode estar vazio!")
        return
    
    # Cadastrar bebida
    bebida = input("Que bebida você vai trazer? ").strip()
    if not bebida:
        print("Tipo de bebida não pode estar vazio!")
        return
    
    # Adicionar aos vetores
    participantes.append(nome)
    carnes.append(f"{carne} (por {nome})")
    bebidas.append(f"{bebida} (por {nome})")
    
    print(f"\n✅ {nome} cadastrado com sucesso!")
    print(f"   Carne: {carne}")
    print(f"   Bebida: {bebida}")

def listar_participantes():
    print("\n--- LISTA DE PARTICIPANTES ---")
    if not participantes:
        print("Nenhum participante cadastrado ainda.")
        return
    
    print(f"Total de participantes: {len(participantes)}\n")
    for i, nome in enumerate(participantes, 1):
        print(f"{i}. {nome}")

def listar_itens():
    print("\n--- ITENS DO CHURRASCO ---")
    
    if not carnes and not bebidas:
        print("Nenhum item cadastrado ainda.")
        return
    
    print("🥩 CARNES:")
    if carnes:
        for i, carne in enumerate(carnes, 1):
            print(f"  {i}. {carne}")
    else:
        print("  Nenhuma carne cadastrada.")
    
    print("\n🍺 BEBIDAS:")
    if bebidas:
        for i, bebida in enumerate(bebidas, 1):
            print(f"  {i}. {bebida}")
    else:
        print("  Nenhuma bebida cadastrada.")

def main():
    print("Bem-vindo ao Sistema de Cadastro de Churrasco!")
    
    while True:
        exibir_menu()
        
        try:
            opcao = int(input("\nEscolha uma opção: "))
            
            if opcao == 1:
                cadastrar_participante()
            elif opcao == 2:
                listar_participantes()
            elif opcao == 3:
                listar_itens()
            elif opcao == 4:
                print("\n🔥 Obrigado por usar o sistema! Bom churrasco! 🔥")
                break
            else:
                print("⚠️  Opção inválida! Escolha entre 1 e 4.")
                
        except ValueError:
            print("⚠️  Por favor, digite apenas números!")
        
        input("\nPressione ENTER para continuar...")

# Executar o programa
if __name__ == "__main__":
    main()