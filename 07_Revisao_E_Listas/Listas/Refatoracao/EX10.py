# Problemas: Repetição massiva de código, validações espalhadas,
# cálculos duplicados, lógica confusa, estrutura linear inadequada,
# falta de tratamento de exceções, múltiplas responsabilidades misturadas

print("Sistema de Análise de Desempenho - Academia")

total_alunos = 0
soma_idades = 0
aluno_mais_pesado = ""
maior_peso = 0
media_imc_geral = 0
soma_imc = 0

# Aluno 1
print("CADASTRO ALUNO 1:")
nome_aluno1 = input("Nome completo: ").strip()
while len(nome_aluno1) < 3 or not all(c.isalpha() or c.isspace() for c in nome_aluno1):
    print("Nome deve ter pelo menos 3 caracteres e conter apenas letras!")
    nome_aluno1 = input("Nome completo: ").strip()

idade1 = int(input("Idade: "))
while idade1 < 16 or idade1 > 80:
    print("Idade deve estar entre 16 e 80 anos!")
    idade1 = int(input("Idade: "))

peso1 = float(input("Peso (kg): "))
while peso1 < 30 or peso1 > 200:
    print("Peso deve estar entre 30kg e 200kg!")
    peso1 = float(input("Peso (kg): "))

altura1 = float(input("Altura (m): "))
while altura1 < 1.30 or altura1 > 2.20:
    print("Altura deve estar entre 1,30m e 2,20m!")
    altura1 = float(input("Altura (m): "))

objetivo1 = input("Objetivo (perder_peso/ganhar_massa/manter): ").lower()
while objetivo1 not in ["perder_peso", "ganhar_massa", "manter"]:
    print("Objetivo inválido!")
    objetivo1 = input("Objetivo (perder_peso/ganhar_massa/manter): ").lower()

experiencia1 = input(
    "Experiência (iniciante/intermediario/avancado): ").lower()
while experiencia1 not in ["iniciante", "intermediario", "avancado"]:
    print("Experiência inválida!")
    experiencia1 = input(
        "Experiência (iniciante/intermediario/avancado): ").lower()

# Cálculos do aluno 1
imc1 = peso1 / (altura1 ** 2)
if imc1 < 18.5:
    classificacao_imc1 = "Abaixo do peso"
elif imc1 < 25:
    classificacao_imc1 = "Peso normal"
elif imc1 < 30:
    classificacao_imc1 = "Sobrepeso"
else:
    classificacao_imc1 = "Obesidade"

if experiencia1 == "iniciante":
    treinos_semana1 = 3
elif experiencia1 == "intermediario":
    treinos_semana1 = 4
else:
    treinos_semana1 = 5

if idade1 >= 60:
    frequencia_cardiaca_max1 = 220 - idade1 - 10
else:
    frequencia_cardiaca_max1 = 220 - idade1

total_alunos += 1
soma_idades += idade1
soma_imc += imc1
if peso1 > maior_peso:
    maior_peso = peso1
    aluno_mais_pesado = nome_aluno1

print(f"Aluno: {nome_aluno1}")
print(f"Idade: {idade1} anos")
print(f"Peso: {peso1} kg | Altura: {altura1} m")
print(f"IMC: {imc1:.2f} ({classificacao_imc1})")
print(f"Objetivo: {objetivo1}")
print(f"Experiência: {experiencia1}")
print(f"Treinos por semana: {treinos_semana1}")
print(f"Frequência cardíaca máxima: {frequencia_cardiaca_max1} bpm")
print("-" * 60)

# Aluno 2
print("CADASTRO ALUNO 2:")
nome_aluno2 = input("Nome completo: ").strip()
while len(nome_aluno2) < 3 or not all(c.isalpha() or c.isspace() for c in nome_aluno2):
    print("Nome deve ter pelo menos 3 caracteres e conter apenas letras!")
    nome_aluno2 = input("Nome completo: ").strip()

idade2 = int(input("Idade: "))
while idade2 < 16 or idade2 > 80:
    print("Idade deve estar entre 16 e 80 anos!")
    idade2 = int(input("Idade: "))

peso2 = float(input("Peso (kg): "))
while peso2 < 30 or peso2 > 200:
    print("Peso deve estar entre 30kg e 200kg!")
    peso2 = float(input("Peso (kg): "))

altura2 = float(input("Altura (m): "))
while altura2 < 1.30 or altura2 > 2.20:
    print("Altura deve estar entre 1,30m e 2,20m!")
    altura2 = float(input("Altura (m): "))

objetivo2 = input("Objetivo (perder_peso/ganhar_massa/manter): ").lower()
while objetivo2 not in ["perder_peso", "ganhar_massa", "manter"]:
    print("Objetivo inválido!")
    objetivo2 = input("Objetivo (perder_peso/ganhar_massa/manter): ").lower()

experiencia2 = input(
    "Experiência (iniciante/intermediario/avancado): ").lower()
while experiencia2 not in ["iniciante", "intermediario", "avancado"]:
    print("Experiência inválida!")
    experiencia2 = input(
        "Experiência (iniciante/intermediario/avancado): ").lower()

# Cálculos do aluno 2
imc2 = peso2 / (altura2 ** 2)
if imc2 < 18.5:
    classificacao_imc2 = "Abaixo do peso"
elif imc2 < 25:
    classificacao_imc2 = "Peso normal"
elif imc2 < 30:
    classificacao_imc2 = "Sobrepeso"
else:
    classificacao_imc2 = "Obesidade"

if experiencia2 == "iniciante":
    treinos_semana2 = 3
elif experiencia2 == "intermediario":
    treinos_semana2 = 4
else:
    treinos_semana2 = 5

if idade2 >= 60:
    frequencia_cardiaca_max2 = 220 - idade2 - 10
else:
    frequencia_cardiaca_max2 = 220 - idade2

total_alunos += 1
soma_idades += idade2
soma_imc += imc2
if peso2 > maior_peso:
    maior_peso = peso2
    aluno_mais_pesado = nome_aluno2

print(f"Aluno: {nome_aluno2}")
print(f"Idade: {idade2} anos")
print(f"Peso: {peso2} kg | Altura: {altura2} m")
print(f"IMC: {imc2:.2f} ({classificacao_imc2})")
print(f"Objetivo: {objetivo2}")
print(f"Experiência: {experiencia2}")
print(f"Treinos por semana: {treinos_semana2}")
print(f"Frequência cardíaca máxima: {frequencia_cardiaca_max2} bpm")
print("-" * 60)

# Aluno 3
print("CADASTRO ALUNO 3:")
nome_aluno3 = input("Nome completo: ").strip()
while len(nome_aluno3) < 3 or not all(c.isalpha() or c.isspace() for c in nome_aluno3):
    print("Nome deve ter pelo menos 3 caracteres e conter apenas letras!")
    nome_aluno3 = input("Nome completo: ").strip()

idade3 = int(input("Idade: "))
while idade3 < 16 or idade3 > 80:
    print("Idade deve estar entre 16 e 80 anos!")
    idade3 = int(input("Idade: "))

peso3 = float(input("Peso (kg): "))
while peso3 < 30 or peso3 > 200:
    print("Peso deve estar entre 30kg e 200kg!")
    peso3 = float(input("Peso (kg): "))

altura3 = float(input("Altura (m): "))
while altura3 < 1.30 or altura3 > 2.20:
    print("Altura deve estar entre 1,30m e 2,20m!")
    altura3 = float(input("Altura (m): "))

objetivo3 = input("Objetivo (perder_peso/ganhar_massa/manter): ").lower()
while objetivo3 not in ["perder_peso", "ganhar_massa", "manter"]:
    print("Objetivo inválido!")
    objetivo3 = input("Objetivo (perder_peso/ganhar_massa/manter): ").lower()

experiencia3 = input(
    "Experiência (iniciante/intermediario/avancado): ").lower()
while experiencia3 not in ["iniciante", "intermediario", "avancado"]:
    print("Experiência inválida!")
    experiencia3 = input(
        "Experiência (iniciante/intermediario/avancado): ").lower()

# Cálculos do aluno 3
imc3 = peso3 / (altura3 ** 2)
if imc3 < 18.5:
    classificacao_imc3 = "Abaixo do peso"
elif imc3 < 25:
    classificacao_imc3 = "Peso normal"
elif imc3 < 30:
    classificacao_imc3 = "Sobrepeso"
else:
    classificacao_imc3 = "Obesidade"

if experiencia3 == "iniciante":
    treinos_semana3 = 3
elif experiencia3 == "intermediario":
    treinos_semana3 = 4
else:
    treinos_semana3 = 5

if idade3 >= 60:
    frequencia_cardiaca_max3 = 220 - idade3 - 10
else:
    frequencia_cardiaca_max3 = 220 - idade3

total_alunos += 1
soma_idades += idade3
soma_imc += imc3
if peso3 > maior_peso:
    maior_peso = peso3
    aluno_mais_pesado = nome_aluno3

print(f"Aluno: {nome_aluno3}")
print(f"Idade: {idade3} anos")
print(f"Peso: {peso3} kg | Altura: {altura3} m")
print(f"IMC: {imc3:.2f} ({classificacao_imc3})")
print(f"Objetivo: {objetivo3}")
print(f"Experiência: {experiencia3}")
print(f"Treinos por semana: {treinos_semana3}")
print(f"Frequência cardíaca máxima: {frequencia_cardiaca_max3} bpm")
print("-" * 60)

# Relatório Final
print("RELATÓRIO GERAL DA ACADEMIA:")
print(f"Total de alunos cadastrados: {total_alunos}")
print(f"Idade média: {soma_idades / total_alunos:.1f} anos")
print(f"IMC médio: {soma_imc / total_alunos:.2f}")
print(f"Aluno mais pesado: {aluno_mais_pesado} ({maior_peso} kg)")

peso_total = peso1 + peso2 + peso3
print(f"Peso médio: {peso_total / total_alunos:.1f} kg")

altura_media = (altura1 + altura2 + altura3) / 3
print(f"Altura média: {altura_media:.2f} m")

treinos_total = treinos_semana1 + treinos_semana2 + treinos_semana3
print(f"Média de treinos por semana: {treinos_total / total_alunos:.1f}")

print("Distribuição de objetivos:")
objetivos = [objetivo1, objetivo2, objetivo3]
print(f"- Perder peso: {objetivos.count('perder_peso')} aluno(s)")
print(f"- Ganhar massa: {objetivos.count('ganhar_massa')} aluno(s)")
print(f"- Manter: {objetivos.count('manter')} aluno(s)")

print("Distribuição de experiência:")
experiencias = [experiencia1, experiencia2, experiencia3]
print(f"- Iniciante: {experiencias.count('iniciante')} aluno(s)")
print(f"- Intermediário: {experiencias.count('intermediario')} aluno(s)")
print(f"- Avançado: {experiencias.count('avancado')} aluno(s)")
