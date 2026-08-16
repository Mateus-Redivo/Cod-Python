# Módulo 11 — Algoritmos de ordenação

Desde o módulo 06 você ordena listas com `sort()`. Uma palavra, e pronto.

Este módulo abre essa caixa. Não porque você vá escrever seu próprio `sort` na vida real (não vai),
mas porque **ordenar é o exemplo mais claro de que existe mais de um jeito de resolver o mesmo
problema, e de que alguns são muito melhores que outros**.

É o primeiro módulo em que a pergunta deixa de ser "funciona?" e passa a ser "quanto custa?".

## Objetivos de aprendizagem

Ao final deste módulo você será capaz de:

- [ ] Explicar como Bubble, Selection e Insertion Sort funcionam
- [ ] Implementar os três do zero
- [ ] Contar comparações e trocas para comparar algoritmos com números
- [ ] Explicar por que Bubble Sort é o mais lento dos três na prática
- [ ] Descrever a ideia do Quick Sort e por que ele é mais rápido
- [ ] Justificar por que, no dia a dia, você deve usar `sort()` mesmo assim

## Pré-requisitos

[Módulo 10 — Tratamento de erros](../modulo-10-tratamento-de-erros/) concluído. O que realmente
importa aqui são os módulos 05, 06 e 08: laços aninhados, índices de lista e funções.

## Conceito

### O problema: ordenar parece trivial até você tentar

Peça a alguém para ordenar cinco cartas na mão e a pessoa faz sem pensar. Agora descreva **o
procedimento exato**, passo a passo, sem usar a palavra "ordene". É aí que fica difícil, e é por
isso que existem vários algoritmos: são descrições diferentes da mesma tarefa.

Todos usam duas operações só:

```python
lista[i] > lista[j]                              # comparar
lista[i], lista[j] = lista[j], lista[i]          # trocar
```

A troca é aquele truque do módulo 01, que voltou.

### Bubble Sort: empurra o maior para o fim

A cada passagem, compara vizinhos e troca os que estão fora de ordem. O maior valor vai
"borbulhando" até o fim.

```python
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
```

O `n - i - 1` é o detalhe que importa: depois de `i` passagens, os `i` últimos elementos **já estão
no lugar certo**, e não precisam ser olhados de novo.

É o mais fácil de entender e o mais lento dos três.

### Selection Sort: acha o menor e traz para a frente

Percorre a parte não ordenada procurando o menor valor e o coloca na posição atual.

```python
def selection_sort(lista):
    for i in range(len(lista)):
        indice_do_menor = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[indice_do_menor]:
                indice_do_menor = j
        lista[i], lista[indice_do_menor] = lista[indice_do_menor], lista[i]
```

É o padrão "achar o maior" do módulo 06, repetido: só que procurando o **menor** e guardando o
**índice**, não o valor.

Faz o mesmo número de comparações que o Bubble, mas **muito menos trocas**: no máximo uma por
passagem.

### Insertion Sort: como se organiza cartas na mão

Pega cada elemento e o insere na posição certa entre os que já estão ordenados.

```python
def insertion_sort(lista):
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > atual:
            lista[j + 1] = lista[j]     # empurra para a direita
            j -= 1
        lista[j + 1] = atual            # encaixa no lugar
```

É o mais rápido dos três quando a lista já está **quase ordenada** (caso comum na prática). Se
estiver totalmente ordenada, ele só percorre uma vez e não move nada.

### Quick Sort: divida para conquistar

Os três anteriores comparam elemento com elemento. O Quick Sort muda a estratégia: escolhe um valor
(o **pivô**), separa quem é menor de quem é maior, e repete o processo em cada metade.

```python
def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivo = lista[0]
    menores = [x for x in lista[1:] if x <= pivo]
    maiores = [x for x in lista[1:] if x > pivo]

    return quick_sort(menores) + [pivo] + quick_sort(maiores)
```

Repare que a função **chama a si mesma**. Isso se chama **recursão**, e é conteúdo além desta
trilha: está aqui para você reconhecer, não para dominar. A ideia central é o que importa:
dividir o problema em dois menores é mais barato que atacar tudo de uma vez.

### Quanto custa: comparando com números

Ordenando a mesma lista `[64, 34, 25, 12, 22, 11, 90, 45, 78, 3]`:

| Algoritmo | Comparações | Trocas / movimentações |
| --- | --- | --- |
| Bubble Sort | 45 | 26 |
| Selection Sort | 45 | 10 |
| Insertion Sort | 30 | 26 |

Bubble e Selection comparam a mesma quantidade: os dois olham todos os pares. A diferença está nas
trocas: o Selection faz **uma por passagem**, no máximo, enquanto o Bubble troca a cada par fora de
ordem que encontra.

O Insertion compara menos porque o `while` dele **para assim que acha o lugar certo**, sem varrer o
resto.

Estes números são reais, medidos pelo [exemplo 04](exemplos/04_comparando_custos.py), que conta
para você ver, com qualquer lista que você inventar.

O que muda tudo é a **escala**. Bubble, Selection e Insertion fazem, no pior caso, um número de
comparações proporcional a `n²`. Quick Sort faz proporcional a `n × log n`:

| Tamanho da lista | `n²` | `n × log n` |
| --- | --- | --- |
| 10 | 100 | ~33 |
| 100 | 10.000 | ~664 |
| 1.000 | 1.000.000 | ~9.966 |
| 10.000 | 100.000.000 | ~132.877 |

Com 10 elementos, a diferença é irrelevante. Com 10 mil, é a diferença entre instantâneo e
inviável. **É por isso que a escolha do algoritmo importa**, e por isso ninguém usa Bubble Sort
para valer.

### E na vida real, o que usar?

`lista.sort()`. Sempre.

O Python usa um algoritmo chamado Timsort, escrito em C, testado por milhares de pessoas ao longo de
décadas, que reconhece trechos já ordenados e se adapta. Nada que você escreva vai chegar perto.

Então por que estudar os outros? Porque a habilidade que fica não é "escrever um sort", é **saber
que a mesma tarefa admite soluções com custos muito diferentes**, e reconhecer quando isso importa.
Essa pergunta vai te acompanhar em todo problema daqui para frente.

## Exemplos guiados

| Arquivo | O que mostra |
| --- | --- |
| [exemplos/01_bubble_sort.py](exemplos/01_bubble_sort.py) | passo a passo, mostrando a lista a cada passagem |
| [exemplos/02_selection_e_insertion.py](exemplos/02_selection_e_insertion.py) | os outros dois, com o mesmo detalhamento |
| [exemplos/03_quick_sort.py](exemplos/03_quick_sort.py) | divisão em torno do pivô |
| [exemplos/04_comparando_custos.py](exemplos/04_comparando_custos.py) | contando comparações e trocas de verdade |

Para rodar qualquer um deles:

```bash
cd modulo-11-algoritmos-de-ordenacao/exemplos
python 01_bubble_sort.py
```

## Exercícios

1. [EXERCICIO-01-implementando-os-tres.md](exercicios/EXERCICIO-01-implementando-os-tres.md) (nível 1): escrever Bubble, Selection e Insertion do zero.
2. [EXERCICIO-02-contando-operacoes.md](exercicios/EXERCICIO-02-contando-operacoes.md) (nível 2): instrumentar os três e comparar com números.
3. [EXERCICIO-03-ordenando-registros.md](exercicios/EXERCICIO-03-ordenando-registros.md) (nível 3): ordenar uma tabela por qualquer coluna.

## Auto-avaliação

- [ ] Explico o Bubble Sort para alguém sem usar a palavra "ordenar"
- [ ] Sei por que o Bubble usa `n - i - 1` no laço interno
- [ ] Sei por que o Selection faz menos trocas que o Bubble
- [ ] Sei em que situação o Insertion é o melhor dos três
- [ ] Explico a ideia do pivô do Quick Sort
- [ ] Sei justificar por que, mesmo assim, uso `sort()` no dia a dia

## Erros comuns

| Erro | O que está acontecendo |
| --- | --- |
| `IndexError` no Bubble | o laço interno passou do fim; use `range(n - i - 1)` |
| A lista não ordena por completo | faltou o laço externo repetir as passagens |
| Troca que perde valor | `a = b; b = a` não troca; use `a, b = b, a` |
| Selection guardando o valor, não o índice | você precisa do índice para trocar depois |
| `while` do Insertion em loop infinito | faltou o `j -= 1` dentro do laço |
| Comparar `lista[j] > lista[j + 1]` no último elemento | não existe `j + 1` ali; o limite do `range` protege |
| Achar que seu sort é rápido | teste com 5.000 elementos e compare com `sort()` |

---

Anterior: [Módulo 10 — Tratamento de erros](../modulo-10-tratamento-de-erros/) | Próximo: [Módulo 12 — Leitura e refatoração](../modulo-12-leitura-e-refatoracao/)
