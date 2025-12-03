"""
=============================
OPERADORES ARITMÉTICOS
=============================
Este arquivo demonstra todos os operadores matemáticos em Python
"""

print("=== OPERADORES ARITMÉTICOS ===")

# Valores para demonstração
a = 10
b = 3

print(f"Valores: a = {a}, b = {b}")
print()

# =============================
# OPERAÇÕES BÁSICAS
# =============================
print("=== OPERAÇÕES BÁSICAS ===")

# Adição
soma = a + b
print(f"Adição: {a} + {b} = {soma}")

# Subtração
subtracao = a - b
print(f"Subtração: {a} - {b} = {subtracao}")

# Multiplicação
multiplicacao = a * b
print(f"Multiplicação: {a} * {b} = {multiplicacao}")

# Divisão (retorna float)
divisao = a / b
print(f"Divisão: {a} / {b} = {divisao}")
print()

# =============================
# OPERAÇÕES ESPECIAIS
# =============================
print("=== OPERAÇÕES ESPECIAIS ===")

# Divisão inteira (elimina a parte decimal)
divisao_inteira = a // b
print(f"Divisão inteira: {a} // {b} = {divisao_inteira}")

# Módulo (resto da divisão)
resto = a % b
print(f"Módulo (resto): {a} % {b} = {resto}")

# Exponenciação (potência)
potencia = a ** b
print(f"Potência: {a} ** {b} = {potencia}")
print()

# =============================
# ORDEM DE PRECEDÊNCIA
# =============================
print("=== ORDEM DE PRECEDÊNCIA ===")

# Python segue a ordem matemática: parênteses, potência, multiplicação/divisão, soma/subtração
expressao1 = 2 + 3 * 4
expressao2 = (2 + 3) * 4
expressao3 = 2 ** 3 * 4
expressao4 = 2 * 3 + 4 / 2

print(f"2 + 3 * 4 = {expressao1}")           # 14 (não 20)
print(f"(2 + 3) * 4 = {expressao2}")         # 20
print(f"2 ** 3 * 4 = {expressao3}")          # 32
print(f"2 * 3 + 4 / 2 = {expressao4}")       # 8.0
print()

# =============================
# EXEMPLOS PRÁTICOS
# =============================
print("=== EXEMPLOS PRÁTICOS ===")

# Calculando área de um retângulo
largura = 5
altura = 8
area_retangulo = largura * altura
print(f"Área do retângulo: {largura} x {altura} = {area_retangulo}")

# Calculando velocidade média
distancia = 120  # km
tempo = 2        # horas
velocidade_media = distancia / tempo
print(
    f"Velocidade média: {distancia} km / {tempo} h = {velocidade_media} km/h")

# Verificando se um número é par
numero = 15
eh_par = (numero % 2 == 0)
print(f"O número {numero} é par? {eh_par}")

# Calculando juros simples
capital = 1000
taxa = 0.05    # 5%
periodo = 12   # meses
juros = capital * taxa * periodo
montante = capital + juros
print(f"Capital: R$ {capital}")
print(f"Juros: R$ {juros}")
print(f"Montante: R$ {montante}")
