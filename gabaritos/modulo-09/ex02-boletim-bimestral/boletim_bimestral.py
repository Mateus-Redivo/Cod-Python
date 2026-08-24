"""
Gabarito — Módulo 09, Exercício 02: Boletim bimestral

Enunciado:
  modulo-09-matrizes/exercicios/EXERCICIO-02-boletim-bimestral.md

Como executar:
  python boletim_bimestral.py
"""

MEDIA_APROVACAO = 7.0
MEDIA_RECUPERACAO = 5.0
LARGURA = 56


def media_do_aluno(notas, indice):
    """Média de uma LINHA. A linha já é uma lista, então sum() resolve."""
    return sum(notas[indice]) / len(notas[indice])


def media_do_bimestre(notas, bimestre):
    """Média de uma COLUNA. A coluna não existe como lista: precisa de laço."""
    total = 0
    for linha in range(len(notas)):
        total += notas[linha][bimestre]     # índice fixo é o SEGUNDO
    return total / len(notas)


def situacao(media):
    if media >= MEDIA_APROVACAO:
        return "Aprovado"
    elif media >= MEDIA_RECUPERACAO:
        return "Recuperação"
    else:
        return "Reprovado"


def melhor_aluno(alunos, notas):
    """Nome de quem tem a maior média. Começa pelo primeiro, não por zero."""
    melhor = alunos[0]
    maior_media = media_do_aluno(notas, 0)
    for i in range(len(alunos)):
        if media_do_aluno(notas, i) > maior_media:
            maior_media = media_do_aluno(notas, i)
            melhor = alunos[i]
    return melhor, maior_media


def mostrar_boletim(alunos, notas):
    quantidade_bimestres = len(notas[0])

    print("=" * LARGURA)
    cabecalho = f"{'Aluno':<12}"
    for b in range(quantidade_bimestres):
        cabecalho += f"{str(b + 1) + 'º B':>7}"
    cabecalho += f"{'Média':>7}  Situação"
    print(cabecalho)
    print("-" * LARGURA)

    for i in range(len(alunos)):
        linha = f"{alunos[i]:<12}"
        for nota in notas[i]:
            linha += f"{nota:>7.1f}"
        media = media_do_aluno(notas, i)
        linha += f"{media:>7.2f}  {situacao(media)}"
        print(linha)

    print("-" * LARGURA)

    rodape = f"{'Média turma':<12}"
    for b in range(quantidade_bimestres):
        rodape += f"{media_do_bimestre(notas, b):>7.1f}"
    print(rodape)

    nome, media = melhor_aluno(alunos, notas)
    print(f"Melhor aluno: {nome} ({media:.2f})")
    print("=" * LARGURA)


# --- Uso -------------------------------------------------------------
alunos = ["Ana", "Bruno", "Carla", "Diego"]
notas = [
    [8.0, 7.5, 9.0, 6.5],
    [5.0, 6.0, 4.5, 7.0],
    [9.5, 9.0, 10.0, 8.5],
    [3.0, 5.5, 6.0, 4.0],
]

mostrar_boletim(alunos, notas)


# --- Por que assim -------------------------------------------------
# 1. As duas funções de média percorrem a matriz em direções
#    DIFERENTES, e é isso que o exercício ensina:
#
#      media_do_aluno    -> notas[indice] é uma LISTA pronta -> sum()
#      media_do_bimestre -> a coluna está espalhada -> laço juntando
#                           notas[linha][bimestre] de cada linha
#
#    Se as suas duas ficaram iguais, uma das duas está somando a
#    direção errada.
#
# 2. Nenhum 4 nem 5 fixo. "quantidade_bimestres = len(notas[0])" e
#    "len(alunos)" fazem o programa funcionar com qualquer tamanho.
#    Acrescente um quinto aluno na lista e rode: nada mais muda.
#
# 3. "situacao" é função separada. Enterrada dentro do laço da tabela,
#    a regra de aprovação ficaria invisível e não daria para reusar no
#    rodapé ou num relatório futuro.
#
# 4. melhor_aluno começa com o PRIMEIRO aluno, não com média zero — o
#    mesmo cuidado dos módulos 06 e 07. Com todas as médias negativas
#    (impossível aqui, mas o hábito vale), começar em zero erraria.
#
# 5. A linha da tabela é montada numa string e impressa de uma vez, em
#    vez de vários print(end=""). As duas formas funcionam; esta deixa
#    mais fácil enxergar a largura total.


# --- Conferência ----------------------------------------------------
# Ana:   (8.0 + 7.5 + 9.0 + 6.5) / 4 = 31.0 / 4 = 7.75   -> Aprovado
# Bruno: (5.0 + 6.0 + 4.5 + 7.0) / 4 = 22.5 / 4 = 5.625  -> Recuperação
# Carla: (9.5 + 9.0 + 10.0 + 8.5)/ 4 = 37.0 / 4 = 9.25   -> Aprovado
# Diego: (3.0 + 5.5 + 6.0 + 4.0) / 4 = 18.5 / 4 = 4.625  -> Reprovado
#
# 1º bimestre: (8.0 + 5.0 + 9.5 + 3.0) / 4 = 25.5 / 4 = 6.375 -> 6.4
# 2º bimestre: (7.5 + 6.0 + 9.0 + 5.5) / 4 = 28.0 / 4 = 7.0
# 3º bimestre: (9.0 + 4.5 + 10.0 + 6.0)/ 4 = 29.5 / 4 = 7.375 -> 7.4
# 4º bimestre: (6.5 + 7.0 + 8.5 + 4.0) / 4 = 26.0 / 4 = 6.5
#
# Repare que 5.625 exibido com 2 casas vira 5.62, não 5.63 — a
# poeirinha dos decimais do módulo 02 de novo.


# --- Solução do desafio opcional ------------------------------------
# Faltas na mesma matriz seria um erro: a última coluna passaria a
# significar outra coisa, e toda função teria que lembrar disso.
# media_do_aluno somaria as faltas junto com as notas.
#
# A saída é uma segunda estrutura, paralela mas explícita:
#
#   faltas = [2, 0, 1, 5]      # uma lista simples, um valor por aluno
#
# Aqui as listas paralelas são aceitáveis porque são de tipos e
# tamanhos diferentes — não há risco de confundir uma nota com uma
# falta. O perigo do módulo 08 era outro: três listas do MESMO
# comprimento que precisavam ficar alinhadas.
