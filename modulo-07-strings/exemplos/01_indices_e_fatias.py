"""
Módulo 07 — Strings
Exemplo 01: string é uma sequência

Este arquivo mostra:
  - índice, índice negativo e fatia — igualzinho a listas
  - percorrer uma string com for
  - a diferença que importa: string não muda

Como executar:
  python 01_indices_e_fatias.py
"""

texto = "Python"
print(f"texto = {texto}")
print("índice:  0 1 2 3 4 5")
print("negativo:-6-5-4-3-2-1")
print()

# --- Tudo igual a listas ---------------------------------------------
print(f"texto[0]   = {texto[0]}")
print(f"texto[-1]  = {texto[-1]}")
print(f"texto[0:3] = {texto[0:3]}")
print(f"texto[:3]  = {texto[:3]}")
print(f"texto[3:]  = {texto[3:]}")
print(f"texto[-2:] = {texto[-2:]}")
print(f"len(texto) = {len(texto)}")
print(f'"th" in texto -> {"th" in texto}')
print()

# Percorrer caractere a caractere
print("Percorrendo 'Ana':")
for letra in "Ana":
    print(f"  {letra}")
print()


# --- A diferença: string é IMUTÁVEL ---------------------------------
notas = [7, 8]
notas[0] = 10
print(f"lista aceita alteração: {notas}")

# Já a string não. Descomente para ver:
#
# nome = "Ana"
# nome[0] = "E"
#
#   TypeError: 'str' object does not support item assignment

print("string NÃO aceita: nome[0] = 'E' dá TypeError")
print()

# Para "mudar" uma string, você monta uma nova:
nome = "Ana"
novo_nome = "E" + nome[1:]
print(f"nome original: {nome}")
print(f"novo montado : {novo_nome}")


# --- Experimento ---------------------------------------------------
# 1. Descomente as duas linhas do nome[0] e rode. Leia o erro inteiro
#    e comente de novo.
#
# 2. Rode print(texto[10]). Qual erro? Compare com o IndexError de
#    listas do módulo 06 — é o mesmo mecanismo.
#
# 3. Rode print(texto[::-1]). O terceiro número da fatia é o passo,
#    igual ao range(). Com -1, o que acontece?
