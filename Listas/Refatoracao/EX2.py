# Problemas: Repetição de código, validação básica inadequada, falta de organização

print("Sistema de Cadastro de Alunos")

nome1 = input("Nome do 1º aluno: ")
if nome1 == "":
    print("Nome inválido")
idade1 = int(input("Idade do 1º aluno: "))
if idade1 < 0:
    print("Idade inválida")
nota1 = float(input("Nota do 1º aluno: "))
if nota1 < 0 or nota1 > 10:
    print("Nota inválida")

nome2 = input("Nome do 2º aluno: ")
if nome2 == "":
    print("Nome inválido")
idade2 = int(input("Idade do 2º aluno: "))
if idade2 < 0:
    print("Idade inválida")
nota2 = float(input("Nota do 2º aluno: "))
if nota2 < 0 or nota2 > 10:
    print("Nota inválida")

nome3 = input("Nome do 3º aluno: ")
if nome3 == "":
    print("Nome inválido")
idade3 = int(input("Idade do 3º aluno: "))
if idade3 < 0:
    print("Idade inválida")
nota3 = float(input("Nota do 3º aluno: "))
if nota3 < 0 or nota3 > 10:
    print("Nota inválida")

print("Alunos cadastrados:")
print(f"{nome1} - {idade1} anos - Nota: {nota1}")
print(f"{nome2} - {idade2} anos - Nota: {nota2}")
print(f"{nome3} - {idade3} anos - Nota: {nota3}")

media = (nota1 + nota2 + nota3) / 3
print(f"Média da turma: {media}")
