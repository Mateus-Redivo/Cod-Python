"""
Módulo 08 — Funções
Exemplo 04: escopo de variáveis

Este arquivo mostra:
  - variável local nasce e morre dentro da função
  - função LÊ global de boa, mas ALTERAR é outra história
  - por que passar e devolver é melhor que global

Como executar:
  python 04_escopo.py
"""


# --- Local: existe só dentro da função -------------------------------
def calcular_desconto(preco):
    desconto = preco * 0.1      # 'desconto' nasce aqui
    return preco - desconto
    # e morre aqui


print(f"  calcular_desconto(100) = {calcular_desconto(100)}")

# print(desconto)   ->  NameError: name 'desconto' is not defined
print("  print(desconto) daria NameError: ela é local e já morreu")
print()


# Cada chamada tem seu próprio espaço. Uma não atrapalha a outra.
def dobrar(numero):
    resultado = numero * 2
    return resultado


print(f"  dobrar(5) = {dobrar(5)}, dobrar(8) = {dobrar(8)}")
print()


# --- Ler global: sem cerimônia ---------------------------------------
TAXA_IMPOSTO = 0.15


def calcular_preco_final(preco):
    return preco + preco * TAXA_IMPOSTO     # lê a global, tudo bem


print(f"  calcular_preco_final(200) = {calcular_preco_final(200)}")
print()


# --- Alterar global: aí complica -------------------------------------
contador = 0


def incrementar_errado():
    # Descomente as duas linhas abaixo para ver o erro:
    #
    # contador = contador + 1
    # return contador
    #
    #   UnboundLocalError: cannot access local variable 'contador'
    #   where it is not associated with a value
    #
    # O Python vê a ATRIBUIÇÃO e decide que contador é local.
    # Aí tenta ler uma local que ainda não recebeu valor nenhum.
    pass


print("  incrementar_errado() daria UnboundLocalError")
print("  (o Python viu a atribuição e tratou contador como local)")
print()


# A palavra global resolve... tecnicamente.
def incrementar_com_global():
    global contador
    contador = contador + 1


incrementar_com_global()
incrementar_com_global()
print(f"  após dois incrementos com global: contador = {contador}")
print()


# --- A forma limpa: entra valor, sai valor ---------------------------
def incrementar(valor):
    return valor + 1


total = 0
total = incrementar(total)
total = incrementar(total)
print(f"  após dois incrementos sem global: total = {total}")
print()
print("  A segunda forma é preferível: para entender a função, basta")
print("  ler a função. A versão com global obriga a conhecer o estado")
print("  do programa inteiro.")
print()


# --- Mesmo nome, escopos diferentes, sem confusão --------------------
nome = "global"


def mostrar_nome():
    nome = "local"          # esta é OUTRA variável
    print(f"  dentro da função: {nome}")


mostrar_nome()
print(f"  fora da função:   {nome}    <- intacta")


# --- Experimento ---------------------------------------------------
# 1. Descomente as duas linhas dentro de incrementar_errado(), chame
#    a função e leia o UnboundLocalError inteiro.
#
# 2. Em mostrar_nome(), acrescente "global nome" como primeira linha
#    e rode. Agora a global muda. Isso é o que você queria?
#
# 3. Crie uma variável "i" dentro de duas funções diferentes e chame
#    as duas. Elas se atrapalham? Esse isolamento é o motivo de o
#    escopo local existir.
