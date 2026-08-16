# Exercício 01 — Implementando os três

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 1 de 3 | 40 min | laços aninhados, troca de variáveis, índices |

## Objetivo

Escrever Bubble, Selection e Insertion Sort do zero, sem consultar o README enquanto escreve. É
fixação pura: os três são curtos, e a dificuldade está nos detalhes de índice.

## Requisitos

1. Crie um arquivo `tres_ordenacoes.py`.
2. Escreva as três funções. Cada uma recebe uma lista e a ordena **no lugar** (como `sort()` faz).
3. Nenhuma pode usar `sort()`, `sorted()`, `min()` ou `max()`.
4. Teste as três com as mesmas quatro listas:

```python
LISTAS_DE_TESTE = [
    [64, 34, 25, 12, 22, 11],       # embaralhada
    [1, 2, 3, 4, 5],                # já ordenada
    [5, 4, 3, 2, 1],                # ordem inversa (pior caso)
    [7],                            # um elemento só
]
```

5. Para cada lista e cada algoritmo, mostre antes e depois.
6. Confirme que o resultado bate com `sorted()`, sem usá-lo dentro das funções, só na conferência.

## Exemplo de saída

```text
=== BUBBLE SORT ===
[64, 34, 25, 12, 22, 11] -> [11, 12, 22, 25, 34, 64]  OK
[1, 2, 3, 4, 5]          -> [1, 2, 3, 4, 5]           OK
[5, 4, 3, 2, 1]          -> [1, 2, 3, 4, 5]           OK
[7]                      -> [7]                       OK

=== SELECTION SORT ===
...
```

## Os três detalhes que derrubam

1. **Bubble:** o laço interno vai até `n - i - 1`. Usar `n` dá `IndexError` no `lista[j + 1]`.
2. **Selection:** guarde o **índice** do menor, não o valor. Sem o índice, não há como trocar.
3. **Insertion:** o `while` precisa do `j -= 1` **dentro** dele. Esquecer é loop infinito.

## Critérios de aceitação

- [ ] As três funções ordenam corretamente as quatro listas
- [ ] Nenhuma usa `sort`, `sorted`, `min` ou `max`
- [ ] As três ordenam **no lugar**: a lista original passada muda
- [ ] A lista de um elemento só não quebra nenhuma
- [ ] A lista vazia `[]` também não quebra: teste
- [ ] A conferência com `sorted()` passa nas 12 combinações

## Desafio opcional

Acrescente ao Bubble a otimização da bandeira: se uma passagem inteira não fizer nenhuma troca, a
lista já está ordenada e dá para parar. Meça quantas passagens ele economiza com a lista já
ordenada.

---

Gabarito: [gabaritos/modulo-11-ex01-implementando-os-tres/](../../gabaritos/modulo-11-ex01-implementando-os-tres/), depois de tentar, não antes.
