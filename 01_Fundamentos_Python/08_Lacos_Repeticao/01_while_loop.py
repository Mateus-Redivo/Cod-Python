"""
=============================
LAÇO DE REPETIÇÃO: WHILE
=============================
O laço WHILE repete um bloco de código enquanto
uma condição for verdadeira.
"""

print("=== O QUE É UM LAÇO DE REPETIÇÃO? ===")
print("Laços permitem que o programa execute o mesmo bloco várias vezes.")
print("Sem laços, teríamos que repetir linhas de código manualmente.")
print()

# --------------------------------------------------
# PROBLEMA SEM LAÇO (jeito errado — difícil de escalar)
# --------------------------------------------------
print("--- Contar de 1 a 5 SEM laço ---")
print("Contagem: 1")
print("Contagem: 2")
print("Contagem: 3")
print("Contagem: 4")
print("Contagem: 5")
print("(Imagine fazer isso até 100... 1000...)")
print()

# =============================
# ESTRUTURA WHILE
# =============================
print("=== ESTRUTURA WHILE ===")
print("Sintaxe:")
print("  while <condição>:")
print("      <bloco de código>")
print()
print("O bloco é executado ENQUANTO a condição for True.")
print("Quando a condição se tornar False, o laço para.")
print()

# --------------------------------------------------
# EXEMPLO 1 — Contador simples
# --------------------------------------------------
print("--- Contar de 1 a 5 COM while ---")
contador = 1               # variável de controle

while contador <= 5:       # condição de parada
    print(f"Contagem: {contador}")
    contador = contador + 1  # atualização (evita loop infinito!)

print("Fim da contagem!")
print()

# --------------------------------------------------
# EXEMPLO 2 — Contagem regressiva
# --------------------------------------------------
print("--- Contagem regressiva ---")
numero = 5

while numero >= 1:
    print(f"{numero}...")
    numero = numero - 1

print("FOGO!")
print()

# =============================
# ACUMULADORES
# =============================
print("=== ACUMULADORES ===")
print("Um acumulador é uma variável que vai somando (ou multiplicando)")
print("valores ao longo das repetições.")
print()

# --------------------------------------------------
# EXEMPLO 3 — Somando números de 1 a 10
# --------------------------------------------------
print("--- Somar todos os números de 1 a 10 ---")
numero = 1
soma = 0               # acumulador começa em zero

while numero <= 10:
    soma = soma + numero   # acumula o valor atual
    numero = numero + 1

print(f"Soma de 1 a 10 = {soma}")
print()

# --------------------------------------------------
# EXEMPLO 4 — Fatorial (acumulador multiplicativo)
# --------------------------------------------------
print("--- Calcular 5! (fatorial de 5) ---")
print("5! = 5 × 4 × 3 × 2 × 1")
n = 5
fatorial = 1          # NÃO começa em 0 (multiplicação!)
i = 1

while i <= n:
    fatorial = fatorial * i
    i = i + 1

print(f"5! = {fatorial}")
print()

# =============================
# WHILE COM INPUT (VALIDAÇÃO)
# =============================
print("=== WHILE PARA VALIDAR ENTRADA ===")
print("Podemos usar while para garantir que o usuário digita um valor válido.")
print()

# --------------------------------------------------
# EXEMPLO 5 — Pedir um número positivo
# --------------------------------------------------
print("--- Solicitar número positivo ---")
numero = int(input("Digite um número positivo: "))

while numero <= 0:
    print("Valor inválido! O número precisa ser positivo.")
    numero = int(input("Tente novamente: "))

print(f"Ótimo! Você digitou: {numero}")
print()

# =============================
# CUIDADO: LOOP INFINITO
# =============================
print("=== CUIDADO: LOOP INFINITO ===")
print("Se a condição NUNCA se tornar False, o programa trava!")
print()
print("Exemplo de loop infinito (NÃO execute este código):")
print()
print("  # ERRADO — nunca atualiza o contador!")
print("  contador = 1")
print("  while contador <= 5:")
print("      print(contador)")
print("      # esqueceu de incrementar contador!")
print()
print("Dica: sempre verifique se a variável de controle é alterada dentro do laço.")
print()

# =============================
# RESUMO
# =============================
print("=== RESUMO DO WHILE ===")
print("• Use WHILE quando não sabe de antemão quantas repetições serão feitas.")
print("• Sempre atualize a variável de controle dentro do laço.")
print("• Acumulador de soma começa em 0; de multiplicação começa em 1.")
print("• Útil para validar entradas do usuário.")
