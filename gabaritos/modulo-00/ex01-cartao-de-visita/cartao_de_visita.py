"""
Gabarito — Módulo 00, Exercício 01: Cartão de visita

Enunciado:
  modulo-00-preparacao/exercicios/EXERCICIO-01-cartao-de-visita.md

Como executar:
  python cartao_de_visita.py
"""

# A linha de "=" é só enfeite, mas ajuda a separar a saída do
# programa do resto do que já está no terminal.
print("=================================")
print("Maria Oliveira")

print()      # linha em branco: separa o nome do resto

print("Cidade: Cascavel - PR")
print("Estudo Python para automatizar os relatórios do meu trabalho.")
print("=================================")


# --- Por que assim -------------------------------------------------
# 1. Cada informação em seu próprio print. Daria para juntar tudo em
#    um print só com vírgulas, mas aí a saída sairia numa linha só —
#    e o enunciado pede blocos separados.
#
# 2. O print() vazio é o único jeito de conseguir uma linha em branco
#    sem imprimir nada nela.
#
# 3. O comentário da primeira linha explica uma DECISÃO ("por que a
#    linha de ="), não o mecanismo ("isto imprime texto"). Comentar o
#    óbvio é o hábito que o exercício está tentando evitar.


# --- Solução do desafio opcional ------------------------------------
# Apagando a aspa final da linha do nome, o Python responde:
#
#   File "cartao_de_visita.py", line 15
#       print("Maria Oliveira)
#             ^
#   SyntaxError: unterminated string literal (detected at line 15)
#
# Linha apontada: 15. Tipo do erro: SyntaxError.
#
# Repare que NENHUMA linha do programa chegou a rodar — nem a linha
# de "=" que vem antes. SyntaxError é detectado quando o Python lê o
# arquivo, antes de executar qualquer coisa.
