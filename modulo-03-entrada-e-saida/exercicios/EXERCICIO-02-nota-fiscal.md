# Exercício 02 — Nota fiscal

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 2 de 3 | 40 min | `input`, `int` vs `float`, formatação alinhada, `sep`/`end` |

## Objetivo

Montar uma nota fiscal simples com alinhamento de colunas: o exercício em que a formatação deixa
de ser enfeite e vira requisito.

## Requisitos

1. Crie um arquivo `nota_fiscal.py`.
2. Pergunte, para **três** produtos: nome, quantidade e preço unitário.
3. Escolha o tipo certo em cada conversão. Quantidade e preço não são o mesmo tipo de coisa:
   justifique sua escolha em um comentário.
4. Calcule o subtotal de cada produto (quantidade x preço) e o total geral.
5. Aplique 10% de desconto sobre o total. Use uma constante para a taxa.
6. Exiba uma tabela **alinhada**: nomes à esquerda, números à direita, valores com duas casas.
7. Use `"-" * 40` para desenhar as linhas separadoras.

## Exemplo de saída

```text
Produto 1
  Nome: Caneta
  Quantidade: 3
  Preço unitário: R$ 2.50

Produto 2
  Nome: Caderno
  Quantidade: 2
  Preço unitário: R$ 18.90

Produto 3
  Nome: Mochila
  Quantidade: 1
  Preço unitário: R$ 129.99

========================================
              NOTA FISCAL
========================================
Produto          Qtd    Unit.   Subtotal
----------------------------------------
Caneta             3     2.50       7.50
Caderno            2    18.90      37.80
Mochila            1   129.99     129.99
----------------------------------------
Total                             175.29
Desconto (10%)                     17.53
TOTAL A PAGAR                     157.76
========================================
```

Cada linha da tabela tem exatamente **40 caracteres**, do mesmo comprimento das linhas de `=` e `-`.

## Dicas de formatação

```python
f"{nome:<15}"        # texto, 15 caracteres, alinhado à esquerda
f"{quantidade:>5}"   # número, 5 caracteres, alinhado à direita
f"{preco:>9.2f}"     # número com 2 casas, 9 caracteres, à direita
```

A soma das larguras precisa bater com o comprimento da linha de `-`. Ajuste até as colunas ficarem
retas na vertical.

## Critérios de aceitação

- [ ] As colunas ficam alinhadas na vertical, com qualquer nome de produto até 15 caracteres
- [ ] Quantidade é `int` e preço é `float`, com o comentário justificando
- [ ] Todos os valores monetários saem com exatamente duas casas
- [ ] O total confere com a soma dos subtotais (confira na calculadora)
- [ ] As linhas separadoras usam multiplicação de string, não 40 traços digitados
- [ ] Testei com um nome longo, como "Estojo de canetas", e vi o que acontece com o alinhamento

## Desafio opcional

O desconto de 10% sobre 175.29 dá 17.529, que arredondado vira 17.53. Mas 175.29 - 17.53 = 157.76,
enquanto 175.29 x 0.9 = 157.761, que arredonda para 157.76 também. Neste caso bateu, mas nem sempre
bate. Encontre um valor de total em que as duas formas de calcular deem resultados **diferentes** na
segunda casa, e escreva em um comentário qual das duas você escolheria.

---

Gabarito: [gabaritos/modulo-03-ex02-nota-fiscal/](../../gabaritos/modulo-03-ex02-nota-fiscal/), depois de tentar, não antes.
