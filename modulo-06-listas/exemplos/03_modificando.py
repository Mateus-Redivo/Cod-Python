"""
Módulo 06 — Listas
Exemplo 03: modificando a lista

Este arquivo mostra:
  - append, insert, remove, pop, sort e reverse
  - a diferença entre remover por VALOR e por POSIÇÃO
  - a cilada do None: métodos que modificam no lugar

Como executar:
  python 03_modificando.py
"""

animais = ["gato", "cachorro", "peixe"]
print(f"original:            {animais}")

# Trocar pelo índice
animais[1] = "hamster"
print(f"animais[1]='hamster':{animais}")

# Acrescentar no fim
animais.append("coelho")
print(f"append('coelho'):    {animais}")

# Inserir numa posição, empurrando o resto
animais.insert(1, "pássaro")
print(f"insert(1,'pássaro'): {animais}")

# Remover pelo VALOR
animais.remove("peixe")
print(f"remove('peixe'):     {animais}")

# Remover o último e guardar o que saiu
ultimo = animais.pop()
print(f"pop() devolveu '{ultimo}': {animais}")

# Remover por POSIÇÃO
removido = animais.pop(0)
print(f"pop(0) devolveu '{removido}':  {animais}")
print()


# --- remove() é por valor, pop() é por posição ----------------------
numeros = [10, 20, 30, 40]
print(f"numeros = {numeros}")

numeros.remove(20)          # remove o VALOR 20
print(f"remove(20) -> {numeros}      <- sumiu o 20, não a posição 20")

numeros.pop(0)              # remove a POSIÇÃO 0
print(f"pop(0)     -> {numeros}          <- sumiu o primeiro")
print()


# --- Ordenar ---------------------------------------------------------
notas = [8, 5, 10, 6, 9]
print(f"notas       = {notas}")

notas.sort()
print(f"após sort() = {notas}")

notas.reverse()
print(f"após reverse() = {notas}")
print()


# --- A cilada do None ------------------------------------------------
# sort(), reverse() e append() modificam a lista NO LUGAR e devolvem
# None. Atribuir o resultado destrói sua lista.
valores = [3, 1, 2]
print(f"valores = {valores}")

resultado_do_sort = valores.sort()
print(f"o que sort() devolveu: {resultado_do_sort}    <- None!")
print(f"mas a lista foi ordenada: {valores}")
print()

# Ou seja: "valores = valores.sort()" faria valores virar None.
# Se você quer a ordenada SEM mexer na original, a função é outra:
originais = [3, 1, 2]
ordenadas = sorted(originais)

print(f"originais após sorted(): {originais}   <- intacta")
print(f"ordenadas:               {ordenadas}")


# --- Experimento ---------------------------------------------------
# 1. Escreva "valores = valores.sort()" numa linha nova e depois
#    print(valores). Confirme que virou None. Este erro custa tempo
#    porque só aparece na linha SEGUINTE.
#
# 2. Rode animais.remove("elefante"), que não está na lista.
#    ValueError. Como você checaria antes? (dica: operador "in")
#
# 3. Rode [].pop(). Qual erro? Por isso listas vazias merecem um if.
