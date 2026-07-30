"""
Módulo 05 — Laços de repetição
Exemplo 04: o padrão acumulador

Este arquivo mostra:
  - somar, contar e achar o maior valor dentro de um laço
  - por que a variável do acumulador nasce ANTES do laço
  - o valor sentinela: repetir até o usuário mandar parar

Como executar:
  python 04_acumulador.py
"""

# --- Somar e contar -------------------------------------------------
# As duas variáveis nascem aqui, ANTES do laço. Se nascessem dentro,
# voltariam a zero a cada volta e o total nunca cresceria.
soma = 0
quantidade = 0

for numero in range(1, 11):
    soma += numero
    quantidade += 1

print(f"Somei {quantidade} números; o total deu {soma}.")
print(f"Média: {soma / quantidade:.2f}")
print()


# --- Achar o maior --------------------------------------------------
# Mesmo padrão, outra pergunta. Repare na inicialização: "maior" começa
# valendo o PRIMEIRO valor da sequência, não zero. Se os valores fossem
# todos negativos, um zero inicial ganharia de todos e a resposta sairia
# errada.
maior = -10                          # o primeiro valor que o laço vai ver

for numero in range(-10, 11, 5):     # -10, -5, 0, 5, 10
    if numero > maior:
        maior = numero
    print(f"  vi {numero}, maior até agora = {maior}")

print(f"O maior de todos foi {maior}.")
print()


# --- Acumulador com sentinela ---------------------------------------
# Aqui não sabemos quantos números virão: quem decide é o usuário.
# Número de repetições desconhecido = while, não for.
soma = 0
quantidade = 0

print("Digite números inteiros. Digite 0 para encerrar.")
numero = int(input("Número: "))

while numero != 0:                  # 0 é a sentinela: o sinal de "acabou"
    soma += numero
    quantidade += 1
    numero = int(input("Número: "))

if quantidade > 0:
    print(f"Soma = {soma} | Quantidade = {quantidade} | Média = {soma / quantidade:.2f}")
else:
    print("Nenhum número informado.")


# --- Experimento ---------------------------------------------------
# 1. No primeiro laço, mova "soma = 0" para dentro do for e rode.
#    O resultado vira 10. Entenda por quê antes de desfazer.
#
# 2. No último bloco, apague o "if quantidade > 0" e deixe só a divisão.
#    Rode e digite 0 de primeira: você ganha um ZeroDivisionError.
#    Dividir por uma contagem que pode ser zero é armadilha clássica.
#
# 3. Ainda no último bloco, digite uma letra em vez de um número.
#    Aparece ValueError e o programa morre. Por enquanto, combine com
#    o programa: só números. No módulo 10 você aprende a tratar isso
#    de verdade e nunca mais deixa o programa morrer por digitação.
