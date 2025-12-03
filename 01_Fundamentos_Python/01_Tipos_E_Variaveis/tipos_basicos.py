"""
=============================
TIPOS BÁSICOS EM PYTHON
=============================
Este arquivo demonstra os tipos de dados fundamentais em Python
"""

# =============================
# 1. NÚMEROS INTEIROS (int)
# =============================
print("=== NÚMEROS INTEIROS ===")
idade = 25
numero_negativo = -10
zero = 0

print(f"Idade: {idade}")
print(f"Número negativo: {numero_negativo}")
print(f"Zero: {zero}")
print(f"Tipo da variável idade: {type(idade)}")
print()

# =============================
# 2. NÚMEROS DECIMAIS (float)
# =============================
print("=== NÚMEROS DECIMAIS ===")
altura = 1.75
peso = 68.5
preco = 19.99
pi = 3.14159

print(f"Altura: {altura} metros")
print(f"Peso: {peso} kg")
print(f"Preço: R$ {preco}")
print(f"Pi: {pi}")
print(f"Tipo da variável altura: {type(altura)}")
print()

# =============================
# 3. TEXTO/STRING (str)
# =============================
print("=== STRINGS (TEXTO) ===")
nome = "João Silva"
cidade = 'São Paulo'
frase = "Python é uma linguagem fantástica!"
texto_vazio = ""

print(f"Nome: {nome}")
print(f"Cidade: {cidade}")
print(f"Frase: {frase}")
print(f"Texto vazio: '{texto_vazio}'")
print(f"Tipo da variável nome: {type(nome)}")
print()

# =============================
# 4. VALORES LÓGICOS (bool)
# =============================
print("=== VALORES BOOLEANOS ===")
esta_chovendo = True
tem_dinheiro = False
aprovado = True

print(f"Está chovendo: {esta_chovendo}")
print(f"Tem dinheiro: {tem_dinheiro}")
print(f"Aprovado: {aprovado}")
print(f"Tipo da variável aprovado: {type(aprovado)}")
print()

# =============================
# 5. VERIFICANDO TIPOS
# =============================
print("=== VERIFICANDO TIPOS ===")
variaveis = [42, 3.14, "Hello", True]

for variavel in variaveis:
    print(f"Valor: {variavel} | Tipo: {type(variavel).__name__}")
