"""
=============================
INTRODUÇÃO ÀS CONDICIONAIS
=============================
"""

print("=== O QUE SÃO CONDICIONAIS ===")
print("Condicionais permitem que o programa tome decisões")
print("O código executa diferentes ações baseado em condições")
print()

# =============================
# IF (SE)
# =============================
print("=== ESTRUTURA IF ===")
print("Executa um bloco de código SE a condição for verdadeira")
print()

idade = 18
print(f"Idade: {idade}")

if idade >= 18:
    print("Você é maior de idade!")
print()

# =============================
# IF-ELSE (SE-SENÃO)
# =============================
print("=== ESTRUTURA IF-ELSE ===")
print("SE a condição for verdadeira, executa o IF")
print("SENÃO, executa o ELSE")
print()

temperatura = 15
print(f"Temperatura: {temperatura}°C")

if temperatura >= 25:
    print("Está quente!")
else:
    print("Está frio!")
print()

# =============================
# IF-ELIF-ELSE (SE-SENÃO SE-SENÃO)
# =============================
print("=== ESTRUTURA IF-ELIF-ELSE ===")
print("Permite testar múltiplas condições")
print()

nota = 7.5
print(f"Nota: {nota}")

if nota >= 9:
    print("Conceito: A")
elif nota >= 7:
    print("Conceito: B")
elif nota >= 5:
    print("Conceito: C")
else:
    print("Conceito: D (Reprovado)")
print()

# =============================
# CONDIÇÕES COMPOSTAS
# =============================
print("=== CONDIÇÕES COMPOSTAS ===")
print("Podemos combinar condições com 'and' e 'or'")
print()

idade = 20
tem_carteira = True
print(f"Idade: {idade}, Tem carteira: {tem_carteira}")

if idade >= 18 and tem_carteira:
    print("Pode dirigir!")
else:
    print("Não pode dirigir!")
print()

# =============================
# CONDICIONAIS ANINHADAS
# =============================
print("=== CONDICIONAIS ANINHADAS ===")
print("Condicionais dentro de condicionais")
print()

numero = 10
print(f"Número: {numero}")

if numero > 0:
    print("O número é positivo")
    if numero % 2 == 0:
        print("E também é par")
    else:
        print("E também é ímpar")
elif numero < 0:
    print("O número é negativo")
else:
    print("O número é zero")
print()

# =============================
# EXEMPLO PRÁTICO: DIVISÃO SEGURA
# =============================
print("=== EXEMPLO: DIVISÃO SEGURA ===")
print("Evitando divisão por zero")
print()

a = 10
b = 0
print(f"Dividendo: {a}, Divisor: {b}")

if b == 0:
    print("Erro: Divisão por zero não é permitida!")
else:
    resultado = a / b
    print(f"Resultado: {resultado}")
print()

# =============================
# OPERADOR TERNÁRIO
# =============================
print("=== OPERADOR TERNÁRIO ===")
print("Forma compacta de escrever if-else simples")
print()

idade = 16
status = "maior" if idade >= 18 else "menor"
print(f"Idade: {idade} -> {status} de idade")

idade = 25
status = "maior" if idade >= 18 else "menor"
print(f"Idade: {idade} -> {status} de idade")
print()

# =============================
# RESUMO
# =============================
print("="*40)
print("RESUMO DAS CONDICIONAIS")
print("="*40)
print("if        -> Executa SE condição verdadeira")
print("else      -> Executa SE condição falsa")
print("elif      -> Testa outra condição")
print("and       -> AMBAS condições verdadeiras")
print("or        -> PELO MENOS UMA verdadeira")
print("not       -> Inverte a condição")
print("="*40)
