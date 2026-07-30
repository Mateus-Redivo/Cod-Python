# Módulo 05 — Laços de repetição

No módulo anterior seu programa aprendeu a **decidir**. Agora ele vai aprender a **insistir**:
fazer a mesma coisa dez, mil ou "quantas vezes o usuário quiser" — sem você escrever dez linhas
iguais.

## Objetivos de aprendizagem

Ao final deste módulo você será capaz de:

- [ ] Explicar quando usar `while` e quando usar `for`
- [ ] Escrever um laço com contador sem cair em loop infinito
- [ ] Usar `range()` com um, dois e três argumentos
- [ ] Interromper e pular iterações com `break` e `continue`
- [ ] Somar, contar e achar o maior valor dentro de um laço (o padrão "acumulador")
- [ ] Validar a entrada do usuário repetindo a pergunta até o dado ser aceitável

## Pré-requisitos

[Módulo 04 — Condicionais](../modulo-04-condicionais/) concluído, exercícios feitos. Você precisa
estar confortável com `if/elif/else` e com os operadores `and`, `or` e `not` — dentro de um laço,
tudo isso aparece de novo.

## Conceito

### O problema: copiar e colar não escala

Para mostrar a tabuada do 7, sem laço, você escreveria:

```python
print(f"7 x 1 = {7 * 1}")
print(f"7 x 2 = {7 * 2}")
print(f"7 x 3 = {7 * 3}")
# ... e mais sete linhas quase idênticas
```

Funciona. Mas e se a tabuada tiver que ir até 100? E se o usuário escolher o número? E se você
precisar mudar o formato da saída — vai editar dez linhas iguais, uma por uma, sem esquecer
nenhuma?

Sempre que você se pegar copiando uma linha e trocando um detalhe, **é um laço pedindo para
nascer**.

### `while`: repete enquanto a condição for verdadeira

```python
contador = 1
while contador <= 10:
    print(f"7 x {contador} = {7 * contador}")
    contador += 1        # <- esquecer esta linha = loop infinito
```

Três coisas que todo `while` precisa ter, e a ordem importa:

1. **Inicializar** a variável de controle (antes do laço)
2. **Testar** a condição (no `while`)
3. **Atualizar** a variável de controle (dentro do laço)

Faltou a 3? O programa trava. Isso não é bug exótico: é o erro mais comum do módulo, e você vai
cometê-lo pelo menos uma vez. Quando acontecer, `Ctrl + C` no terminal mata o programa.

### `for`: repete um número conhecido de vezes

```python
for contador in range(1, 11):
    print(f"7 x {contador} = {7 * contador}")
```

As três responsabilidades acima viraram uma linha só. O `for` inicializa, testa e atualiza sozinho
— por isso é impossível esquecer o incremento. Por isso a regra prática:

| Situação | Use |
| --- | --- |
| Você sabe quantas vezes vai repetir | `for` |
| Você repete "até acontecer alguma coisa" (usuário digitar 0, acertar a senha…) | `while` |

### `range()`: o limite final não entra

Esta é a pegadinha que pega todo mundo uma vez:

| Escrita | Produz |
| --- | --- |
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 6)` | 1, 2, 3, 4, 5 |
| `range(0, 11, 2)` | 0, 2, 4, 6, 8, 10 |
| `range(10, 0, -1)` | 10, 9, 8, … 1 |

Para ir **até 10**, escreva `range(1, 11)`. O segundo argumento é onde o laço **para**, não o
último valor que ele usa.

### `break` e `continue`: sair e pular

```python
for numero in range(1, 13):
    if numero % 3 != 0:
        continue        # não interessa: pula para a próxima volta
    print(numero)       # só chega aqui quem é múltiplo de 3
```

- **`break`** encerra o laço na hora, mesmo que a condição ainda seja verdadeira.
- **`continue`** abandona só a volta atual e segue para a próxima.

A dupla `while True` + `break` merece atenção: um `while True` nunca fica falso, então o `break`
deixa de ser um atalho e passa a ser **a única** condição de parada. Use quando você só descobre
que é hora de parar depois de já ter feito o trabalho da volta.

### O padrão acumulador

O uso mais frequente de laço no material inteiro. Uma variável nasce **antes** do laço e cresce a
cada volta:

```python
soma = 0                    # antes! se ficar dentro, zera a cada volta
for numero in range(1, 101):
    soma += numero
print(soma)                 # 5050
```

Mesmo esqueleto serve para contar (`quantidade += 1`), acumular texto ou guardar o maior valor
visto até agora. Muda a operação; a estrutura é sempre essa.

### Validar entrada com `while`

Aqui o laço deixa de ser exercício e vira ferramenta. Insistir na pergunta até o dado prestar:

```python
nota = float(input("Nota (0 a 10): "))

while nota < 0 or nota > 10:
    print("Nota inválida.")
    nota = float(input("Nota (0 a 10): "))
```

Repare que o `input` aparece **duas vezes**: uma antes do laço, para haver o que testar, e uma
dentro, para dar nova chance. Esquecer a segunda é loop infinito garantido.

> Digite uma **letra** quando o programa pedir um número e veja o que acontece: `ValueError`,
> programa morto. Por enquanto, combine com o programa: só números. No **módulo 10 — Tratamento de
> erros** você vai aprender a tratar isso de verdade e nunca mais deixar o programa morrer por
> causa de uma digitação errada.

## Exemplos guiados

| Arquivo | O que mostra |
| --- | --- |
| [exemplos/01_while.py](exemplos/01_while.py) | as três partes do `while` e o loop infinito na prática |
| [exemplos/02_for_e_range.py](exemplos/02_for_e_range.py) | `range()` com 1, 2 e 3 argumentos; `for` e `while` lado a lado |
| [exemplos/03_break_continue.py](exemplos/03_break_continue.py) | sair antes da hora e pular uma volta |
| [exemplos/04_acumulador.py](exemplos/04_acumulador.py) | somar, contar, achar o maior e usar valor sentinela |

Para rodar qualquer um deles:

```bash
cd modulo-05-lacos-de-repeticao/exemplos
python 01_while.py
```

Abra o `01_while.py`, **comente a linha do `contador += 1`** e rode de novo. Deixe travar de
propósito e interrompa com `Ctrl + C`. Ver o erro acontecer vale mais que ler sobre ele.

Todo exemplo termina com uma seção **Experimento**. Ela não é opcional: é onde o módulo acontece.

## Exercícios

1. [EXERCICIO-01-tabuada.md](exercicios/EXERCICIO-01-tabuada.md) — *nível 1*: fixação de `for` e `range`.
2. [EXERCICIO-02-media-com-validacao.md](exercicios/EXERCICIO-02-media-com-validacao.md) — *nível 2*: `while` a serviço da validação.
3. [EXERCICIO-03-analise-de-codigo.md](exercicios/EXERCICIO-03-analise-de-codigo.md) — *nível 3*: prever saída e caçar bug em código dos outros.

Quer mais prática? [banco-de-exercicios/nivel-2-intermediario/EXERCICIO-acumulador-com-sentinela.md](../banco-de-exercicios/nivel-2-intermediario/EXERCICIO-acumulador-com-sentinela.md)

## Auto-avaliação

- [ ] Sei dizer, olhando um problema, se ele pede `while` ou `for`
- [ ] Já provoquei um loop infinito de propósito e sei por que ele acontece
- [ ] Sei escrever `range(1, 11)` e explicar por que o 11 não aparece na saída
- [ ] Consigo somar todos os números digitados pelo usuário até ele digitar 0
- [ ] Sei explicar a diferença entre `break` e `continue` com um exemplo meu
- [ ] Escrevo uma validação com `while` sem que ela vire loop infinito

Sobrou caixinha em branco? Volte ao exemplo correspondente antes de seguir para o
[módulo 06](../modulo-06-listas/) — listas são percorridas com laço, e um `for` mal entendido cobra
o preço lá.

## Erros comuns

| Erro | O que está acontecendo |
| --- | --- |
| `while` que nunca termina | faltou atualizar a variável de controle dentro do laço |
| `range(1, 10)` para ir até 10 | o segundo argumento é exclusivo; use `range(1, 11)` |
| Zerar o acumulador dentro do laço | `soma = 0` tem que ficar **antes** do `for`, senão zera a cada volta |
| Validação que trava | o `input` só existe antes do `while`; sem novo `input` dentro, a condição nunca muda |
| `while numero < 1 and numero > 5` | nenhum número é menor que 1 **e** maior que 5 ao mesmo tempo; o operador certo é `or` |
| `ZeroDivisionError` ao tirar média | a contagem pode ser zero; teste `if quantidade > 0` antes de dividir |
| Confundir `=` com `==` no `while` | `=` atribui, `==` compara; em Python isso é erro de sintaxe |
| Indentação errada | a linha ficou fora do laço e executa só uma vez, no fim |

---

Anterior: [Módulo 04 — Condicionais](../modulo-04-condicionais/) | Próximo: [Módulo 06 — Listas](../modulo-06-listas/)
