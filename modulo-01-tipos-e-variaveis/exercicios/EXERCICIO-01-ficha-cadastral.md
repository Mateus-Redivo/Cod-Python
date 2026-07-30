# Exercício 01 — Ficha cadastral

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 1 de 3 | 25 min | variáveis, os quatro tipos, f-string, `type()` |

## Objetivo

Montar uma ficha com dados de uma pessoa, usando uma variável para cada informação e pelo menos um
valor de cada tipo básico.

## Requisitos

1. Crie um arquivo `ficha_cadastral.py`.
2. Crie variáveis para, no mínimo: nome (`str`), idade (`int`), altura (`float`) e se a pessoa está
   ativa (`bool`).
3. Crie uma constante para alguma taxa ou limite (por exemplo `IDADE_MINIMA = 18`), respeitando a
   convenção de constantes.
4. Exiba a ficha formatada com f-strings — nada de concatenar com `+`.
5. Ao final, exiba o **tipo** de cada variável usando `type()`.
6. Todos os nomes devem seguir `snake_case` e dizer o que guardam. Nada de `a`, `b`, `x1`.

## Exemplo de saída

```text
===== FICHA CADASTRAL =====
Nome:    Maria Silva
Idade:   25 anos
Altura:  1.75 m
Ativa:   True

Idade mínima exigida: 18

--- Tipos ---
nome   -> str
idade  -> int
altura -> float
ativa  -> bool
```

## Critérios de aceitação

- [ ] Existe pelo menos uma variável de cada tipo: `int`, `float`, `str` e `bool`
- [ ] A constante está em `MAIUSCULO_COM_UNDERLINE`
- [ ] Toda a exibição usa f-string
- [ ] Os tipos exibidos batem com os valores atribuídos
- [ ] Nenhum nome de variável tem uma letra só, acento ou espaço
- [ ] O programa roda sem erro

## Desafio opcional

Acrescente uma variável `imc` calculada a partir de peso e altura (`peso / altura ** 2`) e exiba-a
com duas casas decimais — a formatação é `{imc:.2f}`.

---

Gabarito: [gabaritos/modulo-01-ex01-ficha-cadastral/](../../gabaritos/modulo-01-ex01-ficha-cadastral/) —
depois de tentar, não antes.
