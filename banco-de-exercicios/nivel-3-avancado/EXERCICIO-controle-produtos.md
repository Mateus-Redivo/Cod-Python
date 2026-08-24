# Controle de produtos

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| Avançado | 40 min | matriz, busca em laço, acumulador, saída tabelada |

## O que fazer

Trabalhe com um estoque guardado em uma matriz, onde cada linha é um produto no formato
`[nome, preço, quantidade]`.

Use estes dados como ponto de partida:

```python
produtos = [
    ["Arroz", 22.90, 15],
    ["Feijão", 9.80, 8],
    ["Macarrão", 4.50, 20],
    ["Açúcar", 7.90, 12],
    ["Café", 18.50, 5]
]
```

## Requisitos

Nesta ordem:

1. Exiba todos os produtos em uma tabela alinhada, com cabeçalho.
2. Calcule e exiba o valor total do estoque (a soma de preço × quantidade de cada produto).
3. Encontre e exiba o produto mais caro.
4. Atualize o preço do café para R$ 22,90, procurando pelo nome sem diferenciar maiúsculas de
   minúsculas. Avise se o produto não for encontrado.
5. Exiba a tabela de novo, mostrando o preço atualizado.

## Exemplo de saída

```text
Lista de Produtos:
Produto         Preço (R$)   Quantidade
----------------------------------------
Arroz           R$ 22.90      15
Feijão          R$ 9.80       8
...

Valor total do estoque: R$ 699.20

Produto mais caro: Arroz - R$ 22.90

Atualizando preço do café para R$ 22.90...
Preço atualizado com sucesso!
```

## Critérios de aceitação

- [ ] O total considera a quantidade, não só a soma dos preços
- [ ] A busca pelo café acha "Café" mesmo procurando por "café"
- [ ] A busca para assim que encontra, em vez de percorrer o resto à toa
- [ ] Produto inexistente gera aviso, não erro
- [ ] A segunda tabela mostra o preço novo, provando que a matriz foi mesmo alterada

## Desafio opcional

Transforme cada etapa em uma função (`exibir`, `total_estoque`, `mais_caro`, `atualizar_preco`) e
depois acrescente uma quinta: listar só os produtos com quantidade abaixo de 10, para repor.

---

Gabarito: [gabaritos/banco-de-exercicios/nivel-3-avancado/controle-produtos/](../../gabaritos/banco-de-exercicios/nivel-3-avancado/controle-produtos/),
depois de tentar, não antes.

Pré-requisito: [Módulo 09 — Matrizes](../../modulo-09-matrizes/).
