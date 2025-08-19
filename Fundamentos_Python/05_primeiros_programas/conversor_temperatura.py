"""
=============================
CONVERSOR DE TEMPERATURA
=============================
Programa para converter entre Celsius, Fahrenheit e Kelvin
"""

print("=== CONVERSOR DE TEMPERATURA ===")
print()
print("Opções de conversão:")
print("1 - Celsius para Fahrenheit")
print("2 - Celsius para Kelvin")
print("3 - Fahrenheit para Celsius")
print("4 - Fahrenheit para Kelvin")
print("5 - Kelvin para Celsius")
print("6 - Kelvin para Fahrenheit")
print()

# Coletando dados do usuário
opcao = int(input("Escolha uma opção (1-6): "))
temperatura = float(input("Digite a temperatura: "))

# Realizando as conversões
if opcao == 1:  # Celsius para Fahrenheit
    resultado = (temperatura * 9/5) + 32
    print(f"{temperatura}°C = {resultado:.2f}°F")

elif opcao == 2:  # Celsius para Kelvin
    resultado = temperatura + 273.15
    print(f"{temperatura}°C = {resultado:.2f}K")

elif opcao == 3:  # Fahrenheit para Celsius
    resultado = (temperatura - 32) * 5/9
    print(f"{temperatura}°F = {resultado:.2f}°C")

elif opcao == 4:  # Fahrenheit para Kelvin
    celsius = (temperatura - 32) * 5/9
    resultado = celsius + 273.15
    print(f"{temperatura}°F = {resultado:.2f}K")

elif opcao == 5:  # Kelvin para Celsius
    resultado = temperatura - 273.15
    print(f"{temperatura}K = {resultado:.2f}°C")

elif opcao == 6:  # Kelvin para Fahrenheit
    celsius = temperatura - 273.15
    resultado = (celsius * 9/5) + 32
    print(f"{temperatura}K = {resultado:.2f}°F")

else:
    print("Opção inválida! Escolha um número de 1 a 6.")

print("\nObrigado por usar o conversor!")
