# Gabarito — Módulo 12, Exercício 01: Lendo código alheio

Enunciado: [EXERCICIO-01-lendo-codigo-alheio.md](../../modulo-12-leitura-e-refatoracao/exercicios/EXERCICIO-01-lendo-codigo-alheio.md)

---

## Parte 1 — Os nomes

| Nome atual | O que guarda | Nome proposto |
| --- | --- | --- |
| `p` | a função que processa e devolve os preços | `calcular_precos` |
| `d` | a lista de itens a processar | `itens` |
| `f` | o fator da taxa aplicada (0.1 = 10%) | `taxa` |
| `t` | quantas chamadas recursivas ainda são permitidas | `limite_de_recursao` |
| `r` | a lista de resultados sendo montada | `resultados` |
| `v` | o valor acumulado do item atual | `valor_do_item` |
| `tx` | o desconto calculado sobre o valor | `desconto` |

Nenhum desses nomes é adivinhável sem ler o corpo inteiro da função. Esse é o custo real de nomes
curtos: eles economizam segundos de digitação e cobram minutos de leitura, toda vez.

## Parte 2 — O rastreio

`p([30, 60, 100])` — os três itens são números, não dicionários.

**a)** Três voltas, uma por item.

**b)** Todos caem no `else`. O `isinstance(d[i], dict)` é falso para os três, porque são inteiros.
Todo o bloco grande do `if` — taxas, tipos especiais, recursão — **não executa nenhuma vez**.

**c)** O `else` faz `d[i] * 0.8 if d[i] > 50 else d[i] * 0.9`:

| Item | Maior que 50? | Conta | Resultado |
| --- | --- | --- | --- |
| 30 | não | `30 * 0.9` | `27.0` |
| 60 | sim | `60 * 0.8` | `48.0` |
| 100 | sim | `100 * 0.8` | `80.0` |

**d)** `[27.0, 48.0, 80.0]`

> **A descoberta que importa:** o exemplo de teste do arquivo exercita apenas o `else`, que tem
> duas linhas. Os outros 20 e poucos linhas de lógica — dicionários, `mult`, `special`, `type` —
> **nunca rodam**. Um leitor apressado acharia que entendeu o programa depois de rodar e ver a
> saída. Ver o resultado não é entender o código.

## Parte 3 — Os cinco problemas

1. **Nomes de uma letra** (`p`, `d`, `f`, `t`, `r`, `v`, `tx`) — sinal "nomes de uma letra".
2. **Números soltos** (`0.1`, `10`, `100`, `1.5`, `1.2`, `1.1`, `0.8`, `0.9`, `3`) — sinal "números
   mágicos". De onde vem o `% 3` que decide a taxa? Ninguém sabe.
3. **Indentação profunda** — chega a cinco níveis: `for` → `if` → `for` → `if` → `if`.
4. **Função gigante fazendo coisas demais** — soma valores, aplica taxa, aplica multiplicador,
   trata tipos especiais e ainda chama a si mesma.
5. **Expressão ilegível na recursão** — `v += d[i][k] * p(d[:i], f, t-1)[0] if t > 0 else 0` junta
   chamada recursiva, fatiamento, indexação e condicional numa linha só.

## Parte 4 — Para que serve o `t`

`t` é o **limite de profundidade da recursão**: um contador que impede a função de se chamar
infinitamente.

A função chama a si mesma com `p(d[:i], f, t-1)`. A cada chamada, `t` diminui. Quando chega a zero,
o `if t > 0 else 0` para de recorrer e devolve `0`.

**Sem ele**, a recursão só pararia quando `d[:i]` ficasse vazio. Como `i` começa em 0 na chamada
seguinte e `d[:0]` é lista vazia, o laço não roda e a recursão para sozinha. Ou seja: `t` é uma
proteção **redundante** neste código — um cinto de segurança para um risco que a fatia já elimina.

Isso é comum em código real: proteções que sobraram de uma versão anterior, que ninguém removeu
porque ninguém tem certeza de que dá. E é justamente por isso que **reescrever do zero é perigoso**:
você joga fora as proteções junto com o resto, sem saber quais eram necessárias.

## Depois de terminar

A versão `_depois.py` renomeia os parâmetros e quebra a função em partes. Compare com as suas
propostas — divergências de nome são normais e não significam erro. O que importa é se o nome que
você escolheu responde à pergunta "o que isto guarda?" sem precisar ler o corpo.
