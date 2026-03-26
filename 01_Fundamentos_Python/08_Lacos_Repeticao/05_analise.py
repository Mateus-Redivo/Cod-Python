"""
=============================
ATIVIDADES — ANALISE DE CODIGO: LOOPS E VALIDACOES
=============================
Questoes de analise de codigo e implementacao.
Foco: loops (while / for), validacoes sem try/except.

Nivel: Iniciante -> Intermediario
=============================
"""

# ============================================================
# QUESTAO 1 — ANALISE DE CODIGO (MEDIA SIMPLES)
# ============================================================
# Nivel: Iniciante
#
# Analise o trecho abaixo e responda:
#
#   n = 0
#   for _ in range(4):
#       n += float(input("D: "))
#   print(n / 4)
#
# a) O que esse codigo calcula?
# b) Quantas vezes o laco for e executado?
# c) Qual seria a saida se o usuario digitasse: 8, 6, 10, 4?
# d) O codigo valida se os valores sao positivos? O que
#    acontece se o usuario digitar -5?
# e) Reescreva o codigo adicionando uma validacao que impeca
#    o usuario de digitar valores negativos, SEM usar try/except.
#
# ------------------------------------------------------------
# Suas respostas:
# a)
# b)
# c)
# d)
# e) Escreva sua solucao aqui:

print("=== QUESTAO 1 — Implementacao com validacao ===")


print()

# ============================================================
# QUESTAO 2 — ANALISE DE CODIGO (CONTADOR COM BREAK)
# ============================================================
# Nivel: Iniciante
#
# Analise o trecho abaixo e responda:
#
#   i = 1
#   while True:
#       print(i)
#       i += 1
#       if i > 5:
#           break
#
# a) Que numeros sao impressos?
# b) O que aconteceria se a linha "if i > 5: break" fosse removida?
# c) Reescreva esse mesmo comportamento usando um WHILE
#    com condicao direta (sem usar break).
#
# ------------------------------------------------------------
# Suas respostas:
# a)
# b)
# c) Escreva sua solucao aqui:

print("=== QUESTAO 2 — Reescrita sem break ===")


print()

# ============================================================
# QUESTAO 3 — ANALISE DE CODIGO (CONTINUE E CONTADOR)
# ============================================================
# Nivel: Iniciante / Intermediario
#
# Analise o trecho abaixo e responda:
#
#   total = 0
#   for i in range(1, 11):
#       if i % 2 == 0:
#           continue
#       total += i
#   print(total)
#
# a) Qual e o valor impresso ao final?
# b) O que o continue faz nesse contexto?
# c) Reescreva sem usar continue, mantendo o mesmo resultado.
#
# ------------------------------------------------------------
# Suas respostas:
# a)
# b)
# c) Escreva sua solucao aqui:

print("=== QUESTAO 3 — Reescrita sem continue ===")


print()

# ============================================================
# QUESTAO 4 — ENCONTRE O BUG (VALIDACAO)
# ============================================================
# Nivel: Iniciante / Intermediario
#
# O codigo abaixo deveria pedir uma senha numerica entre
# 1000 e 9999 e so aceitar quando valida. Mas ele tem um bug.
#
#   senha = int(input("Digite a senha (1000-9999): "))
#   if senha < 1000 or senha > 9999:
#       print("Senha invalida!")
#       senha = int(input("Digite novamente: "))
#
# a) Qual e o bug?
# b) Corrija o codigo de forma que ele continue pedindo
#    a senha ate o usuario digitar um valor valido.
#    Use WHILE. Nao use try/except.
#
# ------------------------------------------------------------
# Suas respostas:
# a)
# b) Escreva sua solucao aqui:

print("=== QUESTAO 4 — Correcao de bug na validacao ===")


print()

# ============================================================
# QUESTAO 5 — PREVER SAIDA (FOR + ACUMULADOR)
# ============================================================
# Nivel: Intermediario
#
# Analise o trecho abaixo e responda:
#
#   resultado = 1
#   for i in range(1, 6):
#       resultado *= i
#   print(resultado)
#
# a) Qual e o valor impresso?
# b) O que essa operacao matematica representa?
# c) Modifique o codigo para que o usuario informe o valor
#    de N, e calcule o resultado para N.
#    Adicione validacao: N deve ser inteiro entre 1 e 10.
#    Use WHILE para a validacao. Nao use try/except.
#
# ------------------------------------------------------------
# Suas respostas:
# a)
# b)
# c) Escreva sua solucao aqui:

print("=== QUESTAO 5 — Fatorial com validacao ===")


print()

# ============================================================
# QUESTAO 6 — ANALISE DE CODIGO (WHILE ANINHADO)
# ============================================================
# Nivel: Intermediario
#
# Analise o trecho abaixo e responda:
#
#   i = 1
#   while i <= 3:
#       j = 1
#       while j <= 3:
#           print(i * j, end="  ")
#           j += 1
#       print()
#       i += 1
#
# a) Quantas vezes o print interno (i * j) e executado?
# b) Escreva a saida completa do programa.
# c) O que esse codigo gera visualmente?
#
# ------------------------------------------------------------
# Suas respostas:
# a)
# b)
# c)

print("=== QUESTAO 6 — While aninhado ===")


print()

# ============================================================
# QUESTAO 7 — IMPLEMENTACAO COM VALIDACAO (MENU)
# ============================================================
# Nivel: Intermediario
#
# Implemente um menu que exiba as opcoes abaixo e peca
# ao usuario uma escolha valida. O menu deve continuar
# aparecendo ate o usuario escolher "0" para sair.
#
#   === MENU ===
#   1 - Opcao A
#   2 - Opcao B
#   3 - Opcao C
#   0 - Sair
#
# Regras:
#   - Se o usuario digitar um valor diferente de 0, 1, 2 ou 3,
#     exiba "Opcao invalida!" e repita o menu.
#   - Ao escolher 1, 2 ou 3, exiba "Voce escolheu a opcao X".
#   - Ao escolher 0, exiba "Encerrando..." e encerre.
#   - Use WHILE e IF/ELIF. Nao use try/except.
#
# ------------------------------------------------------------
# Escreva sua solucao aqui:

print("=== QUESTAO 7 — Menu com validacao ===")


print()

# ============================================================
# QUESTAO 8 — ANALISE E CORRECAO (LOOP INFINITO)
# ============================================================
# Nivel: Intermediario
#
# O codigo abaixo tem um loop infinito. Identifique o problema
# e corrija-o.
#
#   numero = int(input("Digite um numero entre 1 e 5: "))
#   while numero < 1 and numero > 5:
#       print("Fora do intervalo!")
#       numero = int(input("Digite novamente: "))
#   print("Numero valido:", numero)
#
# a) Por que esse while nunca executa (ou executa infinitamente)?
# b) Qual operador logico esta errado? Por que?
# c) Corrija o codigo.
#
# ------------------------------------------------------------
# Suas respostas:
# a)
# b)
# c) Escreva sua solucao aqui:

print("=== QUESTAO 8 — Correcao de condicao logica ===")


print()

# ============================================================
# QUESTAO 9 — IMPLEMENTACAO (ACUMULADOR COM SENTINELA)
# ============================================================
# Nivel: Intermediario
#
# Implemente um programa que:
#   - Peca numeros inteiros ao usuario repetidamente.
#   - Encerre quando o usuario digitar 0 (valor sentinela).
#   - Ao final, exiba: soma, quantidade de numeros digitados
#     (excluindo o 0) e a media.
#   - Se nenhum numero for digitado antes do 0, exiba
#     "Nenhum numero informado."
#
# Restricoes:
#   - Use WHILE.
#   - Nao use listas.
#   - Nao use try/except.
#
# Exemplo:
#   Entrada: 4, 7, 2, 0
#   Saida:
#     Soma = 13
#     Quantidade = 3
#     Media = 4.33
#
# ------------------------------------------------------------
# Escreva sua solucao aqui:

print("=== QUESTAO 9 — Acumulador com sentinela ===")


print()

# ============================================================
# QUESTAO 10 — ANALISE DE CODIGO (FOR + BREAK + FLAG)
# ============================================================
# Nivel: Intermediario
#
# Analise o trecho abaixo e responda:
#
#   numero = int(input("Digite um numero: "))
#   primo = True
#   for i in range(2, numero):
#       if numero % i == 0:
#           primo = False
#           break
#   if primo and numero > 1:
#       print(f"{numero} e primo")
#   else:
#       print(f"{numero} nao e primo")
#
# a) O que a variavel "primo" representa? Como ela e usada?
# b) Por que o range comeca em 2?
# c) Por que ha a condicao "numero > 1" no if final?
# d) O que acontece se o usuario digitar 1? E se digitar 2?
# e) Adicione validacao: o numero deve ser inteiro positivo
#    (maior que 0). Use WHILE. Nao use try/except.
#
# ------------------------------------------------------------
# Suas respostas:
# a)
# b)
# c)
# d)
# e) Escreva sua solucao aqui:

print("=== QUESTAO 10 — Numero primo com validacao ===")


print()
