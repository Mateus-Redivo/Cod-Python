# ─────────────────────────────────────────
# QUESTÃO 1 — Criação e acesso por índice
# ─────────────────────────────────────────

planetas = ["Mercúrio", "Vênus", "Terra", "Marte", "Júpiter"]

print(planetas[0])    # a) Primeiro planeta
print(planetas[-1])   # b) Último planeta usando índice negativo
print(planetas[2])    # c) Terceiro planeta usando índice positivo

# ─────────────────────────────────────────
# QUESTÃO 2 — Tamanho e verificação de elemento
# ─────────────────────────────────────────

disciplinas = ["Matemática", "Português", "História", "Ciências", "Inglês"]

print(len(disciplinas))  # a) Quantidade de disciplinas

if "Inglês" in disciplinas:  # b) Verificação de "Inglês"
    print("Inglês está na lista.")
else:
    print("Inglês não está na lista.")

if "Filosofia" in disciplinas:  # c) Verificação de "Filosofia"
    print("Filosofia está na lista.")
else:
    print("Filosofia não está na lista.")


# ─────────────────────────────────────────
# QUESTÃO 3 — Modificar e append
# ─────────────────────────────────────────

times = ["Flamengo", "Palmeiras", "Santos"]

times[2] = "Grêmio"  # a) Modificar "Santos" para "Grêmio"
print(times)        # Imprime após a modificação

times.append("Corinthians")  # b) Adicionar "Corinthians"
print(times)                # Imprime após adicionar "Corinthians"


# ─────────────────────────────────────────
# QUESTÃO 4 — count() e index()
# ─────────────────────────────────────────

notas = [7, 8, 6, 10, 8, 9, 6, 8, 5, 10]

print(f"O valor 8 aparece {notas.count(8)} vezes.")  # a) Contar 8
print(f"O valor 6 aparece {notas.count(6)} vezes.")  # b) Contar 6
# c) Índice do primeiro 10
print(f"O primeiro 10 está no índice {notas.index(10)}.")
# d) Índice do primeiro 5
print(f"O primeiro 5 está no índice {notas.index(5)}.")


# ─────────────────────────────────────────
# QUESTÃO 5 — Fatiamento (slicing)
# ─────────────────────────────────────────

meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun",
         "Jul", "Ago", "Set", "Out", "Nov", "Dez"]

print(meses[:3])       # a) 3 primeiros meses
print(meses[-3:])      # b) 3 últimos meses usando índices negativos
print(meses[6:])       # c) Meses do segundo semestre (Jul a Dez)
print(meses[::2])      # d) Meses de índice par usando passo 2

# ─────────────────────────────────────────
# QUESTÃO 6 — Percorrer lista com for
# ─────────────────────────────────────────

precos = [15.90, 8.50, 22.00, 4.75, 31.20]

total = 0
for i in range(len(precos)):
    # a) Imprimir preço formatado
    print(f"Produto {i + 1}: R$ {precos[i]:.2f}")
    total += precos[i]  # b) Acumular total

print(f"Total: R$ {total:.2f}")  # b) Imprimir total

media = total / len(precos)  # c) Calcular média

# ─────────────────────────────────────────
# QUESTÃO 7 — Índices e acesso avançado
# ─────────────────────────────────────────

cores = ["vermelho", "azul", "verde", "amarelo", "branco", "preto"]

print(cores[-2])  # a) Penúltimo elemento usando índice negativo
print(cores[1], cores[3])  # b) Segundo e quarto elemento usando
if "roxo" in cores:  # c) Verificar se "roxo" está na lista
    print("Roxo está na lista.")
else:
    print("Roxo não está na lista.")

print(f"Total de cores: {len(cores)}")  # d) Total de elementos usando len()

# ─────────────────────────────────────────
# QUESTÃO 8 — append() e construção de lista
# ─────────────────────────────────────────

pares = []
for n in range(2, 21, 2):
    pares.append(n)
print(pares)
print(f"Quantidade de elementos: {len(pares)}")


# ─────────────────────────────────────────
# QUESTÃO 9 — count() e index() avançado
# ─────────────────────────────────────────

letras = ["a", "b", "a", "c", "b", "a", "d", "b", "a", "c"]

print(f'"a" aparece {letras.count("a")} vezes.')
print(f'"b" aparece {letras.count("b")} vezes.')
print(f'O primeiro "c" está no índice {letras.index("c")}.')
print(f'O primeiro "d" está no índice {letras.index("d")}.')
if letras.count("a") > letras.count("b"):
    print('"a" aparece mais vezes.')
elif letras.count("a") < letras.count("b"):
    print('"b" aparece mais vezes.')
else:
    print('"a" e "b" aparecem o mesmo número de vezes.')

# ─────────────────────────────────────────
# QUESTÃO 10 — Fatiamento avançado
# ─────────────────────────────────────────

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numeros[:5])        # a) 5 primeiros elementos
print(numeros[-4:])       # b) 4 últimos elementos
print(numeros[2:8])       # c) Índice 2 ao 7 (inclusive)
print(numeros[::2])       # d) Elementos de passo 2 (pares)
print(numeros[::-1])      # e) Lista de trás para frente

# ─────────────────────────────────────────
# QUESTÃO 11 — for com índice e acumulador
# ─────────────────────────────────────────

idades = [14, 23, 17, 31, 19, 25, 16, 28]

for i in range(len(idades)):
    print(f"Pessoa {i+1} tem {idades[i]} anos")
menores_18 = 0
total_idades = 0
for idade in idades:
    if idade < 18:
        menores_18 += 1
    total_idades += idade
print(f"Quantidade de pessoas com menos de 18 anos: {menores_18}")
print(f"Soma das idades: {total_idades}")
print(f"Idade do meio: {idades[len(idades)//2]}")

# ─────────────────────────────────────────
# QUESTÃO 12 — Combinando len(), in e for
# ─────────────────────────────────────────

frutas = ["maçã", "banana", "uva", "manga", "pera", "uva", "banana", "uva"]

print(f"Total de frutas: {len(frutas)}")
if "abacaxi" in frutas:
    print("Abacaxi está na lista.")
else:
    print("Abacaxi não está na lista.")
for fruta in frutas:
    if len(fruta) > 4:
        print(fruta)
print(f'"uva" aparece {frutas.count("uva")} vezes.')
print(f'A primeira "banana" está no índice {frutas.index("banana")}')

# ─────────────────────────────────────────
# QUESTÃO 13 — Desafio: lista dinâmica
# ─────────────────────────────────────────

alunos = []
for i in range(5):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    alunos.append(nome)
print("Lista de alunos:")
for i in range(len(alunos)):
    print(f"{i+1}. {alunos[i]}")
busca = input("Digite um nome para buscar: ")
if busca in alunos:
    print(f"{busca} está na posição {alunos.index(busca)+1} da lista.")
else:
    print(f"{busca} não foi encontrado na lista.")