# Módulo 08 — Funções

Até aqui seus programas cresceram para baixo: cada recurso novo virava mais linhas no fim do
arquivo. Funciona até uns cinquenta, cem, duzentos… e então você já não acha nada, muda uma coisa e
quebra outra.

Este módulo muda a direção do crescimento. Em vez de mais linhas, **blocos com nome**, pedaços que
você escreve uma vez, entende de uma vez, e usa quantas vezes quiser.

## Objetivos de aprendizagem

Ao final deste módulo você será capaz de:

- [ ] Criar funções com `def` e chamá-las
- [ ] Distinguir parâmetro de argumento
- [ ] Explicar a diferença entre uma função que `return` e uma que só imprime
- [ ] Usar parâmetros com valor padrão
- [ ] Explicar o que é escopo e por que uma variável local morre no fim da função
- [ ] Justificar por que `global` quase nunca é a resposta certa
- [ ] Quebrar um programa longo em funções pequenas

## Pré-requisitos

[Módulo 07 — Strings](../modulo-07-strings/) concluído. Você vai transformar em função os programas
que já escreveu nos módulos anteriores, vale ter os exercícios de listas e laços à mão.

## Conceito

### O problema: o mesmo cálculo em três lugares

```python
notas_turma_1 = [7, 8, 9]
media_1 = sum(notas_turma_1) / len(notas_turma_1)
print(f"Média turma 1: {media_1}")

notas_turma_2 = [6, 5, 8]
media_2 = sum(notas_turma_2) / len(notas_turma_2)
print(f"Média turma 2: {media_2}")
```

Repare no que aconteceu: a fórmula da média aparece duas vezes. Se ela mudar (passar a descartar a
menor nota, por exemplo), você tem que lembrar dos dois lugares. Com dez turmas, dez lugares.

**Código repetido não é feio: é frágil.** Cada cópia é uma chance de esquecer uma.

```python
def calcular_media(notas):
    return sum(notas) / len(notas)

print(f"Média turma 1: {calcular_media([7, 8, 9])}")
print(f"Média turma 2: {calcular_media([6, 5, 8])}")
```

Agora a fórmula mora em um lugar só.

### A anatomia

```python
def calcular_media(notas):      # def, nome, parâmetros, dois-pontos
    return sum(notas) / len(notas)      # corpo, indentado
```

| Parte | O que é |
| --- | --- |
| `def` | a palavra que anuncia "estou criando uma função" |
| `calcular_media` | o nome. `snake_case`, e comece com um **verbo** |
| `(notas)` | os **parâmetros**: os valores que a função espera receber |
| `:` e indentação | o corpo, como em `if` e `for` |
| `return` | o valor que a função devolve |

**Definir não é executar.** O `def` só ensina o Python a fazer algo; nada acontece até você
*chamar*:

```python
def saudar():
    print("Olá!")

# nada foi impresso ainda

saudar()        # AGORA sim
```

### Parâmetro e argumento

Confundem-se o tempo todo, e a diferença é simples:

```python
def saudar(nome):        # nome é o PARÂMETRO — o apelido que a função dá
    print(f"Olá, {nome}!")

saudar("Ana")            # "Ana" é o ARGUMENTO — o valor real que você passou
```

Parâmetro é o nome no contrato; argumento é o que você entrega na hora.

### `return` versus `print`: a distinção que mais confunde

```python
def dobrar_e_mostrar(numero):
    print(numero * 2)           # mostra na tela

def dobrar(numero):
    return numero * 2           # devolve para quem chamou
```

Parecem equivalentes. Não são:

```python
resultado = dobrar_e_mostrar(5)     # imprime 10, mas resultado vira None!
resultado = dobrar(5)               # não imprime nada, e resultado vira 10

total = dobrar(3) + dobrar(4)       # funciona: 14
total = dobrar_e_mostrar(3) + dobrar_e_mostrar(4)   # TypeError!
```

A regra prática: **uma função que calcula deve `return`, não `print`.** Quem chamou decide o que
fazer com o valor: mostrar, somar, guardar. Uma função que imprime já tomou essa decisão por você,
e não dá para desfazer.

> Toda função devolve alguma coisa. Se você não escrever `return`, ela devolve `None`, o mesmo
> `None` que apareceu no módulo 06, quando `lista.sort()` era atribuído por engano. Agora você sabe
> de onde ele vem.

### Valores padrão

```python
def saudar(nome, saudacao="Olá"):
    print(f"{saudacao}, {nome}!")

saudar("Ana")                   # Olá, Ana!
saudar("João", "Bom dia")       # Bom dia, João!
```

O parâmetro com padrão vira opcional. Ele precisa vir **depois** dos obrigatórios: o contrário dá
`SyntaxError`.

### Escopo: onde a variável existe

```python
def calcular_desconto(preco):
    desconto = preco * 0.1      # 'desconto' nasce aqui
    return preco - desconto
                                # e morre aqui

print(desconto)                 # NameError: name 'desconto' is not defined
```

Variável criada dentro da função é **local**: existe só durante a chamada e some no fim. Isso não é
limitação, é proteção: você pode usar `i`, `total`, `resultado` dentro de dez funções diferentes
sem que uma atrapalhe a outra.

### O `global` e por que evitá-lo

Funções **leem** variáveis de fora sem cerimônia:

```python
TAXA_IMPOSTO = 0.15

def calcular_preco_final(preco):
    return preco + preco * TAXA_IMPOSTO     # lê a global, tudo bem
```

Mas **alterar** é outra história:

```python
contador = 0

def incrementar():
    contador = contador + 1     # UnboundLocalError!
```

O Python vê a atribuição e decide que `contador` é local, aí tenta ler uma local que ainda não
existe. A palavra `global` resolve:

```python
def incrementar():
    global contador
    contador = contador + 1
```

**Mas quase nunca é o que você quer.** Uma função que mexe em variável global é imprevisível: para
entender o que ela faz, é preciso saber o estado do programa inteiro. A alternativa é sempre mais
limpa:

```python
def incrementar(contador):
    return contador + 1

contador = incrementar(contador)
```

Entra valor, sai valor. Nada escondido.

### Como quebrar um programa em funções

O sinal mais confiável: **se você precisa de um comentário para explicar o que um bloco faz, esse
bloco quer ser uma função**, e o comentário é o nome dela.

```python
# calcula a média das notas          ->   def calcular_media(notas):
# valida se a nota está entre 0 e 10 ->   def nota_e_valida(nota):
# mostra o boletim formatado         ->   def mostrar_boletim(notas)
```

Uma função deve fazer **uma** coisa. Se o nome precisa de um "e" (`calcular_e_mostrar`), são duas.

## Exemplos guiados

| Arquivo | O que mostra |
| --- | --- |
| [exemplos/01_primeira_funcao.py](exemplos/01_primeira_funcao.py) | `def`, chamada, e que definir não é executar |
| [exemplos/02_parametros_e_retorno.py](exemplos/02_parametros_e_retorno.py) | parâmetros, argumentos, valores padrão |
| [exemplos/03_return_vs_print.py](exemplos/03_return_vs_print.py) | a diferença que mais confunde, lado a lado |
| [exemplos/04_escopo.py](exemplos/04_escopo.py) | local, global, `UnboundLocalError` e a saída limpa |

Para rodar qualquer um deles:

```bash
cd modulo-08-funcoes/exemplos
python 01_primeira_funcao.py
```

## Exercícios

1. [EXERCICIO-01-caixa-de-ferramentas.md](exercicios/EXERCICIO-01-caixa-de-ferramentas.md)
   (nível 1): escrever funções pequenas com `return`.
2. [EXERCICIO-02-boletim-com-funcoes.md](exercicios/EXERCICIO-02-boletim-com-funcoes.md)
   (nível 2): reescrever um programa antigo, agora em funções.
3. [EXERCICIO-03-quebrando-o-monolito.md](exercicios/EXERCICIO-03-quebrando-o-monolito.md)
   (nível 3): decompor um programa longo sem mudar o que ele faz.

## Auto-avaliação

- [ ] Sei explicar a diferença entre parâmetro e argumento com um exemplo meu
- [ ] Sei por que `resultado = funcao_que_so_imprime()` guarda `None`
- [ ] Escrevo funções que devolvem valor em vez de imprimir
- [ ] Já provoquei um `UnboundLocalError` e entendi por que ele acontece
- [ ] Consigo justificar por que não usei `global`
- [ ] Olho um bloco de código e sei dizer se ele quer virar função

## Erros comuns

| Erro | O que está acontecendo |
| --- | --- |
| A função "não faz nada" | você definiu mas não chamou; falta a linha `nome_da_funcao()` |
| `TypeError: missing 1 required positional argument` | a função espera um parâmetro que você não passou |
| `TypeError: takes 1 positional argument but 2 were given` | você passou argumentos demais |
| `resultado` vira `None` | a função imprime mas não tem `return` |
| `UnboundLocalError` | atribuiu a uma variável global dentro da função sem declarar `global` |
| `SyntaxError` na definição | parâmetro com valor padrão veio antes de um obrigatório |
| `NameError` ao usar variável da função | ela é local e já morreu; devolva-a com `return` |
| Código depois do `return` não roda | `return` encerra a função na hora |

---

Anterior: [Módulo 07 — Strings](../modulo-07-strings/) | Próximo: [Módulo 09 — Matrizes](../modulo-09-matrizes/)
