"""
Gabarito — Módulo 12, Exercício 02: Refatorando com prova

Enunciado:
  modulo-12-leitura-e-refatoracao/exercicios/EXERCICIO-02-refatorando-com-prova.md

Saída byte a byte idêntica à do relatorio_antes.py. Prove:
  python relatorio_antes.py  > antiga.txt
  python relatorio_depois.py > nova.txt
  diff antiga.txt nova.txt        (tem que sair vazio)

Como executar:
  python relatorio_depois.py
"""

ESTOQUE_BAIXO = 5

COLUNA_NOME = 0
COLUNA_QUANTIDADE = 1
COLUNA_PRECO = 2

produtos = [
    ["arroz", 5, 4.5],
    ["feijao", 3, 8.9],
    ["oleo", 12, 7.2],
    ["sal", 1, 2.3],
    ["cafe", 8, 18.5],
]


def calcular_subtotal(produto):
    """Quantidade x preço unitário."""
    return produto[COLUNA_QUANTIDADE] * produto[COLUNA_PRECO]


def estoque_esta_baixo(produto):
    """True quando a quantidade fica abaixo do limite."""
    return produto[COLUNA_QUANTIDADE] < ESTOQUE_BAIXO


def classificar_estoque(produto):
    """Rótulo textual da situação do estoque."""
    if estoque_esta_baixo(produto):
        return "BAIXO"
    return "OK"


def calcular_total(produtos):
    """Soma dos subtotais de todos os produtos."""
    total = 0
    for produto in produtos:
        total += calcular_subtotal(produto)
    return total


def contar_estoque_baixo(produtos):
    """Quantos produtos estão abaixo do limite."""
    quantidade = 0
    for produto in produtos:
        if estoque_esta_baixo(produto):
            quantidade += 1
    return quantidade


def encontrar_maior_subtotal(produtos):
    """Devolve nome e valor do produto de maior subtotal, juntos."""
    maior_nome = ""
    maior_valor = 0
    for produto in produtos:
        subtotal = calcular_subtotal(produto)
        if subtotal > maior_valor:
            maior_valor = subtotal
            maior_nome = produto[COLUNA_NOME]
    return maior_nome, maior_valor


def mostrar_relatorio(produtos):
    print("=== RELATORIO ===")
    for produto in produtos:
        # O subtotal agora é calculado UMA vez por produto, aqui.
        subtotal = calcular_subtotal(produto)
        situacao = classificar_estoque(produto)
        # Sem formatação: a saída precisa continuar idêntica, com
        # todos os decimais feios que o original produzia.
        print(f"{produto[COLUNA_NOME]} {produto[COLUNA_QUANTIDADE]} "
              f"{produto[COLUNA_PRECO]} {subtotal} {situacao}")

    maior_nome, maior_valor = encontrar_maior_subtotal(produtos)

    print(f"Total: {calcular_total(produtos)}")
    print(f"Itens baixos: {contar_estoque_baixo(produtos)}")
    print(f"Maior: {maior_nome} {maior_valor}")


mostrar_relatorio(produtos)


# --- Respostas da parte escrita --------------------------------------
#
# a) Por que calcular "s" duas vezes é um problema, além do custo?
#
#    Porque são DUAS FONTES DA VERDADE para o mesmo número. No dia em
#    que a regra do subtotal mudar — passar a ter desconto por volume,
#    por exemplo — quem alterar vai achar uma das duas linhas, mudar,
#    testar e ver funcionando... na tabela mas não no total, ou o
#    contrário.
#
#    O custo de processamento é irrelevante com 5 produtos. O risco de
#    divergência é permanente.
#
#    Extrair "calcular_subtotal" resolve os dois de uma vez: a regra
#    passa a existir em um lugar só.
#
# b) O que sugere "n" e "m" serem sempre atualizadas juntas?
#
#    Que elas não são duas informações — são uma só, com duas partes.
#    "O maior subtotal" é um par (nome, valor); separá-lo em duas
#    variáveis é o mesmo problema das listas paralelas do módulo 08.
#
#    Por isso "encontrar_maior_subtotal" devolve as duas juntas. Não
#    existe estado em que uma esteja certa e a outra errada, porque
#    elas viajam no mesmo return.
#
# c) A saída ficou idêntica?
#
#    Sim, byte a byte — conferido com diff. E foi preciso RESISTIR a
#    melhorá-la:
#
#      - o subtotal do feijão sai como 26.700000000000003
#      - o total sai como 285.90000000000003
#      - as colunas ficam tortas
#
#    Todos os três pediam um ":.2f" ou um alinhamento. Formatar aqui
#    teria mudado o comportamento, e a refatoração deixaria de ser
#    refatoração.
#
#    Isso é o exercício inteiro: separar "deixar mais claro" de
#    "deixar melhor". São duas tarefas, e misturá-las é como se perde
#    o controle do que mudou.


# --- Sobre a f-string sem formato ------------------------------------
# f"{subtotal}" produz exatamente o mesmo texto que str(subtotal) —
# inclusive os decimais longos. É isso que permite trocar a
# concatenação por f-string sem alterar um byte da saída.
#
# Se eu tivesse escrito f"{subtotal:.2f}", o feijão sairia 26.70 e o
# diff acusaria a diferença na hora. Que é exatamente o que ele
# deveria fazer.
