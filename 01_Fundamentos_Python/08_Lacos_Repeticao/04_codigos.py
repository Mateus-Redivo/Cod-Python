"""
=============================
ATIVIDADES — LACOS DE REPETICAO
=============================
Resolva cada atividade no espaco indicado.
Nao use listas — apenas variaveis simples e lacos.

Nivel: Iniciante -> Intermediario
=============================
"""

# ============================================================
# ATIVIDADE 1 — CONTADOR SIMPLES (WHILE)
# ============================================================
# Nivel: Iniciante
#
# Enunciado:
#   Peca ao usuario um numero inteiro positivo N.
#   Imprima todos os numeros de 1 ate N, um por linha.
#
# Exemplo:
#   Entrada: N = 4
#   Saida:
#     1
#     2
#     3
#     4
#
# Restricao: use WHILE
# ------------------------------------------------------------


print("=== ATIVIDADE 1 — Contador simples ===")

# Escreva sua solucao aqui:


print()

# ============================================================
# ATIVIDADE 2 — SOMA DOS NATURAIS (FOR)
# ============================================================
# Nivel: Iniciante
#
# Enunciado:
#   Peca ao usuario um numero inteiro positivo N.
#   Calcule e exiba a soma de todos os numeros de 1 ate N.
#
# Exemplo:
#   Entrada: N = 5
#   Saida: Soma = 15  (1+2+3+4+5)
#
# Restricao: use FOR com range()
# ------------------------------------------------------------

print("=== ATIVIDADE 2 — Soma dos naturais ===")

# Escreva sua solucao aqui:


print()

# ============================================================
# ATIVIDADE 3 — TABUADA PERSONALIZADA (FOR)
# ============================================================
# Nivel: Iniciante
#
# Enunciado:
#   Peca ao usuario um numero inteiro.
#   Exiba a tabuada completa desse numero (de 1 a 10).
#
# Exemplo:
#   Entrada: 3
#   Saida:
#     3 x 1 = 3
#     3 x 2 = 6
#     ...
#     3 x 10 = 30
#
# Restricao: use FOR com range()
# ------------------------------------------------------------

print("=== ATIVIDADE 3 — Tabuada personalizada ===")

# Escreva sua solucao aqui:


print()

# ============================================================
# ATIVIDADE 4 — MEDIA COM VALIDACAO (WHILE)
# ============================================================
# Nivel: Iniciante / Intermediario
#
# Enunciado:
#   Peca ao usuario 5 notas (valores entre 0 e 10).
#   Valide cada nota: se for invalida (< 0 ou > 10),
#   peca novamente ate o usuario digitar um valor correto.
#   Ao final, calcule e exiba a media das 5 notas.
#
# Exemplo:
#   Entrada: 8, 12 (invalida), 7, 6, 9, 5
#   Saida: Media = 7.00
#
# Dica: use um FOR para as 5 repeticoes e um WHILE
#       dentro do FOR para a validacao de cada nota.
# ------------------------------------------------------------

print("=== ATIVIDADE 4 — Media com validacao ===")

# Escreva sua solucao aqui:

print()

# ============================================================
# ATIVIDADE 5 — SEQUENCIA DE FIBONACCI (WHILE)
# ============================================================
# Nivel: Intermediario
#
# Enunciado:
#   A sequencia de Fibonacci comeca com 0 e 1.
#   Cada numero seguinte e a soma dos dois anteriores:
#     0, 1, 1, 2, 3, 5, 8, 13, 21, ...
#
#   Peca ao usuario um numero inteiro N.
#   Exiba todos os termos da sequencia de Fibonacci
#   menores ou iguais a N.
#
# Exemplo:
#   Entrada: N = 20
#   Saida: 0  1  1  2  3  5  8  13
#
# Restricao: use WHILE
# ------------------------------------------------------------

print("=== ATIVIDADE 5 — Sequencia de Fibonacci ===")

# Escreva sua solucao aqui:


print()

# ============================================================
# ATIVIDADE 6 — ADIVINHE O NUMERO (BREAK)
# ============================================================
# Nivel: Intermediario
#
# Enunciado:
#   Defina um numero secreto fixo no codigo (ex: 42).
#   Peca ao usuario que tente adivinhar o numero.
#   A cada tentativa, informe se o chute foi alto, baixo
#   ou correto.
#   Quando acertar, exiba o numero de tentativas e encerre
#   o laco com BREAK.
#
# Exemplo (numero secreto = 42):
#   Chute: 20 -> Muito baixo!
#   Chute: 60 -> Muito alto!
#   Chute: 42 -> Acertou em 3 tentativas!
#
# Restricao: use WHILE True com BREAK
# ------------------------------------------------------------

print("=== ATIVIDADE 6 — Adivinhe o numero ===")

# Escreva sua solucao aqui:
"""
numsec = 3
tentativas = 0

print("Adinhe o numero secreto entre 0 e 100")
while True:
    chute = int(input("Chute: "))
    tentativas += 1
    if(chute > numsec):
        print("Muito alto")
    elif (chute <numsec):
        print("Muito baixo")
    else:
        print(f"Voce acertou em {tentativas} tentativas")
        break
"""
print()

# ============================================================
# ATIVIDADE 7 — SOMADOR SELETIVO (CONTINUE)
# ============================================================
# Nivel: Intermediario
#
# Enunciado:
#   Peca ao usuario 8 numeros inteiros, um por vez.
#   Some APENAS os numeros que forem multiplos de 3.
#   Ao final, exiba a soma e quantos multiplos de 3 foram
#   encontrados.
#
# Exemplo:
#   Entrada: 1, 3, 5, 6, 7, 9, 10, 12
#   Saida: Soma = 30, Quantidade = 4
#
# Restricao: use FOR com range() e CONTINUE para ignorar
#            os nao-multiplos.
# ------------------------------------------------------------

print("=== ATIVIDADE 7 — Somador seletivo ===")

# Escreva sua solucao aqui:
# Escreva o comportamento do codigo se eu informar os numeros 1 2 5 8 9 10 12
"""
soma = 0
quantidade = 0

for i in range(1, 9):
    numero = int(input(f"Digite o {i} numero: "))

    if numero % 3 != 0:
        continue

    soma = soma + numero
    quantidade = quantidade + 1

print(f"A soma dos multiplos de 3 é: {soma}")
print(f"A quantidade de multiplos de 3 é: {quantidade}")
"""
print()

# ============================================================
# ATIVIDADE 8 — NUMERO PERFEITO (FOR + ACUMULADOR)
# ============================================================
# Nivel: Intermediario
#
# Enunciado:
#   Um numero e perfeito quando a soma de seus divisores
#   proprios (excluindo ele mesmo) e igual a ele.
#   Exemplo: 6 -> divisores: 1, 2, 3 -> 1+2+3 = 6 (perfeito!)
#             28 -> divisores: 1,2,4,7,14 -> soma = 28 (perfeito!)
#
#   Peca ao usuario um numero inteiro positivo N.
#   Verifique se N e perfeito e exiba o resultado.
#   Exiba tambem todos os divisores encontrados.
#
# Exemplo:
#   Entrada: 6
#   Saida:
#     Divisores de 6: 1  2  3
#     Soma dos divisores = 6
#     6 e um numero perfeito!
#    
# Restricao: use FOR com range() e acumulador
# ------------------------------------------------------------

print("=== ATIVIDADE 8 — Numero perfeito ===")

# Escreva sua solucao aqui:

numero = int(input("Digite um numero: "))

soma_divisores = 0
divisores_encontrados = ""
#Resposta dos numero 20 10 50 4
for i in range(1, numero):
    if numero % i == 0:
        soma_divisores += i
        divisores_encontrados = divisores_encontrados + str(i) + " "

print(f"Divisores: {soma_divisores}")
print(f"Soma dos divisores: {divisores_encontrados}")

if soma_divisores == numero:
    print(f"{numero} e um numero perfeito")
else: 
    print(f"{numero} nao e um numero perfeito")



print()
