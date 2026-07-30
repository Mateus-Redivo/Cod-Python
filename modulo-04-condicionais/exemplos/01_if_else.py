"""
Módulo 04 — Condicionais
Exemplo 01: if e if/else

Este arquivo mostra:
  - o if simples e os dois-pontos obrigatórios
  - o if/else como dois caminhos exclusivos
  - o peso de quatro espaços de indentação

Valores fixos no código, de propósito: você consegue prever a saída
antes de rodar.

Como executar:
  python 01_if_else.py
"""

# --- if simples: faz, ou não faz nada -------------------------------
idade = 18

print(f"idade = {idade}")
if idade >= 18:
    print("  Você é maior de idade!")
print()

# Com idade menor, o bloco inteiro é pulado e nada aparece.
idade = 15
print(f"idade = {idade}")
if idade >= 18:
    print("  Você é maior de idade!")
print("  (nada foi impresso pelo if acima)")
print()


# --- if/else: sempre exatamente um dos dois -------------------------
temperatura = 15

print(f"temperatura = {temperatura}")
if temperatura >= 25:
    print("  Está quente!")
else:
    print("  Está frio!")
print()


# --- A indentação decide o que está dentro --------------------------
nota = 3.0
print(f"nota = {nota}")

print("Versão A (o parabéns está DENTRO do if):")
if nota >= 6:
    print("  Aprovado")
    print("  Parabéns!")

print("Versão B (o parabéns está FORA do if):")
if nota >= 6:
    print("  Aprovado")
print("  Parabéns!")

print()
print("Com nota 3, a versão A não imprime nada e a versão B parabeniza")
print("um aluno reprovado. A única diferença são quatro espaços.")


# --- Experimento ---------------------------------------------------
# 1. Troque "nota = 3.0" por "nota = 8.0" e rode. Agora as duas
#    versões imprimem a mesma coisa — e o bug da versão B fica
#    invisível. É assim que ele passa despercebido de verdade.
#
# 2. Apague o ":" de qualquer if e rode. Anote o erro.
#
# 3. Apague os 4 espaços da linha depois de um if e rode.
#    O erro é outro: IndentationError. Saiba diferenciar os dois.
