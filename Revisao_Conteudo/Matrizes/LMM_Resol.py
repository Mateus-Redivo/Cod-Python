import random

# =============================
# 1. OPERAÇÕES BÁSICAS COM MATRIZES
# =============================


def ex1():
    """
    Exercício 1:
    Crie uma matriz 2x3 preenchida com zeros e exiba-a.
    Dica: Use list comprehension ou loops aninhados
    """
    return [[0 for _ in range(3)] for _ in range(2)]


def ex2(matriz_a, matriz_b):
    """
    Exercício 2:
    Crie uma função que some duas matrizes de mesma dimensão.
    Parâmetros:
      - matriz_a (list): primeira matriz
      - matriz_b (list): segunda matriz
    Retorno:
      - list: matriz resultante da soma
    """
    return [[matriz_a[i][j] + matriz_b[i][j] for j in range(len(matriz_a[0]))] for i in range(len(matriz_a))]


def ex3(matriz, escalar):
    """
    Exercício 3:
    Crie uma função que multiplique todos os elementos de uma matriz por um escalar.
    Parâmetros:
      - matriz (list): matriz a ser multiplicada
      - escalar (int/float): número multiplicador
    Retorno:
      - list: matriz resultante
    """
    return [[elem * escalar for elem in linha] for linha in matriz]


def ex4(matriz):
    """
    Exercício 4:
    Crie uma função que calcule a transposta de uma matriz.
    A transposta troca linhas por colunas.
    Parâmetro:
      - matriz (list): matriz original
    Retorno:
      - list: matriz transposta
    """
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]


def ex5(matriz):
    """
    Exercício 5:
    Crie uma função que gere uma matriz espelhada horizontalmente.
    (Inverte a ordem das colunas)
    Parâmetro:
      - matriz (list): matriz original
    Retorno:
      - list: matriz espelhada
    """
    return [linha[::-1] for linha in matriz]

# =============================
# 2. ANÁLISE DE MATRIZES
# =============================


def ex6(matriz):
    """
    Exercício 6:
    Crie uma função que encontre o maior e menor valor de uma matriz,
    sem usar as funções max() e min().
    Parâmetro:
      - matriz (list): matriz para análise
    Retorno:
      - tuple: (menor_valor, maior_valor)
    """
    menor = matriz[0][0]
    maior = matriz[0][0]
    for linha in matriz:
        for elem in linha:
            if elem < menor:
                menor = elem
            if elem > maior:
                maior = elem
    return menor, maior


def ex7(matriz):
    """
    Exercício 7:
    Crie uma função que calcule a soma da diagonal principal de uma matriz quadrada.
    Parâmetro:
      - matriz (list): matriz quadrada
    Retorno:
      - int/float: soma da diagonal principal
    """
    return sum(matriz[i][i] for i in range(len(matriz)))


def ex8(matriz):
    """
    Exercício 8:
    Crie uma função que calcule a soma da diagonal secundária de uma matriz quadrada.
    Parâmetro:
      - matriz (list): matriz quadrada
    Retorno:
      - int/float: soma da diagonal secundária
    """
    n = len(matriz)
    return sum(matriz[i][n - 1 - i] for i in range(n))


def ex9(matriz):
    """
    Exercício 9:
    Crie uma função que retorne o maior valor de cada linha da matriz.
    Parâmetro:
      - matriz (list): matriz para análise
    Retorno:
      - list: lista com os maiores valores de cada linha
    """
    return [max(linha) for linha in matriz]


def ex10(matriz):
    """
    Exercício 10:
    Crie uma função que conte quantos números pares existem na matriz.
    Parâmetro:
      - matriz (list): matriz para análise
    Retorno:
      - int: quantidade de números pares
    """
    return sum(1 for linha in matriz for elem in linha if elem % 2 == 0)

# =============================
# 3. MATRIZES COM DADOS ALEATÓRIOS
# =============================


def ex11(linhas, colunas, min_val, max_val):
    """
    Exercício 11:
    Crie uma função que gere uma matriz com números aleatórios.
    Parâmetros:
      - linhas (int): número de linhas
      - colunas (int): número de colunas
      - min_val (int): valor mínimo dos números
      - max_val (int): valor máximo dos números
    Retorno:
      - list: matriz com números aleatórios
    """
    return [[random.randint(min_val, max_val) for _ in range(colunas)] for _ in range(linhas)]


def ex12(tamanho):
    """
    Exercício 12:
    Crie uma função que gere uma matriz identidade (diagonal principal = 1, resto = 0).
    Parâmetro:
      - tamanho (int): dimensão da matriz quadrada
    Retorno:
      - list: matriz identidade
    """
    return [[1 if i == j else 0 for j in range(tamanho)] for i in range(tamanho)]


def ex13(matriz):
    """
    Exercício 13:
    Crie uma função que verifique se uma matriz é simétrica.
    Uma matriz é simétrica se A[i][j] = A[j][i] para todos i,j.
    Parâmetro:
      - matriz (list): matriz quadrada para verificar
    Retorno:
      - bool: True se for simétrica, False caso contrário
    """
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

# =============================
# 4. MANIPULAÇÃO DE STRINGS
# =============================


def ex14(texto1, texto2):
    """
    Exercício 14:
    Crie uma função que compare duas strings ignorando maiúsculas/minúsculas.
    Parâmetros:
      - texto1 (str): primeira string
      - texto2 (str): segunda string
    Retorno:
      - bool: True se forem iguais (ignorando case), False caso contrário
    """
    return texto1.lower() == texto2.lower()


def ex15(texto, palavra):
    """
    Exercício 15:
    Crie uma função que conte quantas vezes uma palavra aparece em um texto.
    Parâmetros:
      - texto (str): texto para buscar
      - palavra (str): palavra a ser contada
    Retorno:
      - int: número de ocorrências
    """
    return texto.lower().split().count(palavra.lower())


def ex16(texto):
    """
    Exercício 16:
    Crie uma função que remova espaços extras de uma string
    (início, fim e espaços duplos no meio).
    Parâmetro:
      - texto (str): texto a ser limpo
    Retorno:
      - str: texto limpo
    """
    return " ".join(texto.strip().split())


def ex17(texto, char_antigo, char_novo):
    """
    Exercício 17:
    Crie uma função que substitua todos os caracteres de um tipo por outro.
    Parâmetros:
      - texto (str): texto original
      - char_antigo (str): caractere a ser substituído
      - char_novo (str): caractere substituto
    Retorno:
      - str: texto com substituições
    """
    return texto.replace(char_antigo, char_novo)


def ex18(lista_palavras):
    """
    Exercício 18:
    Crie uma função que junte uma lista de palavras em uma única string,
    separadas por espaços.
    Parâmetro:
      - lista_palavras (list): lista de strings
    Retorno:
      - str: string única com palavras separadas por espaço
    """
    return " ".join(lista_palavras)

# =============================
# 5. SISTEMAS DE DADOS (DICIONÁRIOS E LISTAS)
# =============================


def ex19():
    """
    Exercício 19:
    Crie uma função que inicialize um dicionário vazio para armazenar
    dados de alunos (nome como chave, lista de notas como valor).
    Retorno:
      - dict: dicionário vazio para alunos
    """
    return {}


def ex20(banco_dados, nome, notas):
    """
    Exercício 20:
    Crie uma função que adicione um aluno e suas notas ao banco de dados.
    Parâmetros:
      - banco_dados (dict): dicionário de alunos
      - nome (str): nome do aluno
      - notas (list): lista de notas do aluno
    Retorno:
      - bool: True se adicionado com sucesso
    """
    banco_dados[nome] = notas
    return True


def ex21(notas):
    """
    Exercício 21:
    Crie uma função que calcule a média de uma lista de notas.
    Parâmetro:
      - notas (list): lista de notas
    Retorno:
      - float: média das notas
    """
    return sum(notas) / len(notas) if notas else 0


def ex22(banco_dados, nome):
    """
    Exercício 22:
    Crie uma função que busque um aluno no banco de dados e retorne suas notas.
    Parâmetros:
      - banco_dados (dict): dicionário de alunos
      - nome (str): nome do aluno a buscar
    Retorno:
      - list ou None: lista de notas do aluno ou None se não encontrado
    """
    return banco_dados.get(nome)


def ex23(produtos):
    """
    Exercício 23:
    Crie uma função que calcule o valor total do estoque.
    Cada produto é uma lista: [nome, preço, quantidade]
    Parâmetro:
      - produtos (list): lista de produtos
    Retorno:
      - float: valor total do estoque
    """
    return sum(preco * quantidade for _, preco, quantidade in produtos)


def ex24(produtos, nome_produto):
    """
    Exercício 24:
    Crie uma função que encontre um produto pelo nome na lista de produtos.
    Parâmetros:
      - produtos (list): lista de produtos
      - nome_produto (str): nome do produto a buscar
    Retorno:
      - list ou None: dados do produto ou None se não encontrado
    """
    for produto in produtos:
        if produto[0].lower() == nome_produto.lower():
            return produto
    return None


def ex25(produtos, nome_produto, novo_preco):
    """
    Exercício 25:
    Crie uma função que atualize o preço de um produto específico.
    Parâmetros:
      - produtos (list): lista de produtos
      - nome_produto (str): nome do produto
      - novo_preco (float): novo preço do produto
    Retorno:
      - bool: True se atualizado com sucesso, False se produto não encontrado
    """
    for produto in produtos:
        if produto[0].lower() == nome_produto.lower():
            produto[1] = novo_preco
            return True
    return False

# =============================
# 6. EXERCÍCIOS INTEGRADOS
# =============================


def ex26(matriz):
    """
    Exercício 26:
    Crie uma função que receba uma matriz e retorne um dicionário com:
    - 'soma_total': soma de todos os elementos
    - 'maior': maior elemento
    - 'menor': menor elemento
    - 'media': média de todos os elementos
    Parâmetro:
      - matriz (list): matriz para análise
    Retorno:
      - dict: dicionário com estatísticas
    """
    valores = [elem for linha in matriz for elem in linha]
    return {
        "soma_total": sum(valores),
        "maior": max(valores),
        "menor": min(valores),
        "media": sum(valores) / len(valores)
    }


def ex27(texto):
    """
    Exercício 27:
    Crie uma função que analise um texto e retorne um dicionário com:
    - 'caracteres': total de caracteres
    - 'palavras': total de palavras
    - 'linhas': total de linhas
    - 'vogais': total de vogais
    Parâmetro:
      - texto (str): texto para análise
    Retorno:
      - dict: dicionário com estatísticas do texto
    """
    vogais = "aeiouAEIOU"
    return {
        "caracteres": len(texto),
        "palavras": len(texto.split()),
        "linhas": texto.count("\n") + 1,
        "vogais": sum(1 for c in texto if c in vogais)
    }


def ex28(lista_numeros, colunas):
    """
    Exercício 28:
    Crie uma função que organize uma lista de números em uma matriz 
    onde cada linha tenha um tamanho específico.
    Parâmetros:
      - lista_numeros (list): lista de números
      - colunas (int): número de colunas da matriz
    Retorno:
      - list: matriz organizada
    """
    return [lista_numeros[i:i+colunas] for i in range(0, len(lista_numeros), colunas)]


def ex29(matriz_vendas, produtos):
    """
    Exercício 29:
    Crie uma função que processe dados de vendas.
    A matriz_vendas contém vendas por dia e produto.
    A lista produtos contém os nomes dos produtos.
    Retorne o produto com maior total de vendas.
    Parâmetros:
      - matriz_vendas (list): matriz com vendas [dia][produto]
      - produtos (list): lista com nomes dos produtos
    Retorno:
      - str: nome do produto com maior total de vendas
    """
    totais = [sum(vendas[i] for vendas in matriz_vendas)
              for i in range(len(produtos))]
    return produtos[totais.index(max(totais))]


def ex30():
    """
    Exercício 30:
    Crie um menu interativo que permita:
    1. Criar matriz
    2. Exibir matriz
    3. Calcular soma das diagonais
    4. Encontrar maior e menor valor
    5. Transpor matriz
    6. Sair

    Implemente todas as funcionalidades usando as funções criadas anteriormente.
    """
    matriz = []
    while True:
        print("\n1. Criar matriz\n2. Exibir matriz\n3. Soma das diagonais\n4. Maior e menor valor\n5. Transpor matriz\n6. Sair")
        op = input("Escolha: ")
        if op == "1":
            linhas = int(input("Linhas: "))
            colunas = int(input("Colunas: "))
            matriz = [[int(input(f"Elemento [{i}][{j}]: "))
                       for j in range(colunas)] for i in range(linhas)]
        elif op == "2":
            print("Matriz:", matriz)
        elif op == "3":
            if len(matriz) == len(matriz[0]):
                print("Soma diagonais:", ex7(matriz) + ex8(matriz))
            else:
                print("A matriz não é quadrada!")
        elif op == "4":
            print("Maior e menor:", ex6(matriz))
        elif op == "5":
            print("Transposta:", ex4(matriz))
        elif op == "6":
            break
        else:
            print("Opção inválida!")
