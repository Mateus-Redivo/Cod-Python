# Parametros, argumentos e retorno


# Parametro e o nome que a funcao usa internamente.
# Argumento e o valor que voce passa ao chamar a funcao.

def cumprimentar(nome):       # 'nome' e o parametro
    print(f"Ola, {nome}!")

cumprimentar("Ana")           # "Ana" e o argumento
cumprimentar("Carlos")


# Multiplos parametros
def somar(a, b):
    return a + b

print(somar(3, 5))            # 8
print(somar(10, 20))          # 30


# Valor padrao: parametro opcional com valor ja definido
def exibir_produto(nome, preco, desconto=0):
    preco_final = preco * (1 - desconto)
    print(f"{nome}: R$ {preco_final:.2f}")

exibir_produto("Caneta", 3.50)               # sem desconto
exibir_produto("Caderno", 20.00, 0.10)       # 10% de desconto


# Argumento nomeado: voce pode passar em qualquer ordem usando o nome
def registrar_aluno(nome, nota, turma):
    print(f"{nome} | Turma {turma} | Nota {nota}")

registrar_aluno("Maria", turma="A", nota=8.5)


# Retorno de multiplos valores (Python retorna uma tupla)
def calcular_min_max(lista):
    return min(lista), max(lista)

minimo, maximo = calcular_min_max([4, 1, 9, 2, 7])
print(f"Minimo: {minimo} | Maximo: {maximo}")


# Funcao pode retornar cedo com return (equivale a um if de saida)
def dividir(a, b):
    if b == 0:
        print("Divisao por zero nao permitida.")
        return None
    return a / b

print(dividir(10, 2))
print(dividir(10, 0))


# Boas praticas
# - Uma funcao deve fazer uma coisa so
# - O nome deve descrever o que ela faz (verbo + substantivo)
# - Prefira retornar valores a imprimir dentro da funcao
#   (facilita reutilizar o resultado)

# Ruim: funcao que mistura calculo e exibicao
def calcular_e_mostrar_area(base, altura):
    area = base * altura
    print(f"Area: {area}")   # dificil de reusar

# Melhor: separa calculo de exibicao
def calcular_area(base, altura):
    return base * altura

area = calcular_area(5, 3)
print(f"Area: {area}")
print(f"Dobro da area: {area * 2}")
