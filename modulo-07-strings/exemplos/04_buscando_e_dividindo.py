"""
Módulo 07 — Strings
Exemplo 04: buscando, dividindo e juntando

Este arquivo mostra:
  - in, find, count, startswith e endswith
  - a armadilha do find() que devolve -1
  - split() virando lista e join() voltando a virar texto

Como executar:
  python 04_buscando_e_dividindo.py
"""

frase = "Python é uma linguagem"
print(f"frase = '{frase}'")
print()

# --- Buscar -----------------------------------------------------------
print(f'"uma" in frase        -> {"uma" in frase}')
print(f'frase.find("uma")     -> {frase.find("uma")}      (a posição)')
print(f'frase.count("a")      -> {frase.count("a")}')
print(f'frase.startswith("Py")-> {frase.startswith("Py")}')
print(f'frase.endswith("gem") -> {frase.endswith("gem")}')
print()

# Use "in" quando só quer saber SE existe.
# Use find() quando precisa saber ONDE.


# --- A armadilha do find() -------------------------------------------
posicao = frase.find("Java")
print(f'frase.find("Java") -> {posicao}    <- não achou!')
print()
print("find() não dá erro quando não encontra: devolve -1.")
print("E -1 é um índice VÁLIDO em Python — o último caractere.")
print(f"  frase[-1] = '{frase[-1]}'")
print()
print("Por isso, nunca use o retorno de find() sem testar:")

if posicao != -1:
    print(f"  encontrado na posição {posicao}")
else:
    print("  não encontrado (testado antes de usar)")
print()


# --- Dividir: split() devolve uma LISTA ------------------------------
palavras = frase.split()
print(f"frase.split() = {palavras}")
print(f"tipo: {type(palavras).__name__}, com {len(palavras)} elementos")
print()

# Com argumento, divide por outro separador:
data = "30/07/2026"
partes = data.split("/")
print(f'"{data}".split("/") = {partes}')
print(f"  dia={partes[0]}, mês={partes[1]}, ano={partes[2]}")
print()

# E como split devolve lista, tudo do módulo 06 vale:
print("Percorrendo as palavras:")
for palavra in palavras:
    print(f"  {palavra:<12} ({len(palavra)} letras)")
print()


# --- Juntar: join() é o caminho de volta ------------------------------
# A escrita estranha: o SEPARADOR vem primeiro, a lista vai dentro.
print(f'" ".join(palavras) = "{" ".join(palavras)}"')
print(f'"-".join(partes)   = "{"-".join(partes)}"')
print(f'"".join(partes)    = "{"".join(partes)}"')
print()

# join só junta TEXTOS. Com números, quebra:
numeros = [1, 2, 3]
print(f"numeros = {numeros}")
print("'-'.join(numeros) daria TypeError: sequence item 0: expected str")
print("Descomente no arquivo para ver.")
#
# print("-".join(numeros))


# --- Experimento ---------------------------------------------------
# 1. Rode frase.find("a") e frase.rfind("a"). Qual a diferença?
#
# 2. Rode "a,b,,c".split(","). O que acontece com o campo vazio?
#    Isso importa quando você lê dados de um arquivo CSV.
#
# 3. Descomente o "-".join(numeros) e leia o erro. Depois faça
#    funcionar convertendo cada número com str().
