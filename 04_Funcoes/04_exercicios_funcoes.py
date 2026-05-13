# Exercicios de funcoes
# Tente resolver cada exercicio antes de ver a solucao.


# Exercicio 1
# Crie uma funcao que recebe um numero e retorna True se for par, False se for impar.

# Sua solucao:


# Exercicio 2
# Crie uma funcao que recebe uma lista de numeros e retorna a soma de todos.
# Nao use sum() — implemente o calculo com um laco.

# Sua solucao:


# Exercicio 3
# Crie uma funcao que recebe um nome e retorna ele com a primeira letra
# de cada palavra em maiusculo.

# Sua solucao:


# Exercicio 4
# Crie uma funcao que recebe uma lista de notas e retorna "Aprovado" se
# a media for >= 6, ou "Reprovado" caso contrario.

# Sua solucao:


# Exercicio 5
# Crie duas funcoes:
# - celsius_para_fahrenheit(celsius): converte e retorna o valor
# - fahrenheit_para_celsius(fahrenheit): converte e retorna o valor
# Depois crie uma terceira funcao que exibe a tabela de conversao
# de 0 a 100 graus Celsius de 10 em 10.

# Sua solucao:


# Exercicio 6
# Crie uma funcao chamada 'validar_senha' que recebe uma string e retorna
# True se a senha tiver pelo menos 8 caracteres, False caso contrario.
# Depois use essa funcao em um programa que pede a senha ao usuario
# ate ele digitar uma valida.

# Sua solucao:


# ---------------------------------------------------------
# Solucoes


# Exercicio 1
def e_par(numero):
    return numero % 2 == 0

print(e_par(4))    # True
print(e_par(7))    # False


# Exercicio 2
def somar_lista(numeros):
    total = 0
    for n in numeros:
        total += n
    return total

print(somar_lista([1, 2, 3, 4, 5]))   # 15


# Exercicio 3
def formatar_nome(nome):
    return nome.title()

print(formatar_nome("joao da silva"))  # Joao Da Silva


# Exercicio 4
def verificar_aprovacao(notas):
    media = sum(notas) / len(notas)
    if media >= 6:
        return "Aprovado"
    return "Reprovado"

print(verificar_aprovacao([7, 8, 6]))    # Aprovado
print(verificar_aprovacao([4, 3, 5]))    # Reprovado


# Exercicio 5
def celsius_para_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def tabela_conversao():
    print(f"{'Celsius':>10} | {'Fahrenheit':>12}")
    print("-" * 26)
    for c in range(0, 101, 10):
        print(f"{c:>10} | {celsius_para_fahrenheit(c):>12.1f}")

tabela_conversao()


# Exercicio 6
def validar_senha(senha):
    return len(senha) >= 8

while True:
    senha = input("Crie uma senha (minimo 8 caracteres): ")
    if validar_senha(senha):
        print("Senha registrada com sucesso.")
        break
    print("Senha muito curta. Tente novamente.")
