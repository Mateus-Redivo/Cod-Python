"""
Gabarito — Módulo 11, Exercício 03: Ordenando registros

Enunciado:
  modulo-11-algoritmos-de-ordenacao/exercicios/EXERCICIO-03-ordenando-registros.md

Como executar:
  python ordenando_registros.py
"""

COLUNA_NOME = 0
COLUNA_IDADE = 1
COLUNA_NOTA = 2
NOMES_DAS_COLUNAS = ["Nome", "Idade", "Nota"]


# --- Leitura segura (módulo 10) --------------------------------------

def ler_inteiro_na_faixa(mensagem, minimo, maximo):
    while True:
        try:
            valor = int(input(mensagem))
        except ValueError:
            print("  Digite um número inteiro.")
            continue
        if minimo <= valor <= maximo:
            return valor
        print(f"  O valor deve estar entre {minimo} e {maximo}.")


# --- Ordenação --------------------------------------------------------

def ordenar_por(registros, coluna, crescente=True):
    """Ordena por uma coluna. Devolve lista nova; usa Insertion (estável)."""
    # Cópia das LINHAS, para não alterar os registros originais.
    resultado = [linha[:] for linha in registros]

    for i in range(1, len(resultado)):
        atual = resultado[i]
        j = i - 1

        while j >= 0 and fora_de_ordem(resultado[j], atual, coluna, crescente):
            resultado[j + 1] = resultado[j]
            j -= 1

        resultado[j + 1] = atual

    return resultado


def fora_de_ordem(anterior, atual, coluna, crescente):
    """True se 'anterior' deve ficar depois de 'atual'."""
    if crescente:
        return anterior[coluna] > atual[coluna]
    return anterior[coluna] < atual[coluna]


def mostrar_tabela(registros):
    print(f"{'Nome':<12}{'Idade':>7}{'Nota':>7}")
    for nome, idade, nota in registros:
        print(f"{nome:<12}{idade:>7}{nota:>7.1f}")
    print()


# --- Dados ------------------------------------------------------------
alunos = [
    ["Carla", 22, 9.5],
    ["Bruno", 19, 7.0],
    ["Ana", 22, 8.0],
    ["Diego", 20, 7.0],
    ["Elena", 19, 9.5],
]


if __name__ == "__main__":
    print("Registros originais:")
    mostrar_tabela(alunos)

    while True:
        print("Ordenar por: (0) Nome (1) Idade (2) Nota (3) Sair")
        escolha = ler_inteiro_na_faixa("-> ", 0, 3)

        if escolha == 3:
            print("Até logo!")
            break

        sentido = ler_inteiro_na_faixa(
            "Sentido: (1) crescente (2) decrescente -> ", 1, 2)

        ordenados = ordenar_por(alunos, escolha, crescente=(sentido == 1))
        print()
        print(f"Ordenado por {NOMES_DAS_COLUNAS[escolha]}:")
        mostrar_tabela(ordenados)


# --- Por que assim -------------------------------------------------
# 1. A troca move a LINHA INTEIRA, nunca um campo isolado:
#
#      resultado[j + 1] = resultado[j]        # a linha toda
#      resultado[j + 1][coluna] = ...         # ERRADO: quebra o registro
#
#    A segunda forma deixaria o aluno com a nota de outro. É o mesmo
#    perigo das listas paralelas do módulo 08, por outro caminho.
#
# 2. "[linha[:] for linha in registros]" copia CADA linha, não só a
#    lista externa. Um "registros[:]" simples copiaria a lista de fora
#    mas as linhas continuariam sendo as mesmas — e alterá-las mexeria
#    no original. É o mesmo mecanismo da armadilha do [[0]*3]*3 do
#    módulo 09: cópia rasa não basta quando há listas dentro de listas.
#
# 3. "fora_de_ordem" isola a comparação numa função. Sem ela, o
#    crescente/decrescente exigiria dois whiles quase iguais, ou um if
#    dentro do laço.
#
# 4. Escolhi o Insertion porque ele é ESTÁVEL — ver abaixo.


# --- A investigação de estabilidade (resultado medido) ---------------
#
# Ordenando os 5 alunos por IDADE, e observando o empate em 22 anos
# (Carla e Ana, nessa ordem no original):
#
#   Bubble    -> Bruno, Elena, Diego, Carla, Ana    ESTÁVEL
#   Insertion -> Bruno, Elena, Diego, Carla, Ana    ESTÁVEL
#   Selection -> Bruno, Elena, Diego, Ana,   Carla  INSTÁVEL
#
# O Selection inverteu Carla e Ana. Por quê? Porque ele TROCA à
# distância: pega o menor lá do fim e o joga na posição i, passando
# por cima de quem estava no meio. Bubble e Insertion só movem
# elementos ADJACENTES, e nunca trocam dois iguais de lugar — daí a
# estabilidade.
#
# Repare que o empate em 19 (Bruno e Elena) não revela nada: eles já
# estavam na ordem certa e os três acertam. É preciso escolher o
# empate certo para o teste enxergar a diferença — e isso vale para
# testes em geral.


# --- Solução do desafio dentro do desafio ----------------------------
# Ordenar por nota decrescente e, no empate, nome crescente.
#
# Com um algoritmo estável, ordena-se DUAS vezes — e a ordem é
# contraintuitiva: primeiro pelo critério SECUNDÁRIO, depois pelo
# PRINCIPAL.
#
#   por_nome = ordenar_por(alunos, COLUNA_NOME, crescente=True)
#   final = ordenar_por(por_nome, COLUNA_NOTA, crescente=False)
#
# Por quê? Porque a segunda ordenação, sendo estável, PRESERVA a ordem
# que a primeira deixou entre os empatados. Se você inverter a
# sequência, a ordenação por nome embaralha as notas e o trabalho da
# primeira é perdido.
#
# Resultado com os dados deste arquivo:
#   Carla 9.5 / Elena 9.5 / Ana 8.0 / Bruno 7.0 / Diego 7.0
#
# Confira os empates: entre Carla e Elena (9.5), C vem antes de E;
# entre Bruno e Diego (7.0), B vem antes de D. Ordem alfabética
# preservada dentro de cada nota.
#
# Se você usasse o Selection aqui, os empates sairiam em ordem
# arbitrária — e você levaria um bom tempo para descobrir por quê.
