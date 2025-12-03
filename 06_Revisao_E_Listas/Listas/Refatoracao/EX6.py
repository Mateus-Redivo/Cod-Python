# Problemas: Repetição excessiva de código, validação inadequada, estrutura confusa,
# falta de tratamento de exceções, cálculos repetidos, lógica embaralhada

print("Sistema de Cadastro de Livros - Biblioteca")

total_paginas = 0
livro_mais_caro = ""
maior_preco = 0

# Livro 1
print("Cadastro do Livro 1:")
titulo1 = input("Título do livro: ")
if titulo1 == "" or titulo1.isdigit():
    print("Título inválido!")
    titulo1 = "Sem Título"

autor1 = input("Autor do livro: ")
if autor1 == "" or len(autor1) < 2:
    print("Autor inválido!")
    autor1 = "Autor Desconhecido"

paginas1 = int(input("Número de páginas: "))
if paginas1 <= 0 or paginas1 > 2000:
    print("Número de páginas inválido!")
    paginas1 = 100

preco1 = float(input("Preço do livro: R$ "))
if preco1 <= 0:
    print("Preço inválido!")
    preco1 = 10.0

ano1 = int(input("Ano de publicação: "))
if ano1 < 1800 or ano1 > 2024:
    print("Ano inválido!")
    ano1 = 2000

total_paginas = total_paginas + paginas1
if preco1 > maior_preco:
    maior_preco = preco1
    livro_mais_caro = titulo1

print(f"Livro cadastrado: {titulo1}")
print(f"Autor: {autor1}")
print(f"Páginas: {paginas1}")
print(f"Preço: R$ {preco1}")
print(f"Ano: {ano1}")
print("-" * 40)

# Livro 2
print("Cadastro do Livro 2:")
titulo2 = input("Título do livro: ")
if titulo2 == "" or titulo2.isdigit():
    print("Título inválido!")
    titulo2 = "Sem Título"

autor2 = input("Autor do livro: ")
if autor2 == "" or len(autor2) < 2:
    print("Autor inválido!")
    autor2 = "Autor Desconhecido"

paginas2 = int(input("Número de páginas: "))
if paginas2 <= 0 or paginas2 > 2000:
    print("Número de páginas inválido!")
    paginas2 = 100

preco2 = float(input("Preço do livro: R$ "))
if preco2 <= 0:
    print("Preço inválido!")
    preco2 = 10.0

ano2 = int(input("Ano de publicação: "))
if ano2 < 1800 or ano2 > 2024:
    print("Ano inválido!")
    ano2 = 2000

total_paginas = total_paginas + paginas2
if preco2 > maior_preco:
    maior_preco = preco2
    livro_mais_caro = titulo2

print(f"Livro cadastrado: {titulo2}")
print(f"Autor: {autor2}")
print(f"Páginas: {paginas2}")
print(f"Preço: R$ {preco2}")
print(f"Ano: {ano2}")
print("-" * 40)

# Livro 3
print("Cadastro do Livro 3:")
titulo3 = input("Título do livro: ")
if titulo3 == "" or titulo3.isdigit():
    print("Título inválido!")
    titulo3 = "Sem Título"

autor3 = input("Autor do livro: ")
if autor3 == "" or len(autor3) < 2:
    print("Autor inválido!")
    autor3 = "Autor Desconhecido"

paginas3 = int(input("Número de páginas: "))
if paginas3 <= 0 or paginas3 > 2000:
    print("Número de páginas inválido!")
    paginas3 = 100

preco3 = float(input("Preço do livro: R$ "))
if preco3 <= 0:
    print("Preço inválido!")
    preco3 = 10.0

ano3 = int(input("Ano de publicação: "))
if ano3 < 1800 or ano3 > 2024:
    print("Ano inválido!")
    ano3 = 2000

total_paginas = total_paginas + paginas3
if preco3 > maior_preco:
    maior_preco = preco3
    livro_mais_caro = titulo3

print(f"Livro cadastrado: {titulo3}")
print(f"Autor: {autor3}")
print(f"Páginas: {paginas3}")
print(f"Preço: R$ {preco3}")
print(f"Ano: {ano3}")
print("-" * 40)

# Livro 4
print("Cadastro do Livro 4:")
titulo4 = input("Título do livro: ")
if titulo4 == "" or titulo4.isdigit():
    print("Título inválido!")
    titulo4 = "Sem Título"

autor4 = input("Autor do livro: ")
if autor4 == "" or len(autor4) < 2:
    print("Autor inválido!")
    autor4 = "Autor Desconhecido"

paginas4 = int(input("Número de páginas: "))
if paginas4 <= 0 or paginas4 > 2000:
    print("Número de páginas inválido!")
    paginas4 = 100

preco4 = float(input("Preço do livro: R$ "))
if preco4 <= 0:
    print("Preço inválido!")
    preco4 = 10.0

ano4 = int(input("Ano de publicação: "))
if ano4 < 1800 or ano4 > 2024:
    print("Ano inválido!")
    ano4 = 2000

total_paginas = total_paginas + paginas4
if preco4 > maior_preco:
    maior_preco = preco4
    livro_mais_caro = titulo4

print(f"Livro cadastrado: {titulo4}")
print(f"Autor: {autor4}")
print(f"Páginas: {paginas4}")
print(f"Preço: R$ {preco4}")
print(f"Ano: {ano4}")
print("-" * 40)

print("RELATÓRIO FINAL:")
print(f"Total de páginas dos livros: {total_paginas}")
print(f"Média de páginas por livro: {total_paginas / 4}")
print(f"Livro mais caro: {livro_mais_caro} - R$ {maior_preco}")

valor_total = preco1 + preco2 + preco3 + preco4
print(f"Valor total dos livros: R$ {valor_total}")
print(f"Preço médio: R$ {valor_total / 4}")
