"""
Gabarito — Módulo 04, Exercício 02: Calculadora com menu

Enunciado:
  modulo-04-condicionais/exercicios/EXERCICIO-02-calculadora-com-menu.md

Como executar:
  python calculadora_com_menu.py
"""

# --- 1. MENU E ENTRADA -----------------------------------------------
print("===== CALCULADORA =====")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")
print("=======================")

opcao = int(input("Escolha a operação (1-4): "))
primeiro = float(input("Primeiro número: "))
segundo = float(input("Segundo número: "))

print()

# --- 2. ESCOLHA DA OPERAÇÃO ------------------------------------------
# match/case porque o teste é "qual das opções exatas" — o caso em que
# ele lê melhor que elif. O nome "opcao" aparece uma vez só.
match opcao:
    case 1:
        print(f"{primeiro:.2f} + {segundo:.2f} = {primeiro + segundo:.2f}")

    case 2:
        print(f"{primeiro:.2f} - {segundo:.2f} = {primeiro - segundo:.2f}")

    case 3:
        print(f"{primeiro:.2f} * {segundo:.2f} = {primeiro * segundo:.2f}")

    case 4:
        # A proteção fica DENTRO do case da divisão: é o único lugar
        # onde o zero é um problema. Multiplicar por zero é normal.
        if segundo == 0:
            print("Não é possível dividir por zero.")
        else:
            print(f"{primeiro:.2f} / {segundo:.2f} = {primeiro / segundo:.2f}")

    case _:
        print("Opção inválida. Escolha entre 1 e 4.")


# --- Por que assim -------------------------------------------------
# 1. match/case e não elif. Funcionalmente são idênticos aqui. O ganho
#    é de leitura: com elif, cada linha repetiria "opcao ==", e num
#    menu de dez opções isso vira ruído. Com match, o nome da variável
#    aparece uma vez, no topo, e cada case mostra só o valor.
#
# 2. O "case _" não é opcional na prática. Sem ele, digitar 9 faria o
#    programa simplesmente não imprimir nada — e sumir em silêncio é
#    pior para o usuário do que dar erro.
#
# 3. A checagem de zero está só no case 4. Colocá-la antes do match,
#    valendo para todas as operações, recusaria "10 * 0", que é uma
#    conta perfeitamente válida. Proteja onde o perigo existe, não em
#    todo lugar.
#
# 4. O resultado é calculado dentro da f-string. Daria para guardar em
#    "resultado" antes; as duas formas estão certas. Aqui a conta é de
#    um operador só, então a variável intermediária não acrescentaria
#    clareza.
#
# 5. float() nos dois números, não int(). Uma calculadora que recusa
#    2.5 não é uma calculadora.


# --- Sobre a ordem das perguntas -------------------------------------
# Este código pergunta os dois números MESMO quando a opção é inválida,
# como o enunciado avisou. Reorganizar para validar antes é possível:
#
#   if opcao < 1 or opcao > 4:
#       print("Opção inválida. Escolha entre 1 e 4.")
#   else:
#       primeiro = float(input("Primeiro número: "))
#       segundo = float(input("Segundo número: "))
#       match opcao:
#           ...
#
# Fica melhor para o usuário e pior para a leitura: tudo desce um nível
# de indentação. E continua sem resolver o problema de verdade, que é
# PERGUNTAR DE NOVO. Isso só chega no módulo 05, com while:
#
#   while opcao < 1 or opcao > 4:
#       print("Opção inválida.")
#       opcao = int(input("Escolha a operação (1-4): "))


# --- Solução do desafio opcional ------------------------------------
# Acrescentar potência custa duas linhas no menu e três no match:
#
#   print("5 - Potência")
#   ...
#       case 5:
#           print(f"{primeiro:.2f} ** {segundo:.2f} = {primeiro ** segundo:.2f}")
#
# E a pergunta: com elif seria a mesma quantidade de linhas — uma
# "elif opcao == 5:" no lugar de "case 5:". A diferença não está no
# custo de ACRESCENTAR, e sim no de LER depois de acrescentar dez
# vezes. Com match, as dez opções ficam alinhadas numa coluna limpa de
# valores; com elif, viram dez repetições de "opcao ==".
