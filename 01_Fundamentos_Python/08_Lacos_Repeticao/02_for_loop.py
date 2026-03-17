"""
=============================
LACO DE REPETICAO: FOR
=============================
O laco FOR repete um bloco de codigo um numero
definido de vezes, usando a funcao range().
"""

print("=== O QUE E O FOR? ===")
print("O FOR e usado quando sabemos exatamente quantas vezes o laco deve repetir.")
print("Em Python, usamos o FOR junto com range() para contar repeticoes.")
print()

# =============================
# FUNCAO RANGE()
# =============================
print("=== FUNCAO range() ===")
print("range(n)         -> gera numeros de 0 ate n-1")
print("range(a, b)      -> gera numeros de a ate b-1")
print("range(a, b, p)   -> gera numeros de a ate b-1, pulando de p em p")
print()

# --------------------------------------------------
# EXEMPLO 1 — range(n): de 0 ate n-1
# --------------------------------------------------
print("--- range(5): de 0 a 4 ---")
for i in range(5):
    print(f"i = {i}")
print()

# --------------------------------------------------
# EXEMPLO 2 — range(a, b): intervalo personalizado
# --------------------------------------------------
print("--- range(1, 6): de 1 a 5 ---")
for i in range(1, 6):
    print(f"i = {i}")
print()

# --------------------------------------------------
# EXEMPLO 3 — range(a, b, passo): pulo personalizado
# --------------------------------------------------
print("--- range(0, 11, 2): numeros pares de 0 a 10 ---")
for i in range(0, 11, 2):
    print(f"i = {i}")
print()

print("--- range(10, 0, -1): contagem regressiva ---")
for i in range(10, 0, -1):
    print(f"{i}...")
print("Fim!")
print()

# =============================
# ACUMULADORES COM FOR
# =============================
print("=== ACUMULADORES COM FOR ===")
print()

# --------------------------------------------------
# EXEMPLO 4 — Soma de 1 a 100
# --------------------------------------------------
print("--- Somar todos os numeros de 1 a 100 ---")
soma = 0

for i in range(1, 101):
    soma = soma + i

print(f"Soma de 1 a 100 = {soma}")
print()

# --------------------------------------------------
# EXEMPLO 5 — Tabuada de um numero
# --------------------------------------------------
print("--- Tabuada do 7 ---")
numero = 7

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
print()

# =============================
# FOR COM INPUT
# =============================
print("=== FOR COM INPUT ===")
print("Podemos usar o FOR para repetir uma leitura um numero fixo de vezes.")
print()

# --------------------------------------------------
# EXEMPLO 6 — Ler 3 numeros e somar
# --------------------------------------------------
print("--- Somar 3 numeros digitados ---")
soma = 0

for i in range(1, 4):
    valor = float(input(f"Digite o {i}o numero: "))
    soma = soma + valor

print(f"Soma total = {soma}")
print()

# =============================
# FOR vs WHILE — QUANDO USAR CADA UM?
# =============================
print("=== FOR vs WHILE ===")
print()
print("Use FOR quando:")
print("  - Sabe exatamente quantas vezes o laco vai repetir.")
print("  - Esta percorrendo uma sequencia de numeros com range().")
print()
print("Use WHILE quando:")
print("  - Nao sabe quantas vezes vai repetir.")
print("  - A repeticao depende de uma condicao (ex: entrada do usuario).")
print()

# --------------------------------------------------
# COMPARACAO LADO A LADO
# --------------------------------------------------
print("--- Mesmo resultado, dois jeitos ---")
print()
print("Com FOR:")
for i in range(1, 6):
    print(f"  FOR: {i}")
print()

print("Com WHILE:")
i = 1
while i <= 5:
    print(f"  WHILE: {i}")
    i = i + 1
print()

# =============================
# RESUMO
# =============================
print("=== RESUMO DO FOR ===")
print("- range(n)       -> 0, 1, 2, ..., n-1")
print("- range(a, b)    -> a, a+1, ..., b-1")
print("- range(a, b, p) -> a, a+p, a+2p, ... (ate antes de b)")
print("- Use FOR quando o numero de repeticoes e conhecido.")
print("- Acumuladores funcionam igual ao WHILE.")
