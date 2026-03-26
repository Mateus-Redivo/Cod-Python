"""
=============================
RESOLUCAO — ATIVIDADES: LACOS DE REPETICAO
=============================
Gabarito das atividades do arquivo 04_atividades.py
=============================
"""

# ============================================================
# ATIVIDADE 1 — CONTADOR SIMPLES (WHILE)
# ============================================================
print("=== ATIVIDADE 1 — Contador simples ===")

n = int(input("Digite um numero inteiro positivo N: "))

contador = 1
while contador <= n:
    print(contador)
    contador = contador + 1

print()

# ============================================================
# ATIVIDADE 2 — SOMA DOS NATURAIS (FOR)
# ============================================================
print("=== ATIVIDADE 2 — Soma dos naturais ===")

n = int(input("Digite um numero inteiro positivo N: "))

soma = 0
for i in range(1, n + 1):
    soma = soma + i

print(f"Soma de 1 a {n} = {soma}")

print()

# ============================================================
# ATIVIDADE 3 — TABUADA PERSONALIZADA (FOR)
# ============================================================
print("=== ATIVIDADE 3 — Tabuada personalizada ===")

numero = int(input("Digite um numero inteiro: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

print()

# ============================================================
# ATIVIDADE 4 — MEDIA COM VALIDACAO (WHILE)
# ============================================================
print("=== ATIVIDADE 4 — Media com validacao ===")

soma = 0

for i in range(1, 6):
    nota = float(input(f"Digite a {i}a nota (0 a 10): "))

    while nota < 0 or nota > 10:
        print("Nota invalida! Digite um valor entre 0 e 10.")
        nota = float(input(f"Digite a {i}a nota novamente: "))

    soma = soma + nota

media = soma / 5
print(f"Media das 5 notas = {media:.2f}")

print()

# ============================================================
# ATIVIDADE 5 — SEQUENCIA DE FIBONACCI (WHILE)
# ============================================================
print("=== ATIVIDADE 5 — Sequencia de Fibonacci ===")

n = int(input("Digite o limite N: "))

anterior = 0
atual = 1

print("Termos menores ou iguais a", n, ":")

while anterior <= n:
    print(anterior, end="  ")
    proximo = anterior + atual
    anterior = atual
    atual = proximo

print()

print()

# ============================================================
# ATIVIDADE 6 — ADIVINHE O NUMERO (BREAK)
# ============================================================
print("=== ATIVIDADE 6 — Adivinhe o numero ===")

numero_secreto = 42
tentativas = 0

while True:
    chute = int(input("Tente adivinhar o numero (1 a 100): "))
    tentativas = tentativas + 1

    if chute < numero_secreto:
        print("Muito baixo!")
    elif chute > numero_secreto:
        print("Muito alto!")
    else:
        print(f"Acertou em {tentativas} tentativa(s)!")
        break

print()

# ============================================================
# ATIVIDADE 7 — SOMADOR SELETIVO (CONTINUE)
# ============================================================
print("=== ATIVIDADE 7 — Somador seletivo ===")

soma = 0
quantidade = 0

for i in range(1, 9):
    numero = int(input(f"Digite o {i}o numero: "))

    if numero % 3 != 0:
        continue

    soma = soma + numero
    quantidade = quantidade + 1

print(f"Soma dos multiplos de 3 = {soma}")
print(f"Quantidade de multiplos de 3 = {quantidade}")

print()

# ============================================================
# ATIVIDADE 8 — NUMERO PERFEITO (FOR + ACUMULADOR)
# ============================================================
print("=== ATIVIDADE 8 — Numero perfeito ===")

n = int(input("Digite um numero inteiro positivo: "))

soma_divisores = 0
divisores_encontrados = ""

for i in range(1, n):
    if n % i == 0:
        soma_divisores = soma_divisores + i
        divisores_encontrados = divisores_encontrados + str(i) + "  "

print(f"Divisores de {n}: {divisores_encontrados}")
print(f"Soma dos divisores = {soma_divisores}")

if soma_divisores == n:
    print(f"{n} e um numero perfeito!")
else:
    print(f"{n} nao e um numero perfeito.")

print()
