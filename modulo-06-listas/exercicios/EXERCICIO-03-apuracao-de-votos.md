# Exercício 03 — Apuração de votos (desafio)

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 3 de 3 | 50 min | listas paralelas, `index`, acumuladores, empate, percentuais |

## Objetivo

Apurar uma votação: contar votos, calcular percentuais, achar o vencedor e — a parte difícil —
**detectar empate**. É o exercício em que a lista deixa de ser depósito de números e vira estrutura
de um problema com regras próprias.

## Requisitos

1. Crie um arquivo `apuracao_de_votos.py`.
2. Comece com os candidatos fixos e uma lista de contagem zerada:

```python
candidatos = ["Ana", "Bruno", "Carla", "Diego"]
votos = [0, 0, 0, 0]
```

3. Leia votos repetidamente: o usuário digita o **número** do candidato (1 a 4), `0` para branco,
   ou `-1` para encerrar a apuração.
4. Voto fora dessa faixa é **nulo** — conte-o à parte e avise, sem encerrar.
5. Ao final, exiba:
   - a tabela de candidatos com votos e percentual sobre os **votos válidos**
   - total de votos válidos, brancos, nulos e o total geral
   - o vencedor, com seus votos e percentual
   - se houve **empate** na primeira colocação, informe todos os empatados
   - se o vencedor teve mais de 50% dos válidos, informe que houve maioria absoluta
6. Se ninguém votou em ninguém, avise em vez de calcular percentuais.

**Restrição:** sem funções (módulo 08) e sem `try` (módulo 10). Valide com `if`.

## Exemplo de saída

```text
Voto (1-4, 0=branco, -1=encerra): 1
Voto (1-4, 0=branco, -1=encerra): 3
Voto (1-4, 0=branco, -1=encerra): 1
Voto (1-4, 0=branco, -1=encerra): 9
  Voto NULO registrado.
Voto (1-4, 0=branco, -1=encerra): 0
Voto (1-4, 0=branco, -1=encerra): 3
Voto (1-4, 0=branco, -1=encerra): -1

========================================
           APURAÇÃO ENCERRADA
========================================
Candidato       Votos    % válidos
Ana                 2        50.00
Bruno               0         0.00
Carla               2        50.00
Diego               0         0.00
----------------------------------------
Votos válidos:      4
Brancos:            1
Nulos:              1
Total geral:        6
========================================
EMPATE entre: Ana, Carla (2 votos cada)
Sem maioria absoluta.
========================================
```

## As três partes difíceis

**Listas paralelas.** `candidatos[i]` e `votos[i]` se referem à mesma pessoa. Toda a apuração
depende dessa correspondência — e o módulo 08 vai mostrar por que isso é frágil. Por ora, mantenha
o cuidado.

**O empate.** Achar o maior valor é fácil (`max(votos)`). Descobrir **quantos** candidatos têm esse
valor exige percorrer de novo, contando. Se mais de um tiver, é empate — e você precisa listar
todos, não só o primeiro.

**O percentual sobre válidos.** Brancos e nulos entram no total geral, mas **não** no denominador
do percentual. Um candidato com 2 de 4 válidos tem 50%, mesmo que o total geral seja 6.

## Critérios de aceitação

- [ ] Votos nulos são contados e avisados, sem encerrar a apuração
- [ ] O `-1` encerra e o `0` conta como branco
- [ ] Os percentuais somam 100% (ou muito perto, por arredondamento)
- [ ] O empate do exemplo acima é detectado e lista os **dois** nomes
- [ ] Um vencedor único é anunciado sem falar em empate
- [ ] Maioria absoluta é detectada corretamente — teste com 3 votos para um só
- [ ] Encerrar sem nenhum voto válido não gera `ZeroDivisionError`
- [ ] As colunas ficam alinhadas

## Confira o caso do empate

Com os votos do exemplo: Ana 2, Carla 2, Bruno 0, Diego 0. O maior é 2, e **dois** candidatos o
têm — então é empate. Se o seu programa anunciar só "Ana venceu", ele está pegando o primeiro que
encontrou e ignorando a regra.

## Desafio dentro do desafio

Em eleição real, empate na primeira colocação se resolve por critério de desempate — o mais velho,
por exemplo. Acrescente uma lista `idades` e use-a para desempatar. E responda em um comentário: com
três listas paralelas em vez de duas, quanto mais fácil ficou errar? O módulo 09 resolve isso.

---

Gabarito: [gabaritos/modulo-06-ex03-apuracao-de-votos/](../../gabaritos/modulo-06-ex03-apuracao-de-votos/) —
depois de tentar, não antes.
