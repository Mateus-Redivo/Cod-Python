"""
Módulo 01 — Tipos e variáveis
Exemplo 03: nomes de variável

Este arquivo mostra:
  - o que é nome válido e o que dá erro
  - a convenção snake_case e as constantes em maiúsculas
  - por que o nome importa mais do que parece

Como executar:
  python 03_nomes.py
"""

# --- Nomes válidos --------------------------------------------------
primeiro_nome = "João"      # snake_case: a convenção do Python
idade_usuario = 25
valor2 = 100                # número no meio ou no fim: pode
_interno = "reservado"      # underline no começo: pode

# Constantes: valores que não devem mudar. Em MAIÚSCULAS, por convenção.
# O Python não impede a mudança — o nome é um aviso para quem lê.
TAXA_JUROS = 0.05
NOTA_MINIMA = 6.0

print(f"{primeiro_nome}, {idade_usuario} anos")
print(f"Taxa: {TAXA_JUROS} | Nota mínima: {NOTA_MINIMA}")
print()


# --- Nomes inválidos: estes QUEBRAM o programa ----------------------
# Descomente uma por vez para ver cada erro.
#
# 2nome = "erro"            # SyntaxError: não pode começar com número
# primeiro-nome = "erro"    # SyntaxError: o hífen é o operador de subtração
# class = "erro"            # SyntaxError: palavra reservada da linguagem


# --- Válido, mas não use --------------------------------------------
# Acento em nome de variável FUNCIONA em Python 3 — a linha abaixo roda:
preço = 10
print(f"'preço' com cedilha e acento funciona: {preço}")

# Mas neste material a convenção é escrever nomes sem acento. O motivo
# é prático: teclado trocado, terminal antigo e colega em outro sistema
# operacional transformam "preço" em dor de cabeça. O texto DENTRO das
# aspas leva acento normalmente; o nome da variável, não.
preco = 10                  # prefira assim


# --- Maiúscula importa ----------------------------------------------
idade = 30
Idade = 40      # esta é OUTRA variável, não a mesma

print(f"idade = {idade} | Idade = {Idade}")
print()


# --- O nome é documentação ------------------------------------------
# Os dois blocos calculam a mesma coisa. Compare a leitura.
a = 8.0
b = 6.0
c = (a + b) / 2
print(f"c = {c}")

nota_prova = 8.0
nota_trabalho = 6.0
media_final = (nota_prova + nota_trabalho) / 2
print(f"media_final = {media_final}")


# --- Experimento ---------------------------------------------------
# 1. Descomente "2nome = ..." e rode. Anote o tipo do erro.
#    Faça o mesmo com "class = ...". Os erros são iguais?
#
# 2. Mude TAXA_JUROS para 0.10 em uma linha nova, no fim do arquivo.
#    O Python reclama? Constante em Python é combinado, não regra.
#
# 3. Volte no bloco "a, b, c" daqui a uma semana e tente lembrar o
#    que ele calcula sem ler o bloco de baixo. Esse é o argumento
#    inteiro a favor de nomes longos.
