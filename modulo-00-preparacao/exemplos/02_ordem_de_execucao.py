"""
Módulo 00 — Preparação
Exemplo 02: de cima para baixo, uma linha por vez

Este arquivo mostra:
  - que a ordem das linhas define a ordem da saída
  - por que usar uma variável antes de criá-la não funciona
  - o que o comentário faz (nada)

Como executar:
  python 02_ordem_de_execucao.py
"""

print("1. Esta linha roda primeiro")
print("2. Esta roda depois")
print("3. E esta por último")

print()

# O interpretador só sabe o que já leu. Aqui a variável é criada
# ANTES de ser usada, e por isso funciona.
mensagem = "Fui criada na linha de cima."
print(mensagem)

print()

# Comentários são ignorados por completo. A linha abaixo não roda:
# print("Você nunca vai me ver na tela.")

print("Fim do programa.")


# --- Experimento ---------------------------------------------------
# 1. Troque a ordem das três primeiras linhas e rode. A saída segue
#    a ordem do arquivo, não a numeração que você escreveu no texto.
#
# 2. Mova a linha "print(mensagem)" para ANTES de "mensagem = ...".
#    Você recebe um NameError. Leia a mensagem: ela diz exatamente
#    qual nome não existe. Isso acontece porque o Python ainda não
#    tinha lido a linha que cria a variável. Desfaça depois.
#
# 3. Apague o "#" da linha comentada e rode. Ela passa a existir.
