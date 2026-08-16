# Exercício 01 — Conversor de medidas

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 1 de 3 | 25 min | `input`, `float`, f-string, `:.2f` |

## Objetivo

Escrever o primeiro programa que conversa: pergunta, calcula e devolve o resultado formatado.

## Requisitos

1. Crie um arquivo `conversor_de_medidas.py`.
2. Pergunte ao usuário uma temperatura em graus **Celsius**.
3. Converta para **Fahrenheit** e para **Kelvin**:
   - `F = C * 9 / 5 + 32`
   - `K = C + 273.15`
4. Exiba os três valores com **uma** casa decimal.
5. Converta o `input()` com `float()`, não `int()`: temperatura tem casas decimais.
6. Use constantes nomeadas para o `273.15` e para os fatores da conversão.

## Exemplo de saída

```text
Digite a temperatura em Celsius: 25

25.0 °C equivale a:
  77.0 °F
  298.1 K
```

Confira: 25 x 9 / 5 + 32 = 45 + 32 = 77. E 25 + 273.15 = 298.15, que com uma casa vira 298.1.

> Repare no arredondamento: `298.15` exibido com uma casa vira `298.1`, não `298.2`. Isso é a
> poeirinha dos decimais do módulo 02 aparecendo de novo. Não é erro seu.

## Critérios de aceitação

- [ ] O programa funciona para qualquer temperatura, inclusive negativa
- [ ] A conversão usa `float()`, e digitar `36.6` não quebra o programa
- [ ] Os três valores saem com exatamente uma casa decimal
- [ ] O `273.15` não aparece solto no meio da conta
- [ ] Testei com `-40` (a temperatura em que Celsius e Fahrenheit se encontram)

## Desafio opcional

Faça o caminho inverso: pergunte também qual unidade o usuário está informando. Ainda não dá para
decidir com `if` (isso é o módulo 04), então por enquanto escreva **dois programas separados** e
guarde a pergunta: "como eu escolheria entre eles?"

---

Gabarito: [gabaritos/modulo-03-ex01-conversor-de-medidas/](../../gabaritos/modulo-03-ex01-conversor-de-medidas/), depois de tentar, não antes.
