"""
=============================
OPERADORES DE COMPARAÇÃO
=============================
Este arquivo demonstra os operadores de comparação em Python
"""

print("=== OPERADORES DE COMPARAÇÃO ===")

# Valores para demonstração
x = 10
y = 5
z = 10

print(f"Valores: x = {x}, y = {y}, z = {z}")
print()

# =============================
# OPERADORES BÁSICOS
# =============================
print("=== COMPARAÇÕES BÁSICAS ===")

# Igual a
print(f"{x} == {y}: {x == y}")    # False
print(f"{x} == {z}: {x == z}")    # True

# Diferente de
print(f"{x} != {y}: {x != y}")    # True
print(f"{x} != {z}: {x != z}")    # False

# Maior que
print(f"{x} > {y}: {x > y}")      # True
print(f"{y} > {x}: {y > x}")      # False

# Menor que
print(f"{x} < {y}: {x < y}")      # False
print(f"{y} < {x}: {y < x}")      # True

# Maior ou igual a
print(f"{x} >= {z}: {x >= z}")    # True
print(f"{y} >= {x}: {y >= x}")    # False

# Menor ou igual a
print(f"{x} <= {z}: {x <= z}")    # True
print(f"{x} <= {y}: {x <= y}")    # False
print()

# =============================
# COMPARAÇÕES COM STRINGS
# =============================
print("=== COMPARAÇÕES COM STRINGS ===")

nome1 = "Ana"
nome2 = "Bruno"
nome3 = "Ana"

print(f"'{nome1}' == '{nome2}': {nome1 == nome2}")    # False
print(f"'{nome1}' == '{nome3}': {nome1 == nome3}")    # True

# Comparação alfabética
print(f"'{nome1}' < '{nome2}': {nome1 < nome2}")      # True (A vem antes de B)
print(f"'{nome2}' > '{nome1}': {nome2 > nome1}")      # True
print()

# =============================
# EXEMPLOS PRÁTICOS
# =============================
print("=== EXEMPLOS PRÁTICOS ===")

# Verificando maioridade
idade = 18
eh_maior_idade = idade >= 18
print(f"Idade {idade} anos - É maior de idade: {eh_maior_idade}")

# Verificando aprovação por nota
nota = 7.5
media_minima = 6.0
aprovado = nota >= media_minima
print(f"Nota: {nota} - Aprovado (≥ {media_minima}): {aprovado}")

# Verificando desconto por quantidade
quantidade = 100
quantidade_minima = 50
tem_desconto = quantidade >= quantidade_minima
print(
    f"Quantidade: {quantidade} - Tem desconto (≥ {quantidade_minima}): {tem_desconto}")

# Verificando senha
senha_digitada = "1234"
senha_correta = "1234"
acesso_liberado = senha_digitada == senha_correta
print(f"Senha correta: {acesso_liberado}")
print()

# =============================
# CUIDADOS IMPORTANTES
# =============================
print("=== CUIDADOS IMPORTANTES ===")

# Diferença entre = (atribuição) e == (comparação)
numero = 5          # Atribui o valor 5 à variável numero
eh_cinco = numero == 5   # Compara se numero é igual a 5

print(f"Número: {numero}")
print(f"É cinco? {eh_cinco}")

# Comparação com números decimais
valor1 = 0.1 + 0.2
valor2 = 0.3
print(f"0.1 + 0.2 = {valor1}")
# Pode ser False devido à precisão!
print(f"0.1 + 0.2 == 0.3: {valor1 == valor2}")

# Forma correta de comparar decimais
diferenca = abs(valor1 - valor2) < 0.0001
print(f"Comparação correta de decimais: {diferenca}")
