# Exercício 02 — Estendendo o sistema

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 2 de 3 | 60 min | funções, listas, menu, preservar o que existe |

## Objetivo

Acrescentar funcionalidades a um sistema que você não escreveu: sem quebrar nada do que já
funcionava. É o trabalho mais comum da profissão.

## Antes de começar

Guarde a versão original. Copie `01_sistema_notas.py` para `sistema_notas_original.py` e trabalhe
numa cópia chamada `sistema_notas.py`. O original fica intocado, para comparação.

## Requisitos — acrescente cinco funcionalidades

**1. Buscar aluno pelo nome.** Nova opção no menu. Recebe parte do nome e lista todos os que contêm
aquele trecho, sem diferenciar maiúsculas. Use a receita `.strip().lower()` do módulo 07.

**2. Relatório da turma.** Nova opção que mostra: total de alunos, média geral, aluno com maior
média, aluno com menor média e quantos estão acima da média geral.

**3. Confirmação antes de excluir.** Modifique a exclusão para perguntar "Confirma? (s/n)" e só
remover se a resposta for sim.

**4. Impedir nome duplicado.** No cadastro, recuse um nome que já exista (comparando sem diferenciar
maiúsculas) e avise.

**5. Ordenar a listagem.** Nova opção que lista os alunos ordenados por média, do maior para o
menor. Use `sorted()` ou um dos algoritmos do módulo 11, e mantenha a ordem de cadastro intacta na
listagem normal.

## A regra que não pode ser quebrada

**Tudo que funcionava antes tem que continuar funcionando.** Cadastrar, listar, alterar, excluir e
lançar notas não podem regredir.

Antes de entregar, refaça o roteiro do exercício 01 inteiro na sua versão e confirme que nada
quebrou.

## Critérios de aceitação

- [ ] As cinco funcionalidades funcionam
- [ ] O roteiro completo do exercício 01 ainda funciona
- [ ] A busca encontra "ana" quando o aluno é "Ana Silva"
- [ ] O relatório não quebra com zero alunos nem com um aluno só
- [ ] Excluir e responder "n" não remove nada
- [ ] Cadastrar "ANA" quando já existe "Ana" é recusado
- [ ] A listagem ordenada não altera a ordem da listagem normal
- [ ] Cada funcionalidade nova é uma função separada, com nome que diz o que faz

## Sobre o `global`

O sistema original usa listas globais (`alunos`, `notas`) que as funções alteram diretamente. Isso
contraria o que o módulo 08 recomendou.

**Não conserte isso agora.** Siga o padrão que o arquivo já usa: misturar "acrescentar
funcionalidade" com "mudar a arquitetura" é exatamente o que o módulo 12 desaconselha. Reescrever a
estrutura é assunto do exercício 03.

Sentir esse incômodo e **não** ceder a ele é parte do exercício.

## Desafio opcional

Acrescente a opção de **desfazer a última exclusão**. Pense em onde guardar o aluno removido e o que
acontece se o usuário pedir para desfazer sem ter excluído nada.

---

Gabarito: [gabaritos/modulo-13-ex02-estendendo-o-sistema/](../../gabaritos/modulo-13-ex02-estendendo-o-sistema/), depois de tentar, não antes.
