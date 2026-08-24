"""
Gabarito — Módulo 03, Exercício 02: Nota fiscal

Enunciado:
  modulo-03-entrada-e-saida/exercicios/EXERCICIO-02-nota-fiscal.md

Como executar:
  python nota_fiscal.py
"""

TAXA_DE_DESCONTO = 0.10
LARGURA = 40

# Larguras das colunas. A soma tem que dar LARGURA, senão a tabela
# desalinha em relação às linhas de "-".
COL_NOME = 15
COL_QTD = 5
COL_UNIT = 9
COL_SUB = 11

# --- 1. ENTRADA ------------------------------------------------------
print("Produto 1")
nome1 = input("  Nome: ")
# Quantidade é int: não se compra 2.5 canetas.
quantidade1 = int(input("  Quantidade: "))
# Preço é float: dinheiro tem centavos.
preco1 = float(input("  Preço unitário: R$ "))

print()
print("Produto 2")
nome2 = input("  Nome: ")
quantidade2 = int(input("  Quantidade: "))
preco2 = float(input("  Preço unitário: R$ "))

print()
print("Produto 3")
nome3 = input("  Nome: ")
quantidade3 = int(input("  Quantidade: "))
preco3 = float(input("  Preço unitário: R$ "))


# --- 2. PROCESSAMENTO ------------------------------------------------
subtotal1 = quantidade1 * preco1
subtotal2 = quantidade2 * preco2
subtotal3 = quantidade3 * preco3

total = subtotal1 + subtotal2 + subtotal3
desconto = total * TAXA_DE_DESCONTO
total_a_pagar = total - desconto


# --- 3. SAÍDA --------------------------------------------------------
print()
print("=" * LARGURA)
print(f"{'NOTA FISCAL':^{LARGURA}}")
print("=" * LARGURA)
print(f"{'Produto':<{COL_NOME}}{'Qtd':>{COL_QTD}}{'Unit.':>{COL_UNIT}}{'Subtotal':>{COL_SUB}}")
print("-" * LARGURA)
print(f"{nome1:<{COL_NOME}}{quantidade1:>{COL_QTD}}{preco1:>{COL_UNIT}.2f}{subtotal1:>{COL_SUB}.2f}")
print(f"{nome2:<{COL_NOME}}{quantidade2:>{COL_QTD}}{preco2:>{COL_UNIT}.2f}{subtotal2:>{COL_SUB}.2f}")
print(f"{nome3:<{COL_NOME}}{quantidade3:>{COL_QTD}}{preco3:>{COL_UNIT}.2f}{subtotal3:>{COL_SUB}.2f}")
print("-" * LARGURA)
print(f"{'Total':<{LARGURA - COL_SUB}}{total:>{COL_SUB}.2f}")
print(f"{'Desconto (10%)':<{LARGURA - COL_SUB}}{desconto:>{COL_SUB}.2f}")
print(f"{'TOTAL A PAGAR':<{LARGURA - COL_SUB}}{total_a_pagar:>{COL_SUB}.2f}")
print("=" * LARGURA)


# --- Por que assim -------------------------------------------------
# 1. A escolha dos tipos não é detalhe. Quantidade como int porque
#    "2.5 canetas" não existe — e se o usuário digitar isso, é melhor
#    o programa recusar do que fingir que entendeu. Preço como float
#    porque R$ 2,50 é o caso normal, não a exceção.
#
# 2. As larguras estão em constantes e a soma delas é LARGURA. Isso é
#    o que mantém a tabela alinhada com as linhas de "=" e "-". Se
#    você mudar COL_NOME para 20, precisa tirar 5 de outra coluna.
#
# 3. As chaves aninhadas — {nome1:<{COL_NOME}} — deixam a f-string ler
#    a largura de uma variável em vez de ter o número fixo. Escrever
#    {nome1:<15} funciona igual, mas aí a largura fica repetida em
#    quatro linhas e uma mudança exige acertar todas.
#
# 4. O {:^} centraliza. É o terceiro alinhamento, junto de < e >.
#
# 5. As três etapas estão separadas por comentários: primeiro TODA a
#    entrada, depois TODO o cálculo, depois TODA a saída. Misturar
#    print no meio da conta funciona, mas embaralha a leitura — e no
#    módulo 08 essa separação vira a base para extrair funções.


# --- Sobre o alinhamento com nome longo ------------------------------
# O enunciado pede para testar "Estojo de canetas" (17 caracteres).
# O ":<15" NÃO corta o texto: ele garante o MÍNIMO de 15, não o
# máximo. Um nome de 17 caracteres empurra as colunas seguintes e a
# linha fica com 42 caracteres em vez de 40.
#
# Para cortar de verdade, o formato é {nome1:<15.15} — o segundo
# número limita o comprimento:
#
#   f"{'Estojo de canetas':<15.15}"   ->  'Estojo de canet'
#
# Qual escolher é decisão de projeto: cortar mantém a tabela reta mas
# esconde informação; não cortar preserva o dado mas quebra o desenho.


# --- Solução do desafio opcional ------------------------------------
# Com os valores do exemplo, as duas formas dão o mesmo resultado:
#
#   total = 175.29
#   forma A: 175.29 - round(17.529, 2) = 175.29 - 17.53 = 157.76
#   forma B: 175.29 * 0.9              = 157.761        -> 157.76
#
# Mas nem sempre. Com total = 0.25:
#
#   forma A: 0.25 - 0.03 (0.025 arredondado)  = 0.22
#   forma B: 0.25 * 0.9 = 0.225               -> 0.23  (ou 0.22!)
#
# Qual escolher: a forma A, que subtrai o desconto JÁ ARREDONDADO. O
# motivo não é matemático, é contábil — o valor do desconto aparece
# impresso na nota, e o cliente vai conferir a subtração na mão. Se o
# papel diz "Total 0.25, Desconto 0.03, A pagar 0.23", a conta não
# fecha e a culpa é do programa, não do cliente.
#
# Regra prática para dinheiro: arredonde CADA valor que for exibido, e
# faça as contas seguintes com os valores já arredondados.
