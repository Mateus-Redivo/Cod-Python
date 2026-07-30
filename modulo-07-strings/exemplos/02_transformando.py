"""
Módulo 07 — Strings
Exemplo 02: transformando texto

Este arquivo mostra:
  - upper, lower, title, capitalize, strip e replace
  - a regra central: o método DEVOLVE, não altera
  - encadear métodos

Como executar:
  python 02_transformando.py
"""

texto = "python é uma linguagem"

print(f"original:      '{texto}'")
print(f".upper()       '{texto.upper()}'")
print(f".lower()       '{texto.lower()}'")
print(f".title()       '{texto.title()}'")
print(f".capitalize()  '{texto.capitalize()}'")
print()
print(f"e o original continua: '{texto}'")
print()


# --- A regra central: o método devolve, não altera ------------------
nome = "ana"
print(f"nome = '{nome}'")

nome.upper()                    # o resultado é jogado fora!
print(f"após nome.upper() sozinho: '{nome}'   <- não mudou nada")

nome = nome.upper()             # agora sim: guardamos o retorno
print(f"após nome = nome.upper(): '{nome}'")
print()

print("Compare com listas, do módulo 06:")
print("  notas.sort()      -> altera a lista, devolve None")
print("  nome.upper()      -> não altera nada, devolve a nova string")
print("A pergunta: este método altera o objeto ou cria um novo?")
print()


# --- strip: tirando espaços das pontas -------------------------------
espacado = "    Python com espaços    "

print(f"original: '{espacado}'")
print(f".strip():  '{espacado.strip()}'")
print(f".lstrip(): '{espacado.lstrip()}'")
print(f".rstrip(): '{espacado.rstrip()}'")
print()
print("Repare: strip só mexe nas PONTAS. O espaço do meio fica.")
print()


# --- replace: troca TODAS as ocorrências -----------------------------
frase = "banana"
print(f"'{frase}'.replace('a', '@') = '{frase.replace('a', '@')}'")
print("Trocou as três, não só a primeira.")
print()

# Para trocar só as N primeiras, existe um terceiro argumento:
print(f"'{frase}'.replace('a', '@', 1) = '{frase.replace('a', '@', 1)}'")
print()


# --- Encadear métodos -------------------------------------------------
# Cada método devolve uma string, e essa string recebe o próximo.
# Lê-se da esquerda para a direita.
bagunca = "   JOÃO da SILVA   "
arrumado = bagunca.strip().lower().title()

print(f"'{bagunca}'")
print(f"  .strip().lower().title() -> '{arrumado}'")


# --- Experimento ---------------------------------------------------
# 1. Troque a ordem para .title().lower().strip(). O resultado é o
#    mesmo? Por que a ordem importa aqui?
#
# 2. Rode "guarda-chuva".title(). O resultado é "Guarda-Chuva".
#    O title() considera o hífen um separador de palavras. Isso é o
#    que você queria?
#
# 3. Rode "  a  b  ".strip() e conte os espaços que sobraram.
