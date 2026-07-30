# Guia do aluno

Antes de estudar o primeiro módulo, gaste vinte minutos aqui. Este guia responde as três perguntas
que todo mundo faz na primeira semana: **como instalo**, **como rodo** e **como estudo**.

---

## 1. Instalar o Python

### Windows

1. Vá em [python.org/downloads](https://www.python.org/downloads/) e baixe a versão mais recente.
2. Abra o instalador e — isto é importante — **marque a caixa "Add Python to PATH"** antes de clicar
   em *Install Now*. Se você esquecer, o terminal vai dizer que não conhece o comando `python` e
   você vai achar que a instalação falhou. Ela não falhou; só ficou escondida.
3. Termine a instalação e feche tudo.

### macOS e Linux

Já vem com Python instalado, mas costuma ser uma versão antiga. No macOS, instale pelo
[python.org](https://www.python.org/downloads/) ou com `brew install python`. No Linux, use o
gerenciador da sua distribuição (`sudo apt install python3` no Ubuntu/Debian).

### Conferir se deu certo

Abra o terminal (no Windows: tecle `Win`, digite "cmd" e abra o Prompt de Comando) e digite:

```bash
python --version
```

Você deve ver algo como `Python 3.12.4`. Qualquer versão **3.10 ou superior** serve para este
material — o módulo de condicionais usa `match/case`, que só existe a partir da 3.10.

Se aparecer erro, tente `python3 --version`. Em vários sistemas o comando é esse, e aí é `python3`
que você vai usar no lugar de `python` no resto do guia.

---

## 2. Instalar o VS Code

O Python roda sem editor nenhum, mas escrever código no Bloco de Notas é sofrimento sem motivo.

1. Baixe em [code.visualstudio.com](https://code.visualstudio.com/) e instale.
2. Abra o VS Code, clique no ícone de **Extensões** na barra lateral (o quadradinho com blocos).
3. Procure por **Python** (a extensão da Microsoft) e instale.

Essa extensão é o que te dá o botão de "play" para rodar o arquivo, o destaque de cores e o aviso
de erro antes mesmo de você rodar.

---

## 3. Rodar o seu primeiro arquivo

### Pelo VS Code

1. `Arquivo → Abrir Pasta` e escolha a pasta deste repositório.
2. Clique em qualquer arquivo `.py` na barra lateral.
3. Clique no **▷** no canto superior direito.
4. A saída aparece no painel **Terminal**, embaixo.

### Pelo terminal

O jeito que sempre funciona, em qualquer máquina:

```bash
cd modulo-05-lacos-de-repeticao/exemplos
python 01_while.py
```

O `cd` (*change directory*) entra na pasta. O `python` executa o arquivo. Se você errar o nome do
arquivo, o Python avisa com `No such file or directory` — não é um erro grave, é só um endereço
errado.

### Dois atalhos que valem ouro

| Atalho | Para que serve |
| --- | --- |
| `Ctrl + C` no terminal | mata o programa. É o seu botão de pânico quando um laço trava. |
| Seta ↑ no terminal | repete o último comando. Você vai rodar o mesmo arquivo dezenas de vezes. |

---

## 4. Como estudar cada módulo

A ordem importa. Cada módulo assume o anterior, e pular etapa cobra o preço depois.

1. **Leia o README do módulo inteiro**, sem correr para o código. É ali que mora a aula.
2. **Rode cada arquivo de `exemplos/`** na ordem numerada, um por vez.
3. **Quebre o exemplo de propósito.** Todo exemplo termina com uma seção *Experimento*, pedindo
   para você mudar alguma coisa e ver o programa reagir. Faça. Ler código não ensina; mexer, sim.
4. **Faça os exercícios** sem olhar gabarito. Erro é a parte do processo em que o aprendizado
   acontece — não é o obstáculo, é o caminho.
5. **Marque a auto-avaliação** no fim do README. Se sobrar caixinha desmarcada, volte para o
   exemplo correspondente antes de seguir.

### Quanto tempo isso leva

Um módulo por sessão de estudo, em média duas horas contando os exercícios. Estudar dois módulos
seguidos no mesmo dia funciona pior do que parece: o conteúdo do segundo depende do primeiro estar
assentado.

---

## 5. Quando travar

Vai travar. Faz parte. A ordem certa de socorro é esta:

1. **Leia a mensagem de erro até o fim.** A última linha diz o *tipo* do erro e a linha diz *onde*.
   `NameError: name 'contdor' is not defined` é um erro de digitação, não um mistério.
2. **Vá na seção "Erros comuns"** do README do módulo. Quatro em cada cinco travadas estão lá.
3. **Consulte o [Glossário](GLOSSARIO.md)** se a dúvida for de vocabulário ("o que é iterar?").
4. **Consulte o [resumo de sintaxe](material-apoio/resumo-sintaxe.md)** se for "como se escreve
   mesmo?".
5. **Tente por mais 20 minutos** antes de abrir [gabaritos/](gabaritos/). Sério: o gabarito é para
   conferir uma solução que você já tem, não para começar uma que você não tem.
6. **Pergunte** — traga o código e a mensagem de erro completa, não só "não funcionou".

---

## 6. Onde fica cada coisa

| Pasta | O que tem dentro |
| --- | --- |
| `modulo-NN-*/` | a trilha principal. README (a aula), `exemplos/` e `exercicios/`. |
| `gabaritos/` | as resoluções comentadas, longe dos enunciados de propósito. |
| `banco-de-exercicios/` | prática extra, por nível, quando um módulo não bastou. |
| `projetos/` | jogos e calculadoras. Opcional, e o melhor jeito de se divertir com o que aprendeu. |
| `material-apoio/` | resumo de sintaxe, guia de comentários e a rubrica de avaliação. |

---

Pronto. Comece pelo [README da raiz](README.md), que tem a trilha completa em ordem.
