"""
Módulo 08 — Funções
Exemplo 02: parâmetros, argumentos e valores padrão

Este arquivo mostra:
  - a diferença entre parâmetro e argumento
  - vários parâmetros e a ordem deles
  - parâmetro com valor padrão

Como executar:
  python 02_parametros_e_retorno.py
"""


# "nome" é o PARÂMETRO: o apelido que a função dá ao valor que receber.
def saudar(nome):
    print(f"  Olá, {nome}!")


saudar("Ana")       # "Ana" é o ARGUMENTO: o valor real, na hora da chamada
saudar("Carlos")
print()


# --- Vários parâmetros: a ORDEM importa ------------------------------
def apresentar(nome, idade, cidade):
    print(f"  {nome}, {idade} anos, mora em {cidade}")


apresentar("Ana", 25, "Cascavel")

# Trocar a ordem não dá erro — dá resultado errado, em silêncio:
apresentar(25, "Ana", "Cascavel")
print("  ^ o Python aceitou, mas a frase virou sem sentido")
print()

# Para não depender da ordem, dá para nomear os argumentos:
apresentar(cidade="Curitiba", nome="João", idade=30)
print()


# --- Valor padrão: o parâmetro vira opcional -------------------------
def saudar_com_estilo(nome, saudacao="Olá"):
    print(f"  {saudacao}, {nome}!")


saudar_com_estilo("Ana")                # usa o padrão
saudar_com_estilo("João", "Bom dia")    # sobrescreve o padrão
print()

# Parâmetro com padrão precisa vir DEPOIS dos obrigatórios.
# Isto daria SyntaxError:
#
#   def errado(saudacao="Olá", nome):
#       ...
print("  def errado(saudacao='Olá', nome): dá SyntaxError")
print()


# --- Retorno de mais de um valor -------------------------------------
def analisar(numeros):
    return min(numeros), max(numeros), sum(numeros) / len(numeros)


menor, maior, media = analisar([8, 3, 10, 5])
print(f"  menor={menor}, maior={maior}, média={media:.2f}")
print("  (é o mesmo desempacotamento da troca de variáveis do módulo 01)")


# --- Experimento ---------------------------------------------------
# 1. Chame apresentar("Ana", 25). Falta um argumento — leia o erro,
#    ele diz qual.
#
# 2. Chame saudar_com_estilo(saudacao="Oi", nome="Ana"). Funciona
#    mesmo com a ordem trocada? Por quê?
#
# 3. Em analisar(), tire o "menor," do desempacotamento e deixe só
#    "maior, media = analisar(...)". Qual erro? O que ele diz sobre a
#    quantidade de valores?
