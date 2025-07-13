import random

<<<<<<< HEAD

def gerar_numero_aleatorio(min_val=1, max_val=100):
    return random.randint(min_val, max_val)


=======
def gerar_numero_aleatorio(min_val=1, max_val=100):
    return random.randint(min_val, max_val)

>>>>>>> 680283a4c776b59b73511f223aa6e8984191356d
def verificar_palpite(palpite, numero_secreto):
    if palpite < numero_secreto:
        return "maior"
    elif palpite > numero_secreto:
        return "menor"
    else:
        return "igual"

<<<<<<< HEAD

=======
>>>>>>> 680283a4c776b59b73511f223aa6e8984191356d
def jogo_adivinhacao():
    numero_secreto = gerar_numero_aleatorio(1, 100)
    tentativas = 0
    max_tentativas = 7
<<<<<<< HEAD

    print("=== JOGO DE ADIVINHAÇÃO ===")
    print(
        f"Tente adivinhar o número entre 1 e 100 em {max_tentativas} tentativas!")

=======
    
    print("=== JOGO DE ADIVINHAÇÃO ===")
    print(f"Tente adivinhar o número entre 1 e 100 em {max_tentativas} tentativas!")
    
>>>>>>> 680283a4c776b59b73511f223aa6e8984191356d
    while tentativas < max_tentativas:
        try:
            palpite = int(input("Seu palpite: "))
            tentativas += 1
<<<<<<< HEAD

=======
            
>>>>>>> 680283a4c776b59b73511f223aa6e8984191356d
            resultado = verificar_palpite(palpite, numero_secreto)
            if resultado == "igual":
                print(f"Parabéns! Você acertou em {tentativas} tentativas!")
                return True
            elif resultado == "maior":
<<<<<<< HEAD
                print(
                    f"Tente um número MAIOR! Tentativas restantes: {max_tentativas - tentativas}")
            else:
                print(
                    f"Tente um número MENOR! Tentativas restantes: {max_tentativas - tentativas}")

        except ValueError:
            print("Por favor, digite um número válido!")

    print(f"Game over! O número secreto era {numero_secreto}.")
    return False


# Para jogar o jogo de adivinhação, descomente a linha abaixo
jogo_adivinhacao()
=======
                print(f"Tente um número MAIOR! Tentativas restantes: {max_tentativas - tentativas}")
            else:
                print(f"Tente um número MENOR! Tentativas restantes: {max_tentativas - tentativas}")
                
        except ValueError:
            print("Por favor, digite um número válido!")
    
    print(f"Game over! O número secreto era {numero_secreto}.")
    return False

# Para jogar o jogo de adivinhação, descomente a linha abaixo
jogo_adivinhacao()

>>>>>>> 680283a4c776b59b73511f223aa6e8984191356d
