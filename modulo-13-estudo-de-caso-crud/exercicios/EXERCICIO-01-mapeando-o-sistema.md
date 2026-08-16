# Exercício 01 — Mapeando o sistema

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 1 de 3 | 40 min | leitura de código, rastreio, estrutura de dados |

## Objetivo

Entender um sistema completo sem alterar uma linha. Você vai usá-lo, mapeá-lo e rastrear uma
operação de ponta a ponta.

## Parte 1 — Use antes de ler

Rode [01_sistema_notas.py](../exemplos/01_sistema_notas.py) e faça, nesta ordem:

1. Cadastre três alunos
2. Lance duas notas para cada um
3. Liste todos
4. Altere o nome de um
5. Exclua um
6. Liste de novo
7. Tente quebrar: opção inválida, aluno que não existe, letra onde se pede número

Anote **o que aconteceu** em cada passo (principalmente no 7).

## Parte 2 — O mapa

Só agora abra o arquivo. Preencha:

| Opção do menu | Função que ela chama | O que a função altera |
| --- | --- | --- |
| 1 | | |
| 2 | | |
| 3 | | |
| ... | | |

E responda:

**a)** Quais variáveis guardam os dados? Em que linha elas nascem?

**b)** Como o programa sabe que a nota `notas[2]` pertence ao aluno `alunos[2]`?

**c)** Quantas funções existem no arquivo? Alguma é chamada por outra função, e não pelo menu?

## Parte 3 — Rastreie a exclusão

Escolha a opção de **excluir aluno** e siga o caminho completo:

1. Qual função o menu chama?
2. O que ela pergunta ao usuário?
3. Como o número digitado vira um índice de lista?
4. Qual linha remove o aluno? E qual remove as notas dele?
5. O que aconteceria se apenas uma das duas listas fosse alterada?

Desenhe o caminho, com os nomes das funções e as linhas.

## Parte 4 — O índice que engana

O sistema mostra os alunos numerados a partir de **1**, mas guarda a partir de **0**.

**a)** Em qual linha exata acontece a conversão?

**b)** Quantas vezes essa conversão aparece no arquivo?

**c)** O que aconteceria se alguém esquecesse o `- 1` em um dos lugares?

## Critérios de aceitação

- [ ] O sistema foi usado antes de o código ser aberto
- [ ] A tabela do menu está completa
- [ ] O rastreio da exclusão cita nomes de funções e números de linha reais
- [ ] A resposta de (b) da Parte 2 fala das listas paralelas
- [ ] A Parte 4 aponta a linha exata da conversão

---

Gabarito: não há, e é de propósito. Este exercício produz **o seu** mapa do sistema, e mapas
diferentes podem estar igualmente certos. Compare com o de um colega: onde vocês divergiram, alguém
enxergou algo que o outro não viu.
