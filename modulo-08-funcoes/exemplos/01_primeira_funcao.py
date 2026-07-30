"""
Módulo 08 — Funções
Exemplo 01: a primeira função

Este arquivo mostra:
  - a estrutura do def e a chamada
  - que DEFINIR não é EXECUTAR
  - uma função chamando outra

Como executar:
  python 01_primeira_funcao.py
"""

print("--- 1. Definir não é executar ---")


# Esta linha só ENSINA o Python a fazer algo. Nada acontece ainda.
def saudar():
    print("  Olá! Bem-vindo ao programa.")


print("A função foi definida, mas nada saiu na tela até agora.")

saudar()        # AGORA sim: a chamada é que executa
saudar()        # e pode chamar quantas vezes quiser
print()


# --- 2. Função com parâmetro ----------------------------------------
print("--- 2. Com parâmetro ---")


def saudar_usuario(nome):
    print(f"  Olá, {nome}!")


saudar_usuario("Ana")
saudar_usuario("Carlos")
print()


# --- 3. Função com retorno -------------------------------------------
print("--- 3. Com retorno ---")


def dobrar(numero):
    return numero * 2


resultado = dobrar(5)
print(f"  dobrar(5) devolveu {resultado}")

# O retorno é um valor como qualquer outro: cabe numa expressão.
print(f"  dobrar(3) + dobrar(4) = {dobrar(3) + dobrar(4)}")
print()


# --- 4. Função chamando outra ----------------------------------------
print("--- 4. Uma chamando a outra ---")


def calcular_area_quadrado(lado):
    return lado * lado


def calcular_area_retangulo(largura, altura):
    return largura * altura


def mostrar_areas(lado, largura, altura):
    print(f"  Área do quadrado:  {calcular_area_quadrado(lado)}")
    print(f"  Área do retângulo: {calcular_area_retangulo(largura, altura)}")


mostrar_areas(4, 5, 3)


# --- Experimento ---------------------------------------------------
# 1. Apague a linha "saudar()" e rode. A função continua definida,
#    mas nada aparece. Definir sem chamar é escrever e não usar.
#
# 2. Chame dobrar() sem argumento nenhum: dobrar().
#    Leia o erro — ele diz exatamente qual parâmetro faltou.
#
# 3. Mova a definição de "dobrar" para DEPOIS da linha que a chama.
#    Qual erro aparece? Lembre do módulo 00: o Python lê de cima
#    para baixo.
