# Excecoes comuns do Python
# Conhecer os tipos de erro mais frequentes ajuda a tratar cada caso corretamente.


# ValueError: o tipo esta certo, mas o valor nao faz sentido
try:
    numero = int("abc")
except ValueError:
    print("ValueError: nao foi possivel converter o valor.")

# Acontece muito quando o usuario digita algo que nao e numero:
entrada = input("Digite um numero: ")
try:
    numero = int(entrada)
    print(f"Voce digitou: {numero}")
except ValueError:
    print("Isso nao e um numero valido.")


# TypeError: operacao aplicada no tipo errado
try:
    resultado = "10" + 5
except TypeError:
    print("TypeError: nao da para somar texto com numero diretamente.")

# Correto:
resultado = int("10") + 5


# IndexError: tentativa de acessar uma posicao que nao existe na lista
lista = [10, 20, 30]
try:
    print(lista[5])
except IndexError:
    print("IndexError: esse indice nao existe na lista.")


# KeyError: tentativa de acessar uma chave que nao existe no dicionario
dados = {"nome": "Ana", "idade": 25}
try:
    print(dados["email"])
except KeyError:
    print("KeyError: a chave 'email' nao existe no dicionario.")


# ZeroDivisionError: divisao por zero
try:
    resultado = 100 / 0
except ZeroDivisionError:
    print("ZeroDivisionError: divisao por zero.")


# FileNotFoundError: arquivo nao encontrado (antecipacao para quando ver arquivos)
try:
    with open("arquivo_que_nao_existe.txt", "r") as f:
        conteudo = f.read()
except FileNotFoundError:
    print("FileNotFoundError: o arquivo nao foi encontrado.")


# AttributeError: tentativa de usar um metodo que o tipo nao tem
try:
    numero = 42
    numero.upper()
except AttributeError:
    print("AttributeError: numeros nao tem o metodo upper().")


# Resumo dos mais comuns:
excecoes_comuns = {
    "ValueError":       "valor invalido para a operacao",
    "TypeError":        "tipo de dado errado",
    "IndexError":       "indice fora do range da lista",
    "KeyError":         "chave nao existe no dicionario",
    "ZeroDivisionError":"divisao por zero",
    "FileNotFoundError":"arquivo nao encontrado",
    "AttributeError":   "metodo ou atributo inexistente no tipo",
}

for excecao, descricao in excecoes_comuns.items():
    print(f"{excecao}: {descricao}")
