# Exercício 01 — Classificador de IMC

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 1 de 3 | 30 min | `if/elif/else`, ordem de faixas, `input`, f-string |

## Objetivo

Calcular o IMC de uma pessoa e classificá-lo em faixas: o exercício clássico para treinar a ordem
correta de uma cadeia de `elif`.

## Requisitos

1. Crie um arquivo `classificador_de_imc.py`.
2. Pergunte **peso** (kg) e **altura** (m). Escolha o tipo certo na conversão.
3. Calcule o IMC: `peso / altura ** 2`.
4. Classifique segundo a tabela abaixo, usando **uma única cadeia** `if/elif/else`.
5. Exiba o IMC com duas casas decimais e a classificação.
6. **Proteja o cálculo**: se a altura for zero, avise e não calcule. Nada de `ZeroDivisionError`.

| IMC | Classificação |
| --- | --- |
| abaixo de 18.5 | Abaixo do peso |
| de 18.5 a 24.9 | Peso normal |
| de 25.0 a 29.9 | Sobrepeso |
| de 30.0 a 39.9 | Obesidade |
| 40.0 ou mais | Obesidade grave |

## Exemplo de saída

```text
Digite seu peso em kg: 70
Digite sua altura em m: 1.75

IMC: 22.86
Classificação: Peso normal
```

E com altura zero:

```text
Digite seu peso em kg: 70
Digite sua altura em m: 0

Altura inválida: não é possível calcular o IMC.
```

## Critérios de aceitação

- [ ] Nenhum `elif` fica inalcançável (teste com um valor de cada faixa)
- [ ] Nenhuma condição repete a faixa anterior (nada de `elif imc >= 25 and imc < 30`)
- [ ] Altura zero é tratada e o programa não quebra
- [ ] O IMC sai com exatamente duas casas decimais
- [ ] Testei os valores de fronteira: 18.5, 25.0, 30.0 e 40.0
- [ ] A altura é lida com `float()` (digitar `1.75` não pode quebrar)

## Armadilha conhecida

As fronteiras são onde este exercício morde. Com IMC exatamente `25.0`, sua cadeia responde
"Peso normal" ou "Sobrepeso"? Decida olhando a tabela (`25.0` pertence ao Sobrepeso) e confira se
seus operadores (`>=` ou `>`) fazem o que você quer nesse ponto exato.

## Desafio opcional

Um IMC negativo ou absurdo (peso 5000) passa sem reclamar. Acrescente uma validação de faixa para o
peso e para a altura. Você vai perceber que só dá para **avisar** e encerrar. Para **insistir** na
pergunta até vir um valor válido, falta o `while` do módulo 05.

---

Gabarito: [gabaritos/modulo-04/ex01-classificador-de-imc/](../../gabaritos/modulo-04/ex01-classificador-de-imc/), depois de tentar, não antes.
