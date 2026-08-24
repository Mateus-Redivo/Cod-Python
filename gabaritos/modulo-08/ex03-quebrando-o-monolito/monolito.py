"""
Código de partida do Módulo 08, Exercício 03.

Este é o programa ORIGINAL, com todos os defeitos. Está aqui para você
comparar a saída com a da versão refatorada:

  python monolito.py > antiga.txt
  python estoque_refatorado.py > nova.txt
  diff antiga.txt nova.txt

Não estude por este arquivo — ele é o problema, não a solução.
"""

produtos = ["caneta", "caderno", "mochila", "estojo", "borracha"]
precos = [2.50, 18.90, 129.99, 24.00, 1.75]
estoque = [40, 12, 3, 0, 25]

print("=" * 46)
print("RELATORIO DE ESTOQUE")
print("=" * 46)

valor_total = 0
sem_estoque = 0
critico = 0
mais_caro = precos[0]
nome_mais_caro = produtos[0]

for i in range(len(produtos)):
    valor = precos[i] * estoque[i]
    valor_total = valor_total + valor

    if estoque[i] == 0:
        situacao = "SEM ESTOQUE"
        sem_estoque = sem_estoque + 1
    elif estoque[i] < 5:
        situacao = "CRITICO"
        critico = critico + 1
    else:
        situacao = "OK"

    if precos[i] > mais_caro:
        mais_caro = precos[i]
        nome_mais_caro = produtos[i]

    print(f"{produtos[i]:<12}{estoque[i]:>4}{precos[i]:>10.2f}{valor:>11.2f}  {situacao}")

print("-" * 46)
print(f"Valor total em estoque: R$ {valor_total:.2f}")
print(f"Produtos sem estoque:   {sem_estoque}")
print(f"Produtos criticos:      {critico}")
print(f"Mais caro: {nome_mais_caro} (R$ {mais_caro:.2f})")

media_precos = 0
for i in range(len(precos)):
    media_precos = media_precos + precos[i]
media_precos = media_precos / len(precos)
print(f"Preco medio: R$ {media_precos:.2f}")
print("=" * 46)
