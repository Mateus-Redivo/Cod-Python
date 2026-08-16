# Módulo 03 — Entrada e saída

Até aqui todos os seus programas eram monólogos: os valores estavam fixos no código e o resultado
era sempre o mesmo. Agora o programa vai **perguntar**, e é aí que ele deixa de ser um exercício e
começa a servir para alguma coisa.

Este módulo junta dois assuntos que só fazem sentido juntos: ler o que o usuário digitou e
**converter** esse texto no tipo certo. Porque tudo que vem do teclado chega como texto, sempre.

## Objetivos de aprendizagem

Ao final deste módulo você será capaz de:

- [ ] Usar `input()` para receber dados e explicar por que ele sempre devolve `str`
- [ ] Converter entre tipos com `int()`, `float()` e `str()`
- [ ] Formatar saída com f-strings, controlando casas decimais e largura
- [ ] Usar os parâmetros `sep` e `end` do `print()`
- [ ] Reconhecer as conversões que dão erro e saber o caminho alternativo
- [ ] Escrever um programa completo que lê, calcula e exibe

## Pré-requisitos

[Módulo 02 — Operadores](../modulo-02-operadores/) concluído. Você vai calcular com os valores que
o usuário digitar, então precisa dos operadores na ponta da língua, e da lembrança do `TypeError`
do módulo 01, que vai reaparecer aqui em forma de dor real.

## Conceito

### O problema: um programa que só sabe uma coisa

```python
largura = 5
altura = 8
print(f"Área: {largura * altura}")
```

Esse programa calcula a área de exatamente um retângulo. Para outro, você edita o código. Um
programa que precisa ser editado para dar outra resposta não é um programa: é uma conta escrita de
um jeito complicado.

### `input()`: o programa pergunta

```python
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")
```

O `input()` faz três coisas: mostra o texto entre parênteses, **pausa** o programa até você digitar
algo e apertar Enter, e devolve o que foi digitado.

### A regra que vale o módulo inteiro

> **`input()` devolve SEMPRE uma string.** Sempre. Mesmo quando o usuário digita um número.

```python
idade = input("Digite sua idade: ")     # usuário digita 25
print(type(idade))                      # <class 'str'>
print(idade + 10)                       # TypeError!
```

Aquele `TypeError: can only concatenate str (not "int") to str` do módulo 01 volta aqui, e agora
com consequência prática. O Python não tem como saber se você quer somar ou concatenar, então ele
para.

A solução é converter na hora de ler:

```python
idade = int(input("Digite sua idade: "))    # agora é int
print(idade + 10)                           # funciona
```

Leia de dentro para fora: primeiro o `input()` roda e devolve texto, depois o `int()` transforma
esse texto em número. As duas funções numa linha só: este é o padrão que você vai escrever
centenas de vezes.

### Qual conversão usar

| Função | Converte para | Use quando |
| --- | --- | --- |
| `int()` | inteiro | idade, quantidade, ano: coisas que não têm meio |
| `float()` | decimal | preço, altura, nota: coisas que têm casas decimais |
| `str()` | texto | juntar um número a um texto sem f-string |

Na dúvida entre `int` e `float`, pergunte: **"faz sentido meio disso?"** Meia pessoa não faz;
meio quilo faz.

### As conversões que quebram

```python
int("abc")      # ValueError: invalid literal for int() with base 10: 'abc'
int("3.14")     # ValueError — sim, mesmo sendo um número!
float("texto")  # ValueError: could not convert string to float: 'texto'
```

O segundo caso surpreende todo mundo: `"3.14"` **é** um número, mas não é a escrita de um
**inteiro**. O Python não arredonda por conta própria porque arredondar seria adivinhar sua
intenção: 3 ou 4?

Se você precisa mesmo do inteiro a partir de `"3.14"`, o caminho tem duas etapas:

```python
int(float("3.14"))      # 3 — descarta a parte decimal
```

> **Digite uma letra quando o programa pedir um número e veja o que acontece:** `ValueError`, e o
> programa morre no meio. Por enquanto, combine com o programa: só números. No **módulo 10 —
> Tratamento de erros** você vai aprender a tratar isso de verdade e nunca mais deixar o programa
> morrer por causa de uma digitação errada.

### f-strings: formatando a saída

O `f` antes das aspas libera as chaves para valores e expressões:

```python
nome = "Maria"
salario = 3500.75

print(f"Nome: {nome}")
print(f"Salário: R$ {salario:.2f}")     # R$ 3500.75
print(f"Dobro: {salario * 2}")          # aceita expressão dentro
```

Os formatos que você vai usar de verdade:

| Escrita | Resultado com `salario = 3500.75` | Para que serve |
| --- | --- | --- |
| `{salario}` | `3500.75` | valor cru |
| `{salario:.2f}` | `3500.75` | força duas casas decimais |
| `{salario:.0f}` | `3501` | zero casas, arredondando |
| `{salario:10.2f}` | `   3500.75` | largura 10, alinhado à direita |
| `{numero:03d}` | `007` (se `numero = 7`) | inteiro com zeros à esquerda |

O `:.2f` é o mais importante: sem ele, uma média sai como `7.333333333333333` e uma soma de dinheiro
como `10.000000000000002`.

### `print()` tem dois parâmetros que ninguém ensina

```python
print("A", "B", "C")                # A B C     (separador padrão: espaço)
print("A", "B", "C", sep="-")       # A-B-C
print("A", "B", "C", sep="")        # ABC

print("Esta linha", end="")         # não pula linha no fim
print(" continua aqui")             # Esta linha continua aqui
```

O `end=""` é o que permite montar uma saída aos poucos: você vai usá-lo no módulo 05 para imprimir
valores lado a lado dentro de um laço.

### O esqueleto de todo programa deste ponto em diante

```python
# 1. ENTRADA — pergunte e converta
largura = float(input("Largura: "))
altura = float(input("Altura: "))

# 2. PROCESSAMENTO — calcule
area = largura * altura

# 3. SAÍDA — mostre formatado
print(f"Área: {area:.2f} m2")
```

Entrada, processamento, saída. Todo programa dos próximos módulos é uma variação disso, com mais
decisões e mais repetições no meio.

## Exemplos guiados

| Arquivo | O que mostra |
| --- | --- |
| [exemplos/01_print.py](exemplos/01_print.py) | `print` com vários valores, `sep` e `end` |
| [exemplos/02_f_strings.py](exemplos/02_f_strings.py) | casas decimais, largura e zeros à esquerda |
| [exemplos/03_input.py](exemplos/03_input.py) | `input` devolve texto, e o `TypeError` que isso causa |
| [exemplos/04_conversoes.py](exemplos/04_conversoes.py) | `int`, `float`, `str` e as conversões que quebram |
| [exemplos/05_programa_completo.py](exemplos/05_programa_completo.py) | entrada, processamento e saída juntos |

Para rodar qualquer um deles:

```bash
cd modulo-03-entrada-e-saida/exemplos
python 01_print.py
```

Os exemplos 03, 04 e 05 pedem coisas digitadas. Responda de verdade, e depois responda errado de
propósito, que é onde o aprendizado mora.

## Exercícios

1. [EXERCICIO-01-conversor-de-medidas.md](exercicios/EXERCICIO-01-conversor-de-medidas.md) (nível 1): ler, calcular e formatar.
2. [EXERCICIO-02-nota-fiscal.md](exercicios/EXERCICIO-02-nota-fiscal.md) (nível 2): formatação alinhada e escolha de tipos.
3. [EXERCICIO-03-planejador-de-viagem.md](exercicios/EXERCICIO-03-planejador-de-viagem.md) (nível 3): sete entradas, nove cálculos e um relatório em três blocos.

## Auto-avaliação

- [ ] Sei dizer, sem pensar, qual o tipo devolvido por `input()`
- [ ] Escrevo `int(input(...))` de cabeça e sei ler a linha de dentro para fora
- [ ] Escolho entre `int` e `float` perguntando se "meio disso" faz sentido
- [ ] Sei mostrar um valor com exatamente duas casas decimais
- [ ] Já provoquei um `ValueError` digitando letra onde se pedia número
- [ ] Sei por que `int("3.14")` quebra e como contornar

## Erros comuns

| Erro | O que está acontecendo |
| --- | --- |
| `TypeError: can only concatenate str` | esqueceu de converter o `input()`; texto não soma com número |
| `ValueError: invalid literal for int()` | o usuário digitou letra, ou você usou `int()` num decimal |
| `int("3.14")` quebra | `int()` não arredonda; use `int(float("3.14"))` |
| Resultado sai como `7.333333333333333` | faltou `:.2f` na f-string |
| Usuário digita `1,75` e o programa quebra | o separador decimal do Python é ponto |
| Esqueceu o `f` antes das aspas | a saída mostra `{nome}` literalmente, sem substituir |
| `print("Total: " + total)` | concatenar com número dá erro; use f-string |
| O programa "não faz nada" | ele está parado esperando você digitar e apertar Enter |

---

Anterior: [Módulo 02 — Operadores](../modulo-02-operadores/) | Próximo: [Módulo 04 — Condicionais](../modulo-04-condicionais/)
