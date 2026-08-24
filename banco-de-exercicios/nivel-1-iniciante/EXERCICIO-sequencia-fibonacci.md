# Sequência de Fibonacci

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| Iniciante | 20 min | `for`, troca de variáveis, validação de entrada |

## O que fazer

Leia um número inteiro positivo N e exiba os N primeiros números da sequência de Fibonacci,
separados por espaço, na mesma linha.

Na sequência, cada número é a soma dos dois anteriores. Ela começa em `0, 1`.

## Requisitos

1. Se N não for positivo, avise o usuário e encerre sem imprimir nada da sequência.
2. Se o usuário digitar algo que não é número, avise em vez de deixar o programa quebrar.
3. A sequência começa em 0, não em 1.

## Exemplo de saída

```text
Digite um número inteiro positivo: 8
0 1 1 2 3 5 8 13
```

E quando a entrada não presta:

```text
Digite um número inteiro positivo: abc
Entrada inválida. Por favor, digite um número inteiro.
```

## Critérios de aceitação

- [ ] `N = 1` imprime só `0`
- [ ] `N = 2` imprime `0 1`
- [ ] `N = 0` ou negativo não imprime sequência nenhuma
- [ ] Letra no lugar de número não derruba o programa

## Armadilha conhecida

Para avançar a sequência você precisa dos **dois** valores anteriores ao mesmo tempo. Se atualizar
um antes do outro, o segundo já usa o valor novo e a conta sai errada a partir do terceiro termo.
Pense em como trocar os dois de uma vez só.

---

Gabarito: [gabaritos/banco-de-exercicios/nivel-1-iniciante/sequencia-fibonacci/](../../gabaritos/banco-de-exercicios/nivel-1-iniciante/sequencia-fibonacci/),
depois de tentar, não antes.

Pré-requisito: [Módulo 05 — Laços de repetição](../../modulo-05-lacos-de-repeticao/) e
[Módulo 10 — Tratamento de erros](../../modulo-10-tratamento-de-erros/) para o requisito 2.
