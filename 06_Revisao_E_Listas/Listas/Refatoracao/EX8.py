# Problemas: Repetição massiva de código, validações inconsistentes,
# lógica embaralhada, cálculos espalhados, falta de estrutura, tratamento inadequado de erros

print("Sistema de Cadastro de Produtos - Supermercado")

total_produtos = 0
produto_mais_barato = ""
menor_preco = 999999
estoque_total = 0

# Produto 1
print("Produto 1:")
nome_produto1 = input("Nome do produto: ").strip()
while nome_produto1 == "" or len(nome_produto1) < 2:
    print("Nome deve ter pelo menos 2 caracteres!")
    nome_produto1 = input("Nome do produto: ").strip()

categoria1 = input("Categoria (higiene/alimenticio/limpeza/outros): ").lower()
while categoria1 not in ["higiene", "alimenticio", "limpeza", "outros"]:
    print("Categoria inválida!")
    categoria1 = input(
        "Categoria (higiene/alimenticio/limpeza/outros): ").lower()

preco1 = float(input("Preço: R$ "))
while preco1 <= 0 or preco1 > 1000:
    print("Preço deve ser entre R$ 0,01 e R$ 1000,00!")
    preco1 = float(input("Preço: R$ "))

quantidade1 = int(input("Quantidade em estoque: "))
while quantidade1 < 0:
    print("Quantidade não pode ser negativa!")
    quantidade1 = int(input("Quantidade em estoque: "))

codigo1 = input("Código do produto: ")
while len(codigo1) != 6 or not codigo1.isdigit():
    print("Código deve ter exatamente 6 dígitos!")
    codigo1 = input("Código do produto: ")

if categoria1 == "higiene":
    desconto1 = 0.05
elif categoria1 == "alimenticio":
    desconto1 = 0.02
else:
    desconto1 = 0.0

preco_final1 = preco1 - (preco1 * desconto1)
valor_estoque1 = preco_final1 * quantidade1

total_produtos += 1
estoque_total += quantidade1
if preco_final1 < menor_preco:
    menor_preco = preco_final1
    produto_mais_barato = nome_produto1

print(f"Produto cadastrado: {nome_produto1}")
print(f"Categoria: {categoria1}")
print(f"Código: {codigo1}")
print(f"Preço: R$ {preco1}")
print(f"Desconto: {desconto1 * 100}%")
print(f"Preço final: R$ {preco_final1}")
print(f"Estoque: {quantidade1} unidades")
print(f"Valor total em estoque: R$ {valor_estoque1}")
print("-" * 50)

# Produto 2
print("Produto 2:")
nome_produto2 = input("Nome do produto: ").strip()
while nome_produto2 == "" or len(nome_produto2) < 2:
    print("Nome deve ter pelo menos 2 caracteres!")
    nome_produto2 = input("Nome do produto: ").strip()

categoria2 = input("Categoria (higiene/alimenticio/limpeza/outros): ").lower()
while categoria2 not in ["higiene", "alimenticio", "limpeza", "outros"]:
    print("Categoria inválida!")
    categoria2 = input(
        "Categoria (higiene/alimenticio/limpeza/outros): ").lower()

preco2 = float(input("Preço: R$ "))
while preco2 <= 0 or preco2 > 1000:
    print("Preço deve ser entre R$ 0,01 e R$ 1000,00!")
    preco2 = float(input("Preço: R$ "))

quantidade2 = int(input("Quantidade em estoque: "))
while quantidade2 < 0:
    print("Quantidade não pode ser negativa!")
    quantidade2 = int(input("Quantidade em estoque: "))

codigo2 = input("Código do produto: ")
while len(codigo2) != 6 or not codigo2.isdigit():
    print("Código deve ter exatamente 6 dígitos!")
    codigo2 = input("Código do produto: ")

if categoria2 == "higiene":
    desconto2 = 0.05
elif categoria2 == "alimenticio":
    desconto2 = 0.02
else:
    desconto2 = 0.0

preco_final2 = preco2 - (preco2 * desconto2)
valor_estoque2 = preco_final2 * quantidade2

total_produtos += 1
estoque_total += quantidade2
if preco_final2 < menor_preco:
    menor_preco = preco_final2
    produto_mais_barato = nome_produto2

print(f"Produto cadastrado: {nome_produto2}")
print(f"Categoria: {categoria2}")
print(f"Código: {codigo2}")
print(f"Preço: R$ {preco2}")
print(f"Desconto: {desconto2 * 100}%")
print(f"Preço final: R$ {preco_final2}")
print(f"Estoque: {quantidade2} unidades")
print(f"Valor total em estoque: R$ {valor_estoque2}")
print("-" * 50)

# Produto 3
print("Produto 3:")
nome_produto3 = input("Nome do produto: ").strip()
while nome_produto3 == "" or len(nome_produto3) < 2:
    print("Nome deve ter pelo menos 2 caracteres!")
    nome_produto3 = input("Nome do produto: ").strip()

categoria3 = input("Categoria (higiene/alimenticio/limpeza/outros): ").lower()
while categoria3 not in ["higiene", "alimenticio", "limpeza", "outros"]:
    print("Categoria inválida!")
    categoria3 = input(
        "Categoria (higiene/alimenticio/limpeza/outros): ").lower()

preco3 = float(input("Preço: R$ "))
while preco3 <= 0 or preco3 > 1000:
    print("Preço deve ser entre R$ 0,01 e R$ 1000,00!")
    preco3 = float(input("Preço: R$ "))

quantidade3 = int(input("Quantidade em estoque: "))
while quantidade3 < 0:
    print("Quantidade não pode ser negativa!")
    quantidade3 = int(input("Quantidade em estoque: "))

codigo3 = input("Código do produto: ")
while len(codigo3) != 6 or not codigo3.isdigit():
    print("Código deve ter exatamente 6 dígitos!")
    codigo3 = input("Código do produto: ")

if categoria3 == "higiene":
    desconto3 = 0.05
elif categoria3 == "alimenticio":
    desconto3 = 0.02
else:
    desconto3 = 0.0

preco_final3 = preco3 - (preco3 * desconto3)
valor_estoque3 = preco_final3 * quantidade3

total_produtos += 1
estoque_total += quantidade3
if preco_final3 < menor_preco:
    menor_preco = preco_final3
    produto_mais_barato = nome_produto3

print(f"Produto cadastrado: {nome_produto3}")
print(f"Categoria: {categoria3}")
print(f"Código: {codigo3}")
print(f"Preço: R$ {preco3}")
print(f"Desconto: {desconto3 * 100}%")
print(f"Preço final: R$ {preco_final3}")
print(f"Estoque: {quantidade3} unidades")
print(f"Valor total em estoque: R$ {valor_estoque3}")
print("-" * 50)

# Relatório Final
print("RELATÓRIO GERAL:")
print(f"Total de produtos cadastrados: {total_produtos}")
print(f"Total de itens em estoque: {estoque_total}")
print(f"Produto mais barato: {produto_mais_barato} - R$ {menor_preco}")

valor_total_estoque = valor_estoque1 + valor_estoque2 + valor_estoque3
print(f"Valor total do estoque: R$ {valor_total_estoque}")

media_preco = (preco_final1 + preco_final2 + preco_final3) / 3
print(f"Preço médio dos produtos: R$ {media_preco}")

print("Produtos por categoria:")
if categoria1 == "higiene" or categoria2 == "higiene" or categoria3 == "higiene":
    print("- Higiene: Presente")
if categoria1 == "alimenticio" or categoria2 == "alimenticio" or categoria3 == "alimenticio":
    print("- Alimentício: Presente")
if categoria1 == "limpeza" or categoria2 == "limpeza" or categoria3 == "limpeza":
    print("- Limpeza: Presente")
if categoria1 == "outros" or categoria2 == "outros" or categoria3 == "outros":
    print("- Outros: Presente")
