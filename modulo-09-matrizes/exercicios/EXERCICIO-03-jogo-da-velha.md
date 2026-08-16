# Exercício 03 — Jogo da velha (desafio)

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 3 de 3 | 60 min | matriz, funções, validação, laços, condições de vitória |

## Objetivo

Construir um jogo da velha jogável para duas pessoas no mesmo teclado. É o primeiro programa da
trilha que junta **tudo**: matriz, funções, laços, validação e decisão.

## Requisitos

1. Crie um arquivo `jogo_da_velha.py`.
2. O tabuleiro é uma matriz 3x3, criada com laço (nunca `[[" "] * 3] * 3`).
3. Escreva, no mínimo:

| Função | Devolve |
| --- | --- |
| `criar_tabuleiro()` | matriz 3x3 vazia |
| `mostrar_tabuleiro(tabuleiro)` | nada: desenha o tabuleiro |
| `posicao_valida(tabuleiro, linha, coluna)` | `True` se está dentro e livre |
| `verificar_vitoria(tabuleiro, simbolo)` | `True` se o símbolo venceu |
| `tabuleiro_cheio(tabuleiro)` | `True` se não há mais espaço |

4. Os jogadores alternam entre `X` e `O`.
5. Cada jogada pede linha e coluna (1 a 3, não 0 a 2, o usuário não conta a partir do zero).
6. Uma jogada inválida (fora do tabuleiro ou em casa ocupada) **não passa a vez**: pergunte de novo.
7. O jogo termina quando alguém vence ou o tabuleiro enche (velha).

## Exemplo de saída

```text
   1   2   3
1    |   |
  ---+---+---
2    |   |
  ---+---+---
3    |   |

Jogador X - linha: 2
Jogador X - coluna: 2

   1   2   3
1    |   |
  ---+---+---
2    | X |
  ---+---+---
3    |   |

Jogador O - linha: 5
Posição inválida! Tente de novo.
Jogador O - linha: 1
Jogador O - coluna: 1
...

Jogador X venceu!
```

## As oito condições de vitória

Um símbolo vence se ocupar:

- qualquer uma das **3 linhas**
- qualquer uma das **3 colunas**
- qualquer uma das **2 diagonais**

Escrever oito `if` funciona, mas é o caminho longo. As linhas e colunas cabem em laços, e você já
sabe percorrer os dois sentidos, do exemplo 03. As diagonais são as duas do mesmo exemplo.

## Critérios de aceitação

- [ ] O jogo é jogável do início ao fim, sem travar
- [ ] Jogada fora do tabuleiro é recusada e a vez **não** passa
- [ ] Jogada em casa ocupada é recusada e a vez **não** passa
- [ ] Vitória é detectada nas 3 linhas, nas 3 colunas e nas 2 diagonais (teste as oito)
- [ ] O empate (velha) é detectado e anunciado
- [ ] O usuário digita 1 a 3, e o programa converte para o índice interno
- [ ] Nenhuma função usa `global`
- [ ] O tabuleiro foi criado com laço, não com `* 3`

## A armadilha da conversão

O usuário pensa em 1, 2, 3. A matriz pensa em 0, 1, 2. A conversão tem que acontecer **em um lugar
só**, logo depois da leitura:

```python
linha = int(input("linha: ")) - 1
```

Se você espalhar `- 1` por várias funções, uma hora vai esquecer em alguma, e o bug vai parecer
aleatório.

## Desafio dentro do desafio

Depois de funcionando, responda em um comentário: quantas linhas você mudaria para transformá-lo num
jogo 4x4 (quatro em linha)? Se a resposta for "muitas", olhe onde os números 3 aparecem fixos no seu
código.

---

Gabarito: [gabaritos/modulo-09-ex03-jogo-da-velha/](../../gabaritos/modulo-09-ex03-jogo-da-velha/), depois de tentar, não antes.
