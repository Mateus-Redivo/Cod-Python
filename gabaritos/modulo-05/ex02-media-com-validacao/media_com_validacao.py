"""
Gabarito — Módulo 05, Exercício 02: Média com validação

Enunciado:
  modulo-05-lacos-de-repeticao/exercicios/EXERCICIO-02-media-com-validacao.md

Como executar:
  python media_com_validacao.py
"""

QUANTIDADE_DE_NOTAS = 5
NOTA_MINIMA = 0
NOTA_MAXIMA = 10

soma = 0

# O FOR cuida da contagem: exatamente 5 notas, sabemos disso de antemão.
for indice in range(1, QUANTIDADE_DE_NOTAS + 1):
    nota = float(input(f"Digite a {indice}a nota (0 a 10): "))

    # O WHILE cuida da validação: não sabemos quantas vezes o usuário
    # vai errar, então o número de repetições é desconhecido.
    while nota < NOTA_MINIMA or nota > NOTA_MAXIMA:
        print("Nota inválida! Digite um valor entre 0 e 10.")
        nota = float(input(f"Digite a {indice}a nota (0 a 10): "))

    # Só chega aqui quem passou pela validação.
    soma += nota

media = soma / QUANTIDADE_DE_NOTAS
print(f"Média das {QUANTIDADE_DE_NOTAS} notas = {media:.2f}")


# --- Por que assim -------------------------------------------------
# 1. FOR por fora, WHILE por dentro. Essa é a decisão central do
#    exercício: repetição de quantidade conhecida (5 notas) é FOR;
#    repetição de quantidade desconhecida (tentativas) é WHILE.
#
# 2. O "input" aparece DUAS vezes, e isso não é duplicação por
#    descuido. A primeira dá ao while algo para testar; a segunda dá
#    ao usuário nova chance. Sem a segunda, "nota" nunca muda e o
#    laço roda para sempre.
#
# 3. A condição usa OR, não AND. "Inválida" significa abaixo de 0 OU
#    acima de 10. Com AND a condição seria impossível de satisfazer,
#    o while nunca executaria e toda nota passaria.
#
# 4. "soma += nota" está fora do while e dentro do for: soma só o que
#    já foi validado, uma vez por nota.
#
# 5. As constantes em maiúsculas no topo evitam números soltos no meio
#    do código. Para mudar de 5 para 8 notas, muda-se um lugar só.
#
# 6. A divisão usa QUANTIDADE_DE_NOTAS, não um contador. Aqui isso é
#    seguro porque o for garante exatamente 5 notas válidas — diferente
#    do exercício 03, onde a quantidade pode ser zero.


# --- Solução do desafio opcional ------------------------------------
# Contar as tentativas inválidas: um acumulador antes de tudo,
# incrementado dentro do while da validação.
#
#   tentativas_invalidas = 0
#   ...
#       while nota < NOTA_MINIMA or nota > NOTA_MAXIMA:
#           tentativas_invalidas += 1
#           print("Nota inválida! Digite um valor entre 0 e 10.")
#           nota = float(input(f"Digite a {indice}a nota (0 a 10): "))
#   ...
#   print(f"Tentativas inválidas: {tentativas_invalidas}")
