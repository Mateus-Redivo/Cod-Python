# Problemas: Código extremamente repetitivo, lógica complexa embaralhada,
# múltiplas responsabilidades misturadas, falta de estrutura, tratamento de erros inadequado,
# cálculos repetidos, validações inconsistentes, apresentação confusa

import datetime

print("Sistema de Gerenciamento de Funcionários - RH")

# Funcionário 1
print("CADASTRO FUNCIONÁRIO 1:")
nome_func1 = input("Nome completo: ").strip()
while len(nome_func1) < 3 or not all(c.isalpha() or c.isspace() for c in nome_func1):
    print("Nome deve ter pelo menos 3 caracteres e conter apenas letras!")
    nome_func1 = input("Nome completo: ").strip()

cargo_func1 = input("Cargo (gerente/supervisor/operador/estagiario): ").lower()
while cargo_func1 not in ["gerente", "supervisor", "operador", "estagiario"]:
    print("Cargo inválido!")
    cargo_func1 = input(
        "Cargo (gerente/supervisor/operador/estagiario): ").lower()

salario_base_func1 = float(input("Salário base: R$ "))
while salario_base_func1 <= 0 or salario_base_func1 > 50000:
    print("Salário deve ser entre R$ 0,01 e R$ 50.000,00!")
    salario_base_func1 = float(input("Salário base: R$ "))

horas_extras_func1 = int(input("Horas extras no mês: "))
while horas_extras_func1 < 0 or horas_extras_func1 > 100:
    print("Horas extras devem ser entre 0 e 100!")
    horas_extras_func1 = int(input("Horas extras no mês: "))

anos_empresa_func1 = int(input("Anos na empresa: "))
while anos_empresa_func1 < 0 or anos_empresa_func1 > 50:
    print("Anos na empresa devem ser entre 0 e 50!")
    anos_empresa_func1 = int(input("Anos na empresa: "))

# Cálculos Funcionário 1
if cargo_func1 == "gerente":
    bonus_cargo_func1 = salario_base_func1 * 0.20
    valor_hora_extra_func1 = (salario_base_func1 / 160) * 2.0
elif cargo_func1 == "supervisor":
    bonus_cargo_func1 = salario_base_func1 * 0.15
    valor_hora_extra_func1 = (salario_base_func1 / 160) * 1.8
elif cargo_func1 == "operador":
    bonus_cargo_func1 = salario_base_func1 * 0.10
    valor_hora_extra_func1 = (salario_base_func1 / 160) * 1.5
else:  # estagiario
    bonus_cargo_func1 = 0
    valor_hora_extra_func1 = (salario_base_func1 / 160) * 1.2

if anos_empresa_func1 >= 10:
    bonus_tempo_func1 = salario_base_func1 * 0.10
elif anos_empresa_func1 >= 5:
    bonus_tempo_func1 = salario_base_func1 * 0.05
else:
    bonus_tempo_func1 = 0

total_horas_extras_func1 = horas_extras_func1 * valor_hora_extra_func1
salario_bruto_func1 = salario_base_func1 + bonus_cargo_func1 + \
    bonus_tempo_func1 + total_horas_extras_func1

if salario_bruto_func1 <= 2000:
    desconto_ir_func1 = 0
elif salario_bruto_func1 <= 4000:
    desconto_ir_func1 = salario_bruto_func1 * 0.075
elif salario_bruto_func1 <= 8000:
    desconto_ir_func1 = salario_bruto_func1 * 0.15
else:
    desconto_ir_func1 = salario_bruto_func1 * 0.275

desconto_inss_func1 = min(salario_bruto_func1 * 0.11, 828.39)
salario_liquido_func1 = salario_bruto_func1 - \
    desconto_ir_func1 - desconto_inss_func1

# Funcionário 2
print("\nCADASTRO FUNCIONÁRIO 2:")
nome_func2 = input("Nome completo: ").strip()
while len(nome_func2) < 3 or not all(c.isalpha() or c.isspace() for c in nome_func2):
    print("Nome deve ter pelo menos 3 caracteres e conter apenas letras!")
    nome_func2 = input("Nome completo: ").strip()

cargo_func2 = input("Cargo (gerente/supervisor/operador/estagiario): ").lower()
while cargo_func2 not in ["gerente", "supervisor", "operador", "estagiario"]:
    print("Cargo inválido!")
    cargo_func2 = input(
        "Cargo (gerente/supervisor/operador/estagiario): ").lower()

salario_base_func2 = float(input("Salário base: R$ "))
while salario_base_func2 <= 0 or salario_base_func2 > 50000:
    print("Salário deve ser entre R$ 0,01 e R$ 50.000,00!")
    salario_base_func2 = float(input("Salário base: R$ "))

horas_extras_func2 = int(input("Horas extras no mês: "))
while horas_extras_func2 < 0 or horas_extras_func2 > 100:
    print("Horas extras devem ser entre 0 e 100!")
    horas_extras_func2 = int(input("Horas extras no mês: "))

anos_empresa_func2 = int(input("Anos na empresa: "))
while anos_empresa_func2 < 0 or anos_empresa_func2 > 50:
    print("Anos na empresa devem ser entre 0 e 50!")
    anos_empresa_func2 = int(input("Anos na empresa: "))

# Cálculos Funcionário 2
if cargo_func2 == "gerente":
    bonus_cargo_func2 = salario_base_func2 * 0.20
    valor_hora_extra_func2 = (salario_base_func2 / 160) * 2.0
elif cargo_func2 == "supervisor":
    bonus_cargo_func2 = salario_base_func2 * 0.15
    valor_hora_extra_func2 = (salario_base_func2 / 160) * 1.8
elif cargo_func2 == "operador":
    bonus_cargo_func2 = salario_base_func2 * 0.10
    valor_hora_extra_func2 = (salario_base_func2 / 160) * 1.5
else:  # estagiario
    bonus_cargo_func2 = 0
    valor_hora_extra_func2 = (salario_base_func2 / 160) * 1.2

if anos_empresa_func2 >= 10:
    bonus_tempo_func2 = salario_base_func2 * 0.10
elif anos_empresa_func2 >= 5:
    bonus_tempo_func2 = salario_base_func2 * 0.05
else:
    bonus_tempo_func2 = 0

total_horas_extras_func2 = horas_extras_func2 * valor_hora_extra_func2
salario_bruto_func2 = salario_base_func2 + bonus_cargo_func2 + \
    bonus_tempo_func2 + total_horas_extras_func2

if salario_bruto_func2 <= 2000:
    desconto_ir_func2 = 0
elif salario_bruto_func2 <= 4000:
    desconto_ir_func2 = salario_bruto_func2 * 0.075
elif salario_bruto_func2 <= 8000:
    desconto_ir_func2 = salario_bruto_func2 * 0.15
else:
    desconto_ir_func2 = salario_bruto_func2 * 0.275

desconto_inss_func2 = min(salario_bruto_func2 * 0.11, 828.39)
salario_liquido_func2 = salario_bruto_func2 - \
    desconto_ir_func2 - desconto_inss_func2

# Funcionário 3
print("\nCADASTRO FUNCIONÁRIO 3:")
nome_func3 = input("Nome completo: ").strip()
while len(nome_func3) < 3 or not all(c.isalpha() or c.isspace() for c in nome_func3):
    print("Nome deve ter pelo menos 3 caracteres e conter apenas letras!")
    nome_func3 = input("Nome completo: ").strip()

cargo_func3 = input("Cargo (gerente/supervisor/operador/estagiario): ").lower()
while cargo_func3 not in ["gerente", "supervisor", "operador", "estagiario"]:
    print("Cargo inválido!")
    cargo_func3 = input(
        "Cargo (gerente/supervisor/operador/estagiario): ").lower()

salario_base_func3 = float(input("Salário base: R$ "))
while salario_base_func3 <= 0 or salario_base_func3 > 50000:
    print("Salário deve ser entre R$ 0,01 e R$ 50.000,00!")
    salario_base_func3 = float(input("Salário base: R$ "))

horas_extras_func3 = int(input("Horas extras no mês: "))
while horas_extras_func3 < 0 or horas_extras_func3 > 100:
    print("Horas extras devem ser entre 0 e 100!")
    horas_extras_func3 = int(input("Horas extras no mês: "))

anos_empresa_func3 = int(input("Anos na empresa: "))
while anos_empresa_func3 < 0 or anos_empresa_func3 > 50:
    print("Anos na empresa devem ser entre 0 e 50!")
    anos_empresa_func3 = int(input("Anos na empresa: "))

# Cálculos Funcionário 3
if cargo_func3 == "gerente":
    bonus_cargo_func3 = salario_base_func3 * 0.20
    valor_hora_extra_func3 = (salario_base_func3 / 160) * 2.0
elif cargo_func3 == "supervisor":
    bonus_cargo_func3 = salario_base_func3 * 0.15
    valor_hora_extra_func3 = (salario_base_func3 / 160) * 1.8
elif cargo_func3 == "operador":
    bonus_cargo_func3 = salario_base_func3 * 0.10
    valor_hora_extra_func3 = (salario_base_func3 / 160) * 1.5
else:  # estagiario
    bonus_cargo_func3 = 0
    valor_hora_extra_func3 = (salario_base_func3 / 160) * 1.2

if anos_empresa_func3 >= 10:
    bonus_tempo_func3 = salario_base_func3 * 0.10
elif anos_empresa_func3 >= 5:
    bonus_tempo_func3 = salario_base_func3 * 0.05
else:
    bonus_tempo_func3 = 0

total_horas_extras_func3 = horas_extras_func3 * valor_hora_extra_func3
salario_bruto_func3 = salario_base_func3 + bonus_cargo_func3 + \
    bonus_tempo_func3 + total_horas_extras_func3

if salario_bruto_func3 <= 2000:
    desconto_ir_func3 = 0
elif salario_bruto_func3 <= 4000:
    desconto_ir_func3 = salario_bruto_func3 * 0.075
elif salario_bruto_func3 <= 8000:
    desconto_ir_func3 = salario_bruto_func3 * 0.15
else:
    desconto_ir_func3 = salario_bruto_func3 * 0.275

desconto_inss_func3 = min(salario_bruto_func3 * 0.11, 828.39)
salario_liquido_func3 = salario_bruto_func3 - \
    desconto_ir_func3 - desconto_inss_func3

# Relatório Final
print("\n" + "="*80)
print("RELATÓRIO DE FOLHA DE PAGAMENTO")
print("="*80)
print(f"Data de Geração: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}")

print(f"\n1. FUNCIONÁRIO: {nome_func1.upper()}")
print(f"   Cargo: {cargo_func1.title()}")
print(f"   Salário Base: R$ {salario_base_func1:,.2f}")
print(f"   Bônus Cargo: R$ {bonus_cargo_func1:,.2f}")
print(
    f"   Bônus Tempo ({anos_empresa_func1} anos): R$ {bonus_tempo_func3:,.2f}")
print(
    f"   Horas Extras ({horas_extras_func1}h): R$ {total_horas_extras_func1:,.2f}")
print(f"   Salário Bruto: R$ {salario_bruto_func1:,.2f}")
print(f"   Desconto IR: R$ {desconto_ir_func1:,.2f}")
print(f"   Desconto INSS: R$ {desconto_inss_func1:,.2f}")
print(f"   SALÁRIO LÍQUIDO: R$ {salario_liquido_func1:,.2f}")

print(f"\n2. FUNCIONÁRIO: {nome_func2.upper()}")
print(f"   Cargo: {cargo_func2.title()}")
print(f"   Salário Base: R$ {salario_base_func2:,.2f}")
print(f"   Bônus Cargo: R$ {bonus_cargo_func2:,.2f}")
print(
    f"   Bônus Tempo ({anos_empresa_func2} anos): R$ {bonus_tempo_func2:,.2f}")
print(
    f"   Horas Extras ({horas_extras_func2}h): R$ {total_horas_extras_func2:,.2f}")
print(f"   Salário Bruto: R$ {salario_bruto_func2:,.2f}")
print(f"   Desconto IR: R$ {desconto_ir_func2:,.2f}")
print(f"   Desconto INSS: R$ {desconto_inss_func2:,.2f}")
print(f"   SALÁRIO LÍQUIDO: R$ {salario_liquido_func2:,.2f}")

print(f"\n3. FUNCIONÁRIO: {nome_func3.upper()}")
print(f"   Cargo: {cargo_func3.title()}")
print(f"   Salário Base: R$ {salario_base_func3:,.2f}")
print(f"   Bônus Cargo: R$ {bonus_cargo_func3:,.2f}")
print(
    f"   Bônus Tempo ({anos_empresa_func3} anos): R$ {bonus_tempo_func3:,.2f}")
print(
    f"   Horas Extras ({horas_extras_func3}h): R$ {total_horas_extras_func3:,.2f}")
print(f"   Salário Bruto: R$ {salario_bruto_func3:,.2f}")
print(f"   Desconto IR: R$ {desconto_ir_func3:,.2f}")
print(f"   Desconto INSS: R$ {desconto_inss_func3:,.2f}")
print(f"   SALÁRIO LÍQUIDO: R$ {salario_liquido_func3:,.2f}")

# Resumo Geral
total_salario_bruto = salario_bruto_func1 + \
    salario_bruto_func2 + salario_bruto_func3
total_salario_liquido = salario_liquido_func1 + \
    salario_liquido_func2 + salario_liquido_func3
total_descontos = (desconto_ir_func1 + desconto_inss_func1 +
                   desconto_ir_func2 + desconto_inss_func2 +
                   desconto_ir_func3 + desconto_inss_func3)

print("\n" + "="*80)
print("RESUMO GERAL:")
print(f"Total Salário Bruto: R$ {total_salario_bruto:,.2f}")
print(f"Total Descontos: R$ {total_descontos:,.2f}")
print(f"Total Salário Líquido: R$ {total_salario_liquido:,.2f}")

# Análises
maior_salario = max(salario_liquido_func1,
                    salario_liquido_func2, salario_liquido_func3)
if salario_liquido_func1 == maior_salario:
    funcionario_maior_salario = nome_func1
elif salario_liquido_func2 == maior_salario:
    funcionario_maior_salario = nome_func2
else:
    funcionario_maior_salario = nome_func3

print(
    f"\nFuncionário com maior salário: {funcionario_maior_salario} (R$ {maior_salario:,.2f})")

media_salarial = total_salario_liquido / 3
print(f"Média salarial da empresa: R$ {media_salarial:,.2f}")

print("="*80)
