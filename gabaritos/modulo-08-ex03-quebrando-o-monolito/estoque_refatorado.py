"""
Gabarito — Módulo 08, Exercício 03: Quebrando o monólito

Enunciado:
  modulo-08-funcoes/exercicios/EXERCICIO-03-quebrando-o-monolito.md

Mesma saída do monolito.py, byte a byte. Confira:
  python monolito.py > antiga.txt
  python estoque_refatorado.py > nova.txt
  diff antiga.txt nova.txt

Como executar:
  python estoque_refatorado.py
"""

LARGURA = 46
ESTOQUE_CRITICO = 5


# --- Cálculo: devolvem valores, não imprimem -------------------------

def classificar_situacao(quantidade):
    """Devolve a situação de um produto a partir da quantidade."""
    if quantidade == 0:
        return "SEM ESTOQUE"
    elif quantidade < ESTOQUE_CRITICO:
        return "CRITICO"
    else:
        return "OK"


def calcular_valor_em_estoque(precos, estoque):
    """Valor total imobilizado: preço x quantidade, somado."""
    total = 0
    for i in range(len(precos)):
        total += precos[i] * estoque[i]
    return total


def contar_por_situacao(estoque, situacao_procurada):
    """Quantos produtos estão na situação informada."""
    total = 0
    for quantidade in estoque:
        if classificar_situacao(quantidade) == situacao_procurada:
            total += 1
    return total


def encontrar_mais_caro(produtos, precos):
    """Devolve o nome e o preço do produto mais caro."""
    nome = produtos[0]
    maior_preco = precos[0]
    for i in range(len(precos)):
        if precos[i] > maior_preco:
            maior_preco = precos[i]
            nome = produtos[i]
    return nome, maior_preco


def calcular_preco_medio(precos):
    """Média simples dos preços."""
    return sum(precos) / len(precos)


# --- Exibição: imprimem, não calculam --------------------------------

def mostrar_cabecalho():
    print("=" * LARGURA)
    print("RELATORIO DE ESTOQUE")
    print("=" * LARGURA)


def mostrar_linha_produto(nome, quantidade, preco):
    valor = preco * quantidade
    situacao = classificar_situacao(quantidade)
    print(f"{nome:<12}{quantidade:>4}{preco:>10.2f}{valor:>11.2f}  {situacao}")


def mostrar_resumo(produtos, precos, estoque):
    nome_mais_caro, preco_mais_caro = encontrar_mais_caro(produtos, precos)

    print("-" * LARGURA)
    print(f"Valor total em estoque: R$ {calcular_valor_em_estoque(precos, estoque):.2f}")
    print(f"Produtos sem estoque:   {contar_por_situacao(estoque, 'SEM ESTOQUE')}")
    print(f"Produtos criticos:      {contar_por_situacao(estoque, 'CRITICO')}")
    print(f"Mais caro: {nome_mais_caro} (R$ {preco_mais_caro:.2f})")
    print(f"Preco medio: R$ {calcular_preco_medio(precos):.2f}")
    print("=" * LARGURA)


# --- Programa principal: lê como um roteiro --------------------------

produtos = ["caneta", "caderno", "mochila", "estojo", "borracha"]
precos = [2.50, 18.90, 129.99, 24.00, 1.75]
estoque = [40, 12, 3, 0, 25]

mostrar_cabecalho()

for i in range(len(produtos)):
    mostrar_linha_produto(produtos[i], estoque[i], precos[i])

mostrar_resumo(produtos, precos, estoque)


# --- Por que assim -------------------------------------------------
# 1. Duas famílias de função, separadas de propósito: as que CALCULAM
#    (devolvem, nunca imprimem) e as que EXIBEM (imprimem, nunca
#    calculam). No original, o laço fazia as duas coisas ao mesmo
#    tempo — e por isso era impossível reaproveitar qualquer pedaço.
#
# 2. "classificar_situacao" virou função de uma responsabilidade só, e
#    passou a ser usada em dois lugares: na linha do produto e na
#    contagem. No original, a regra "menos de 5 é crítico" estava
#    escrita uma vez só porque contagem e exibição aconteciam juntas.
#    Agora a regra mora em um lugar e os dois usos a consultam.
#
# 3. O programa principal virou um roteiro de cinco linhas. Dá para
#    ler e entender o que o relatório faz sem descer para nenhuma
#    função.
#
# 4. LARGURA e ESTOQUE_CRITICO saíram do meio do código. O "46" e o
#    "5" apareciam soltos e ninguém sabia de onde vinham.


# --- Os três problemas escondidos ------------------------------------
#
# PROBLEMA 1 — A média recalculada na mão.
# O original termina com um laço para somar os preços, embora sum()
# resolva em uma expressão desde o módulo 06. Não é erro de resultado:
# é trabalho repetido e mais superfície para errar. Aqui virou
# "return sum(precos) / len(precos)".
#
# PROBLEMA 2 — A busca do mais caro dentro do laço de exibição.
# No original, descobrir o produto mais caro acontecia no meio do laço
# que imprime as linhas. Isso amarra duas coisas que não têm relação:
# não dá para saber o mais caro sem imprimir o relatório inteiro, e
# não dá para imprimir o relatório sem calcular o mais caro. Separadas,
# cada uma pode ser usada, testada e corrigida sozinha.
#
# PROBLEMA 3 — A inicialização de "mais_caro".
# O original começa com "mais_caro = precos[0]", o que está CERTO — e
# é o cuidado que os módulos 06 e 07 insistiram em ensinar. O defeito
# real está em outro lugar: com a lista de produtos VAZIA, "precos[0]"
# dá IndexError, e o mesmo vale para a versão refatorada. Nenhuma das
# duas trata esse caso.
#
#   Confira: troque as três listas por [] e rode.
#
# Consertar isso exigiria decidir o que um relatório de estoque vazio
# deveria mostrar — e essa é uma decisão de produto, não de código.
# O enunciado pede para PRESERVAR o comportamento, então o defeito
# ficou. Refatorar e corrigir na mesma passada é como se perde o
# controle do que mudou.


# --- Solução do desafio dentro do desafio ----------------------------
# Três listas paralelas quebram no dia em que alguém acrescenta um
# produto e esquece o preço: as listas ficam de tamanhos diferentes e o
# "range(len(produtos))" passa a ler índice inexistente em precos.
#
# A saída é guardar cada produto como uma unidade, em vez de espalhá-lo
# por três listas. Com o que você tem até aqui, uma lista de listas:
#
#   produtos = [
#       ["caneta",   2.50,  40],
#       ["caderno",  18.90, 12],
#       ["mochila",  129.99, 3],
#   ]
#
#   for produto in produtos:
#       nome, preco, quantidade = produto
#
# Agora é impossível o preço "desalinhar" do nome — eles viajam juntos.
# É exatamente o assunto do módulo 09.
