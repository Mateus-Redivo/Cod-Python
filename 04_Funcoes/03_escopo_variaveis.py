# Escopo de variaveis

# Escopo define onde uma variavel existe e pode ser acessada.
# Em Python, variaveis criadas dentro de uma funcao so existem ali dentro.


# Variavel local: existe apenas dentro da funcao
def calcular_desconto(preco):
    desconto = preco * 0.1        # 'desconto' e local
    return preco - desconto

print(calcular_desconto(100))
# print(desconto)                 # isso causaria NameError


# Cada chamada tem seu proprio espaco de variaveis
def dobrar(numero):
    resultado = numero * 2        # 'resultado' so existe aqui
    return resultado

print(dobrar(5))
print(dobrar(8))


# Variavel global: definida fora de qualquer funcao
# Funcoes podem ler variaveis globais, mas nao alterar sem declarar global

taxa_imposto = 0.15

def calcular_preco_final(preco):
    return preco + preco * taxa_imposto   # le a global sem problema

print(calcular_preco_final(200))


# Tentar modificar uma global sem declarar cria uma local separada
contador = 0

def incrementar():
    contador = contador + 1       # NameError: Python trata como local nao iniciada

# Para modificar uma global, use a palavra 'global'
def incrementar_correto():
    global contador
    contador = contador + 1

incrementar_correto()
incrementar_correto()
print(contador)    # 2


# Evite usar 'global' sempre que possivel.
# O jeito mais limpo e passar o valor como parametro e retornar o novo valor.
def incrementar_limpo(contador):
    return contador + 1

contador = 0
contador = incrementar_limpo(contador)
contador = incrementar_limpo(contador)
print(contador)    # 2


# Variaveis com mesmo nome em escopos diferentes nao se confundem
nome = "global"

def mostrar_nome():
    nome = "local"
    print(nome)   # imprime "local"

mostrar_nome()
print(nome)       # imprime "global" — a global nao foi alterada
