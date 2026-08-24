# Exercício 03 — Anatomia de um número (desafio)

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 3 de 3 | 45 min | `//`, `%`, `**`, precedência, expressões booleanas |

## Objetivo

Desmontar um número de quatro dígitos usando **apenas aritmética**: sem `if`, sem laço, sem lista,
sem string. Só os operadores deste módulo.

É o exercício que prova que `//` e `%` não são detalhes: eles são a ferramenta para chegar dentro
de um número.

## A restrição

Você ainda não tem `if` (módulo 04), laço (módulo 05), lista (módulo 06) nem os métodos de string
(módulo 07). **Isso é de propósito.** Resolver com as ferramentas certas é fácil; resolver com
poucas ferramentas é o que ensina a enxergar o mecanismo.

Todo resultado de "sim ou não" deve ser guardado como `bool`, vindo de uma comparação (como você
fez no exemplo 03).

## Requisitos

1. Crie um arquivo `anatomia_de_um_numero.py`.
2. Comece com `numero = 4832` fixo no código.
3. Extraia os **quatro dígitos** em variáveis separadas, usando só `//` e `%`.
4. Calcule e exiba:
   - a soma dos quatro dígitos
   - o produto dos quatro dígitos
   - o maior e o menor dígito, **sem** `max()` e `min()` (dica abaixo)
   - o número invertido (4832 vira 2384), montado com aritmética
5. Guarde em variáveis `bool` e exiba:
   - se o número é par
   - se é múltiplo de 3 (dica: um número é múltiplo de 3 se a soma dos dígitos for)
   - se é capicua (palíndromo, igual de trás para frente)
   - se todos os dígitos são diferentes entre si
6. Teste também com `numero = 1221` e `numero = 7777`, trocando a linha.

## Exemplo de saída

```text
Número: 4832

Dígitos: 4 8 3 2
Soma:     17
Produto:  192
Maior:    8
Menor:    2
Invertido: 2384

É par?                    True
É múltiplo de 3?          False
É capicua?                False
Todos dígitos diferentes? True
```

## Dicas

**Extrair os dígitos.** O da unidade é `numero % 10`. O da dezena é `numero // 10 % 10`. Siga o
padrão.

**Maior e menor sem `max()`.** Existe um truque puramente aritmético:

```python
maior_de_dois = (a + b + abs(a - b)) / 2
menor_de_dois = (a + b - abs(a - b)) / 2
```

Entenda por que funciona antes de usar, e cuidado com o tipo do resultado.

**Todos diferentes.** Compare cada par com `!=` e combine tudo com `and`. São seis comparações.

## Critérios de aceitação

- [ ] Nenhum `if`, `for`, `while`, lista ou `str()` no arquivo
- [ ] Nenhum `max()` nem `min()`
- [ ] Os quatro dígitos estão corretos para os três números de teste
- [ ] `1221` é detectado como capicua; `4832` não
- [ ] `7777` tem "todos diferentes" como `False`
- [ ] As quatro perguntas produzem `bool`, não texto
- [ ] O invertido foi montado com aritmética, não invertendo texto

## Confira na mão

Para `numero = 1221`: dígitos 1, 2, 2, 1. Soma 6: múltiplo de 3, então 1221 também é
(1221 / 3 = 407). É capicua. Nem todos os dígitos são diferentes.

## Desafio dentro do desafio

Escreva, em um comentário, como cada item ficaria **depois** que você aprender listas e laços, e
quantas linhas você economizaria. Guarde o arquivo: vale reabri-lo depois do módulo 06.

---

Gabarito: [gabaritos/modulo-02/ex03-anatomia-de-um-numero/](../../gabaritos/modulo-02/ex03-anatomia-de-um-numero/), depois de tentar, não antes.
