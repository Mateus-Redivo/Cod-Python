"""
=============================
CONVERSÕES DE TIPOS (CASTING)
=============================
Este arquivo demonstra como converter entre diferentes tipos de dados
"""

print("=== CONVERSÕES DE TIPOS ===")

# =============================
# CONVERTENDO PARA INTEIRO - int()
# =============================
print("=== CONVERSÃO PARA INT ===")

# De string para int
texto_numero = "123"
numero_inteiro = int(texto_numero)
print(f"String '{texto_numero}' -> int {numero_inteiro}")

# De float para int (perde a parte decimal)
numero_decimal = 45.89
numero_inteiro = int(numero_decimal)
print(f"Float {numero_decimal} -> int {numero_inteiro}")

# De bool para int
verdadeiro = True
falso = False
print(f"Bool {verdadeiro} -> int {int(verdadeiro)}")  # 1
print(f"Bool {falso} -> int {int(falso)}")            # 0
print()

# =============================
# CONVERTENDO PARA FLOAT - float()
# =============================
print("=== CONVERSÃO PARA FLOAT ===")

# De string para float
texto_decimal = "3.14"
numero_float = float(texto_decimal)
print(f"String '{texto_decimal}' -> float {numero_float}")

# De int para float
inteiro = 42
numero_float = float(inteiro)
print(f"Int {inteiro} -> float {numero_float}")

# De bool para float
print(f"Bool {True} -> float {float(True)}")    # 1.0
print(f"Bool {False} -> float {float(False)}")  # 0.0
print()

# =============================
# CONVERTENDO PARA STRING - str()
# =============================
print("=== CONVERSÃO PARA STRING ===")

# De int para string
numero = 456
texto = str(numero)
print(f"Int {numero} -> string '{texto}'")

# De float para string
decimal = 78.9
texto = str(decimal)
print(f"Float {decimal} -> string '{texto}'")

# De bool para string
booleano = True
texto = str(booleano)
print(f"Bool {booleano} -> string '{texto}'")
print()

# =============================
# CONVERTENDO PARA BOOL - bool()
# =============================
print("=== CONVERSÃO PARA BOOL ===")

# Números para bool
print(f"int 0 -> bool {bool(0)}")        # False
print(f"int 1 -> bool {bool(1)}")        # True
print(f"int -5 -> bool {bool(-5)}")      # True (qualquer número != 0)
print(f"float 0.0 -> bool {bool(0.0)}")  # False
print(f"float 2.5 -> bool {bool(2.5)}")  # True

# Strings para bool
print(f"string '' -> bool {bool('')}")         # False (string vazia)
print(f"string 'texto' -> bool {bool('texto')}")  # True (string com conteúdo)
print(f"string '0' -> bool {bool('0')}")       # True (string não vazia!)
print()

# =============================
# EXEMPLO PRÁTICO COM INPUT
# =============================
print("=== EXEMPLO PRÁTICO ===")

print("Vamos calcular a área de um retângulo:")

# Coletando dados e convertendo
largura_texto = input("Digite a largura: ")
altura_texto = input("Digite a altura: ")

# Convertendo strings para float
largura = float(largura_texto)
altura = float(altura_texto)

# Calculando e exibindo
area = largura * altura
print(f"\nÁrea do retângulo:")
print(f"Largura: {largura} metros")
print(f"Altura: {altura} metros")
print(f"Área: {area} metros quadrados")
print()

# =============================
# TRATAMENTO DE ERROS
# =============================
print("=== CUIDADOS COM CONVERSÕES ===")

# Exemplo de conversões que podem dar erro
print("Estas conversões funcionam:")
print(f"int('123') = {int('123')}")
print(f"float('45.6') = {float('45.6')}")

print("\nEstas conversões dariam erro:")
print("int('abc') - ERRO! Não é um número válido")
print("float('texto') - ERRO! Não é um número válido")
print("int('3.14') - ERRO! Float em formato de string")
print()

print("Soluções:")
print("- Para '3.14': primeiro float('3.14'), depois int()")
numero_texto = "3.14"
numero_float = float(numero_texto)
numero_int = int(numero_float)
print(f"'{numero_texto}' -> float -> int = {numero_int}")
print()

# =============================
# VERIFICAÇÃO DE TIPOS
# =============================
print("=== VERIFICAÇÃO DE TIPOS ===")

# Função type() mostra o tipo
valor = 42
print(f"Valor: {valor}, Tipo: {type(valor)}")

# Função isinstance() verifica se é de um tipo específico
print(f"42 é int? {isinstance(42, int)}")
print(f"42 é str? {isinstance(42, str)}")
print(f"'texto' é str? {isinstance('texto', str)}")

# Verificando múltiplos tipos
valor = 3.14
eh_numero = isinstance(valor, (int, float))
print(f"3.14 é número (int ou float)? {eh_numero}")
