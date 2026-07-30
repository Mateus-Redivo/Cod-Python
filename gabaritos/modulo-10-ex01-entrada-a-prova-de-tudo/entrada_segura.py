"""
Gabarito — Módulo 10, Exercício 01: Entrada à prova de tudo

Enunciado:
  modulo-10-tratamento-de-erros/exercicios/EXERCICIO-01-entrada-a-prova-de-tudo.md

Estas quatro funções são a sua biblioteca pessoal. Copie-as para todos
os programas seguintes.

Como executar:
  python entrada_segura.py
"""

RESPOSTAS_SIM = ("sim", "s")
RESPOSTAS_NAO = ("nao", "não", "n")


def ler_inteiro(mensagem):
    """Insiste até receber um inteiro."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("  Digite um número inteiro.")


def ler_inteiro_na_faixa(mensagem, minimo, maximo):
    """Insiste até receber um inteiro DENTRO da faixa."""
    while True:
        try:
            valor = int(input(mensagem))
        except ValueError:
            print("  Digite um número inteiro.")
            continue

        # Chegou aqui: o tipo está certo. Falta o valor.
        if minimo <= valor <= maximo:
            return valor
        print(f"  O valor deve estar entre {minimo} e {maximo}.")


def ler_decimal(mensagem):
    """Insiste até receber um número. Aceita 1.75 e também 7."""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("  Digite um número.")


def ler_sim_ou_nao(mensagem):
    """True para sim, False para não. Tolera maiúsculas e espaços."""
    while True:
        # A receita .strip().lower() do módulo 07.
        resposta = input(mensagem).strip().lower()

        if resposta in RESPOSTAS_SIM:
            return True
        if resposta in RESPOSTAS_NAO:
            return False
        print("  Responda com s ou n.")


# --- Demonstração ----------------------------------------------------
if __name__ == "__main__":
    idade = ler_inteiro("Idade: ")
    nota = ler_inteiro_na_faixa("Nota (0 a 10): ", 0, 10)
    altura = ler_decimal("Altura: ")
    confirma = ler_sim_ou_nao("Confirma? (s/n): ")

    if confirma:
        print("Confirmado!")
        print(f"  idade={idade}, nota={nota}, altura={altura}")
    else:
        print("Cancelado.")


# --- Por que assim -------------------------------------------------
# 1. "return" direto dentro do try, em ler_inteiro e ler_decimal. Se a
#    conversão der certo, a função devolve na hora e o while acaba
#    junto. Não precisa de break nem de variável intermediária.
#
# 2. Em ler_inteiro_na_faixa o return NÃO pode ficar no try, porque
#    ainda falta checar a faixa. Daí o "continue" no except: ele
#    volta ao topo sem tentar usar uma variável que não foi criada.
#
#    Sem o continue, o código seguiria para o if com "valor"
#    inexistente e daria NameError — trocando um erro por outro.
#
# 3. Cada except captura ValueError, o tipo específico. Um except
#    pelado engoliria também o Ctrl+C do usuário tentando sair.
#
# 4. As mensagens dizem O QUE FAZER ("Digite um número inteiro"), não
#    o que aconteceu ("ValueError"). O usuário não sabe o que é
#    ValueError, e não deveria precisar saber.
#
# 5. ler_sim_ou_nao não tem try nenhum — e está certo. Não há
#    conversão, logo não há exceção possível. É um if. Nem todo
#    problema de entrada é exceção.
#
# 6. O "if __name__ == '__main__'" faz a demonstração rodar quando
#    você executa o arquivo, mas ficar quieta quando outro programa
#    importa as funções. É o jeito de o arquivo ser biblioteca e
#    demonstração ao mesmo tempo.


# --- A pegadinha do vazio --------------------------------------------
# Aperte Enter sem digitar nada:
#   input() devolve ""
#   int("") levanta ValueError: invalid literal for int() with base 10: ''
#
# Ou seja: já está tratado, de graça. O mesmo except que pega "abc"
# pega o vazio.


# --- Solução do desafio opcional ------------------------------------
# def ler_texto_nao_vazio(mensagem):
#     while True:
#         texto = input(mensagem).strip()
#         if len(texto) > 0:
#             return texto
#         print("  Este campo não pode ficar vazio.")
#
# Repare: nenhum try. Não há conversão de tipo, então não há exceção —
# só uma regra de negócio, que é trabalho do if. Escrever try aqui
# seria ruído: um except que nunca dispararia.
