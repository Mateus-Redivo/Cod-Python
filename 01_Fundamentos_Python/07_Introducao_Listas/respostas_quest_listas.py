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

media = total / len(precos)
print(f"Média: R$ {media:.2f}")  # c) Imprimir média

# ─────────────────────────────────────────
# QUESTÃO 7 — Índices e acesso avançado
# ─────────────────────────────────────────

cores = ["vermelho", "azul", "verde", "amarelo", "branco", "preto"]

print(cores[-2])  # a) Penúltimo elemento usando índice negativo
print(cores[1], cores[3])  # b) Segundo e quarto elemento usando índices positivos
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


# ─────────────────────────────────────────
# QUESTÃO 14 — TEORIA: Verdadeiro ou Falso
# ─────────────────────────────────────────

# a) FALSA — O índice do primeiro elemento é 0, não 1.
# b) VERDADEIRA — O índice -1 sempre se refere ao último elemento.
# c) FALSA — len() retorna o número de elementos da lista, não o maior valor.


# ─────────────────────────────────────────
# QUESTÃO 15 — ANÁLISE DE CÓDIGO
# ─────────────────────────────────────────

# animais = ["gato", "cachorro", "peixe", "pássaro", "hamster"]
# print(animais[1])   → cachorro
# print(animais[-2])  → pássaro
# print(len(animais)) → 5

# a) animais[1] exibe: cachorro
#    animais[-2] exibe: pássaro
#    len(animais) exibe: 5
# b) Após animais.append("tartaruga"), o novo len(animais) será 6.
# c) "cachorro" está no índice 1; o índice negativo equivalente é -4.


# ─────────────────────────────────────────
# QUESTÃO 16 — ANÁLISE DE CÓDIGO: slicing
# ─────────────────────────────────────────

# numeros = [10, 20, 30, 40, 50, 60, 70, 80]

# a) numeros[2:5]  → [30, 40, 50]
# b) numeros[:3]   → [10, 20, 30]
# c) numeros[5:]   → [60, 70, 80]


# ─────────────────────────────────────────
# QUESTÃO 17 — TEORIA: Lacunas conceituais
# ─────────────────────────────────────────

# a) x[1]
# b) count()
# c) index()


# ─────────────────────────────────────────
# QUESTÃO 18 — ANÁLISE DE CÓDIGO: for
# ─────────────────────────────────────────

# valores = [3, 7, 2, 9, 5, 1, 8]
# a) Elementos maiores que 4: 7, 9, 5, 8
# b) print(total)    → 29  (7 + 9 + 5 + 8)
# c) print(contador) → 4


# ─────────────────────────────────────────
# QUESTÃO 19 — Prática: construção com for e append
# ─────────────────────────────────────────

quadrados = []
for n in range(1, 11):
    quadrados.append(n ** 2)
print(quadrados)


# ─────────────────────────────────────────
# QUESTÃO 20 — Prática: filtragem com for
# ─────────────────────────────────────────

temperaturas = [36.5, 37.0, 38.2, 35.9, 39.1, 36.8, 40.0, 37.5]

normais = 0
total_temp = 0
for temp in temperaturas:
    if temp > 37.5:
        print(f"Febre alta: {temp}°C")  # a)
    else:
        normais += 1                    # b)
    total_temp += temp

print(f"Temperaturas normais (abaixo de 37.5): {normais}")  # b)
print(f"Temperatura média: {total_temp / len(temperaturas):.2f}°C")  # c)


# ─────────────────────────────────────────
# QUESTÃO 21 — ANÁLISE DE CÓDIGO: append e for
# ─────────────────────────────────────────

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# resultado = []
# for n in numeros:
#     if n % 3 == 0:
#         resultado.append(n)

# a) resultado contém: [3, 6, 9]
# b) len(resultado) → 3
# c) Critério: números divisíveis por 3 (resto da divisão por 3 igual a 0)


# ─────────────────────────────────────────
# QUESTÃO 22 — Prática: índices e modificação
# ─────────────────────────────────────────

notas = [5, 7, 4, 9, 6, 3, 8, 7]

notas[0] = 6     # a) Substitui a primeira nota por 6
notas[-1] = 10   # b) Substitui a última nota por 10
print(notas[len(notas) // 2])  # c) Nota do meio (índice 4 → valor 6)


# ─────────────────────────────────────────
# QUESTÃO 23 — TEORIA: corrija os erros
# ─────────────────────────────────────────

# a) lista[3] causa IndexError pois o último índice válido é 2.
#    Correção: print(lista[2])  ou  print(lista[-1])

# b) frutas.append["uva"] usa colchetes em vez de parênteses.
#    Correção: frutas.append("uva")

# c) len[nomes] usa colchetes em vez de parênteses.
#    Correção: print(len(nomes))


# ─────────────────────────────────────────
# QUESTÃO 24 — Prática: count() e index() com lógica
# ─────────────────────────────────────────

respostas = ["A", "B", "A", "C", "A", "B", "D", "A", "C", "B"]

qtd_a = respostas.count("A")
qtd_b = respostas.count("B")
qtd_c = respostas.count("C")
qtd_d = respostas.count("D")

print(f"A: {qtd_a} vez(es)")  # a)
print(f"B: {qtd_b} vez(es)")
print(f"C: {qtd_c} vez(es)")
print(f"D: {qtd_d} vez(es)")

contagens = {"A": qtd_a, "B": qtd_b, "C": qtd_c, "D": qtd_d}
mais_marcada = max(contagens, key=contagens.get)
print(f'Alternativa mais marcada: {mais_marcada}')  # b)

print(f'Primeira resposta "D" no índice: {respostas.index("D")}')  # c)


# ─────────────────────────────────────────
# QUESTÃO 25 — ANÁLISE DE CÓDIGO: slicing com passo
# ─────────────────────────────────────────

# letras = ["a", "b", "c", "d", "e", "f", "g", "h"]
# índices:   0    1    2    3    4    5    6    7

# a) letras[1::2]   → ['b', 'd', 'f', 'h']  (começa no 1, passo 2)
#    letras[::3]    → ['a', 'd', 'g']         (começa no 0, passo 3)
#    letras[6:1:-2] → ['g', 'e', 'c']         (começa no 6, para antes de 1, passo -2)

# b) O passo negativo indica que a lista é percorrida de trás para frente,
#    ou seja, os índices diminuem a cada passo.

# c) O índice 1 é o limite de parada (exclusivo). Com passo -2 partindo do 6:
#    6 → 4 → 2 → o próximo seria 0, mas 0 < 1 não satisfaz stop=1, então para no 2.


# ─────────────────────────────────────────
# QUESTÃO 26 — Prática: for com range(len())
# ─────────────────────────────────────────

produtos = ["Arroz", "Feijão", "Macarrão", "Óleo", "Sal"]
precos = [5.49, 8.90, 3.25, 6.70, 2.10]

total_compra = 0
for i in range(len(produtos)):
    print(f"{i+1}. {produtos[i]} — R$ {precos[i]:.2f}")  # a)
    total_compra += precos[i]

print(f"Total da compra: R$ {total_compra:.2f}")  # b)

indice_barato = precos.index(min(precos))
print(f"Produto mais barato: {produtos[indice_barato]}")  # c)


# ─────────────────────────────────────────
# QUESTÃO 27 — TEORIA: preveja a saída
# ─────────────────────────────────────────

# Bloco A:
#   x = [1, 2, 3, 4, 5]
#   print(x[len(x) - 1])  → x[4] → 5

# Bloco B:
#   y = ["sol", "lua", "estrela", "cometa"]  (após append)
#   print(y[-2])  → estrela

# Bloco C:
#   print(z.count(30))  → 1
#   print(z.index(40))  → 3


# ─────────────────────────────────────────
# QUESTÃO 28 — Desafio: votação
# ─────────────────────────────────────────

candidatos = ["Alice", "Bruno", "Carla"]
votos = []

for i in range(8):
    nome = input(f"Voto {i+1} — Digite um nome: ")
    if nome in candidatos:
        votos.append(nome)
    else:
        print("Voto inválido!")

for candidato in candidatos:
    print(f"{candidato}: {votos.count(candidato)} voto(s)")  # b)

vencedor = candidatos[0]
for candidato in candidatos[1:]:
    if votos.count(candidato) > votos.count(vencedor):
        vencedor = candidato

print(f"Vencedor: {vencedor}")  # c)