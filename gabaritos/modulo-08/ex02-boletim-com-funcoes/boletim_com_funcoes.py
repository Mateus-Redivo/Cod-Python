"""
Gabarito — Módulo 08, Exercício 02: Boletim, agora com funções

Enunciado:
  modulo-08-funcoes/exercicios/EXERCICIO-02-boletim-com-funcoes.md

Mesma saída do gabarito do módulo 06, byte a byte. Confira:
  printf '5\\n8\\n12\\n7.5\\n9\\n6.5\\n10\\n' | python ../modulo-06-ex02-boletim/boletim.py
  printf '5\\n8\\n12\\n7.5\\n9\\n6.5\\n10\\n' | python boletim_com_funcoes.py

Como executar:
  python boletim_com_funcoes.py
"""

NOTA_MINIMA = 0
NOTA_MAXIMA = 10
MEDIA_APROVACAO = 7.0
MEDIA_RECUPERACAO = 5.0


def nota_e_valida(nota, minima=NOTA_MINIMA, maxima=NOTA_MAXIMA):
    """True se a nota está dentro do intervalo permitido."""
    return minima <= nota <= maxima


def ler_notas(quantidade):
    """Lê a quantidade pedida de notas, insistindo até cada uma valer."""
    notas = []
    for indice in range(1, quantidade + 1):
        nota = float(input(f"Nota {indice}: "))
        while not nota_e_valida(nota):
            print("Nota inválida! Digite um valor entre 0 e 10.")
            nota = float(input(f"Nota {indice}: "))
        notas.append(nota)
    return notas


def calcular_media(notas):
    """Média simples das notas."""
    return sum(notas) / len(notas)


def contar_acima_da_media(notas):
    """Quantas notas superam a média da própria lista."""
    media = calcular_media(notas)
    total = 0
    for nota in notas:
        if nota > media:
            total += 1
    return total


def classificar_turma(media):
    """Situação da turma a partir da média."""
    if media >= MEDIA_APROVACAO:
        return "Aprovada"
    elif media >= MEDIA_RECUPERACAO:
        return "Recuperação"
    else:
        return "Reprovada"


def mostrar_boletim(notas):
    """Única função que imprime."""
    media = calcular_media(notas)
    print("===== BOLETIM =====")
    print(f"Notas:   {notas}")
    print(f"Quantidade: {len(notas)}")
    print(f"Soma:       {sum(notas):.2f}")
    print(f"Média:      {media:.2f}")
    print(f"Maior:      {max(notas)}")
    print(f"Menor:      {min(notas)}")
    print(f"Acima da média: {contar_acima_da_media(notas)}")
    print(f"Situação: {classificar_turma(media)}")


# --- Programa principal: 6 linhas ------------------------------------
quantidade = int(input("Quantas notas? "))
notas = ler_notas(quantidade)

print()

if len(notas) == 0:
    print("Nenhuma nota informada.")
else:
    mostrar_boletim(notas)


# --- Por que assim -------------------------------------------------
# 1. Só mostrar_boletim imprime. As outras seis devolvem valores. Essa
#    separação é o que permitiria, amanhã, gravar o boletim num arquivo
#    ou mandá-lo por e-mail sem reescrever nenhum cálculo.
#
#    A exceção honesta é ler_notas, que imprime a mensagem de erro da
#    validação. Poderia devolver o erro em vez de imprimir, mas aí o
#    laço de insistência sairia da função e voltaria para o programa
#    principal — trocando um problema por outro. Interação com o
#    usuário é um caso em que a regra "não imprima" cede.
#
# 2. nota_e_valida usa "minima <= nota <= maxima", o atalho de
#    intervalo do módulo 02. E já nasce com os limites como parâmetros
#    de valor padrão — que é o desafio opcional do enunciado, resolvido
#    de graça. Para notas de 0 a 100:
#
#      nota_e_valida(85, 0, 100)   -> True
#
# 3. contar_acima_da_media chama calcular_media internamente, em vez de
#    receber a média pronta. Assim quem chama não pode passar a média
#    errada por engano. O custo é recalcular — irrelevante aqui.
#
# 4. O programa principal tem 6 linhas e lê como um roteiro: pergunte
#    quantas, leia, mostre. Toda a complexidade desceu para funções
#    com nome.
#
# 5. Nenhum global. As notas viajam como parâmetro e retorno.


# --- O que a refatoração revelou -------------------------------------
# Compare com o gabarito do módulo 06 e repare em duas coisas.
#
# Primeira: a versão antiga precisava de comentários explicando o que
# cada trecho fazia ("# --- COLETA ---", "# o segundo laço"). Aqui os
# nomes das funções dizem o mesmo, e os comentários viraram desnecessários.
# Nome bom é comentário que não apodrece.
#
# Segunda: na versão antiga, a regra "aprovada acima de 7" estava
# enterrada no meio de um bloco de trinta linhas. Agora ela é uma
# função de cinco linhas chamada classificar_turma, e mudar o critério
# é mexer em um lugar óbvio.
#
# Responda para si mesmo as duas perguntas do enunciado:
#   - mudar 7.0 para 6.0: um lugar nas duas versões (a constante) —
#     mas na versão antiga você precisa LER o programa todo para ter
#     certeza de que ela só é usada ali.
#   - reaproveitar o cálculo da média em outro programa: aqui é copiar
#     três linhas; lá é extrair do meio de um bloco e torcer.
