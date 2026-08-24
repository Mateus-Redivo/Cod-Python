# Exercício 03 — Quebrando o monólito (desafio)

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 3 de 3 | 60 min | decomposição, `return`, escopo, leitura de código alheio |

## Objetivo

Receber um programa longo, escrito por outra pessoa, e reorganizá-lo em funções, sem alterar o
comportamento e sem ter escrito uma linha dele. É o trabalho real de manutenção de software.

## O código de partida

Copie este programa para `monolito.py` e **rode-o primeiro**, anotando a saída. Ela é o seu
gabarito: no fim, sua versão refatorada tem que produzir exatamente a mesma coisa.

```python
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
```

## Requisitos

1. Crie `estoque_refatorado.py` com a versão em funções.
2. Extraia, no mínimo, estas funções, todas com `return`, exceto as de exibição:
   - `calcular_valor_em_estoque(precos, estoque)`: o valor total
   - `classificar_situacao(quantidade)`: devolve `"SEM ESTOQUE"`, `"CRITICO"` ou `"OK"`
   - `contar_por_situacao(estoque, situacao)`: quantos produtos estão naquela situação
   - `encontrar_mais_caro(produtos, precos)`: devolve nome e preço
   - `calcular_preco_medio(precos)`: a média
   - `mostrar_cabecalho()`, `mostrar_linha_produto(...)`, `mostrar_resumo(...)`
3. O corpo principal deve virar uma sequência legível de chamadas.
4. A saída tem que ser **byte a byte idêntica** à do original.
5. Nenhum `global`.

## Três problemas escondidos no código original

Encontre-os durante a refatoração e escreva sobre cada um em um comentário. Não os conserte ainda:
o objetivo desta etapa é **preservar o comportamento**, incluindo os defeitos.

1. O último bloco recalcula a média com um laço manual, embora exista uma função pronta para isso
   desde o módulo 06. Qual?
2. A busca pelo produto mais caro está dentro do laço de exibição, misturando duas
   responsabilidades. Por que isso atrapalha?
3. Existe um valor inicial que daria resposta errada em um caso específico. Qual variável, e com
   qual lista de produtos ela falharia?

## Critérios de aceitação

- [ ] As duas saídas são idênticas (conferidas linha por linha)
- [ ] Existem pelo menos as oito funções pedidas
- [ ] Funções de cálculo não têm `print`; funções de exibição não têm cálculo
- [ ] Nenhum `global`
- [ ] O corpo principal cabe em menos de 15 linhas e lê como um roteiro
- [ ] Os três problemas escondidos estão identificados em comentários
- [ ] Testei com uma lista onde **todos** os produtos têm estoque zero

## Como conferir a igualdade das saídas

Rode os dois e compare com o terminal, em vez de olhar a olho nu:

```bash
python monolito.py > saida_antiga.txt
python estoque_refatorado.py > saida_nova.txt
diff saida_antiga.txt saida_nova.txt
```

Se o `diff` não imprimir nada, as saídas são idênticas. No Windows sem `diff`, use
`fc saida_antiga.txt saida_nova.txt`.

## Desafio dentro do desafio

Três listas paralelas (`produtos`, `precos`, `estoque`) que precisam ficar sempre na mesma ordem são
um convite ao erro: basta alguém acrescentar um produto e esquecer o preço. Escreva em um comentário
como você guardaria esses dados de um jeito mais seguro. O módulo 09 dá uma pista.

---

Gabarito: [gabaritos/modulo-08/ex03-quebrando-o-monolito/](../../gabaritos/modulo-08/ex03-quebrando-o-monolito/), depois de tentar, não antes.
