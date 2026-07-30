# Exercício 03 — Simulador de troco (desafio)

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 3 de 3 | 45 min | tipos, conversão, `//`, `%`, constantes, precisão de `float` |

## Objetivo

Calcular o troco de uma compra e decompô-lo em notas e moedas. É o primeiro exercício em que a
**escolha do tipo** deixa de ser detalhe e passa a ser a diferença entre acertar e errar por um
centavo.

## Requisitos

1. Crie um arquivo `simulador_de_troco.py`.
2. Defina duas variáveis fixas no código: `valor_da_compra` e `valor_pago`. Ainda não use `input()`
   — ele é do módulo 03.
3. Calcule o troco.
4. Decomponha o troco em: notas de 50, 20, 10, 5 e 2; moedas de 1 real, 50, 25, 10, 5 e 1 centavo.
5. Exiba apenas as denominações cuja quantidade for maior que zero.
6. Use constantes nomeadas para cada denominação.
7. Exiba o total conferido no fim: some tudo que você distribuiu e mostre que bate com o troco.

**Restrição:** não use `if` (módulo 04), listas (módulo 06) nem laços (módulo 05). Só `//`, `%`,
variáveis e `print`. Para o requisito 5, veja a dica abaixo.

## Exemplo de saída

```text
Compra:  R$ 37.45
Pago:    R$ 50.00
Troco:   R$ 12.55

10 x 1 = R$ 10.00
 2 x 1 = R$  2.00
50c x 1 = R$  0.50
 5c x 1 = R$  0.05

Conferência: R$ 12.55
```

## A armadilha central

Este é o coração do exercício. A tentação é guardar o troco como `float` e multiplicar por 100 para
virar centavos:

```python
troco = 19.99
centavos = int(troco * 100)
```

Rode isso e confira o resultado: sai **1998**, não 1999.

O motivo é a poeirinha dos decimais que você viu no módulo 02 — `19.99 * 100` dá
`1998.9999999999998`. E o `int()` **corta** em vez de arredondar, então o centavo desaparece em
silêncio. Não dá erro, não dá aviso: o programa só entrega um resultado errado.

> Nem todo valor falha. `12.55 * 100` dá exatamente `1255.0` e passaria despercebido. É isso que
> torna o bug traiçoeiro: ele aparece em alguns valores e não em outros, então testar com um número
> só não pega nada.

**A solução é trabalhar em centavos desde o começo**, como inteiros:

```python
VALOR_DA_COMPRA_EM_CENTAVOS = 3745
VALOR_PAGO_EM_CENTAVOS = 5000
troco = VALOR_PAGO_EM_CENTAVOS - VALOR_DA_COMPRA_EM_CENTAVOS   # 1255, exato
```

Aí toda a decomposição é aritmética de inteiros, sem nenhuma imprecisão. Na hora de **exibir**,
divida por 100. Este é o motivo real pelo qual sistemas financeiros guardam dinheiro em centavos
inteiros, e não em `float`.

## Dica para o requisito 5

Sem `if`, você não consegue esconder as linhas com quantidade zero. Faça o programa completo
primeiro, exibindo todas as denominações — inclusive as zeradas. Depois, em um comentário, escreva
qual `if` você usaria. O módulo 04 fecha essa lacuna.

## Critérios de aceitação

- [ ] O troco está correto até o último centavo, conferido na calculadora
- [ ] A conferência final bate exatamente com o troco calculado
- [ ] Nenhum valor monetário é guardado como `float` durante os cálculos
- [ ] As denominações estão em constantes nomeadas
- [ ] Testei com um troco que exige moeda de 1 centavo (por exemplo, compra de 19.99, pago 20.00)
- [ ] Testei com pagamento exato (troco zero) e o programa não quebra
- [ ] Não há `if`, laço nem lista no código

## Desafio dentro do desafio

E se o valor pago for **menor** que a compra? Hoje seu programa calcula um troco negativo e
distribui notas negativas, sem reclamar. Escreva em um comentário o que deveria acontecer — e qual
recurso, de qual módulo, você precisa para tratar isso.

---

Gabarito: [gabaritos/modulo-01-ex03-simulador-de-troco/](../../gabaritos/modulo-01-ex03-simulador-de-troco/) —
depois de tentar, não antes.
