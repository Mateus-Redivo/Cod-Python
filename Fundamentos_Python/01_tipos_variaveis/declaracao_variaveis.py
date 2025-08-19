"""
=============================
DECLARAÇÃO E ATRIBUIÇÃO DE VARIÁVEIS
=============================
Este arquivo demonstra como criar e usar variáveis em Python
"""

# =============================
# 1. CRIANDO VARIÁVEIS
# =============================
print("=== CRIANDO VARIÁVEIS ===")

# Em Python, não precisamos declarar o tipo da variável
# O tipo é determinado automaticamente pelo valor atribuído
nome = "Maria"           # Automaticamente será string
idade = 30               # Automaticamente será int
salario = 5000.50       # Automaticamente será float
ativo = True            # Automaticamente será bool

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: {salario}")
print(f"Ativo: {ativo}")
print()

# =============================
# 2. REGRAS PARA NOMES DE VARIÁVEIS
# =============================
print("=== REGRAS PARA NOMES ===")

# ✅ CORRETO - Nomes válidos
primeiro_nome = "João"
idade_usuario = 25
valor2 = 100
_variavel_privada = "secreto"
CONSTANTE = 3.14

print("Nomes válidos criados com sucesso!")

# ❌ INCORRETO - Estes dariam erro:
# 2nome = "erro"          # Não pode começar com número
# primeiro-nome = "erro"  # Não pode ter hífen
# class = "erro"          # Não pode usar palavras reservadas
print()

# =============================
# 3. CONVENÇÕES DE NOMENCLATURA
# =============================
print("=== CONVENÇÕES ===")

# Snake Case (recomendado em Python)
nome_completo = "João Silva"
data_nascimento = "01/01/1990"
valor_total = 1500.00

# Constantes (maiúsculas)
PI = 3.14159
TAXA_JUROS = 0.05

print(f"Nome completo: {nome_completo}")
print(f"Data nascimento: {data_nascimento}")
print(f"Valor total: {valor_total}")
print(f"PI: {PI}")
print(f"Taxa de juros: {TAXA_JUROS}")
print()

# =============================
# 4. REATRIBUIÇÃO DE VARIÁVEIS
# =============================
print("=== REATRIBUIÇÃO ===")

contador = 0
print(f"Contador inicial: {contador}")

contador = 5
print(f"Contador após mudança: {contador}")

# Pode mudar até o tipo!
contador = "agora sou texto"
print(f"Contador como texto: {contador}")
print()

# =============================
# 5. MÚLTIPLAS ATRIBUIÇÕES
# =============================
print("=== MÚLTIPLAS ATRIBUIÇÕES ===")

# Atribuir o mesmo valor a várias variáveis
a = b = c = 10
print(f"a = {a}, b = {b}, c = {c}")

# Atribuir valores diferentes simultaneamente
x, y, z = 1, 2, 3
print(f"x = {x}, y = {y}, z = {z}")

# Trocar valores de variáveis
primeiro = "A"
segundo = "B"
print(f"Antes da troca: primeiro = {primeiro}, segundo = {segundo}")

primeiro, segundo = segundo, primeiro
print(f"Após a troca: primeiro = {primeiro}, segundo = {segundo}")
