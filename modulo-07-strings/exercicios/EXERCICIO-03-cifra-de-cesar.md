# Exercício 03 — Cifra de César (desafio)

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 3 de 3 | 55 min | `ord`, `chr`, `%`, percorrer string, montar string nova |

## Objetivo

Implementar a cifra de César: o método de criptografia que Júlio César usava para mensagens
militares. Cada letra é deslocada um número fixo de posições no alfabeto.

É o exercício que junta strings, aritmética modular e a construção de texto caractere a caractere.

## Como a cifra funciona

Com deslocamento 3, cada letra vira a que está três posições adiante:

```text
A -> D      B -> E      C -> F      ...      W -> Z
X -> A      Y -> B      Z -> C      <- dá a volta no alfabeto
```

`PYTHON` com deslocamento 3 vira `SBWKRQ`.

Para decifrar, desloque no sentido contrário (ou, mais elegante, cifre de novo com `26 - 3`).

## As duas funções novas

Você precisa de duas funções embutidas que ainda não apareceram:

```python
ord("A")      # 65   — o número que representa o caractere
chr(65)       # "A"  — o caractere daquele número
```

As letras maiúsculas ocupam de 65 (`A`) a 90 (`Z`); as minúsculas, de 97 (`a`) a 122 (`z`). Foi
essa tabela que explicou, no módulo 02, por que `"Zebra" < "ana"`.

## Requisitos

1. Crie um arquivo `cifra_de_cesar.py`.
2. Peça a mensagem e o deslocamento (1 a 25).
3. Cifre a mensagem, respeitando:
   - maiúsculas continuam maiúsculas, minúsculas continuam minúsculas
   - espaços, números e pontuação passam **intactos**
   - o alfabeto **dá a volta**: `Z` com deslocamento 3 vira `C`
4. Exiba a mensagem cifrada.
5. Decifre a mensagem cifrada e confirme que ela volta a ser a original.
6. Mostre um teste automático: para os 25 deslocamentos possíveis, cifrar e decifrar deve devolver
   o texto original. Exiba se todos passaram.

**Restrição:** sem funções (módulo 08), ou, se preferir, use-as e considere isto um aquecimento
para o próximo módulo.

## Exemplo de saída

```text
Mensagem: Ataque ao amanhecer!
Deslocamento (1-25): 3

Original:  Ataque ao amanhecer!
Cifrada:   Dwdtxh dr dpdqkhfhu!
Decifrada: Ataque ao amanhecer!

Teste dos 25 deslocamentos: 25/25 passaram.
```

## A parte que exige atenção

O cálculo do novo caractere tem três passos, e errar a ordem é o erro clássico:

```python
posicao_no_alfabeto = ord(letra) - ord("A")          # 0 a 25
nova_posicao = (posicao_no_alfabeto + deslocamento) % 26
nova_letra = chr(nova_posicao + ord("A"))
```

O `% 26` é o que faz o alfabeto dar a volta. Sem ele, `Z + 3` produz um caractere que não é letra.

E repare: é preciso **subtrair** `ord("A")` antes e **somar** depois. Aplicar o `% 26` direto sobre
o `ord()` não funciona, porque a tabela não começa em zero.

## Critérios de aceitação

- [ ] `PYTHON` com deslocamento 3 vira `SBWKRQ`
- [ ] `Z` com deslocamento 3 vira `C`, e `z` vira `c`
- [ ] Espaços, pontuação e números saem inalterados
- [ ] Maiúsculas e minúsculas mantêm a caixa original
- [ ] Decifrar devolve exatamente a mensagem original (compare com `==`)
- [ ] O teste dos 25 deslocamentos passa em todos
- [ ] Deslocamento fora de 1 a 25 é recusado

## Desafio dentro do desafio

A cifra de César é trivial de quebrar: só há 25 chaves possíveis. Escreva um modo "quebrar" que
mostre as 25 decifragens possíveis de uma mensagem, para o usuário identificar a legível a olho.

Depois pense: como um programa poderia escolher **sozinho** a decifragem certa, sem um humano olhar?
Escreva a ideia em um comentário: não precisa implementar. (Dica: em português, algumas letras são
muito mais frequentes que outras.)

---

Gabarito: [gabaritos/modulo-07-ex03-cifra-de-cesar/](../../gabaritos/modulo-07-ex03-cifra-de-cesar/), depois de tentar, não antes.
