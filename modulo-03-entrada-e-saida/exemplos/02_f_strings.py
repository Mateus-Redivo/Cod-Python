"""
Módulo 03 — Entrada e saída
Exemplo 02: formatando com f-strings

Este arquivo mostra:
  - o f antes das aspas e as chaves
  - casas decimais com :.2f
  - largura fixa e zeros à esquerda

Como executar:
  python 02_f_strings.py
"""

nome = "Maria"
salario = 3500.75
pi = 3.14159

# O "f" antes das aspas libera as chaves para valores.
print(f"Nome: {nome}")

# Sem o f, as chaves aparecem literalmente. Erro clássico:
print("Sem o f: {nome}")
print()

# Dentro das chaves cabe qualquer expressão, não só o nome.
print(f"Salário: {salario}")
print(f"Dobro:   {salario * 2}")
print(f"Metade:  {salario / 2}")
print()


# --- Casas decimais: o formato mais usado do material ---------------
print(f"pi cru:      {pi}")
print(f"pi com 2:    {pi:.2f}")
print(f"pi com 4:    {pi:.4f}")
print(f"pi com 0:    {pi:.0f}       <- arredonda")
print()

# Sem o :.2f, uma média sai assim:
media = 22 / 3
print(f"média crua:  {media}")
print(f"média boa:   {media:.2f}")
print()


# --- Largura e alinhamento ------------------------------------------
# Útil para montar tabelas que ficam alinhadas na vertical.
print(f"|{'Produto':<12}|{'Preço':>9}|")
print(f"|{'Caneta':<12}|{2.5:>9.2f}|")
print(f"|{'Notebook':<12}|{2499.99:>9.2f}|")
print(f"|{'Café':<12}|{18.9:>9.2f}|")
print()
# <  alinha à esquerda
# >  alinha à direita
# 12 e 9 são as larguras em caracteres


# --- Zeros à esquerda -----------------------------------------------
numero = 7
print(f"sem zeros:  {numero}")
print(f"com zeros:  {numero:03d}")
print(f"hora:       {9:02d}:{5:02d}")
print()

# --- Porcentagem ----------------------------------------------------
taxa = 0.157
print(f"taxa: {taxa:.1%}")


# --- Experimento ---------------------------------------------------
# 1. Troque {2.5:>9.2f} por {2.5:<9.2f} nas linhas da tabela.
#    O alinhamento dos preços quebra. Por isso número alinha à direita.
#
# 2. Rode print(f"{2.675:.2f}"). O resultado é 2.67, não 2.68.
#    Não é bug: é a poeirinha dos decimais que você viu no módulo 02.
#
# 3. Monte uma linha de tabela com o seu nome e a sua idade, com o
#    nome ocupando 15 caracteres à esquerda.
