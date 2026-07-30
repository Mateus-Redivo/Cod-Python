"""
Módulo 00 — Preparação
Exemplo 03: lendo a mensagem de erro

Este arquivo mostra:
  - como é a estrutura de uma mensagem de erro
  - os dois erros mais comuns de quem está começando

ATENÇÃO: este arquivo roda normalmente do jeito que está. Os erros
estão comentados, esperando você tirar o "#" para provocá-los de
propósito — um de cada vez.

Como executar:
  python 03_lendo_o_erro.py
"""

print("Este arquivo roda sem erro nenhum agora.")
print("Descomente uma linha por vez, lá embaixo, para ver cada erro.")
print()

print("Toda mensagem de erro tem três informações:")
print("  1. a LINHA onde o Python travou")
print("  2. um ^ apontando o ponto exato")
print("  3. o TIPO do erro, sempre na última linha")
print()
print("Leia sempre a ÚLTIMA LINHA PRIMEIRO: é ela que nomeia o problema.")


# --- Erro 1: NameError ---------------------------------------------
# Tire o # da linha abaixo e rode.
#
# print(quantidade)
#
# Você vai ver:
#   NameError: name 'quantidade' is not defined
#
# Tradução: "esse nome não existe". A variável nunca foi criada, ou
# foi criada com outra grafia. É o erro de digitação clássico.


# --- Erro 2: SyntaxError -------------------------------------------
# Tire o # da linha abaixo e rode.
#
# print("faltou fechar as aspas)
#
# Você vai ver:
#   SyntaxError: unterminated string literal
#
# Tradução: "abriu aspas e não fechou". Repare que SyntaxError é
# diferente: o programa não roda NADA, nem as linhas de cima. É erro
# de escrita, detectado antes da execução começar.


# --- Experimento ---------------------------------------------------
# 1. Descomente o Erro 1, rode, leia a mensagem inteira e comente
#    de novo. Depois faça o mesmo com o Erro 2.
#
# 2. Compare os dois: com o SyntaxError, as mensagens do começo do
#    arquivo aparecem na tela? Por que não?
#
# 3. Escreva "primt("teste")" numa linha nova e rode. Que tipo de
#    erro aparece? Ele diz qual é a palavra errada?
