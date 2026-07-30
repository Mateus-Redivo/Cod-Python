# Exercício 01 — Analisador de frases

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 1 de 3 | 35 min | `len`, `count`, `split`, `upper`, `for` em string |

## Objetivo

Receber uma frase e produzir um relatório sobre ela — juntando o que você sabe de strings, listas e
laços.

## Requisitos

1. Crie um arquivo `analisador_de_frases.py`.
2. Peça uma frase ao usuário e remova os espaços das pontas.
3. Exiba:
   - a frase em MAIÚSCULAS e em minúsculas
   - o total de caracteres **com** espaços
   - o total de caracteres **sem** espaços
   - a quantidade de palavras
   - a quantidade de vogais (`a`, `e`, `i`, `o`, `u`), sem diferenciar maiúsculas
   - a palavra mais longa
   - a frase invertida
4. Liste cada palavra com o seu tamanho, uma por linha, alinhadas.
5. **Proteja**: se a frase estiver vazia, avise e não calcule nada.

## Exemplo de saída

```text
Digite uma frase: Python e uma linguagem simples

===== ANÁLISE =====
Maiúsculas: PYTHON E UMA LINGUAGEM SIMPLES
Minúsculas: python e uma linguagem simples

Caracteres (com espaços): 30
Caracteres (sem espaços): 26
Palavras: 5
Vogais: 10
Palavra mais longa: linguagem
Invertida: selpmis megaugnil amu e nohtyP

--- Palavras ---
Python          6 letras
e               1 letras
uma             3 letras
linguagem       9 letras
simples         7 letras
```

Confira as vogais na mão: **o** (Python) + **e** + **u,a** (uma) + **i,u,a,e** (linguagem) +
**i,e** (simples) = 1+1+2+4+2 = 10. O `y` de "Python" não conta: não está em `"aeiou"`. Não precisa acertar o plural de "1 letras" — isso exigiria um `if` que o
enunciado não pede.

## Dicas

- Para contar vogais, percorra a frase com `for letra in frase` e teste se a letra está em
  `"aeiou"` — lembrando de passar a frase para minúsculas antes.
- Para a palavra mais longa, use o padrão do "maior valor" do módulo 06: comece com a primeira e
  compare `len()` a cada volta.
- Para inverter, a fatia com passo `-1` resolve em uma linha.

## Critérios de aceitação

- [ ] A contagem sem espaços realmente ignora os espaços — confira na mão
- [ ] A contagem de vogais funciona com a frase digitada em maiúsculas
- [ ] A palavra mais longa está correta mesmo quando é a primeira ou a última
- [ ] Frase vazia não gera erro
- [ ] A listagem final fica alinhada na vertical
- [ ] Testei com uma frase de uma palavra só

## Sobre acentos

Se você digitar "é", a contagem de vogais **não** vai incluí-lo, porque `"é" in "aeiou"` é `False`.
Isso está tecnicamente correto para o enunciado como escrito. Se quiser tratar acentos, acrescente
os caracteres acentuados na sua string de vogais — e note quanto trabalho isso dá. Textos com
acento são mais complicados do que parecem.

## Desafio opcional

Conte também as consoantes. Cuidado: "tudo que não é vogal" inclui espaços, números e pontuação.
Use `.isalpha()` para checar se o caractere é mesmo uma letra.

---

Gabarito: [gabaritos/modulo-07-ex01-analisador-de-frases/](../../gabaritos/modulo-07-ex01-analisador-de-frases/) —
depois de tentar, não antes.
