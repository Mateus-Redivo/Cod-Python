# Exercício 03 — Auditoria do sistema (desafio)

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 3 de 3 | 60 min | teste exploratório, julgamento, projeto de dados |

## Objetivo

Encontrar os defeitos de um sistema que **funciona**. Não há erro de sintaxe, não há tela vermelha,
e mesmo assim há problemas. Achá-los é a diferença entre "roda" e "está pronto".

## Parte 1 — Quebre o sistema

Rode [01_sistema_notas.py](../exemplos/01_sistema_notas.py) e tente cada item, anotando o que
acontece:

| Tentativa | O que aconteceu? | É defeito? |
| --- | --- | --- |
| Listar sem nenhum aluno cadastrado | | |
| Cadastrar aluno com nome vazio (só Enter) | | |
| Cadastrar dois alunos com o mesmo nome | | |
| Lançar nota 15 ou -3 | | |
| Lançar nota com letra | | |
| Alterar aluno número 99 | | |
| Alterar aluno número 0 | | |
| Excluir o último aluno e depois listar | | |
| Ver a média de um aluno sem notas | | |
| Digitar letra na opção do menu | | |
| Fechar e abrir o programa de novo | | |

Marque como defeito o que **surpreenderia um usuário**, não só o que dá erro.

## Parte 2 — Classifique

Separe o que você achou em três grupos:

- **Bug**: o programa faz errado o que promete
- **Falta de validação**: aceita dado que não deveria
- **Decisão de projeto discutível**: funciona como foi feito, mas talvez não devesse

Para cada item, justifique o grupo em uma frase.

## Parte 3 — A pergunta dos dados

O sistema guarda os dados em duas listas paralelas:

```python
alunos = ["Ana", "Bruno"]
notas  = [[8.0, 7.5], [6.0]]
```

**a)** Descreva uma sequência de operações que deixaria as duas listas com **tamanhos diferentes**.
Se você concluir que não existe, explique o que impede.

**b)** Reescreva a estrutura usando o que o módulo 09 ensinou, de forma que nome e notas não possam
desalinhar.

**c)** Quantas funções do sistema você precisaria alterar para adotar a nova estrutura? Liste-as.

**d)** Vale a pena fazer essa mudança? Responda considerando o que o módulo 12 diz sobre quando
refatorar.

## Parte 4 — O relatório

Escreva um relatório curto, de até uma página, para o autor do sistema:

1. Os três defeitos mais graves, em ordem de gravidade, com a justificativa da ordem
2. Para cada um, o que aconteceria com um usuário real
3. Uma recomendação de por onde começar a consertar

Escreva como se fosse para alguém que vai ler e agir, não como lista de reclamações.

## Critérios de aceitação

- [ ] As 11 tentativas da Parte 1 foram executadas de verdade, com o resultado anotado
- [ ] A classificação distingue bug de falta de validação e de decisão de projeto
- [ ] A Parte 3(a) apresenta uma sequência concreta, ou explica por que não existe
- [ ] A nova estrutura de dados da Parte 3(b) está escrita em código
- [ ] O relatório ordena por gravidade **e justifica a ordem**
- [ ] A recomendação final é acionável, não genérica

## Uma observação

Este sistema não foi escrito para ser ruim. Ele foi escrito para funcionar, por alguém que estava
aprendendo, provavelmente com menos recursos do que você tem agora.

Auditar código alheio exige separar "está errado" de "eu faria diferente". As duas coisas aparecem
neste exercício, e distingui-las é metade do trabalho. Um relatório que trata preferência pessoal
como defeito perde a credibilidade para apontar os defeitos de verdade.

---

Gabarito: [gabaritos/modulo-13-ex03-auditoria-do-sistema/](../../gabaritos/modulo-13-ex03-auditoria-do-sistema/), depois de tentar, não antes.
