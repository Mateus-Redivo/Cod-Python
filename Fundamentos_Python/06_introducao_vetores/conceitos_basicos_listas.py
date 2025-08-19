"""
=============================
INTRODUÇÃO AOS VETORES (LISTAS)
=============================
Este arquivo introduz o conceito de listas/vetores em Python
"""

print("=== O QUE SÃO LISTAS/VETORES ===")
print("Listas são coleções ordenadas que podem armazenar múltiplos valores")
print()

# =============================
# CRIANDO LISTAS
# =============================
print("=== CRIANDO LISTAS ===")

# Lista vazia
lista_vazia = []
print(f"Lista vazia: {lista_vazia}")

# Lista com números
numeros = [1, 2, 3, 4, 5]
print(f"Lista de números: {numeros}")

# Lista com strings
nomes = ["Ana", "Bruno", "Carlos", "Diana"]
print(f"Lista de nomes: {nomes}")

# Lista com tipos mistos
lista_mista = [10, "texto", 3.14, True]
print(f"Lista mista: {lista_mista}")
print()

# =============================
# ACESSANDO ELEMENTOS
# =============================
print("=== ACESSANDO ELEMENTOS ===")

cores = ["vermelho", "azul", "verde", "amarelo"]
print(f"Lista de cores: {cores}")

# Acesso por índice (começa em 0)
print(f"Primeira cor (índice 0): {cores[0]}")
print(f"Segunda cor (índice 1): {cores[1]}")
print(f"Última cor (índice 3): {cores[3]}")

# Índices negativos (conta de trás para frente)
print(f"Última cor (índice -1): {cores[-1]}")
print(f"Penúltima cor (índice -2): {cores[-2]}")
print()

# =============================
# PROPRIEDADES BÁSICAS
# =============================
print("=== PROPRIEDADES DAS LISTAS ===")

frutas = ["maçã", "banana", "laranja", "uva", "pêra"]
print(f"Lista de frutas: {frutas}")

# Tamanho da lista
tamanho = len(frutas)
print(f"Quantidade de frutas: {tamanho}")

# Verificando se um item existe
tem_banana = "banana" in frutas
tem_manga = "manga" in frutas
print(f"Tem banana na lista? {tem_banana}")
print(f"Tem manga na lista? {tem_manga}")
print()

# =============================
# MODIFICANDO LISTAS
# =============================
print("=== MODIFICANDO LISTAS ===")

# Lista original
animais = ["gato", "cachorro", "peixe"]
print(f"Lista original: {animais}")

# Alterando um elemento
animais[1] = "hamster"
print(f"Após alterar índice 1: {animais}")

# Adicionando no final
animais.append("coelho")
print(f"Após adicionar coelho: {animais}")

# Inserindo em posição específica
animais.insert(1, "pássaro")
print(f"Após inserir pássaro no índice 1: {animais}")
print()

# =============================
# PERCORRENDO LISTAS
# =============================
print("=== PERCORRENDO LISTAS ===")

notas = [8.5, 7.0, 9.2, 6.8, 8.0]
print(f"Lista de notas: {notas}")

print("Percorrendo com for:")
for nota in notas:
    print(f"  Nota: {nota}")

print("Percorrendo com índices:")
for i in range(len(notas)):
    print(f"  Posição {i}: {notas[i]}")
print()

# =============================
# EXEMPLO PRÁTICO
# =============================
print("=== EXEMPLO PRÁTICO ===")
print("Vamos criar uma lista de compras!")

# Criando lista vazia
lista_compras = []

print("Digite 3 itens para sua lista de compras:")
for i in range(3):
    item = input(f"Item {i+1}: ")
    lista_compras.append(item)

print(f"\nSua lista de compras: {lista_compras}")
print("Itens numerados:")
for i in range(len(lista_compras)):
    print(f"  {i+1}. {lista_compras[i]}")

# Calculando total de itens
total_itens = len(lista_compras)
print(f"\nTotal de itens na lista: {total_itens}")

# Verificando se tem um item específico
item_procurado = input("\nDigite um item para procurar na lista: ")
if item_procurado in lista_compras:
    print(f"✅ '{item_procurado}' está na sua lista!")
else:
    print(f"❌ '{item_procurado}' não está na sua lista.")
