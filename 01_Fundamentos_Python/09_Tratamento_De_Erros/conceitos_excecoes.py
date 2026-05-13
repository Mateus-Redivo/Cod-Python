# O que sao excecoes

# Quando um programa encontra algo inesperado durante a execucao, ele levanta
# uma excecao. Sem tratamento, o programa para e mostra uma mensagem de erro.

# Exemplo de erro sem tratamento:
numero = int("abc")   # ValueError: nao da para converter "abc" em int

# O Python interrompe o programa aqui. Com try/except, a gente controla isso.


# Estrutura basica
try:
    # codigo que pode dar erro
    resultado = 10 / 0
except ZeroDivisionError:
    # o que fazer quando o erro acontece
    print("Nao e possivel dividir por zero.")


# Capturando o erro para ver a mensagem original
try:
    numero = int("abc")
except ValueError as erro:
    print(f"Erro: {erro}")


# Tratando mais de um tipo de erro
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("O divisor nao pode ser zero.")
    except TypeError:
        print("Os valores precisam ser numeros.")

dividir(10, 0)
dividir(10, "dois")


# else: executado quando nao ocorre nenhum erro
try:
    numero = int("42")
except ValueError:
    print("Valor invalido.")
else:
    print(f"Conversao bem-sucedida: {numero}")


# finally: executado sempre, independente de erro ou nao
# Util para fechar arquivos, conexoes, etc.
try:
    resultado = 10 / 2
except ZeroDivisionError:
    print("Divisao por zero.")
finally:
    print("Este bloco sempre executa.")


# Capturando qualquer excecao (use com cuidado)
try:
    lista = [1, 2, 3]
    print(lista[10])
except Exception as erro:
    print(f"Algo deu errado: {type(erro).__name__} - {erro}")
