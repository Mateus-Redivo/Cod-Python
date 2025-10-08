# Problemas: Repetição complexa, lógica embaralhada, falta de tratamento de erros,
# validações inconsistentes, estrutura de dados inadequada

print("Sistema de Controle de Estoque - Farmácia")

# Medicamento 1
nome_med1 = input("Nome do medicamento 1: ").strip()
while nome_med1 == "" or len(nome_med1) < 2:
    print("Nome deve ter pelo menos 2 caracteres!")
    nome_med1 = input("Nome do medicamento 1: ").strip()

preco_med1 = float(input("Preço do medicamento 1: R$ "))
while preco_med1 <= 0:
    print("Preço deve ser positivo!")
    preco_med1 = float(input("Preço do medicamento 1: R$ "))

estoque_med1 = int(input("Quantidade em estoque do medicamento 1: "))
while estoque_med1 < 0:
    print("Estoque não pode ser negativo!")
    estoque_med1 = int(input("Quantidade em estoque do medicamento 1: "))

categoria_med1 = input("Categoria (antibiotico/analgesico/vitamina): ").lower()
while categoria_med1 not in ["antibiotico", "analgesico", "vitamina"]:
    print("Categoria inválida!")
    categoria_med1 = input(
        "Categoria (antibiotico/analgesico/vitamina): ").lower()

if categoria_med1 == "antibiotico":
    desconto_med1 = 0.05
elif categoria_med1 == "analgesico":
    desconto_med1 = 0.10
else:
    desconto_med1 = 0.15

preco_final_med1 = preco_med1 * (1 - desconto_med1)
valor_estoque_med1 = preco_final_med1 * estoque_med1

if estoque_med1 < 10:
    status_med1 = "ESTOQUE BAIXO"
elif estoque_med1 < 50:
    status_med1 = "ESTOQUE OK"
else:
    status_med1 = "ESTOQUE ALTO"

# Medicamento 2
nome_med2 = input("Nome do medicamento 2: ").strip()
while nome_med2 == "" or len(nome_med2) < 2:
    print("Nome deve ter pelo menos 2 caracteres!")
    nome_med2 = input("Nome do medicamento 2: ").strip()

preco_med2 = float(input("Preço do medicamento 2: R$ "))
while preco_med2 <= 0:
    print("Preço deve ser positivo!")
    preco_med2 = float(input("Preço do medicamento 2: R$ "))

estoque_med2 = int(input("Quantidade em estoque do medicamento 2: "))
while estoque_med2 < 0:
    print("Estoque não pode ser negativo!")
    estoque_med2 = int(input("Quantidade em estoque do medicamento 2: "))

categoria_med2 = input("Categoria (antibiotico/analgesico/vitamina): ").lower()
while categoria_med2 not in ["antibiotico", "analgesico", "vitamina"]:
    print("Categoria inválida!")
    categoria_med2 = input(
        "Categoria (antibiotico/analgesico/vitamina): ").lower()

if categoria_med2 == "antibiotico":
    desconto_med2 = 0.05
elif categoria_med2 == "analgesico":
    desconto_med2 = 0.10
else:
    desconto_med2 = 0.15

preco_final_med2 = preco_med2 * (1 - desconto_med2)
valor_estoque_med2 = preco_final_med2 * estoque_med2

if estoque_med2 < 10:
    status_med2 = "ESTOQUE BAIXO"
elif estoque_med2 < 50:
    status_med2 = "ESTOQUE OK"
else:
    status_med2 = "ESTOQUE ALTO"

# Medicamento 3
nome_med3 = input("Nome do medicamento 3: ").strip()
while nome_med3 == "" or len(nome_med3) < 2:
    print("Nome deve ter pelo menos 2 caracteres!")
    nome_med3 = input("Nome do medicamento 3: ").strip()

preco_med3 = float(input("Preço do medicamento 3: R$ "))
while preco_med3 <= 0:
    print("Preço deve ser positivo!")
    preco_med3 = float(input("Preço do medicamento 3: R$ "))

estoque_med3 = int(input("Quantidade em estoque do medicamento 3: "))
while estoque_med3 < 0:
    print("Estoque não pode ser negativo!")
    estoque_med3 = int(input("Quantidade em estoque do medicamento 3: "))

categoria_med3 = input("Categoria (antibiotico/analgesico/vitamina): ").lower()
while categoria_med3 not in ["antibiotico", "analgesico", "vitamina"]:
    print("Categoria inválida!")
    categoria_med3 = input(
        "Categoria (antibiotico/analgesico/vitamina): ").lower()

if categoria_med3 == "antibiotico":
    desconto_med3 = 0.05
elif categoria_med3 == "analgesico":
    desconto_med3 = 0.10
else:
    desconto_med3 = 0.15

preco_final_med3 = preco_med3 * (1 - desconto_med3)
valor_estoque_med3 = preco_final_med3 * estoque_med3

if estoque_med3 < 10:
    status_med3 = "ESTOQUE BAIXO"
elif estoque_med3 < 50:
    status_med3 = "ESTOQUE OK"
else:
    status_med3 = "ESTOQUE ALTO"

# Relatório
print("\n" + "="*50)
print("RELATÓRIO DE ESTOQUE")
print("="*50)

print(f"1. {nome_med1}")
print(f"   Categoria: {categoria_med1.title()}")
print(f"   Preço Original: R$ {preco_med1:.2f}")
print(f"   Preço com Desconto: R$ {preco_final_med1:.2f}")
print(f"   Estoque: {estoque_med1} unidades ({status_med1})")
print(f"   Valor Total: R$ {valor_estoque_med1:.2f}")

print(f"\n2. {nome_med2}")
print(f"   Categoria: {categoria_med2.title()}")
print(f"   Preço Original: R$ {preco_med2:.2f}")
print(f"   Preço com Desconto: R$ {preco_final_med2:.2f}")
print(f"   Estoque: {estoque_med2} unidades ({status_med2})")
print(f"   Valor Total: R$ {valor_estoque_med2:.2f}")

print(f"\n3. {nome_med3}")
print(f"   Categoria: {categoria_med3.title()}")
print(f"   Preço Original: R$ {preco_med3:.2f}")
print(f"   Preço com Desconto: R$ {preco_final_med3:.2f}")
print(f"   Estoque: {estoque_med3} unidades ({status_med3})")
print(f"   Valor Total: R$ {valor_estoque_med3:.2f}")

total_geral = valor_estoque_med1 + valor_estoque_med2 + valor_estoque_med3
print(f"\nVALOR TOTAL DO ESTOQUE: R$ {total_geral:.2f}")

# Alertas
print("\nALERTAS:")
if status_med1 == "ESTOQUE BAIXO":
    print(f"⚠️  {nome_med1} precisa ser reposto!")
if status_med2 == "ESTOQUE BAIXO":
    print(f"⚠️  {nome_med2} precisa ser reposto!")
if status_med3 == "ESTOQUE BAIXO":
    print(f"⚠️  {nome_med3} precisa ser reposto!")
