# Exercicios de tratamento de erros
# Tente resolver cada exercicio antes de ver a solucao comentada abaixo.


# Exercicio 1
# Peca um numero ao usuario. Se ele digitar algo invalido,
# mostre uma mensagem e peca de novo ate ele digitar um numero valido.

# Sua solucao aqui:

# Exercicio 2
# Receba dois numeros do usuario e divida o primeiro pelo segundo.
# Trate o caso em que o segundo numero e zero.

# Sua solucao aqui:


# Exercicio 3
# Crie uma lista com 5 nomes. Peca ao usuario um indice e mostre o nome
# naquela posicao. Trate o caso em que o indice nao existe.

# Sua solucao aqui:


# Exercicio 4
# Peca ao usuario sua idade. Valide que:
# - e um numero inteiro (ValueError)
# - e um valor positivo (use if dentro do try)
# Se nao for valido, mostre uma mensagem adequada para cada caso.

# Sua solucao aqui:


# Exercicio 5
# Crie uma calculadora simples com menu (soma, subtracao, multiplicacao, divisao).
# Trate todos os possiveis erros: entrada invalida, divisao por zero.
# O programa deve continuar rodando ate o usuario escolher sair.

# Sua solucao aqui:


# ---------------------------------------------------------
# Solucoes


# Exercicio 1
def pedir_numero():
    while True:
        entrada = input("Digite um numero: ")
        try:
            return float(entrada)
        except ValueError:
            print("Isso nao e um numero. Tente novamente.")

numero = pedir_numero()
print(f"Numero recebido: {numero}")


# Exercicio 2
def dividir_com_tratamento():
    try:
        a = float(input("Primeiro numero: "))
        b = float(input("Segundo numero: "))
        resultado = a / b
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Digite apenas numeros.")
    except ZeroDivisionError:
        print("Nao e possivel dividir por zero.")

dividir_com_tratamento()


# Exercicio 3
nomes = ["Ana", "Carlos", "Maria", "Pedro", "Julia"]
try:
    indice = int(input("Digite um indice (0 a 4): "))
    print(f"Nome: {nomes[indice]}")
except ValueError:
    print("O indice precisa ser um numero inteiro.")
except IndexError:
    print(f"Indice invalido. A lista tem {len(nomes)} elementos (0 a {len(nomes)-1}).")


# Exercicio 4
try:
    idade = int(input("Qual a sua idade? "))
    if idade <= 0:
        print("A idade precisa ser um numero positivo.")
    else:
        print(f"Idade registrada: {idade}")
except ValueError:
    print("Por favor, digite um numero inteiro.")


# Exercicio 5
def calculadora():
    print("Calculadora - digite 'sair' para encerrar")
    while True:
        operacao = input("\nEscolha a operacao (+, -, *, /): ")
        if operacao.lower() == "sair":
            print("Encerrando.")
            break
        if operacao not in ["+", "-", "*", "/"]:
            print("Operacao invalida.")
            continue
        try:
            a = float(input("Primeiro numero: "))
            b = float(input("Segundo numero: "))
        except ValueError:
            print("Entrada invalida. Digite apenas numeros.")
            continue
        try:
            if operacao == "+":
                print(f"Resultado: {a + b}")
            elif operacao == "-":
                print(f"Resultado: {a - b}")
            elif operacao == "*":
                print(f"Resultado: {a * b}")
            elif operacao == "/":
                print(f"Resultado: {a / b}")
        except ZeroDivisionError:
            print("Nao e possivel dividir por zero.")

calculadora()
