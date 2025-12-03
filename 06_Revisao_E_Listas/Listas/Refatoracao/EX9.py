# Problemas: Repetição excessiva, lógica duplicada, validações básicas,
# cálculos repetidos, falta de estruturação, tratamento de erros inadequado

print("Sistema de Reservas - Hotel")

reservas_ativas = 0
receita_total = 0
quarto_mais_caro = ""
maior_diaria = 0

# Reserva 1
print("RESERVA 1:")
nome_hospede = input("Nome do hóspede: ")
if nome_hospede == "" or len(nome_hospede) < 3:
    print("Nome inválido!")
    nome_hospede = "Hóspede"

tipo_quarto = input("Tipo de quarto (simples/duplo/suite): ").lower()
if tipo_quarto not in ["simples", "duplo", "suite"]:
    print("Tipo inválido!")
    tipo_quarto = "simples"

numero_quarto = int(input("Número do quarto: "))
if numero_quarto <= 0 or numero_quarto > 200:
    print("Número inválido!")
    numero_quarto = 101

dias_estadia = int(input("Dias de estadia: "))
if dias_estadia <= 0 or dias_estadia > 30:
    print("Dias inválidos!")
    dias_estadia = 1

valor_diaria = float(input("Valor da diária: R$ "))
if valor_diaria <= 0:
    print("Valor inválido!")
    valor_diaria = 100

cafe_incluso = input("Café da manhã incluso? (s/n): ").lower()
if cafe_incluso not in ["s", "n"]:
    print("Opção inválida!")
    cafe_incluso = "n"

# Cálculos da reserva 1
if tipo_quarto == "simples":
    desconto = 0
elif tipo_quarto == "duplo":
    desconto = 0.05
else:  # suite
    desconto = 0.10

valor_total = valor_diaria * dias_estadia
if cafe_incluso == "s":
    valor_total += dias_estadia * 25

valor_com_desconto = valor_total - (valor_total * desconto)

reservas_ativas += 1
receita_total += valor_com_desconto
if valor_diaria > maior_diaria:
    maior_diaria = valor_diaria
    quarto_mais_caro = f"Quarto {numero_quarto}"

print(f"Hóspede: {nome_hospede}")
print(f"Quarto: {numero_quarto} ({tipo_quarto})")
print(f"Estadia: {dias_estadia} dias")
print(f"Diária: R$ {valor_diaria}")
print(f"Café incluso: {'Sim' if cafe_incluso == 's' else 'Não'}")
print(f"Desconto: {desconto * 100}%")
print(f"Total: R$ {valor_com_desconto}")
print("-" * 40)

# Reserva 2
print("RESERVA 2:")
nome_hospede = input("Nome do hóspede: ")
if nome_hospede == "" or len(nome_hospede) < 3:
    print("Nome inválido!")
    nome_hospede = "Hóspede"

tipo_quarto = input("Tipo de quarto (simples/duplo/suite): ").lower()
if tipo_quarto not in ["simples", "duplo", "suite"]:
    print("Tipo inválido!")
    tipo_quarto = "simples"

numero_quarto = int(input("Número do quarto: "))
if numero_quarto <= 0 or numero_quarto > 200:
    print("Número inválido!")
    numero_quarto = 101

dias_estadia = int(input("Dias de estadia: "))
if dias_estadia <= 0 or dias_estadia > 30:
    print("Dias inválidos!")
    dias_estadia = 1

valor_diaria = float(input("Valor da diária: R$ "))
if valor_diaria <= 0:
    print("Valor inválido!")
    valor_diaria = 100

cafe_incluso = input("Café da manhã incluso? (s/n): ").lower()
if cafe_incluso not in ["s", "n"]:
    print("Opção inválida!")
    cafe_incluso = "n"

# Cálculos da reserva 2
if tipo_quarto == "simples":
    desconto = 0
elif tipo_quarto == "duplo":
    desconto = 0.05
else:  # suite
    desconto = 0.10

valor_total = valor_diaria * dias_estadia
if cafe_incluso == "s":
    valor_total += dias_estadia * 25

valor_com_desconto = valor_total - (valor_total * desconto)

reservas_ativas += 1
receita_total += valor_com_desconto
if valor_diaria > maior_diaria:
    maior_diaria = valor_diaria
    quarto_mais_caro = f"Quarto {numero_quarto}"

print(f"Hóspede: {nome_hospede}")
print(f"Quarto: {numero_quarto} ({tipo_quarto})")
print(f"Estadia: {dias_estadia} dias")
print(f"Diária: R$ {valor_diaria}")
print(f"Café incluso: {'Sim' if cafe_incluso == 's' else 'Não'}")
print(f"Desconto: {desconto * 100}%")
print(f"Total: R$ {valor_com_desconto}")
print("-" * 40)

# Reserva 3
print("RESERVA 3:")
nome_hospede = input("Nome do hóspede: ")
if nome_hospede == "" or len(nome_hospede) < 3:
    print("Nome inválido!")
    nome_hospede = "Hóspede"

tipo_quarto = input("Tipo de quarto (simples/duplo/suite): ").lower()
if tipo_quarto not in ["simples", "duplo", "suite"]:
    print("Tipo inválido!")
    tipo_quarto = "simples"

numero_quarto = int(input("Número do quarto: "))
if numero_quarto <= 0 or numero_quarto > 200:
    print("Número inválido!")
    numero_quarto = 101

dias_estadia = int(input("Dias de estadia: "))
if dias_estadia <= 0 or dias_estadia > 30:
    print("Dias inválidos!")
    dias_estadia = 1

valor_diaria = float(input("Valor da diária: R$ "))
if valor_diaria <= 0:
    print("Valor inválido!")
    valor_diaria = 100

cafe_incluso = input("Café da manhã incluso? (s/n): ").lower()
if cafe_incluso not in ["s", "n"]:
    print("Opção inválida!")
    cafe_incluso = "n"

# Cálculos da reserva 3
if tipo_quarto == "simples":
    desconto = 0
elif tipo_quarto == "duplo":
    desconto = 0.05
else:  # suite
    desconto = 0.10

valor_total = valor_diaria * dias_estadia
if cafe_incluso == "s":
    valor_total += dias_estadia * 25

valor_com_desconto = valor_total - (valor_total * desconto)

reservas_ativas += 1
receita_total += valor_com_desconto
if valor_diaria > maior_diaria:
    maior_diaria = valor_diaria
    quarto_mais_caro = f"Quarto {numero_quarto}"

print(f"Hóspede: {nome_hospede}")
print(f"Quarto: {numero_quarto} ({tipo_quarto})")
print(f"Estadia: {dias_estadia} dias")
print(f"Diária: R$ {valor_diaria}")
print(f"Café incluso: {'Sim' if cafe_incluso == 's' else 'Não'}")
print(f"Desconto: {desconto * 100}%")
print(f"Total: R$ {valor_com_desconto}")
print("-" * 40)

# Reserva 4
print("RESERVA 4:")
nome_hospede = input("Nome do hóspede: ")
if nome_hospede == "" or len(nome_hospede) < 3:
    print("Nome inválido!")
    nome_hospede = "Hóspede"

tipo_quarto = input("Tipo de quarto (simples/duplo/suite): ").lower()
if tipo_quarto not in ["simples", "duplo", "suite"]:
    print("Tipo inválido!")
    tipo_quarto = "simples"

numero_quarto = int(input("Número do quarto: "))
if numero_quarto <= 0 or numero_quarto > 200:
    print("Número inválido!")
    numero_quarto = 101

dias_estadia = int(input("Dias de estadia: "))
if dias_estadia <= 0 or dias_estadia > 30:
    print("Dias inválidos!")
    dias_estadia = 1

valor_diaria = float(input("Valor da diária: R$ "))
if valor_diaria <= 0:
    print("Valor inválido!")
    valor_diaria = 100

cafe_incluso = input("Café da manhã incluso? (s/n): ").lower()
if cafe_incluso not in ["s", "n"]:
    print("Opção inválida!")
    cafe_incluso = "n"

# Cálculos da reserva 4
if tipo_quarto == "simples":
    desconto = 0
elif tipo_quarto == "duplo":
    desconto = 0.05
else:  # suite
    desconto = 0.10

valor_total = valor_diaria * dias_estadia
if cafe_incluso == "s":
    valor_total += dias_estadia * 25

valor_com_desconto = valor_total - (valor_total * desconto)

reservas_ativas += 1
receita_total += valor_com_desconto
if valor_diaria > maior_diaria:
    maior_diaria = valor_diaria
    quarto_mais_caro = f"Quarto {numero_quarto}"

print(f"Hóspede: {nome_hospede}")
print(f"Quarto: {numero_quarto} ({tipo_quarto})")
print(f"Estadia: {dias_estadia} dias")
print(f"Diária: R$ {valor_diaria}")
print(f"Café incluso: {'Sim' if cafe_incluso == 's' else 'Não'}")
print(f"Desconto: {desconto * 100}%")
print(f"Total: R$ {valor_com_desconto}")
print("-" * 40)

print("RELATÓRIO DE RESERVAS:")
print(f"Total de reservas ativas: {reservas_ativas}")
print(f"Receita total: R$ {receita_total}")
print(f"Receita média por reserva: R$ {receita_total / reservas_ativas}")
print(f"Quarto com maior diária: {quarto_mais_caro} - R$ {maior_diaria}")
print(
    f"Ocupação: {(reservas_ativas / 200) * 100:.1f}% (200 quartos disponíveis)")
