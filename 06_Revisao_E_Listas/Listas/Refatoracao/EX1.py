# Problemas: Repetição de código, validação inadequada, desenvolvimento desorganizado

print("Cadastro de Pratos")

nome = input("Informe o nome do prato ").strip().replace(" ", "")
if not nome.isalpha():
    print("Informe um nome válido.")

preco = int(input("Informe o preço do prato "))
if preco <= 0 or preco.isalpha():
    print("Informe um preço válido.")

print(f"O prato {nome} foi cadastrado com o preço de R$ {preco},00")

nome = input("Informe o nome do prato ").strip().replace(" ", "")
if not nome.isalpha():
    print("Informe um nome válido.")

preco = int(input("Informe o preço do prato "))
if preco <= 0 or preco.isalpha():
    print("Informe um preço válido.")

print(f"O prato {nome} foi cadastrado com o preço de R$ {preco},00")

nome = input("Informe o nome do prato ").strip().replace(" ", "")
if not nome.isalpha():
    print("Informe um nome válido.")

preco = int(input("Informe o preço do prato "))
if preco <= 0 or preco.isalpha():
    print("Informe um preço válido.")

print(f"O prato {nome} foi cadastrado com o preço de R$ {preco},00")

nome = input("Informe o nome do prato ").strip().replace(" ", "")
if not nome.isalpha():
    print("Informe um nome válido.")

preco = int(input("Informe o preço do prato "))
if preco <= 0 or preco.isalpha():
    print("Informe um preço válido.")

print(f"O prato {nome} foi cadastrado com o preço de R$ {preco},00")
