"""
Gabarito — Módulo 07, Exercício 01: Analisador de frases

Enunciado:
  modulo-07-strings/exercicios/EXERCICIO-01-analisador-de-frases.md

Como executar:
  python analisador_de_frases.py
"""

VOGAIS = "aeiou"

# .strip() já na leitura: espaços nas pontas nunca deveriam contar.
frase = input("Digite uma frase: ").strip()

print()

if len(frase) == 0:
    print("Frase vazia: não há o que analisar.")
else:
    # --- Contagens ---------------------------------------------------
    caracteres_com_espacos = len(frase)
    caracteres_sem_espacos = len(frase.replace(" ", ""))

    palavras = frase.split()

    # Vogais: passa a frase para minúsculas UMA vez, antes do laço.
    # Assim "A" e "a" contam igual sem precisar testar as duas.
    vogais = 0
    for letra in frase.lower():
        if letra in VOGAIS:
            vogais += 1

    # Palavra mais longa: o padrão "maior valor" do módulo 06.
    # Começa com a PRIMEIRA palavra, não com uma string vazia.
    palavra_mais_longa = palavras[0]
    for palavra in palavras:
        if len(palavra) > len(palavra_mais_longa):
            palavra_mais_longa = palavra

    # --- Saída -------------------------------------------------------
    print("===== ANÁLISE =====")
    print(f"Maiúsculas: {frase.upper()}")
    print(f"Minúsculas: {frase.lower()}")
    print()
    print(f"Caracteres (com espaços): {caracteres_com_espacos}")
    print(f"Caracteres (sem espaços): {caracteres_sem_espacos}")
    print(f"Palavras: {len(palavras)}")
    print(f"Vogais: {vogais}")
    print(f"Palavra mais longa: {palavra_mais_longa}")
    print(f"Invertida: {frase[::-1]}")
    print()
    print("--- Palavras ---")
    for palavra in palavras:
        print(f"{palavra:<15} {len(palavra)} letras")


# --- Por que assim -------------------------------------------------
# 1. O .lower() é aplicado à frase inteira, uma vez, antes do laço de
#    vogais. A alternativa seria testar cada letra duas vezes:
#
#      if letra in "aeiou" or letra in "AEIOU":
#
#    Funciona, mas é o dobro do trabalho e o dobro de chance de
#    esquecer uma letra. Normalizar antes de comparar é o mesmo
#    princípio da receita .strip().lower() do exemplo 03.
#
# 2. "palavra_mais_longa = palavras[0]" e não "= ''". Começar com a
#    primeira palavra real é o padrão seguro — o mesmo cuidado que o
#    módulo 06 pedia ao procurar o maior número. Aqui a string vazia
#    até funcionaria (qualquer palavra é maior que ela), mas o hábito
#    vale: em "maior valor", comece pelo primeiro elemento.
#
# 3. O critério é ">" e não ">=". Com ">", em caso de empate fica a
#    PRIMEIRA palavra mais longa; com ">=", ficaria a última. Nenhum
#    dos dois é errado — mas é uma decisão, e vale saber qual você
#    tomou.
#
# 4. frase[::-1] inverte usando o passo -1 da fatia. É a mesma
#    sintaxe do range(inicio, fim, passo) do módulo 05: os dois
#    primeiros vazios significam "do começo ao fim".
#
# 5. O len(frase) == 0 é a proteção. Sem ele, "palavras[0]" daria
#    IndexError numa frase vazia — porque "".split() devolve [].


# --- Conferência ----------------------------------------------------
# Entrada: "Python e uma linguagem simples"
#
#   com espaços: 30 caracteres
#   sem espaços: 26 (os 4 espaços saíram)
#   palavras: 5
#   vogais: o(Python) + e + u,a(uma) + i,u,a,e(linguagem) + i,e(simples)
#           = 1 + 1 + 2 + 4 + 2 = 10
#   mais longa: "linguagem", com 9 letras
#
# O "y" de Python NÃO conta como vogal aqui, porque a constante
# VOGAIS é "aeiou". Em português o y não é vogal mesmo, então está
# certo — mas é uma decisão do enunciado, não uma verdade absoluta.


# --- Sobre acentos ---------------------------------------------------
# Se a frase tiver "é", ele não é contado: "é" in "aeiou" é False.
# São caracteres diferentes para o Python, por mais parecidos que
# pareçam para nós.
#
# Para contar acentuadas, a constante cresce:
#
#   VOGAIS = "aeiouáàâãéêíóôõúü"
#
# E note o trabalho: são 17 caracteres, e ainda faltam maiúsculas
# acentuadas se você não tiver feito o .lower() antes. Texto com
# acento é mais complicado do que parece — existem bibliotecas
# inteiras dedicadas a isso.


# --- Solução do desafio opcional ------------------------------------
# Consoantes = letras que não são vogais. O .isalpha() é essencial:
# sem ele, espaços e pontuação entrariam na conta.
#
#   consoantes = 0
#   for letra in frase.lower():
#       if letra.isalpha() and letra not in VOGAIS:
#           consoantes += 1
#
# Confira somando: vogais + consoantes deve dar o total de letras,
# que é menor que "caracteres sem espaços" se houver pontuação.
