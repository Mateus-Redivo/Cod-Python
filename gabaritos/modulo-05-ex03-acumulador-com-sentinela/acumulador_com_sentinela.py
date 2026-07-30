"""
Gabarito — Módulo 05, Exercício 03: Acumulador com sentinela

Enunciado:
  modulo-05-lacos-de-repeticao/exercicios/EXERCICIO-03-acumulador-com-sentinela.md

Como executar:
  python acumulador_com_sentinela.py
"""

SENTINELA = 0

soma = 0
quantidade = 0

print("Digite números inteiros. Digite 0 para encerrar.")

# Primeira leitura antes do laço: o while precisa de algo para testar.
numero = int(input("Número: "))

while numero != SENTINELA:
    soma += numero
    quantidade += 1

    # Nova leitura no fim do bloco. Sem esta linha, "numero" nunca muda
    # e o laço roda para sempre.
    numero = int(input("Número: "))

# A sentinela saiu do laço sem ser somada nem contada — que é o pedido.

if quantidade > 0:
    print(f"Soma = {soma}")
    print(f"Quantidade = {quantidade}")
    print(f"Média = {soma / quantidade:.2f}")
else:
    print("Nenhum número informado.")


# --- Por que assim -------------------------------------------------
# 1. WHILE, não FOR. Quem decide quantas voltas o laço dá é o usuário,
#    em tempo de execução. FOR exigiria saber o total de antemão.
#
# 2. O par "ler antes / ler no fim" é o esqueleto de todo laço com
#    sentinela. A leitura de fora inicializa; a de dentro atualiza.
#    São as partes 1 e 3 das três do while.
#
# 3. O 0 encerra e não entra na conta porque o "soma += numero" está
#    DENTRO do laço, e o laço já terminou quando o 0 chegou.
#
# 4. O "if quantidade > 0" é obrigatório, não zelo excessivo. Com o
#    usuário digitando 0 de primeira, quantidade vale 0 e a divisão
#    "soma / quantidade" levanta ZeroDivisionError. Sempre que dividir
#    por uma contagem acumulada, teste-a antes.
#
# 5. SENTINELA como constante deixa a intenção explícita: o 0 daquela
#    comparação não é um número qualquer, é o sinal combinado.


# --- Solução do desafio opcional ------------------------------------
# Maior e menor. A armadilha está na inicialização: começar ambos em
# zero dá resposta errada se o usuário digitar só negativos (o zero
# ganharia como "maior" sem nunca ter sido digitado).
#
# A saída é usar o PRIMEIRO número digitado como valor inicial dos dois:
#
#   numero = int(input("Número: "))
#   maior = numero
#   menor = numero
#
#   while numero != SENTINELA:
#       if numero > maior:
#           maior = numero
#       if numero < menor:
#           menor = numero
#       soma += numero
#       quantidade += 1
#       numero = int(input("Número: "))
#
# Cuidado: se o usuário digitar 0 de primeira, "maior" e "menor" ficam
# valendo 0 — mas o if de quantidade já impede que sejam exibidos.
