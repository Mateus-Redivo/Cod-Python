# Exercício 02 — Calculadora com menu

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 2 de 3 | 40 min | `match/case`, proteção de operação, `input`, f-string |

## Objetivo

Escrever uma calculadora que mostra um menu, executa a operação escolhida e não quebra quando o
usuário pede algo impossível.

## Requisitos

1. Crie um arquivo `calculadora_com_menu.py`.
2. Exiba um menu com quatro operações: soma, subtração, multiplicação e divisão.
3. Peça a opção (1 a 4) e depois os dois números.
4. Use **`match/case`** para escolher a operação: este é o caso em que ele lê melhor que `elif`.
5. Na divisão, **verifique se o segundo número é zero antes de dividir**. Avise em vez de quebrar.
6. Trate a opção inválida com `case _`.
7. Exiba o resultado com duas casas decimais, mostrando a conta completa.

**Restrição:** não use `try/except` (módulo 10) nem funções (módulo 08). Só o que você tem até aqui.

## Exemplo de saída

```text
===== CALCULADORA =====
1 - Somar
2 - Subtrair
3 - Multiplicar
4 - Dividir
=======================
Escolha a operação (1-4): 4
Primeiro número: 10
Segundo número: 4

10.00 / 4.00 = 2.50
```

Com divisão por zero:

```text
Escolha a operação (1-4): 4
Primeiro número: 10
Segundo número: 0

Não é possível dividir por zero.
```

Com opção inválida:

```text
Escolha a operação (1-4): 9
Primeiro número: 1
Segundo número: 2

Opção inválida. Escolha entre 1 e 4.
```

## Critérios de aceitação

- [ ] As quatro operações funcionam e o resultado está correto
- [ ] A escolha da operação usa `match/case`, não uma cadeia de `elif`
- [ ] Dividir por zero avisa e não gera `ZeroDivisionError`
- [ ] Uma opção fora de 1 a 4 cai no `case _` com mensagem clara
- [ ] Os números são lidos com `float()`, e `2.5` funciona
- [ ] O resultado sai com duas casas decimais
- [ ] Não há `try/except` nem `def` no código

## Sobre a ordem das perguntas

Repare que o exemplo pede os números **mesmo quando a opção é inválida**. Isso é meio bobo: o
ideal seria só perguntar depois de validar a opção. Faça funcionar primeiro do jeito simples;
depois, se quiser, reorganize. E note a limitação: você consegue **avisar** que a opção é inválida,
mas não consegue **perguntar de novo**. Repetir é assunto do módulo 05.

## Desafio opcional

Acrescente uma quinta opção: potência (`primeiro ** segundo`). E responda em um comentário: com
`case 5`, quantas linhas você precisou mudar? Se estivesse escrito com `elif`, seriam mais ou
menos?

---

Gabarito: [gabaritos/modulo-04-ex02-calculadora-com-menu/](../../gabaritos/modulo-04-ex02-calculadora-com-menu/), depois de tentar, não antes.
