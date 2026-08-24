# Gabarito — Módulo 05, Exercício 03: Análise de código

Enunciado: [EXERCICIO-03-analise-de-codigo.md](../../modulo-05-lacos-de-repeticao/exercicios/EXERCICIO-03-analise-de-codigo.md)

> Se você chegou aqui sem ter escrito suas previsões primeiro, feche este arquivo. Este exercício
> mede onde a sua leitura de código falha: ler a resposta antes apaga justamente a informação que
> ele produziria.

---

## Questão 1 — `continue` e acumulador

**a)** `25`

**b)** O `continue` abandona a volta atual assim que `i` é par, antes de chegar no `total += i`.
Sobram apenas os ímpares: `1 + 3 + 5 + 7 + 9 = 25`.

**c)** Sem `continue`, o mesmo resultado sai invertendo a condição:

```python
total = 0
for i in range(1, 11):
    if i % 2 != 0:      # se for ímpar, soma
        total += i
print(total)
```

As duas versões estão corretas. A segunda costuma ler melhor para quem está começando, porque diz
o que **acontece** em vez de dizer o que é pulado. O `continue` ganha valor quando o bloco a ser
pulado é longo: evita indentar dez linhas dentro de um `if`.

---

## Questão 2 — Fatorial

**a)** `120`

**b)** O fatorial de 5 (`5!`): `1 × 2 × 3 × 4 × 5`.

**c)** Porque o acumulador precisa começar no **elemento neutro da operação**. Na soma, o neutro é
0; na multiplicação, é 1. Se `resultado` começasse em 0, toda multiplicação daria 0 e o resultado
final seria 0: o clássico "acumulador zerado na operação errada".

**d)** Com N informado e validado:

```python
numero = int(input("Digite N (1 a 10): "))

while numero < 1 or numero > 10:
    print("Valor inválido! N deve estar entre 1 e 10.")
    numero = int(input("Digite N (1 a 10): "))

resultado = 1
for i in range(1, numero + 1):
    resultado *= i

print(f"{numero}! = {resultado}")
```

Repare no `numero + 1` do `range`: sem ele o fatorial sai errado, faltando o último fator.

---

## Questão 3 — Senha: o bug da chance única

**a)** O `if` executa **uma vez só**. Ele dá exatamente uma segunda chance e depois segue em frente
com o que vier (válido ou não).

Sequência que expõe o problema: digite `12` e depois `7`. As duas são inválidas, mas o programa
imprime `Senha aceita: 7` e continua. O `if` testa uma vez; ele não insiste.

**b)** Trocando `if` por `while`, a mesma estrutura passa a insistir:

```python
senha = int(input("Digite a senha (1000-9999): "))

while senha < 1000 or senha > 9999:
    print("Senha inválida!")
    senha = int(input("Digite novamente: "))

print("Senha aceita:", senha)
```

Essa é a lição da questão: **`if` verifica, `while` insiste.** Toda validação que precisa de mais de
uma tentativa é `while`.

---

## Questão 4 — O operador lógico errado

**a)** Digitando 99, o programa imprime `Número válido: 99` na hora, sem reclamar. O `while` nunca
executa.

**b)** O operador errado é o `and`. A condição `numero < 1 and numero > 5` exige que o número seja
menor que 1 **e**, ao mesmo tempo, maior que 5. Nenhum número no universo satisfaz as duas coisas
juntas, então a condição é sempre `False` e o laço nunca roda.

O correto é `or`: um valor é inválido se está abaixo de 1 **ou** acima de 5, basta uma das duas.

Regra prática que evita o erro: quando você descreve um intervalo **proibido** (fora de), o
conector é `or`. Quando descreve um intervalo **permitido** (dentro de), é `and`.

**c)** Correção:

```python
numero = int(input("Digite um número entre 1 e 5: "))

while numero < 1 or numero > 5:
    print("Fora do intervalo!")
    numero = int(input("Digite novamente: "))

print("Número válido:", numero)
```

---

## Questão 5 — Laço dentro de laço

**a)** 9 vezes: 3 voltas do laço externo × 3 voltas do interno.

**b)** Saída completa:

```text
1  2  3  
2  4  6  
3  6  9  
```

**c)** Uma tabela de multiplicação 3 × 3. A linha `i` mostra a tabuada do `i` até o 3. O `print()`
vazio depois do laço interno é o que quebra a linha ao fim de cada faixa.

**d)** `j = 1` está dentro do laço externo para **reiniciar** o contador a cada linha nova. Sem
esse reinício, `j` chegaria a 4 no fim da primeira linha e o `while` interno nunca mais seria
verdadeiro: a saída teria só a primeira linha, e as duas seguintes sairiam vazias.

Vale rodar com `j = 1` movido para fora, para ver acontecer.

---

## Questão 6 — Flag e `break`

**a)** `primo` é uma **flag**: uma variável booleana que registra se algo foi encontrado. Ela começa
`True` porque a suposição inicial é "é primo até que se prove o contrário". Achar um divisor é
essa prova: aí ela vira `False`.

**b)** Porque todo número é divisível por 1. Começar em 1 encontraria um divisor sempre, e nenhum
número seria classificado como primo.

**c)** Porque 1 não é primo, mas o laço não consegue detectar isso. Com `numero = 1`, o `range(2, 1)`
é vazio, o `for` não roda nenhuma vez e `primo` continua `True`. Sem a condição `numero > 1`, o
programa afirmaria que 1 é primo. O `and` no `if` final é o remendo desse caso.

**d)** Rastreando os dois:

| Entrada | `range(2, numero)` | Voltas do `for` | `primo` no fim | `numero > 1` | Saída |
| --- | --- | --- | --- | --- | --- |
| 1 | `range(2, 1)` → vazio | nenhuma | `True` | `False` | "1 não é primo" ✔ |
| 2 | `range(2, 2)` → vazio | nenhuma | `True` | `True` | "2 é primo" ✔ |

Os dois casos acertam, mas por caminhos diferentes: o 1 é salvo pela condição extra, e o 2 acerta
porque de fato não tem divisor no intervalo. Um `range` vazio não é erro: é um laço que roda zero
vezes, e vale conhecer esse comportamento.

**e)** Com validação:

```python
numero = int(input("Digite um número inteiro positivo: "))

while numero < 1:
    print("O número deve ser positivo.")
    numero = int(input("Digite novamente: "))

primo = True
for i in range(2, numero):
    if numero % i == 0:
        primo = False
        break

if primo and numero > 1:
    print(f"{numero} é primo")
else:
    print(f"{numero} não é primo")
```

O `break` continua ali por eficiência: assim que um divisor aparece, a resposta já está decidida e
continuar procurando é trabalho jogado fora. Para 1.000.000 a diferença é visível.

---

## O que rever, conforme onde você errou

| Errou na questão | Volte para |
| --- | --- |
| 1 | [exemplos/03_break_continue.py](../../modulo-05-lacos-de-repeticao/exemplos/03_break_continue.py) |
| 2 | seção "O padrão acumulador" do [README do módulo](../../modulo-05-lacos-de-repeticao/) |
| 3 e 4 | seção "Validar entrada com `while`" do README: as duas são o mesmo erro com roupas diferentes |
| 5 | [exemplos/01_while.py](../../modulo-05-lacos-de-repeticao/exemplos/01_while.py), com atenção às três partes |
| 6 | [exemplos/03_break_continue.py](../../modulo-05-lacos-de-repeticao/exemplos/03_break_continue.py) e a tabela de erros comuns |
