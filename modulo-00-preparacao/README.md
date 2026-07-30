# Módulo 00 — Preparação

Antes de aprender a programar, você precisa conseguir **rodar** um programa. Este módulo existe
para resolver isso e mais nada: no fim dele você terá o Python instalado, um arquivo seu
funcionando e — o que mais importa — não terá medo da tela vermelha de erro.

É o módulo mais curto da trilha. Também é o único que, se você pular, trava todos os outros.

## Objetivos de aprendizagem

Ao final deste módulo você será capaz de:

- [ ] Explicar o que acontece quando você "roda" um arquivo `.py`
- [ ] Executar um programa Python pelo VS Code e pelo terminal
- [ ] Ler uma mensagem de erro e identificar a linha e o tipo do problema
- [ ] Escrever comentários e saber quando eles valem a pena
- [ ] Interromper um programa travado sem fechar o computador

## Pré-requisitos

Nenhum. Este é o começo.

Só é preciso ter o Python e o VS Code instalados — o passo a passo está no
[Guia do aluno](../GUIA-DO-ALUNO.md), seções 1 e 2. Faça a instalação antes de continuar.

## Conceito

### O que é, afinal, "rodar" um programa

Um arquivo `.py` é texto puro. Você poderia abri-lo no Bloco de Notas: não tem mágica nem nada
compilado dentro. O que dá vida a ele é o **interpretador** — o programa chamado `python`, que você
instalou.

Quando você digita `python ola.py`, acontece o seguinte:

1. O interpretador abre o arquivo e lê a **primeira linha**
2. Executa o que ela manda
3. Passa para a linha seguinte
4. Repete até acabar o arquivo — ou até encontrar um erro

Esse detalhe — **de cima para baixo, uma linha por vez** — explica quase todo comportamento
estranho que você vai encontrar no começo. Se uma variável "não existe", quase sempre é porque a
linha que a cria está *abaixo* da linha que a usa.

### O primeiro programa

```python
print("Olá, mundo!")
```

Uma linha. `print` é uma **função**: um comando pronto que já vem com o Python. O que estiver entre
os parênteses é mostrado na tela. As aspas dizem "isto é texto" — sem elas, o Python tentaria
entender `Olá, mundo!` como nomes de variáveis e reclamaria.

### O erro não é o inimigo

Todo mundo trava aqui na primeira semana: o programa quebra, aparece um bloco vermelho e a reação
natural é fechar tudo. Erro de leitura, não de programação.

A mensagem de erro é a coisa mais útil que o Python te dá. Ela tem três partes:

```text
  File "ola.py", line 3
    print("Olá
          ^
SyntaxError: unterminated string literal
```

| Parte | O que diz |
| --- | --- |
| `line 3` | **onde** olhar |
| `^` | o ponto exato que confundiu o interpretador |
| `SyntaxError: ...` | **o quê** aconteceu |

Leia sempre a **última linha primeiro** — é ela que nomeia o problema. Depois suba para achar a
linha. Nesse exemplo: faltou fechar as aspas.

Vale decorar dois nomes que você vai ver muito:

| Erro | Significado prático |
| --- | --- |
| `SyntaxError` | erro de escrita. O Python nem começou a rodar. |
| `NameError` | você usou um nome que não existe. Quase sempre erro de digitação. |

### Comentários

Tudo depois de `#` é ignorado pelo interpretador:

```python
# Isto é um comentário: o Python não lê
print("Isto roda")     # o comentário pode vir no fim da linha também
```

Comentário serve para explicar **por que** o código faz algo, não o que ele faz:

```python
# Ruim: repete o óbvio
idade = 18          # atribui 18 a idade

# Bom: explica a decisão
idade = 18          # idade mínima exigida pela legislação
```

No começo você vai comentar demais, e tudo bem — comentar demais é fase, e ensina a pensar sobre o
próprio código.

### Quando o programa trava

Vai acontecer, principalmente a partir do módulo 05. O programa não responde, o cursor fica
piscando e nada acontece.

**`Ctrl + C` no terminal.** Isso interrompe o programa em execução. Não precisa fechar a janela,
nem reiniciar nada.

## Exemplos guiados

| Arquivo | O que mostra |
| --- | --- |
| [exemplos/01_ola_mundo.py](exemplos/01_ola_mundo.py) | o menor programa possível e o `print` com mais de um valor |
| [exemplos/02_ordem_de_execucao.py](exemplos/02_ordem_de_execucao.py) | de cima para baixo, uma linha por vez |
| [exemplos/03_lendo_o_erro.py](exemplos/03_lendo_o_erro.py) | provocar erros de propósito e aprender a ler a mensagem |

Para rodar qualquer um deles:

```bash
cd modulo-00-preparacao/exemplos
python 01_ola_mundo.py
```

Se `python` não for reconhecido, tente `python3`. Se nenhum funcionar, a instalação não colocou o
Python no PATH — volte à seção 1 do [Guia do aluno](../GUIA-DO-ALUNO.md).

## Exercícios

1. [EXERCICIO-01-cartao-de-visita.md](exercicios/EXERCICIO-01-cartao-de-visita.md) — seu primeiro
   programa escrito do zero.

## Auto-avaliação

- [ ] Rodei um arquivo `.py` pelo terminal, não só pelo botão do VS Code
- [ ] Sei explicar por que o Python lê o arquivo de cima para baixo
- [ ] Provoquei um erro de propósito e li a mensagem inteira
- [ ] Sei dizer, olhando um erro, qual linha olhar
- [ ] Sei o que `Ctrl + C` faz
- [ ] Escrevi um comentário que explica uma decisão, não o óbvio

## Erros comuns

| Erro | O que está acontecendo |
| --- | --- |
| `'python' não é reconhecido como comando` | o Python não está no PATH; reinstale marcando "Add Python to PATH" |
| `No such file or directory` | você está na pasta errada, ou digitou o nome do arquivo diferente do real |
| `SyntaxError: unterminated string literal` | faltou fechar aspas |
| `SyntaxError: '(' was never closed` | faltou fechar parêntese |
| `NameError: name 'primt' is not defined` | erro de digitação; o Python ainda completa com `Did you mean: 'print'?` — leia até o fim |
| Acentos saem trocados no terminal do Windows | o `cmd.exe` antigo não usa UTF-8; use o terminal do VS Code ou o Windows Terminal |
| Salvou o arquivo com `.txt` no fim | o Windows esconde extensões; confira se é mesmo `.py` |

---

Próximo: [Módulo 01 — Tipos e variáveis](../modulo-01-tipos-e-variaveis/)
