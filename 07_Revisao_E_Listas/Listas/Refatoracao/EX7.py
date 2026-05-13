# Problemas: Código repetitivo, validação básica, falta de organização,
# cálculos embaralhados, estrutura linear confusa, tratamento de erros inadequado

print("Sistema de Controle de Vendas - Concessionária")

vendas_mes = 0
comissao_total = 0

# Venda 1
print("Registrar Venda 1:")
modelo_carro = input("Modelo do carro: ")
if modelo_carro == "":
    print("Modelo inválido!")
    modelo_carro = "Não informado"

cor_carro = input("Cor do carro: ")
if cor_carro == "":
    print("Cor inválida!")
    cor_carro = "Branco"

preco_carro = float(input("Preço do carro: R$ "))
if preco_carro <= 0:
    print("Preço inválido!")
    preco_carro = 30000

nome_vendedor = input("Nome do vendedor: ")
if nome_vendedor == "":
    print("Nome inválido!")
    nome_vendedor = "Vendedor"

desconto = float(input("Desconto aplicado (%): "))
if desconto < 0 or desconto > 30:
    print("Desconto inválido!")
    desconto = 0

preco_final = preco_carro - (preco_carro * desconto / 100)
vendas_mes = vendas_mes + preco_final
comissao = preco_final * 0.05
comissao_total = comissao_total + comissao

print(f"Carro: {modelo_carro} {cor_carro}")
print(f"Preço original: R$ {preco_carro}")
print(f"Desconto: {desconto}%")
print(f"Preço final: R$ {preco_final}")
print(f"Vendedor: {nome_vendedor}")
print(f"Comissão: R$ {comissao}")
print("-" * 30)

# Venda 2
print("Registrar Venda 2:")
modelo_carro = input("Modelo do carro: ")
if modelo_carro == "":
    print("Modelo inválido!")
    modelo_carro = "Não informado"

cor_carro = input("Cor do carro: ")
if cor_carro == "":
    print("Cor inválida!")
    cor_carro = "Branco"

preco_carro = float(input("Preço do carro: R$ "))
if preco_carro <= 0:
    print("Preço inválido!")
    preco_carro = 30000

nome_vendedor = input("Nome do vendedor: ")
if nome_vendedor == "":
    print("Nome inválido!")
    nome_vendedor = "Vendedor"

desconto = float(input("Desconto aplicado (%): "))
if desconto < 0 or desconto > 30:
    print("Desconto inválido!")
    desconto = 0

preco_final = preco_carro - (preco_carro * desconto / 100)
vendas_mes = vendas_mes + preco_final
comissao = preco_final * 0.05
comissao_total = comissao_total + comissao

print(f"Carro: {modelo_carro} {cor_carro}")
print(f"Preço original: R$ {preco_carro}")
print(f"Desconto: {desconto}%")
print(f"Preço final: R$ {preco_final}")
print(f"Vendedor: {nome_vendedor}")
print(f"Comissão: R$ {comissao}")
print("-" * 30)

# Venda 3
print("Registrar Venda 3:")
modelo_carro = input("Modelo do carro: ")
if modelo_carro == "":
    print("Modelo inválido!")
    modelo_carro = "Não informado"

cor_carro = input("Cor do carro: ")
if cor_carro == "":
    print("Cor inválida!")
    cor_carro = "Branco"

preco_carro = float(input("Preço do carro: R$ "))
if preco_carro <= 0:
    print("Preço inválido!")
    preco_carro = 30000

nome_vendedor = input("Nome do vendedor: ")
if nome_vendedor == "":
    print("Nome inválido!")
    nome_vendedor = "Vendedor"

desconto = float(input("Desconto aplicado (%): "))
if desconto < 0 or desconto > 30:
    print("Desconto inválido!")
    desconto = 0

preco_final = preco_carro - (preco_carro * desconto / 100)
vendas_mes = vendas_mes + preco_final
comissao = preco_final * 0.05
comissao_total = comissao_total + comissao

print(f"Carro: {modelo_carro} {cor_carro}")
print(f"Preço original: R$ {preco_carro}")
print(f"Desconto: {desconto}%")
print(f"Preço final: R$ {preco_final}")
print(f"Vendedor: {nome_vendedor}")
print(f"Comissão: R$ {comissao}")
print("-" * 30)

# Venda 4
print("Registrar Venda 4:")
modelo_carro = input("Modelo do carro: ")
if modelo_carro == "":
    print("Modelo inválido!")
    modelo_carro = "Não informado"

cor_carro = input("Cor do carro: ")
if cor_carro == "":
    print("Cor inválida!")
    cor_carro = "Branco"

preco_carro = float(input("Preço do carro: R$ "))
if preco_carro <= 0:
    print("Preço inválido!")
    preco_carro = 30000

nome_vendedor = input("Nome do vendedor: ")
if nome_vendedor == "":
    print("Nome inválido!")
    nome_vendedor = "Vendedor"

desconto = float(input("Desconto aplicado (%): "))
if desconto < 0 or desconto > 30:
    print("Desconto inválido!")
    desconto = 0

preco_final = preco_carro - (preco_carro * desconto / 100)
vendas_mes = vendas_mes + preco_final
comissao = preco_final * 0.05
comissao_total = comissao_total + comissao

print(f"Carro: {modelo_carro} {cor_carro}")
print(f"Preço original: R$ {preco_carro}")
print(f"Desconto: {desconto}%")
print(f"Preço final: R$ {preco_final}")
print(f"Vendedor: {nome_vendedor}")
print(f"Comissão: R$ {comissao}")
print("-" * 30)

# Venda 5
print("Registrar Venda 5:")
modelo_carro = input("Modelo do carro: ")
if modelo_carro == "":
    print("Modelo inválido!")
    modelo_carro = "Não informado"

cor_carro = input("Cor do carro: ")
if cor_carro == "":
    print("Cor inválida!")
    cor_carro = "Branco"

preco_carro = float(input("Preço do carro: R$ "))
if preco_carro <= 0:
    print("Preço inválido!")
    preco_carro = 30000

nome_vendedor = input("Nome do vendedor: ")
if nome_vendedor == "":
    print("Nome inválido!")
    nome_vendedor = "Vendedor"

desconto = float(input("Desconto aplicado (%): "))
if desconto < 0 or desconto > 30:
    print("Desconto inválido!")
    desconto = 0

preco_final = preco_carro - (preco_carro * desconto / 100)
vendas_mes = vendas_mes + preco_final
comissao = preco_final * 0.05
comissao_total = comissao_total + comissao

print(f"Carro: {modelo_carro} {cor_carro}")
print(f"Preço original: R$ {preco_carro}")
print(f"Desconto: {desconto}%")
print(f"Preço final: R$ {preco_final}")
print(f"Vendedor: {nome_vendedor}")
print(f"Comissão: R$ {comissao}")
print("-" * 30)

print("RESUMO DO MÊS:")
print(f"Total de vendas: R$ {vendas_mes}")
print(f"Média por venda: R$ {vendas_mes / 5}")
print(f"Total de comissões: R$ {comissao_total}")
print(
    f"Meta do mês (R$ 500.000): {'ATINGIDA' if vendas_mes >= 500000 else 'NÃO ATINGIDA'}")
