# Problemas: Código repetitivo, falta de tratamento de exceções, validação inadequada, estrutura confusa

print("Sistema de Vendas - Lanchonete")

total_vendas = 0
produto_mais_vendido = ""
maior_quantidade = 0

# Produto 1
print("Cadastro Produto 1:")
nome_produto = input("Nome do produto: ")
if nome_produto == "" or nome_produto.isdigit():
    print("Nome inválido!")
    nome_produto = "Produto Sem Nome"

preco_produto = float(input("Preço unitário: R$ "))
if preco_produto <= 0:
    print("Preço inválido!")
    preco_produto = 1.0

qtd_vendida = int(input("Quantidade vendida hoje: "))
if qtd_vendida < 0:
    print("Quantidade inválida!")
    qtd_vendida = 0

subtotal = preco_produto * qtd_vendida
total_vendas = total_vendas + subtotal
if qtd_vendida > maior_quantidade:
    maior_quantidade = qtd_vendida
    produto_mais_vendido = nome_produto

print(f"Produto: {nome_produto}")
print(f"Preço: R$ {preco_produto}")
print(f"Quantidade: {qtd_vendida}")
print(f"Subtotal: R$ {subtotal}")
print("-" * 30)

# Produto 2
print("Cadastro Produto 2:")
nome_produto = input("Nome do produto: ")
if nome_produto == "" or nome_produto.isdigit():
    print("Nome inválido!")
    nome_produto = "Produto Sem Nome"

preco_produto = float(input("Preço unitário: R$ "))
if preco_produto <= 0:
    print("Preço inválido!")
    preco_produto = 1.0

qtd_vendida = int(input("Quantidade vendida hoje: "))
if qtd_vendida < 0:
    print("Quantidade inválida!")
    qtd_vendida = 0

subtotal = preco_produto * qtd_vendida
total_vendas = total_vendas + subtotal
if qtd_vendida > maior_quantidade:
    maior_quantidade = qtd_vendida
    produto_mais_vendido = nome_produto

print(f"Produto: {nome_produto}")
print(f"Preço: R$ {preco_produto}")
print(f"Quantidade: {qtd_vendida}")
print(f"Subtotal: R$ {subtotal}")
print("-" * 30)

# Produto 3
print("Cadastro Produto 3:")
nome_produto = input("Nome do produto: ")
if nome_produto == "" or nome_produto.isdigit():
    print("Nome inválido!")
    nome_produto = "Produto Sem Nome"

preco_produto = float(input("Preço unitário: R$ "))
if preco_produto <= 0:
    print("Preço inválido!")
    preco_produto = 1.0

qtd_vendida = int(input("Quantidade vendida hoje: "))
if qtd_vendida < 0:
    print("Quantidade inválida!")
    qtd_vendida = 0

subtotal = preco_produto * qtd_vendida
total_vendas = total_vendas + subtotal
if qtd_vendida > maior_quantidade:
    maior_quantidade = qtd_vendida
    produto_mais_vendido = nome_produto

print(f"Produto: {nome_produto}")
print(f"Preço: R$ {preco_produto}")
print(f"Quantidade: {qtd_vendida}")
print(f"Subtotal: R$ {subtotal}")
print("-" * 30)

# Produto 4
print("Cadastro Produto 4:")
nome_produto = input("Nome do produto: ")
if nome_produto == "" or nome_produto.isdigit():
    print("Nome inválido!")
    nome_produto = "Produto Sem Nome"

preco_produto = float(input("Preço unitário: R$ "))
if preco_produto <= 0:
    print("Preço inválido!")
    preco_produto = 1.0

qtd_vendida = int(input("Quantidade vendida hoje: "))
if qtd_vendida < 0:
    print("Quantidade inválida!")
    qtd_vendida = 0

subtotal = preco_produto * qtd_vendida
total_vendas = total_vendas + subtotal
if qtd_vendida > maior_quantidade:
    maior_quantidade = qtd_vendida
    produto_mais_vendido = nome_produto

print(f"Produto: {nome_produto}")
print(f"Preço: R$ {preco_produto}")
print(f"Quantidade: {qtd_vendida}")
print(f"Subtotal: R$ {subtotal}")
print("-" * 30)

print("RESUMO DO DIA:")
print(f"Total de vendas: R$ {total_vendas}")
print(
    f"Produto mais vendido: {produto_mais_vendido} ({maior_quantidade} unidades)")
