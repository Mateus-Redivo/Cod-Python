# Módulo 13 — Estudo de caso: um sistema CRUD

Todos os módulos anteriores ensinaram peças. Este mostra uma **casa construída**: um sistema
completo, funcionando, com menu, cadastro, edição, exclusão e relatórios.

A diferença é que aqui você não escreve, você **lê**. O objetivo é ver como as peças se encaixam
antes de montar as suas, no módulo 14.

## O que é CRUD

É a sigla das quatro operações que quase todo sistema de cadastro faz:

| Letra | Operação | No sistema de notas |
| --- | --- | --- |
| **C** | *Create*: criar | cadastrar um aluno |
| **R** | *Read*: ler | listar alunos e médias |
| **U** | *Update*: atualizar | alterar nome ou notas |
| **D** | *Delete*: excluir | remover um aluno |

Sistema de biblioteca, de estoque, de pacientes, de pedidos: todos são CRUD com nomes diferentes.
Aprender um é aprender o padrão.

## Objetivos de aprendizagem

Ao final deste módulo você será capaz de:

- [ ] Explicar as quatro operações de um CRUD
- [ ] Descrever como o menu principal organiza um programa inteiro
- [ ] Identificar onde os dados moram e por que ficam em listas paralelas
- [ ] Rastrear uma operação do menu até o dado sendo alterado
- [ ] Reconhecer as decisões de projeto e discutir alternativas
- [ ] Apontar defeitos num sistema que funciona

## Pré-requisitos

[Módulo 12 — Leitura e refatoração](../modulo-12-leitura-e-refatoracao/) concluído. Este módulo usa
**tudo**: listas, laços, condicionais, funções, tratamento de erros e a habilidade de ler código
alheio.

## Conceito

### A anatomia de um CRUD

Todo sistema deste tipo tem três camadas, mesmo quando ninguém as nomeia:

```text
┌─────────────────────────────────────┐
│  MENU        while True: escolha    │  <- conversa com o usuário
├─────────────────────────────────────┤
│  OPERAÇÕES   cadastrar(), listar()  │  <- uma função por ação
├─────────────────────────────────────┤
│  DADOS       alunos = []            │  <- onde tudo fica guardado
└─────────────────────────────────────┘
```

O menu não sabe como um aluno é guardado. As operações não sabem qual tecla o usuário apertou. Essa
separação é o que permite mudar uma camada sem mexer nas outras.

### O laço principal

O coração de qualquer sistema interativo é sempre o mesmo:

```python
while True:
    mostrar_menu()
    opcao = ler_opcao()

    if opcao == 1:
        cadastrar()
    elif opcao == 2:
        listar()
    ...
    elif opcao == 0:
        break
```

É o menu com sentinela do módulo 05, com o `match/case` do módulo 04 e as funções do módulo 08.
Nada de novo: só tudo junto.

### Onde os dados moram

```python
alunos = []     # ["Ana", "Bruno"]
notas = []      # [[8.0, 7.5], [6.0]]
```

Duas listas **paralelas**: `alunos[0]` é a Ana, e `notas[0]` são as notas dela. É a mesma estrutura
que o módulo 08 apontou como frágil e o módulo 09 mostrou como resolver.

Repare que o sistema real usa a versão frágil. Isso é honesto: o código foi escrito assim, funciona,
e reescrevê-lo seria o exercício 03.

### As decisões escondidas

Um sistema que funciona está cheio de escolhas que ninguém anuncia. Ao ler, procure por elas:

| Decisão | Alternativa que existia |
| --- | --- |
| Índice mostrado ao usuário começa em 1 | mostrar o índice interno, começando em 0 |
| Excluir remove sem confirmar | pedir "tem certeza?" antes |
| Dados somem ao fechar o programa | gravar em arquivo (é o que o exemplo 03 faz) |
| Nome duplicado é permitido | recusar cadastro repetido |
| Média de aluno sem notas é 0 | avisar "sem notas" em vez de inventar zero |

Nenhuma é obviamente certa. Todas têm consequência.

## Exemplos guiados

| Arquivo | O que mostra |
| --- | --- |
| [exemplos/01_sistema_notas.py](exemplos/01_sistema_notas.py) | o CRUD completo, com listas paralelas (comece por ele) |
| [exemplos/02_sistema_produtos.py](exemplos/02_sistema_produtos.py) | o mesmo padrão, com mais campos e relatórios |
| [exemplos/03_sistema_com_arquivo.py](exemplos/03_sistema_com_arquivo.py) | dados que **sobrevivem** ao fechar o programa |

Para rodar:

```bash
cd modulo-13-estudo-de-caso-crud/exemplos
python 01_sistema_notas.py
```

**Use o sistema antes de ler o código.** Cadastre três alunos, lance notas, altere um, exclua outro,
tente quebrar. Só depois abra o arquivo: você vai reconhecer cada função pelo que ela fazia na
tela.

### Sobre o exemplo 03

Ele grava os dados num arquivo `.txt`, e por isso eles continuam lá na próxima execução. Ler e
escrever arquivos é assunto **além desta trilha**: está aqui para você ver que existe, e entender
por que os outros dois "esquecem" tudo ao fechar.

## Exercícios

1. [EXERCICIO-01-mapeando-o-sistema.md](exercicios/EXERCICIO-01-mapeando-o-sistema.md) (nível 1): usar, mapear e rastrear uma operação.
2. [EXERCICIO-02-estendendo-o-sistema.md](exercicios/EXERCICIO-02-estendendo-o-sistema.md) (nível 2): acrescentar funcionalidades sem quebrar o que existe.
3. [EXERCICIO-03-auditoria-do-sistema.md](exercicios/EXERCICIO-03-auditoria-do-sistema.md) (nível 3): encontrar os defeitos de um sistema que funciona.

## Auto-avaliação

- [ ] Sei dizer o que significa cada letra de CRUD e apontá-la no código
- [ ] Consigo rastrear a opção "excluir" do menu até a linha que remove o dado
- [ ] Sei explicar por que o sistema mostra `1.` mas guarda no índice `0`
- [ ] Identifiquei pelo menos três decisões de projeto e suas alternativas
- [ ] Encontrei pelo menos um defeito por conta própria
- [ ] Consigo descrever a estrutura de dados sem olhar o código

## Erros comuns

| Erro | O que está acontecendo |
| --- | --- |
| Ler o código antes de usar o sistema | você perde a chance de ligar cada função ao que viu na tela |
| Confundir o índice mostrado com o guardado | o usuário vê 1, a lista usa 0: a conversão fica num lugar só |
| Achar que "funciona" significa "está certo" | o exercício 03 existe para desfazer essa ideia |
| Alterar o sistema sem guardar a saída antes | sem a versão original, não há como comparar |
| Excluir um item enquanto percorre a lista | o laço se perde; é o erro clássico do módulo 06 |

---

Anterior: [Módulo 12 — Leitura e refatoração](../modulo-12-leitura-e-refatoracao/) | Próximo: [Módulo 14 — Projeto integrador](../modulo-14-projeto-integrador/)
