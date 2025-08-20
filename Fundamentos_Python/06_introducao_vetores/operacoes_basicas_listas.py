"""
=============================
OPERAÇÕES BÁSICAS COM LISTAS
=============================
Este arquivo demonstra as operações fundamentais com listas
"""

print("=== OPERAÇÕES BÁSICAS COM LISTAS ===")

# =============================
# ADICIONANDO ELEMENTOS
# =============================
print("=== ADICIONANDO ELEMENTOS ===")

# Lista inicial
numeros = [1, 2, 3]
print(f"Lista inicial: {numeros}")

# append() - adiciona no final
numeros.append(4)
print(f"Após append(4): {numeros}")

# insert() - adiciona em posição específica
numeros.insert(0, 0)  # Insere 0 na posição 0
print(f"Após insert(0, 0): {numeros}")

# extend() - adiciona múltiplos elementos
numeros.extend([5, 6, 7])
print(f"Após extend([5, 6, 7]): {numeros}")
print()

# =============================
# REMOVENDO ELEMENTOS
# =============================
print("=== REMOVENDO ELEMENTOS ===")

frutas = ["maçã", "banana", "laranja", "banana", "uva"]
print(f"Lista inicial: {frutas}")

# remove() - remove primeira ocorrência
frutas.remove("banana")  # Remove apenas a primeira banana
print(f"Após remove('banana'): {frutas}")

# pop() - remove por índice e retorna o valor
fruta_removida = frutas.pop(0)  # Remove índice 0
print(f"Fruta removida: {fruta_removida}")
print(f"Lista após pop(0): {frutas}")

# pop() sem parâmetro remove o último
ultima_fruta = frutas.pop()
print(f"Última fruta removida: {ultima_fruta}")
print(f"Lista final: {frutas}")

# del - deleta por índice (não retorna valor)
cores = ["red", "green", "blue", "yellow"]
print(f"Cores antes: {cores}")
del cores[1]  # Remove "green"
print(f"Cores após del cores[1]: {cores}")

# clear() - remove todos os elementos
cores.clear()
print(f"Cores após clear(): {cores}")
print()

# =============================
# PROCURANDO ELEMENTOS
# =============================
print("=== PROCURANDO ELEMENTOS ===")

animais = ["gato", "cachorro", "peixe", "cachorro", "coelho"]
print(f"Lista de animais: {animais}")

# in - verifica se existe
tem_gato = "gato" in animais
print(f"Tem gato na lista? {tem_gato}")

# count() - conta ocorrências
quantidade_cachorro = animais.count("cachorro")
print(f"Quantos cachorros? {quantidade_cachorro}")

# index() - encontra primeira posição
posicao_peixe = animais.index("peixe")
print(f"Posição do peixe: {posicao_peixe}")
print()

# =============================
# ORDENANDO LISTAS
# =============================
print("=== ORDENANDO LISTAS ===")

# Lista com números
valores = [5, 2, 8, 1, 9]
print(f"Valores originais: {valores}")

# sort() - ordena a própria lista
valores.sort()
print(f"Após sort(): {valores}")

# sort(reverse=True) - ordem decrescente
valores.sort(reverse=True)
print(f"Ordem decrescente: {valores}")

# sorted() - retorna nova lista ordenada (não modifica original)
nomes = ["Maria", "Ana", "João", "Carlos"]
print(f"Nomes originais: {nomes}")
nomes_ordenados = sorted(nomes)
print(f"Nomes ordenados: {nomes_ordenados}")
print(f"Lista original: {nomes}")  # Permanece inalterada

# reverse() - inverte a ordem
letras = ["A", "B", "C", "D"]
print(f"Letras originais: {letras}")
letras.reverse()
print(f"Após reverse(): {letras}")
print()

# =============================
# FATIAMENTO (SLICING)
# =============================
print("=== FATIAMENTO DE LISTAS ===")

dias = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
print(f"Dias da semana: {dias}")

# Pegando pedaços da lista
print(f"Primeiros 3 dias: {dias[0:3]}")      # índices 0, 1, 2
print(f"Primeiros 3 dias: {dias[:3]}")       # mesmo resultado
print(f"Últimos 3 dias: {dias[4:]}")         # do índice 4 até o final
print(f"Últimos 3 dias: {dias[-3:]}")        # usando índices negativos
print(f"Dias do meio: {dias[2:5]}")          # índices 2, 3, 4
print(f"Todos os dias: {dias[::]}")          # cópia completa
print()

# =============================
# EXEMPLO PRÁTICO COMPLETO
# =============================
print("=== EXEMPLO: GERENCIADOR DE TAREFAS ===")

# Lista de tarefas
tarefas = []

print("Vamos gerenciar suas tarefas!")
print("Digite 3 tarefas:")

# Adicionando tarefas
for i in range(3):
    tarefa = input(f"Tarefa {i+1}: ")
    tarefas.append(tarefa)

# Mostrando tarefas
print(f"\nSuas tarefas: {tarefas}")
print("Lista numerada:")
for i, tarefa in enumerate(tarefas, 1):
    print(f"  {i}. {tarefa}")

# Removendo uma tarefa
if tarefas:
    print(f"\nVocê tem {len(tarefas)} tarefas.")
    tarefa_concluida = input("Digite uma tarefa concluída para remover: ")

    if tarefa_concluida in tarefas:
        tarefas.remove(tarefa_concluida)
        print(f"SUCESSO: Tarefa '{tarefa_concluida}' removida!")
    else:
        print("ERRO: Tarefa não encontrada.")

# Lista final
print(f"\nTarefas restantes: {tarefas}")
print(f"Total de tarefas pendentes: {len(tarefas)}")
