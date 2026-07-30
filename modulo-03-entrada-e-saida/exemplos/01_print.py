"""
Módulo 03 — Entrada e saída
Exemplo 01: o print por dentro

Este arquivo mostra:
  - print com vários valores separados por vírgula
  - o parâmetro sep, que troca o separador
  - o parâmetro end, que controla o fim da linha

Como executar:
  python 01_print.py
"""

nome = "João"
idade = 25

# Com vírgula, o print aceita quantos valores você quiser e separa
# cada um com um espaço. Repare que ele NÃO reclama de misturar
# texto com número — diferente do "+".
print("Nome:", nome, "| Idade:", idade)
print()

# --- sep: troca o separador entre os valores ------------------------
print("A", "B", "C")                # separador padrão: um espaço
print("A", "B", "C", sep="-")
print("A", "B", "C", sep=" | ")
print("A", "B", "C", sep="")        # nenhum separador
print()

# Uso prático: montar uma data ou um caminho
print(30, 7, 2026, sep="/")
print()

# --- end: controla o que vem DEPOIS da linha ------------------------
# Por padrão, todo print termina com uma quebra de linha.
# Com end="", ele não quebra, e o próximo print continua na mesma linha.
print("Esta linha", end="")
print(" continua aqui.")

print("Carregando", end="")
print(".", end="")
print(".", end="")
print(".", end="")
print(" pronto!")
print()

# end também aceita qualquer outro texto
print("primeiro", end=" -> ")
print("segundo", end=" -> ")
print("terceiro")
print()

# print() sozinho pula uma linha: é só um end="\n" sem conteúdo.
print("acima da linha em branco")
print()
print("abaixo da linha em branco")


# --- Experimento ---------------------------------------------------
# 1. Troque o sep="/" da data por sep="-". Qual formato de data ficou?
#
# 2. Apague o end="" da linha "Esta linha". O que muda na saída?
#
# 3. O end="" vai ser essencial no módulo 05, para imprimir vários
#    números lado a lado dentro de um laço. Guarde-o.
