"""
Gabarito — Módulo 05, Exercício 01: Tabuada

Enunciado:
  modulo-05-lacos-de-repeticao/exercicios/EXERCICIO-01-tabuada.md

Como executar:
  python tabuada.py
"""

numero = int(input("Digite um número: "))

# O título fica FORA do laço: ele aparece uma vez só.
print(f"Tabuada do {numero}:")

# range(1, 11) para chegar até o 10 — o segundo argumento é o ponto
# de parada, não o último valor usado.
for multiplicador in range(1, 11):
    print(f"{numero} x {multiplicador} = {numero * multiplicador}")


# --- Por que assim -------------------------------------------------
# 1. O cálculo "numero * multiplicador" está dentro da f-string. Podia
#    estar numa variável "resultado" antes do print — as duas versões
#    estão certas. Escolhi a curta porque a conta é trivial; se fosse
#    uma expressão longa, a variável com nome ajudaria a ler.
#
# 2. O nome "multiplicador" é longo de propósito. "i" também seria
#    aceito (é contador de laço), mas aqui o nome diz o papel do valor.
#
# 3. Um único print dentro do laço. Se você precisou de dois, provavelmente
#    está imprimindo o título junto — mova-o para fora.


# --- Solução do desafio opcional ------------------------------------
# Perguntar até onde a tabuada vai:
#
#   numero = int(input("Digite um número: "))
#   limite = int(input("Até quanto? "))
#
#   print(f"Tabuada do {numero}:")
#   for multiplicador in range(1, limite + 1):
#       print(f"{numero} x {multiplicador} = {numero * multiplicador}")
#
# Repare no "limite + 1": sem ele, a tabuada para uma linha antes do
# que o usuário pediu. É o mesmo limite exclusivo de sempre.
