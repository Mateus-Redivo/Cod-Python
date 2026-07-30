"""
Módulo 04 — Condicionais
Exemplo 04: match/case

Este arquivo mostra:
  - match/case comparando uma variável com valores exatos
  - o "case _" fazendo o papel do else
  - o mesmo menu escrito com elif, para comparar a leitura

Exige Python 3.10 ou superior. Confira com: python --version

Como executar:
  python 04_match_case.py
"""

opcao = 3

print(f"opcao = {opcao}")
print()

# --- Com match/case --------------------------------------------------
print("Com match/case:")
match opcao:
    case 1:
        print("  Somar")
    case 2:
        print("  Subtrair")
    case 3:
        print("  Multiplicar")
    case 4:
        print("  Dividir")
    case _:                     # o _ é o "qualquer outro valor"
        print("  Opção inválida")
print()

# --- O mesmo, com elif ----------------------------------------------
print("Com if/elif:")
if opcao == 1:
    print("  Somar")
elif opcao == 2:
    print("  Subtrair")
elif opcao == 3:
    print("  Multiplicar")
elif opcao == 4:
    print("  Dividir")
else:
    print("  Opção inválida")
print()

print("Os dois fazem exatamente a mesma coisa. A diferença é que o")
print("match diz o nome da variável UMA vez; o elif repete 'opcao =='")
print("em toda linha. Num menu de dez opções, isso pesa na leitura.")
print()


# --- O | agrupa vários valores no mesmo case ------------------------
dia = 7
print(f"dia = {dia}")

match dia:
    case 1 | 2 | 3 | 4 | 5:
        print("  Dia útil")
    case 6 | 7:
        print("  Fim de semana")
    case _:
        print("  Dia inválido")
print()


# --- Onde o match NÃO serve -----------------------------------------
# match compara valores EXATOS. Para faixas, ele não ajuda:
nota = 7.5
print(f"nota = {nota}")

# Isto continua sendo trabalho do if/elif:
if nota >= 9:
    print("  Conceito A")
elif nota >= 7:
    print("  Conceito B")
else:
    print("  Conceito C ou menos")

print()
print("Regra: valores exatos (menu, código, opção) -> match/case.")
print("       faixas e condições combinadas        -> if/elif.")


# --- Experimento ---------------------------------------------------
# 1. Troque opcao para 9 e rode. Os dois blocos caem no ramo final?
#
# 2. Apague o "case _:" e rode com opcao = 9. Nada é impresso, e não
#    dá erro: um match sem correspondência simplesmente não faz nada.
#    Isso é diferente de um if/elif sem else? Não — é igual.
#
# 3. Tente escrever "case nota >= 9:" no bloco de notas. Não funciona:
#    case espera um valor, não uma comparação. É o limite do match.
