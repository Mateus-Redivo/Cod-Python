"""
Gabarito — Módulo 10, Exercício 02: Calculadora robusta

Enunciado:
  modulo-10-tratamento-de-erros/exercicios/EXERCICIO-02-calculadora-robusta.md

Como executar:
  python calculadora_robusta.py
"""

OPCAO_SAIR = 0
OPCAO_MINIMA = 0
OPCAO_MAXIMA = 4


# --- Biblioteca de leitura (do exercício 01) -------------------------

def ler_inteiro_na_faixa(mensagem, minimo, maximo):
    while True:
        try:
            valor = int(input(mensagem))
        except ValueError:
            print("  Digite um número inteiro.")
            continue

        if minimo <= valor <= maximo:
            return valor
        print(f"  O valor deve estar entre {minimo} e {maximo}.")


def ler_decimal(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("  Digite um número.")


# --- Calculadora ------------------------------------------------------

def mostrar_menu():
    print()
    print("===== CALCULADORA =====")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")
    print("=======================")


def executar_operacao(opcao, primeiro, segundo):
    """Devolve o texto do resultado, ou uma mensagem de erro."""
    match opcao:
        case 1:
            return f"{primeiro:.2f} + {segundo:.2f} = {primeiro + segundo:.2f}"
        case 2:
            return f"{primeiro:.2f} - {segundo:.2f} = {primeiro - segundo:.2f}"
        case 3:
            return f"{primeiro:.2f} * {segundo:.2f} = {primeiro * segundo:.2f}"
        case 4:
            # PREVENIR com if, não capturar. Você já sabe que zero não
            # serve — não há nada de imprevisto aqui.
            if segundo == 0:
                return "Não é possível dividir por zero."
            return f"{primeiro:.2f} / {segundo:.2f} = {primeiro / segundo:.2f}"
        case _:
            return "Opção inválida."


# --- Programa principal ----------------------------------------------
while True:
    mostrar_menu()
    opcao = ler_inteiro_na_faixa("Escolha: ", OPCAO_MINIMA, OPCAO_MAXIMA)

    if opcao == OPCAO_SAIR:
        print("Até logo!")
        break

    primeiro = ler_decimal("Primeiro número: ")
    segundo = ler_decimal("Segundo número: ")

    print(executar_operacao(opcao, primeiro, segundo))


# --- Por que assim -------------------------------------------------
# 1. A tabela de decisão do enunciado, aplicada:
#
#      letra na opção    -> try   (o int() pode explodir)
#      opção fora de 0-4 -> if    (é número válido, só não serve)
#      letra no número   -> try   (o float() pode explodir)
#      divisão por zero  -> if    (você SABE que zero não serve)
#
#    As duas primeiras estão dentro de ler_inteiro_na_faixa; a
#    terceira em ler_decimal; a quarta no case 4.
#
# 2. A divisão por zero é PREVENIDA, não capturada. Poderia ser:
#
#      try:
#          return f"... = {primeiro / segundo:.2f}"
#      except ZeroDivisionError:
#          return "Não é possível dividir por zero."
#
#    Funciona igual. Mas o if diz a intenção com mais clareza: não é
#    um imprevisto, é uma regra conhecida. Guarde o try para o que
#    está fora do seu controle.
#
# 3. executar_operacao DEVOLVE texto em vez de imprimir — a regra do
#    módulo 08. Assim a mesma função serviria para gravar num arquivo
#    ou montar um histórico, sem reescrever nada.
#
# 4. O "while True" com break na opção 0 é o menu com sentinela do
#    módulo 05. Agora ele é inquebrável, porque a leitura da opção já
#    filtra tudo antes.
#
# 5. O case _ virou inalcançável na prática, porque
#    ler_inteiro_na_faixa já garante 0 a 4. Mantê-lo é barato e
#    protege se alguém mudar a faixa e esquecer do match.


# --- Solução do desafio opcional ------------------------------------
# Guardar o último resultado:
#
#   ultimo_resultado = None
#   ...
#   if ultimo_resultado is not None:
#       usar = ler_sim_ou_nao(f"Usar {ultimo_resultado:.2f} como primeiro? (s/n): ")
#       if usar:
#           primeiro = ultimo_resultado
#       else:
#           primeiro = ler_decimal("Primeiro número: ")
#   else:
#       primeiro = ler_decimal("Primeiro número: ")
#
# E a pergunta do enunciado: na primeira conta não existe resultado
# anterior. O None marca esse "ainda não há" — e é o mesmo None dos
# módulos 06 e 08. Inicializar com 0 seria errado: o usuário poderia
# escolher usar um resultado que nunca existiu.
