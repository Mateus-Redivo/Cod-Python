"""
Módulo 02 — Operadores
Exemplo 03: operadores de comparação

Este arquivo mostra:
  - os seis operadores e o bool que eles produzem
  - guardar uma comparação numa variável de nome descritivo
  - comparação de texto e a cilada dos decimais

Como executar:
  python 03_comparacao.py
"""

x = 10
y = 5

print(f"x = {x}, y = {y}")
print(f"x == y  ->  {x == y}")
print(f"x != y  ->  {x != y}")
print(f"x >  y  ->  {x > y}")
print(f"x <  y  ->  {x < y}")
print(f"x >= 10 ->  {x >= 10}")
print(f"x <= 9  ->  {x <= 9}")
print()

# Toda comparação produz um bool, e bool cabe numa variável.
# Dar um bom nome a ela é o que vai deixar o if legível no módulo 04.
idade = 20
nota = 7.5

eh_maior_de_idade = idade >= 18
foi_aprovado = nota >= 6.0

print(f"eh_maior_de_idade = {eh_maior_de_idade} (tipo {type(eh_maior_de_idade).__name__})")
print(f"foi_aprovado      = {foi_aprovado}")
print()


# --- Comparando texto -----------------------------------------------
print(f'"Ana" == "Ana"   ->  {"Ana" == "Ana"}')
print(f'"Ana" <  "Bruno" ->  {"Ana" < "Bruno"}    <- ordem alfabética')

# Mas cuidado: maiúsculas vêm ANTES das minúsculas na tabela de
# caracteres. Isso não é a ordem do dicionário.
print(f'"Zebra" < "ana"  ->  {"Zebra" < "ana"}    <- surpresa!')
print()


# --- A cilada dos decimais ------------------------------------------
soma = 0.1 + 0.2

print(f"0.1 + 0.2        = {soma}")
print(f"0.1 + 0.2 == 0.3 -> {soma == 0.3}    <- False!")
print()
print("Não é bug do Python: é como todo computador guarda decimais,")
print("em binário. Sobra uma poeirinha no fim da conta.")
print()

# A saída é comparar a DIFERENÇA, não a igualdade exata.
print(f"abs(soma - 0.3) < 0.0001 -> {abs(soma - 0.3) < 0.0001}    <- assim funciona")

# Para dinheiro e notas, arredondar na exibição resolve na prática.
print(f"exibindo com 2 casas: {soma:.2f}")


# --- Experimento ---------------------------------------------------
# 1. Troque "eh_maior_de_idade" por "x" e leia a linha do print de
#    novo. O nome descritivo é metade da legibilidade do código.
#
# 2. Rode print("zebra" < "ana"). Agora sem maiúscula, a ordem é a
#    esperada? O módulo 07 mostra o .lower(), que resolve isso.
#
# 3. Rode print(0.1 + 0.2 + 0.3 == 0.6). E print(1.5 + 1.5 == 3.0)?
#    Por que o segundo funciona e o primeiro não?
