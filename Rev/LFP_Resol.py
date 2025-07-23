"""
=============================
LISTA DE EXERCÍCIOS – FUNÇÕES E PROCEDIMENTOS
=============================
Aluno:
Linguagem: Python
"""

# =============================
# 1. INTRODUÇÃO A FUNÇÕES E PROCEDIMENTOS
# =============================


def ex1():
    """
    Exercício 1:
    Crie um procedimento que exiba a frase:
    "Bem-vindo ao mundo das funções!"
    """
    print("Bem-vindo ao mundo das funções!")


def ex2():
    """
    Exercício 2:
    Crie uma função que retorne a string:
    "Olá, mundo!"
    """
    return "Olá, mundo!"


def ex3(nome):
    """
    Exercício 3:
    Crie um procedimento que exiba o nome do aluno.
    Parâmetro:
      - nome (str): nome do aluno
    """
    print(f"Nome do aluno: {nome}")


def ex4():
    """
    Exercício 4:
    Crie uma função que retorne um número fixo, por exemplo 10.
    """
    return 10


def ex5():
    """
    Exercício 5:
    Crie um procedimento que exiba três mensagens diferentes em linhas separadas.
    """
    print("Mensagem 1: Aprender a diferencias funções e procedimentos é importante!")
    print("Mensagem 2: Funções tornam o código reutilizável.")
    print("Mensagem 3: Procedimentos tornam o codigo mais limpo.")


# =============================
# 2. INTRODUÇÃO AOS PARÂMETROS DE FUNÇÕES
# =============================

def ex6(a, b):
    """
    Exercício 6:
    Crie uma função que receba dois números e retorne a soma deles.
    Parâmetros:
      - a (int ou float)
      - b (int ou float)
    """
    soma = a + b
    return soma


def ex7(nome):
    """
    Exercício 7:
    Crie um procedimento que receba um nome e exiba a saudação:
    "Olá, [nome]! Seja bem-vindo!"
    """
    print(f"Olá {nome}! Seja bem-vindo!")


def ex8(base, altura):
    """
    Exercício 8:
    Crie uma função que calcule a área de um retângulo.
    Fórmula: base * altura
    """
    return base * altura


# =============================
# 3. FUNÇÕES UTILIZANDO ALGORITMOS DO 1º SEMESTRE
# =============================

def ex9(numero):
    """
    Exercício 9:
    Crie uma função que receba um número e retorne se ele é par ou ímpar.
    Retorno:
      - "Par" ou "Ímpar"
    """
    return "Par" if numero % 2 == 0 else "Ímpar"


def ex10(n1, n2, n3):
    """
    Exercício 10:
    Crie uma função que calcule a média de três notas.
    Retorno:
      - Média aritmética
    """
    return (n1 + n2 + n3) / 3


def ex11(a, b, c):
    """
    Exercício 11:
    Crie uma função que retorne o maior de três números.
    """
    return max(a, b, c)


def ex12(celsius):
    """
    Exercício 12:
    Crie uma função que converta graus Celsius em Fahrenheit.
    Fórmula: F = C * 9/5 + 32
    """
    return celsius * 9/5 + 32


def ex13(lista):
    """
    Exercício 13:
    Crie uma função que receba uma lista de números e retorne a soma deles.
    """
    return sum(lista)


def ex14(lista):
    """
    Exercício 14:
    Crie uma função que retorne a quantidade de números pares em uma lista.
    """
    return sum(1 for n in lista if n % 2 == 0)


# =============================
# 4. FUNÇÕES CLÁSSICAS COM ESTRUTURAS DE REPETIÇÃO
# =============================

def ex15(base, expoente):
    """
    Exercício 15:
    Crie uma função que calcule a potência de um número (base^expoente)
    usando estrutura de repetição.
    Parâmetros:
      - base (int ou float): o número base
      - expoente (int): o expoente (deve ser não-negativo)
    Retorno:
      - Resultado da potenciação
    """
    resultado = 1
    for i in range(expoente):
        resultado *= base
    return resultado


def ex16(numero, digito):
    """
    Exercício 16:
    Crie uma função que conte quantas vezes um dígito específico aparece em um número.
    Use estrutura de repetição para percorrer os dígitos.
    Parâmetros:
      - numero (int): o número para analisar
      - digito (int): o dígito a ser contado (0-9)
    Retorno:
      - int: quantidade de vezes que o dígito aparece
    """
    contador = 0
    numero_str = str(abs(numero))
    digito_str = str(digito)

    for d in numero_str:
        if d == digito_str:
            contador += 1

    return contador


def ex17(numero):
    """
    Exercício 17:
    Crie uma função que retorne a soma dos dígitos de um número.
    Exemplo: 123 -> 1 + 2 + 3 = 6
    """
    return sum(int(digito) for digito in str(abs(numero)))


def ex18(numero):
    """
    Exercício 18:
    Crie uma função que calcule o fatorial de um número.
    O fatorial de n (n!) é o produto de todos os números inteiros positivos menores ou iguais a n.
    Exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120
    Parâmetro:
      - numero (int): número para calcular o fatorial (deve ser não-negativo)
    Retorno:
      - int: o fatorial do número
    """
    if numero < 0:
        return None  # Fatorial não existe para números negativos
    elif numero == 0 or numero == 1:
        return 1

    fatorial = 1
    for i in range(2, numero + 1):
        fatorial *= i

    return fatorial


def ex19(lista):
    """
    Exercício 19:
    Crie uma função que receba uma lista e retorne outra lista ordenada.
    Utilize um algoritmo simples de ordenação (ex.: Bubble Sort).
    """
    lista_ordenada = lista.copy()
    for i in range(len(lista_ordenada)):
        for j in range(0, len(lista_ordenada) - i - 1):
            if lista_ordenada[j] > lista_ordenada[j + 1]:
                lista_ordenada[j], lista_ordenada[j +
                                                  1] = lista_ordenada[j + 1], lista_ordenada[j]
    return lista_ordenada


def ex20(valor):
    """
    Exercício 20:
    Crie uma função que inverta uma string ou lista.
    """
    return valor[::-1]
