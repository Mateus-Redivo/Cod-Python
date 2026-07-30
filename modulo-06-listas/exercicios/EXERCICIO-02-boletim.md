# Exercício 02 — Boletim

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 2 de 3 | 35 min | listas, `append`, `for`, `len`, `sum`, `max`, `min` |

## Objetivo

Ler várias notas para dentro de uma lista e produzir um resumo — o programa que era impossível de
escrever antes deste módulo, porque a quantidade de notas é decidida pelo usuário.

## Requisitos

1. Crie um arquivo `boletim.py`.
2. Pergunte **quantas notas** o usuário vai digitar.
3. Leia essa quantidade de notas, guardando todas em **uma lista** com `append()`.
4. Valide cada nota: só aceite valores de 0 a 10, insistindo com `while` até vir um válido.
5. Exiba um resumo com: a lista completa, a quantidade, a soma, a média (2 casas), a maior e a menor
   nota.
6. Exiba também quantas notas ficaram **acima da média** — isso exige um segundo `for`, depois de a
   média existir.
7. Classifique a turma: média `>= 7.0` é "Aprovada", `>= 5.0` é "Recuperação", abaixo disso
   "Reprovada".
8. **Proteja a divisão**: se a quantidade for zero, avise e não calcule nada.

## Exemplo de saída

```text
Quantas notas? 5
Nota 1: 8
Nota 2: 12
Nota inválida! Digite um valor entre 0 e 10.
Nota 2: 7.5
Nota 3: 9
Nota 4: 6.5
Nota 5: 10

===== BOLETIM =====
Notas:   [8.0, 7.5, 9.0, 6.5, 10.0]
Quantidade: 5
Soma:       41.00
Média:      8.20
Maior:      10.0
Menor:      6.5
Acima da média: 2
Situação: Aprovada
```

Confira na mão: a média é 8.2, e só o 9.0 e o 10.0 estão acima dela. O 8.0 fica **abaixo** — é o
tipo de detalhe que só aparece quando você confere em vez de confiar.

## Critérios de aceitação

- [ ] As notas ficam todas em **uma** lista, não em variáveis numeradas
- [ ] Uma nota inválida não entra na lista e a pergunta se repete
- [ ] Digitar `0` como quantidade não gera `ZeroDivisionError`
- [ ] A média sai com duas casas decimais
- [ ] A contagem de "acima da média" está correta — confira na mão
- [ ] O programa funciona para 1 nota e para 20 notas, sem mudar o código

## Armadilha conhecida

Você **não consegue** contar quantas notas estão acima da média dentro do mesmo laço que lê as
notas — porque a média só existe depois de todas terem sido lidas. São necessariamente dois laços:
um para coletar, outro para comparar. Perceber isso é metade do exercício.

## Desafio opcional

Exiba as notas em ordem decrescente, **sem destruir** a lista na ordem original de digitação.
Cuidado: `notas.sort()` modifica a lista no lugar. Qual é a função que devolve uma nova?

---

Gabarito: [gabaritos/modulo-06-ex02-boletim/](../../gabaritos/modulo-06-ex02-boletim/) —
depois de tentar, não antes.
