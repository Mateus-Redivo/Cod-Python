# Exercício 02 — Média com validação

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 2 de 3 | 30 min | `for`, `while` dentro de `for`, acumulador, validação |

## Objetivo

Ler 5 notas do usuário, recusando qualquer valor fora do intervalo permitido, e mostrar a média.

## Requisitos

1. Peça ao usuário 5 notas, uma por vez.
2. Uma nota válida é um valor entre 0 e 10, inclusive os extremos.
3. Se a nota for inválida, avise e **peça de novo** — quantas vezes for preciso. O usuário pode
   errar cinco vezes seguidas na mesma nota; o programa não pode desistir nem seguir em frente com
   o valor ruim.
4. Ao final, mostre a média das 5 notas com duas casas decimais.
5. Use `for` para as 5 repetições e `while` para a validação de cada nota.

## Exemplo de saída

```text
Digite a 1a nota (0 a 10): 8
Digite a 2a nota (0 a 10): 12
Nota inválida! Digite um valor entre 0 e 10.
Digite a 2a nota (0 a 10): -3
Nota inválida! Digite um valor entre 0 e 10.
Digite a 2a nota (0 a 10): 7
Digite a 3a nota (0 a 10): 6
Digite a 4a nota (0 a 10): 9
Digite a 5a nota (0 a 10): 5
Média das 5 notas = 7.00
```

## Critérios de aceitação

- [ ] O programa aceita exatamente 5 notas válidas, nem mais nem menos
- [ ] Uma nota inválida **não** entra na soma
- [ ] Digitar 0 ou 10 é aceito (os extremos são válidos)
- [ ] Errar três vezes seguidas na mesma nota continua funcionando
- [ ] A média sai com duas casas decimais
- [ ] O número da nota na pergunta ("2a nota") acompanha o laço, não fica fixo

## Armadilha conhecida

A condição de "nota inválida" precisa de `or`, não de `and`:

```python
while nota < 0 or nota > 10:      # certo
while nota < 0 and nota > 10:     # nunca é verdade: o laço nem começa
```

Nenhum número é menor que 0 **e** maior que 10 ao mesmo tempo.

## Desafio opcional

Conte quantas tentativas inválidas o usuário fez no total e mostre esse número no final.

---

Gabarito: [gabaritos/modulo-05-ex02-media-com-validacao/](../../gabaritos/modulo-05-ex02-media-com-validacao/) —
depois de tentar, não antes.
