# Criar uma matriz de produtos com nome, preço e quantidade
produtos = [
    ["Arroz", 22.90, 15],
    ["Feijão", 9.80, 8],
    ["Macarrão", 4.50, 20],
    ["Açúcar", 7.90, 12],
    ["Café", 18.50, 5]
]

# Mostrar todos os produtos
print("\nLista de Produtos:")
print(f"{'Produto':<15} {'Preço (R$)':<12} {'Quantidade':<10}")
print("-" * 40)

for produto in produtos:
    nome = produto[0]
    preco = produto[1]
    qtd = produto[2]
    print(f"{nome:<15} R$ {preco:<9.2f} {qtd:<10}")

# Calcular valor total do estoque
total = 0
for produto in produtos:
    preco = produto[1]
    qtd = produto[2]
    total += preco * qtd

print(f"\nValor total do estoque: R$ {total:.2f}")

# Encontrar produto mais caro
mais_caro = produtos[0]
for produto in produtos:
    if produto[1] > mais_caro[1]:
        mais_caro = produto

print(f"\nProduto mais caro: {mais_caro[0]} - R$ {mais_caro[1]:.2f}")

# Atualizar preço de um produto
print("\nAtualizando preço do café para R$ 22.90...")
nome_produto = "café"
novo_preco = 22.90
produto_encontrado = False

for produto in produtos:
    if produto[0].lower() == nome_produto.lower():
        produto[1] = novo_preco
        produto_encontrado = True
        break

if produto_encontrado:
    print("Preço atualizado com sucesso!")
else:
    print("Produto não encontrado.")

# Mostrar produtos atualizados
print("\nLista atualizada de produtos:")
print(f"{'Produto':<15} {'Preço (R$)':<12} {'Quantidade':<10}")
print("-" * 40)

for produto in produtos:
    nome = produto[0]
    preco = produto[1]
    qtd = produto[2]
    print(f"{nome:<15} R$ {preco:<9.2f} {qtd:<10}")