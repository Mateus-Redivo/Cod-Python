# Módulo 01 — Tipos e variáveis

No módulo anterior você conseguiu rodar um programa. Mas ele era só um papagaio: mostrava textos
fixos e esquecia tudo. Agora seu programa ganha **memória**: a capacidade de guardar um valor,
dar um nome a ele e usá-lo mais adiante.

## Objetivos de aprendizagem

Ao final deste módulo você será capaz de:

- [ ] Criar variáveis e explicar o que o sinal `=` realmente faz
- [ ] Identificar os quatro tipos básicos: `int`, `float`, `str` e `bool`
- [ ] Descobrir o tipo de um valor com `type()`
- [ ] Escolher nomes de variável que sigam as regras e as convenções do Python
- [ ] Prever o resultado de somar valores de tipos diferentes
- [ ] Trocar o conteúdo de duas variáveis

## Pré-requisitos

[Módulo 00 — Preparação](../modulo-00-preparacao/) concluído. Você precisa conseguir rodar um
arquivo `.py` e ler uma mensagem de erro: as duas coisas vão ser usadas o tempo todo aqui.

## Conceito

### O problema: repetir valor é pedir para errar

Sem variáveis, todo valor fica solto no meio do código:

```python
print("O preço é 49.90")
print("Com 10% de desconto: 44.91")
print("Em 3x de 14.97")
```

Funciona, até o preço mudar. Aí você tem que achar e ajustar três números diferentes, sem esquecer
nenhum e sem errar as contas. **Um valor que aparece em mais de um lugar quer virar variável.**

```python
preco = 49.90
print(f"O preço é {preco}")
print(f"Com 10% de desconto: {preco * 0.9}")
print(f"Em 3x de {preco / 3}")
```

Agora o preço mora em um lugar só. Mudou ali, mudou em tudo.

### O `=` não é igualdade

Esta é a confusão mais comum de quem vem da matemática. Em Python:

```python
idade = 20
```

não afirma que "idade é igual a 20". É uma **ordem**: "guarde o valor 20 e chame isso de idade".
Lê-se da direita para a esquerda: primeiro o valor existe, depois recebe o nome.

Por isso esta linha, que na matemática seria absurda, é perfeitamente normal:

```python
contador = contador + 1
```

Ela diz: pegue o valor atual de `contador`, some 1, e guarde o resultado de volta em `contador`.

> Para **comparar** dois valores, o operador é `==`, com dois sinais. Isso é assunto do
> [módulo 02](../modulo-02-operadores/), mas já anote: `=` guarda, `==` pergunta.

### Os quatro tipos básicos

Todo valor em Python tem um tipo, e o tipo define o que dá para fazer com ele.

| Tipo | O que guarda | Exemplos |
| --- | --- | --- |
| `int` | número inteiro | `25`, `0`, `-10` |
| `float` | número com casas decimais | `1.75`, `49.90`, `-0.5` |
| `str` | texto (*string*) | `"Maria"`, `'São Paulo'`, `""` |
| `bool` | verdadeiro ou falso | `True`, `False` |

Três detalhes que pegam todo mundo uma vez:

1. **O separador decimal é ponto, não vírgula.** `1.75` é um número; `1,75` é outra coisa.
2. **Texto precisa de aspas.** `"25"` e `25` parecem iguais na tela, mas o primeiro é texto.
3. **`True` e `False` começam com maiúscula.** `true` dá `NameError`.

Para descobrir o tipo de qualquer valor:

```python
altura = 1.75
print(type(altura))         # <class 'float'>
```

### O tipo vem do valor, e pode mudar

Em Python você não declara o tipo. Ele é deduzido do que você guardou:

```python
dado = 25            # agora é int
dado = "vinte e cinco"   # agora é str, e o Python aceita numa boa
```

Isso é conveniente e é uma armadilha. Conveniente porque você escreve menos. Armadilha porque
ninguém te avisa quando o tipo muda por engano, e o erro só aparece lá na frente, quando você
tenta fazer uma conta com o que virou texto.

### O mesmo `+` faz duas coisas diferentes

```python
2 + 3           # 5      -> com números, soma
"2" + "3"       # "23"   -> com textos, gruda (concatena)
"2" + 3         # TypeError: erro
```

O terceiro caso é o mais importante do módulo. Python não adivinha o que você quis dizer: se um
lado é texto e o outro é número, ele para e reclama.

Guarde este erro, porque ele vai voltar no módulo 03: tudo que vem de `input()` é texto, mesmo
quando o usuário digita um número.

### Nomes de variável

**Regras** (quebrar dá erro):

- Só letras, números e `_` (nada de espaço nem hífen)
- Não pode começar com número: `2nome` é inválido, `nome2` é válido
- Não pode ser palavra reservada: `class`, `if`, `for`, `return`…
- Maiúscula e minúscula são diferentes: `idade` e `Idade` são duas variáveis

**Convenções** (quebrar não dá erro, mas denuncia):

| Item | Convenção | Exemplo |
| --- | --- | --- |
| Variável comum | `snake_case` | `nome_completo`, `valor_total` |
| Constante | `MAIUSCULO_COM_UNDERLINE` | `TAXA_JUROS`, `PI` |
| Acentuação | sem acento no **nome**; com acento no **texto** | `preco_medio = "média"` |

> Sobre acento: `preço = 10` **funciona** em Python 3, não é erro. A escolha de não usar é
> convenção deste material, por um motivo prático: teclado trocado, terminal antigo e colega em
> outro sistema operacional transformam isso em dor de cabeça. Dentro das aspas, acentue normalmente.

E a regra que vale mais que todas: **o nome deve dizer o que a variável guarda.** `x` não diz nada;
`media_da_turma` diz tudo. A única exceção aceita neste material é o contador de laço, que pode ser
`i`.

### Trocar duas variáveis

Um truque que Python faz melhor que quase toda linguagem:

```python
primeiro = "A"
segundo = "B"

primeiro, segundo = segundo, primeiro    # pronto, trocados
```

Vale conhecer agora porque ele reaparece no módulo 11, quando você for ordenar valores.

## Exemplos guiados

| Arquivo | O que mostra |
| --- | --- |
| [exemplos/01_tipos_basicos.py](exemplos/01_tipos_basicos.py) | os quatro tipos e o `type()` |
| [exemplos/02_variaveis.py](exemplos/02_variaveis.py) | criar, reatribuir e por que `=` não é igualdade |
| [exemplos/03_nomes.py](exemplos/03_nomes.py) | nomes válidos, inválidos e as convenções |
| [exemplos/04_somando_tipos.py](exemplos/04_somando_tipos.py) | o `+` com números, com textos e o `TypeError` |

Para rodar qualquer um deles:

```bash
cd modulo-01-tipos-e-variaveis/exemplos
python 01_tipos_basicos.py
```

## Exercícios

1. [EXERCICIO-01-ficha-cadastral.md](exercicios/EXERCICIO-01-ficha-cadastral.md) (nível 1): criar
   variáveis dos quatro tipos e exibi-las formatadas.
2. [EXERCICIO-02-prevendo-tipos.md](exercicios/EXERCICIO-02-prevendo-tipos.md) (nível 2): prever
   tipo e resultado antes de rodar.
3. [EXERCICIO-03-simulador-de-troco.md](exercicios/EXERCICIO-03-simulador-de-troco.md) (nível 3):
   por que dinheiro não se guarda em `float`.

## Auto-avaliação

- [ ] Sei explicar por que `contador = contador + 1` não é uma contradição
- [ ] Diferencio `25` de `"25"` e sei dizer o que acontece ao somar cada um com `5`
- [ ] Sei descobrir o tipo de qualquer valor sem chutar
- [ ] Consigo dizer, olhando um nome de variável, se ele segue a convenção do Python
- [ ] Escrevi um `TypeError` de propósito e entendi a mensagem
- [ ] Sei trocar o conteúdo de duas variáveis

## Erros comuns

| Erro | O que está acontecendo |
| --- | --- |
| `1,75` em vez de `1.75` | em Python o separador decimal é ponto; a vírgula cria outra coisa |
| `TypeError: can only concatenate str` | você somou texto com número; converta antes (módulo 03) |
| `NameError: name 'true' is not defined` | `True` e `False` começam com maiúscula |
| `SyntaxError: invalid decimal literal` | nome de variável começando com número, como `2nome` |
| `nome` e `Nome` tratados como a mesma coisa | Python diferencia maiúsculas; são duas variáveis |
| Espaço ou hífen no nome da variável | `preco medio` e `preco-medio` dão `SyntaxError`; use `preco_medio` |
| Usar a variável antes de criá-la | o Python lê de cima para baixo; a criação tem que vir antes |

---

Anterior: [Módulo 00 — Preparação](../modulo-00-preparacao/) | Próximo: [Módulo 02 — Operadores](../modulo-02-operadores/)
