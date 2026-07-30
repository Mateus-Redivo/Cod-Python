"""
Módulo 03 — Entrada e saída
Exemplo 03: input devolve sempre texto

Este arquivo mostra:
  - o input pausando o programa e devolvendo o que foi digitado
  - a prova de que o resultado é str, mesmo com número digitado
  - o padrão int(input(...)) lido de dentro para fora

Como executar:
  python 03_input.py
"""

# O texto entre parênteses é a pergunta. O programa PARA aqui até
# você digitar algo e apertar Enter.
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")
print()

# --- A prova ---------------------------------------------------------
idade_texto = input("Digite sua idade: ")

print(f"Você digitou: '{idade_texto}'")
print(f"O tipo disso é: {type(idade_texto).__name__}")
print()
print("Repare: mesmo você tendo digitado um número, o Python guardou")
print("como TEXTO. É assim sempre, sem exceção.")
print()

# Some 10 a esse texto e o Python reclama. Descomente para ver:
#
# print(idade_texto + 10)
#
#   TypeError: can only concatenate str (not "int") to str
#
# É o mesmo erro do módulo 01, agora com consequência real.

# Grudar com outro texto, porém, funciona — e mostra que é mesmo str:
print("Concatenando com texto (funciona, mas não é o que queremos):")
print("  " + idade_texto + " anos")
print()


# --- A solução: converter na hora de ler ----------------------------
# Leia de DENTRO para FORA:
#   1. input(...) roda e devolve texto
#   2. int(...) transforma esse texto em número
idade = int(input("Digite sua idade de novo: "))

print(f"Agora o tipo é: {type(idade).__name__}")
print(f"E dá para calcular: daqui a 10 anos você terá {idade + 10}.")


# --- Experimento ---------------------------------------------------
# 1. Descomente o print(idade_texto + 10), rode e leia o erro inteiro.
#    Comente de novo depois.
#
# 2. Na última pergunta, digite uma LETRA em vez de um número.
#    O programa morre com ValueError. Isso é o assunto do módulo 10 —
#    por enquanto, combine com o programa: só números.
#
# 3. Na última pergunta, digite 25.7. Também quebra: int() não aceita
#    decimal. Troque o int() por float() e teste de novo.
