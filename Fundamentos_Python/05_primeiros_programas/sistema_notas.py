"""
=============================
SISTEMA DE NOTAS
=============================
Programa para calcular média e determinar situação do aluno
"""

print("=== SISTEMA DE NOTAS ===")
print("Digite as 4 notas do aluno:")
print()

# Coletando as notas
nota1 = float(input("1ª nota: "))
nota2 = float(input("2ª nota: "))
nota3 = float(input("3ª nota: "))
nota4 = float(input("4ª nota: "))

# Calculando a média
media = (nota1 + nota2 + nota3 + nota4) / 4

# Exibindo as notas e a média
print("\n=== RESULTADO ===")
print(f"Notas: {nota1} | {nota2} | {nota3} | {nota4}")
print(f"Média: {media:.2f}")

# Determinando a situação do aluno
if media >= 7.0:
    situacao = "APROVADO"
    print(f"Situação: {situacao} ✅")
elif media >= 5.0:
    situacao = "RECUPERAÇÃO"
    print(f"Situação: {situacao} ⚠️")
    print("Você precisa fazer a prova de recuperação.")
else:
    situacao = "REPROVADO"
    print(f"Situação: {situacao} ❌")

# Informações adicionais
print()
print("Critérios de avaliação:")
print("• Média ≥ 7,0: Aprovado")
print("• 5,0 ≤ Média < 7,0: Recuperação")
print("• Média < 5,0: Reprovado")
