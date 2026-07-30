"""
Módulo 08 — Funções
Exemplo 03: return vs print

Este arquivo mostra:
  - duas funções quase idênticas que se comportam de forma oposta
  - por que uma função que calcula deve devolver, não imprimir
  - de onde vem o None

Este é o ponto que mais confunde no módulo. Rode devagar.

Como executar:
  python 03_return_vs_print.py
"""


def dobrar_e_mostrar(numero):
    print(f"  (de dentro da função) {numero * 2}")


def dobrar(numero):
    return numero * 2


# --- Na chamada simples, parecem iguais ------------------------------
print("--- Chamando as duas ---")
dobrar_e_mostrar(5)
print(f"  (de fora) {dobrar(5)}")
print()


# --- Na hora de GUARDAR, a diferença aparece -------------------------
print("--- Guardando o resultado ---")

a = dobrar_e_mostrar(5)
b = dobrar(5)

print(f"  a = {a}      <- None! a função imprimiu, mas não devolveu nada")
print(f"  b = {b}        <- o valor de verdade")
print()


# --- Na hora de CALCULAR, uma delas simplesmente não serve -----------
print("--- Usando numa expressão ---")
print(f"  dobrar(3) + dobrar(4) = {dobrar(3) + dobrar(4)}")
print()
print("  dobrar_e_mostrar(3) + dobrar_e_mostrar(4) daria:")
print("    TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'")
print("  Descomente no arquivo para ver.")
#
# print(dobrar_e_mostrar(3) + dobrar_e_mostrar(4))
print()


# --- De onde vem o None -----------------------------------------------
def sem_return():
    x = 1 + 1


print("--- Toda função devolve algo ---")
print(f"  uma função sem return devolve: {sem_return()}")
print("  É o mesmo None do módulo 06, quando lista.sort() era atribuído.")
print()


# --- A forma certa: calcular devolve, quem chama decide --------------
def calcular_media(notas):
    return sum(notas) / len(notas)


media = calcular_media([7, 8, 9])

# Quem chamou decide o que fazer: mostrar...
print(f"  Média: {media:.2f}")
# ...ou comparar...
print(f"  Aprovado: {media >= 6}")
# ...ou usar em outra conta. A função não decidiu nada disso.
print(f"  Em porcentagem: {media * 10:.0f}%")


# --- Experimento ---------------------------------------------------
# 1. Descomente a linha do TypeError e leia o erro inteiro.
#
# 2. Reescreva calcular_media para dar print em vez de return.
#    Agora tente usar o resultado nas três linhas finais. Quantas
#    ainda funcionam?
#
# 3. Acrescente um print DEPOIS do return, dentro de dobrar().
#    Ele executa? Por quê?
