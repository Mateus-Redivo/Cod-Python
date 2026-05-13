def menu():
    print("Pedra Papel Tesoura")
    print("1. Jogar")
    print("0. Sair")
    op = int(input("Escolha uma opção: "))
    return op

def jogar():
    import random

    opcoes = ["pedra", "papel", "tesoura"]
    computador = random.choice(opcoes)
    
    print("Escolha uma opção:")
    print("1. Pedra")
    print("2. Papel")
    print("3. Tesoura")
    
    escolha_usuario = int(input("Digite o número da sua escolha: "))
    
    if escolha_usuario < 1 or escolha_usuario > 3:
        print("Opção inválida!")
        return
    
    usuario = opcoes[escolha_usuario - 1]
    
    print(f"Você escolheu: {usuario}")
    print(f"O computador escolheu: {computador}")
    
    if usuario == computador:
        print("Empate!")
    elif (usuario == "pedra" and computador == "tesoura") or \
         (usuario == "papel" and computador == "pedra") or \
         (usuario == "tesoura" and computador == "papel"):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

def main():
    while True:
        opcao = menu()
        if opcao == 1:
            jogar()
        elif opcao == 0:
            print("Saindo do jogo...")
            break
        else:
            print("Opção inválida! Tente novamente.")
    
if __name__ == "__main__":
    main()