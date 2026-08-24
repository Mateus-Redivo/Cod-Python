# Cadastro de notas

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| Avançado | 50 min | funções, menu em laço, dicionário, `try/except`, saída tabelada |

## O que fazer

Monte um sistema de menu que registra alunos com três notas cada e calcula médias.

## Requisitos

1. Menu em laço, com quatro opções: registrar aluno, ver todos, calcular média de um aluno, sair.
2. Registrar pede nome e as três notas. Se alguma nota não for um número válido, avise e não
   registre o aluno.
3. Ver todos exibe uma tabela alinhada com nome, as três notas e a média. Se não houver ninguém
   cadastrado, diga isso em vez de mostrar tabela vazia.
4. Calcular média pede o nome e mostra a média. Se o aluno não existir, avise.
5. Opção fora do menu mostra "Opção inválida" e volta ao menu, sem encerrar o programa.
6. Cada responsabilidade em sua própria função. Nada de tudo dentro do `while`.

## Exemplo de saída

```text
===== SISTEMA DE NOTAS =====
1 - Registrar novo aluno
2 - Ver todos os alunos
3 - Calcular média de um aluno
4 - Sair
Escolha uma opção: 1
Nome do aluno: Ana
Nota 1: 8
Nota 2: 7.5
Nota 3: 9
Aluno Ana registrado com sucesso!
```

E a listagem:

```text
===== REGISTROS DE ALUNOS =====
Nome            Nota 1  Nota 2  Nota 3  Média
---------------------------------------
Ana                8.0     7.5     9.0     8.2
```

## Critérios de aceitação

- [ ] Letra no lugar de nota não derruba o programa
- [ ] Listar sem nenhum aluno cadastrado avisa em vez de quebrar
- [ ] Buscar aluno inexistente avisa em vez de quebrar
- [ ] Opção inválida não encerra o programa
- [ ] A função que calcula a média não imprime nada, só retorna

## Sobre a estrutura de dados

O gabarito guarda os dados em um **dicionário**, com o nome do aluno como chave e a lista de notas
como valor. Se você ainda não viu dicionários, resolva com duas listas paralelas (uma de nomes,
outra de notas), como no [módulo 13](../../modulo-13-estudo-de-caso-crud/). Depois compare as duas
soluções: repare quanto código o dicionário economiza na hora de procurar um aluno pelo nome.

---

Gabarito: [gabaritos/banco-de-exercicios/nivel-3-avancado/cadastro-notas/](../../gabaritos/banco-de-exercicios/nivel-3-avancado/cadastro-notas/),
depois de tentar, não antes.

Pré-requisito: [Módulo 10 — Tratamento de erros](../../modulo-10-tratamento-de-erros/).
