"""
Gabarito — Módulo 11, Exercício 02: Contando operações

Enunciado:
  modulo-11-algoritmos-de-ordenacao/exercicios/EXERCICIO-02-contando-operacoes.md

Como executar:
  python contando_operacoes.py
"""

import random


def bubble_sort(lista):
    lista = lista[:]                # cópia: não estraga o cenário dos outros
    comparacoes = trocas = 0
    n = len(lista)
    for i in range(n):
        for j in range(n - i - 1):
            comparacoes += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1
    return comparacoes, trocas


def selection_sort(lista):
    lista = lista[:]
    comparacoes = trocas = 0
    for i in range(len(lista)):
        menor = i
        for j in range(i + 1, len(lista)):
            comparacoes += 1
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
        trocas += 1                 # troca SEMPRE, mesmo consigo mesmo
    return comparacoes, trocas


def insertion_sort(lista):
    lista = lista[:]
    comparacoes = movimentacoes = 0
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > atual:
            comparacoes += 1
            lista[j + 1] = lista[j]
            movimentacoes += 1
            j -= 1
        if j >= 0:
            comparacoes += 1        # a comparação que fez o while parar
        lista[j + 1] = atual
    return comparacoes, movimentacoes


ALGORITMOS = [("Bubble", bubble_sort),
              ("Selection", selection_sort),
              ("Insertion", insertion_sort)]


def medir(titulo, lista):
    print(f"=== {titulo} ({len(lista)} elementos) ===")
    print(f"{'Algoritmo':<14}{'Comparações':>13}{'Trocas':>9}")
    for nome, funcao in ALGORITMOS:
        comparacoes, trocas = funcao(lista)
        print(f"{nome:<14}{comparacoes:>13}{trocas:>9}")
    print()


embaralhada = [64, 34, 25, 12, 22, 11, 90, 45, 78, 3]

medir("LISTA EMBARALHADA", embaralhada)
medir("JÁ ORDENADA", list(range(1, 11)))
medir("ORDEM INVERSA", list(range(10, 0, -1)))

print("=== CRESCIMENTO (Bubble, embaralhada) ===")
print(f"{'Tamanho':>9}{'Comparações':>15}")
random.seed(1)
for tamanho in [10, 50, 100]:
    aleatoria = [random.randint(1, 999) for _ in range(tamanho)]
    comparacoes, _ = bubble_sort(aleatoria)
    print(f"{tamanho:>9}{comparacoes:>15,}")


# --- Respostas da parte escrita --------------------------------------
#
# a) Por que Bubble e Selection comparam sempre o mesmo tanto?
#
#    Porque os dois comparam TODOS os pares possíveis, sem exceção.
#    Nenhum dos dois tem como parar cedo: o Bubble percorre o trecho
#    não ordenado inteiro em cada passagem, e o Selection precisa ver
#    todos os candidatos antes de afirmar qual é o menor.
#
#    O total é sempre n(n-1)/2. Com n = 10: 10 x 9 / 2 = 45. Bate com
#    a medição, nos TRÊS cenários — inclusive na lista já ordenada,
#    onde o trabalho é completamente inútil.
#
# b) Por que o Insertion compara tão pouco na lista já ordenada?
#
#    Porque a condição do while é "lista[j] > atual". Numa lista
#    ordenada, o elemento anterior nunca é maior que o atual — então o
#    while falha na PRIMEIRA verificação e o laço não roda nenhuma vez.
#
#    Sobra uma comparação por elemento: 9 no total, para 10 elementos.
#    Contra 45 dos outros dois. O Insertion é o único dos três que
#    "percebe" que a lista já está pronta.
#
# c) Por que o Selection troca 10 vezes mesmo já ordenado?
#
#    Porque a troca está FORA do if, no fim de cada passagem. Quando o
#    menor já está na posição certa, ele executa
#    "lista[i], lista[i] = lista[i], lista[i]" — troca o elemento
#    consigo mesmo. Inútil, mas contada.
#
#    Para evitar, basta um if:
#
#        if menor != i:
#            lista[i], lista[menor] = lista[menor], lista[i]
#            trocas += 1
#
#    Com isso, a lista já ordenada passa a fazer 0 trocas.
#
# d) Por que dobrar o tamanho QUADRUPLICA as comparações?
#
#    Porque o total é n(n-1)/2, que cresce com o QUADRADO de n. Ao
#    dobrar n, o n² multiplica por 2² = 4.
#
#    Confira na medição: 50 -> 1.225 e 100 -> 4.950. E 4.950 / 1.225 =
#    4,04 — praticamente 4. (Não é exatamente 4 porque a fórmula tem o
#    "-1", que pesa menos conforme n cresce.)
#
#    É por isso que esses algoritmos são inviáveis em escala: com
#    10.000 elementos seriam cerca de 50 milhões de comparações.
#
# e) Qual é o melhor em cada cenário? Algum nunca ganha?
#
#    - JÁ ORDENADA ou QUASE: Insertion, disparado (9 contra 45).
#    - EMBARALHADA: Insertion compara menos (30 contra 45); Selection
#      movimenta menos (10 contra 26). Depende do que custa caro —
#      se mover dados for caro, Selection leva vantagem.
#    - ORDEM INVERSA: é o pior caso dos três, e eles empatam em
#      comparações (45). Selection ainda ganha em trocas.
#
#    O BUBBLE NUNCA GANHA. Ele compara tanto quanto o Selection e
#    movimenta tanto quanto o Insertion — o pior dos dois mundos.
#    Sobrevive no ensino só por ser o mais fácil de explicar.
#
#    (A versão com bandeira do exercício 01 empata com o Insertion na
#    lista já ordenada. É a única situação em que ele não perde.)
