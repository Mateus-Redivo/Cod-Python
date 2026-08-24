# Exercício 01 — Calculadora de tempo

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 1 de 3 | 25 min | `//`, `%`, f-string, variáveis |

## Objetivo

Converter uma quantidade de segundos em horas, minutos e segundos: o problema que a dupla `//` e
`%` resolve melhor que qualquer outra ferramenta.

## Requisitos

1. Crie um arquivo `calculadora_de_tempo.py`.
2. Defina uma variável com um total de segundos (por exemplo, `10000`). Ainda não é preciso pedir
   ao usuário: `input()` é assunto do módulo 03.
3. Calcule quantas **horas**, **minutos** e **segundos** completos esse total representa.
4. Use apenas `//` e `%`. Nada de `if`, e nada de arredondar com `round()`.
5. Exiba o resultado no formato do exemplo, e também no formato `HH:MM:SS`.
6. Use constantes para os números mágicos (`SEGUNDOS_POR_HORA = 3600`, etc.).

## Exemplo de saída

```text
Total: 10000 segundos

Equivale a: 2 h, 46 min e 40 s
No relógio:  02:46:40
```

Confira na mão: 2 x 3600 = 7200; 46 x 60 = 2760; 7200 + 2760 + 40 = 10000. Bate.

## Dicas

O padrão é sempre o mesmo: `//` pega a unidade maior, `%` guarda o que sobrou para a próxima.

```python
horas = total // SEGUNDOS_POR_HORA
resto = total % SEGUNDOS_POR_HORA
```

Para o formato `02:46:40`, a f-string preenche com zero à esquerda com `{horas:02d}`.

## Critérios de aceitação

- [ ] O programa funciona para qualquer total de segundos, não só para o exemplo
- [ ] Não há nenhum `if` no código
- [ ] Os números 3600 e 60 aparecem como constantes nomeadas, não soltos no meio das contas
- [ ] O formato `HH:MM:SS` mostra dois dígitos mesmo quando o valor é menor que 10
- [ ] Testei com `59` (menos de um minuto) e com `86399` (um segundo antes de 24h)

## Desafio opcional

Acrescente o cálculo de **dias**. E responda em um comentário: o que acontece com o formato
`HH:MM:SS` quando o total passa de 24 horas?

---

Gabarito: [gabaritos/modulo-02/ex01-calculadora-de-tempo/](../../gabaritos/modulo-02/ex01-calculadora-de-tempo/), depois de tentar, não antes.
