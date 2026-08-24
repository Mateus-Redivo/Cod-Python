"""
Gabarito — Módulo 06, Exercício 02: Boletim

Enunciado:
  modulo-06-listas/exercicios/EXERCICIO-02-boletim.md

Como executar:
  python boletim.py
"""

NOTA_MINIMA = 0
NOTA_MAXIMA = 10
MEDIA_APROVACAO = 7.0
MEDIA_RECUPERACAO = 5.0

# A lista nasce VAZIA, antes do laço. É o acumulador do módulo 05 —
# só que acumulando valores em vez de somar.
notas = []

quantidade = int(input("Quantas notas? "))

# --- 1. COLETA -------------------------------------------------------
for indice in range(1, quantidade + 1):
    nota = float(input(f"Nota {indice}: "))

    # Validação com while: não sabemos quantas vezes o usuário erra.
    while nota < NOTA_MINIMA or nota > NOTA_MAXIMA:
        print("Nota inválida! Digite um valor entre 0 e 10.")
        nota = float(input(f"Nota {indice}: "))

    # Só entra na lista depois de validada.
    notas.append(nota)

print()

# --- 2. PROTEÇÃO + RESUMO --------------------------------------------
if len(notas) == 0:
    print("Nenhuma nota informada.")
else:
    soma = sum(notas)
    media = soma / len(notas)

    # O segundo laço: só possível DEPOIS que a média existe.
    acima_da_media = 0
    for nota in notas:
        if nota > media:
            acima_da_media += 1

    if media >= MEDIA_APROVACAO:
        situacao = "Aprovada"
    elif media >= MEDIA_RECUPERACAO:
        situacao = "Recuperação"
    else:
        situacao = "Reprovada"

    print("===== BOLETIM =====")
    print(f"Notas:   {notas}")
    print(f"Quantidade: {len(notas)}")
    print(f"Soma:       {soma:.2f}")
    print(f"Média:      {media:.2f}")
    print(f"Maior:      {max(notas)}")
    print(f"Menor:      {min(notas)}")
    print(f"Acima da média: {acima_da_media}")
    print(f"Situação: {situacao}")


# --- Por que assim -------------------------------------------------
# 1. DOIS laços, e não um. Esta é a lição central do exercício:
#    contar quantas notas estão acima da média é impossível enquanto
#    a média não existe — e ela só existe depois da última nota.
#    Primeiro colete tudo, depois analise. Guardar os valores numa
#    lista é justamente o que permite voltar a olhá-los.
#
# 2. FOR para as leituras (quantidade conhecida, o usuário disse) e
#    WHILE para a validação (quantidade desconhecida, depende de
#    quantas vezes ele erra). É o mesmo par do módulo 05.
#
# 3. O append() acontece DEPOIS do while, não dentro. Uma nota
#    inválida nunca chega à lista.
#
# 4. sum(), max() e min() em vez de laços manuais. O acumulador
#    continua sendo necessário no "acima_da_media", porque ali a
#    contagem tem CONDIÇÃO — e para isso não existe função pronta.
#
# 5. O "if len(notas) == 0" protege duas coisas: a divisão da média
#    e as chamadas max()/min(), que também quebram em lista vazia
#    (ValueError: max() iterable argument is empty).
#
# 6. A situação vai para uma variável e o print é único, no fim.
#    Mesmo motivo do gabarito do módulo 04.


# --- Conferência ----------------------------------------------------
# Entrada do enunciado: 5 notas — 8, (12 rejeitada), 7.5, 9, 6.5, 10
#
#   notas = [8.0, 7.5, 9.0, 6.5, 10.0]
#   soma  = 41.0
#   média = 41.0 / 5 = 8.2
#   acima de 8.2: 9.0 e 10.0 ... e o 8.0? NÃO, porque 8.0 < 8.2.
#
#   Contando: 9.0 (sim), 10.0 (sim), 8.0 (não), 7.5 (não), 6.5 (não)
#   -> 2 notas acima da média.
#
# O 8.0 engana: ele é alto, mas a média é 8.2, então ele fica ABAIXO.
# Uma nota boa pode perfeitamente estar abaixo da média de uma turma
# boa. Se a sua contagem deu 3, confira se você não comparou com o
# valor errado.
#
# Neste conjunto, usar ">" ou ">=" dá o mesmo resultado, porque
# nenhuma nota é exatamente 8.2. Com notas [5, 5, 5], porém, a média
# é 5 e as três são "iguais à média": com ">" a contagem é 0, com
# ">=" é 3. Vale decidir qual você quer e nomear a variável de acordo.


# --- Solução do desafio opcional ------------------------------------
# Ordem decrescente sem destruir a lista original:
#
#   decrescentes = sorted(notas, reverse=True)
#   print(f"Ranking: {decrescentes}")
#   print(f"Ordem de digitação preservada: {notas}")
#
# sorted() devolve uma lista NOVA. Se você tivesse usado
# notas.sort(reverse=True), a ordem de digitação seria perdida para
# sempre — e o boletim não teria mais como mostrar "a terceira nota
# que você digitou".
