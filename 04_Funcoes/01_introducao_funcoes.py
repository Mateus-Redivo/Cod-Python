# O que sao funcoes e por que usar

# Imagine que voce precisa calcular a media de notas em varios momentos do programa.
# Sem funcao, voce repete o mesmo calculo toda vez:

notas1 = [7, 8, 9]
media1 = sum(notas1) / len(notas1)
print(f"Media turma 1: {media1}")

notas2 = [6, 5, 8]
media2 = sum(notas2) / len(notas2)
print(f"Media turma 2: {media2}")

# Se a formula mudar, voce precisa alterar em varios lugares.
# Com funcao, voce escreve uma vez e chama quando precisar:


def calcular_media(notas):
    return sum(notas) / len(notas)


print(f"Media turma 1: {calcular_media([7, 8, 9])}")
print(f"Media turma 2: {calcular_media([6, 5, 8])}")


# Estrutura basica de uma funcao
# def nome_da_funcao(parametros):
#     corpo da funcao
#     return resultado (opcional)


# Funcao sem parametros e sem retorno
def saudar():
    print("Ola! Bem-vindo ao programa.")

saudar()


# Funcao sem retorno (so executa uma acao)
def mostrar_linha():
    print("-" * 30)

mostrar_linha()
print("Titulo")
mostrar_linha()


# Funcao com parametro
def saudar_usuario(nome):
    print(f"Ola, {nome}!")

saudar_usuario("Ana")
saudar_usuario("Carlos")


# Funcao com retorno
def dobrar(numero):
    return numero * 2

resultado = dobrar(5)
print(resultado)       # 10
print(dobrar(12))      # 24


# Voce pode usar o retorno em uma expressao
total = dobrar(3) + dobrar(4)
print(total)           # 14


# Funcao chamando outra funcao
def calcular_area_quadrado(lado):
    return lado * lado

def calcular_area_retangulo(largura, altura):
    return largura * altura

def mostrar_areas(lado, largura, altura):
    print(f"Area do quadrado: {calcular_area_quadrado(lado)}")
    print(f"Area do retangulo: {calcular_area_retangulo(largura, altura)}")

mostrar_areas(4, 5, 3)
