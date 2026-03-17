"""
=============================
BREAK, CONTINUE E ELSE NO LACO
=============================
Comandos que controlam o fluxo dentro de um laco.
"""

# =============================
# BREAK — INTERROMPE O LACO
# =============================
print("=== BREAK ===")
print("O comando BREAK interrompe o laco imediatamente,")
print("mesmo que a condicao ainda seja verdadeira.")
print()

# --------------------------------------------------
# EXEMPLO 1 — Parar ao encontrar numero negativo
# --------------------------------------------------
print("--- Ler numeros ate digitar um negativo ---")
print("(O programa para assim que um numero negativo for digitado)")
print()

while True:
    numero = int(input("Digite um numero (negativo para parar): "))

    if numero < 0:
        print("Numero negativo detectado. Encerrando...")
        break

    print(f"Voce digitou: {numero}")

print("Laco encerrado pelo break.")
print()

# --------------------------------------------------
# EXEMPLO 2 — Parar ao atingir um total
# --------------------------------------------------
print("--- Somar numeros ate a soma passar de 50 ---")
soma = 0
i = 1

while True:
    soma = soma + i
    print(f"Somando {i} -> soma atual = {soma}")

    if soma > 50:
        print(f"Soma ultrapassou 50 ao adicionar {i}. Parando!")
        break

    i = i + 1

print()

# =============================
# CONTINUE — PULA PARA A PROXIMA ITERACAO
# =============================
print("=== CONTINUE ===")
print("O comando CONTINUE pula o restante do bloco na iteracao atual")
print("e vai direto para a proxima repeticao.")
print()

# --------------------------------------------------
# EXEMPLO 3 — Imprimir apenas numeros impares
# --------------------------------------------------
print("--- Imprimir numeros impares de 1 a 10 ---")

for i in range(1, 11):
    if i % 2 == 0:     # se for par...
        continue       # ...pula esta iteracao
    print(f"{i} e impar")

print()

# --------------------------------------------------
# EXEMPLO 4 — Ignorar valor zero na media
# --------------------------------------------------
print("--- Calcular media ignorando zeros ---")
soma = 0
validos = 0

for i in range(1, 6):
    valor = float(input(f"Digite o valor {i} (0 = ignorar): "))

    if valor == 0:
        print("  Valor ignorado.")
        continue       # pula soma e contagem

    soma = soma + valor
    validos = validos + 1
    print(f"  Valor aceito. Total valido: {validos}")

if validos > 0:
    media = soma / validos
    print(f"Media dos valores validos = {media:.2f}")
else:
    print("Nenhum valor valido foi digitado.")

print()

# =============================
# ELSE NO LACO
# =============================
print("=== ELSE NO LACO ===")
print("Um laco pode ter um bloco ELSE que e executado quando")
print("o laco termina NORMALMENTE (sem break).")
print()

# --------------------------------------------------
# EXEMPLO 5 — Verificar se algum numero e negativo
# --------------------------------------------------
print("--- Verificar se existe numero negativo em uma sequencia ---")
quantidade = int(input("Quantos numeros voce quer digitar? "))

for i in range(1, quantidade + 1):
    numero = int(input(f"Digite o {i}o numero: "))

    if numero < 0:
        print("Encontrado numero negativo! Interrompendo...")
        break
else:
    # So executa se o for concluiu sem break
    print("Nenhum numero negativo encontrado na sequencia.")

print()

# =============================
# BREAK E CONTINUE JUNTOS
# =============================
print("=== BREAK E CONTINUE JUNTOS ===")
print("--- Somar apenas numeros positivos, parar se digitar 0 ---")
soma = 0
quantidade = 0

while True:
    numero = int(
        input("Digite um numero (0 = encerrar, negativo = ignorar): "))

    if numero == 0:
        break          # encerra o laco

    if numero < 0:
        print("  Numero negativo ignorado.")
        continue       # pula esta iteracao

    soma = soma + numero
    quantidade = quantidade + 1
    print(f"  Somado! Total parcial = {soma}")

if quantidade > 0:
    print(f"Soma final = {soma}")
    print(f"Media dos positivos = {soma / quantidade:.2f}")
else:
    print("Nenhum numero positivo foi digitado.")

print()

# =============================
# RESUMO
# =============================
print("=== RESUMO ===")
print("BREAK    -> interrompe o laco imediatamente.")
print("CONTINUE -> pula o restante da iteracao atual e continua o laco.")
print("ELSE     -> executado quando o laco termina sem break.")
print()
print("Dica: use BREAK para parar ao encontrar uma condicao especial.")
print("Dica: use CONTINUE para filtrar/ignorar certos valores.")
