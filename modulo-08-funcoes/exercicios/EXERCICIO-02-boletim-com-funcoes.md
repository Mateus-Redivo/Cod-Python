# Exercício 02 — Boletim, agora com funções

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 2 de 3 | 40 min | `def`, `return`, decomposição, reescrita |

## Objetivo

Pegar o boletim que você escreveu no módulo 06 e reescrevê-lo em funções — **sem mudar o que ele
faz**. É a sua primeira refatoração de verdade.

## Ponto de partida

Use a sua própria solução do
[EXERCICIO-02-boletim.md do módulo 06](../../modulo-06-listas/exercicios/EXERCICIO-02-boletim.md).
Se não a tiver mais, o gabarito de lá serve.

Ele hoje é um bloco corrido: lê as notas, valida, calcula soma, média, maior, menor, conta quantas
estão acima da média, decide a situação e imprime tudo.

## Requisitos

1. Crie um arquivo `boletim_com_funcoes.py`.
2. Extraia, no mínimo, estas funções:

| Função | Recebe | Devolve |
| --- | --- | --- |
| `nota_e_valida` | uma nota | `True` ou `False` |
| `ler_notas` | a quantidade | a lista de notas já validadas |
| `calcular_media` | a lista | a média |
| `contar_acima_da_media` | a lista | quantas notas superam a média |
| `classificar_turma` | a média | `"Aprovada"`, `"Recuperação"` ou `"Reprovada"` |
| `mostrar_boletim` | a lista | nada (esta pode `print`) |

3. O corpo principal do programa deve caber em **poucas linhas**, quase todas chamadas de função.
4. A saída tem que ser **idêntica** à do exercício original. Compare rodando os dois.
5. Nenhuma função pode usar `global`.

## O critério que define o exercício

Refatorar significa mudar a estrutura **sem mudar o comportamento**. Se a saída mudou, não foi
refatoração — foi um programa novo, e provavelmente com bug.

Rode os dois programas com as mesmas notas e compare a saída linha por linha.

## Critérios de aceitação

- [ ] A saída é idêntica à do boletim do módulo 06, para as mesmas entradas
- [ ] Existem pelo menos as seis funções pedidas
- [ ] Só `mostrar_boletim` tem `print`; as demais devolvem valores
- [ ] Nenhum `global` no arquivo
- [ ] O programa principal tem menos de 12 linhas
- [ ] Testei com 0 notas, 1 nota e 5 notas

## Por que isto vale a pena

Compare os dois arquivos lado a lado e responda para si mesmo:

- Se a regra de aprovação mudasse de 7.0 para 6.0, em quantos lugares você mexeria em cada versão?
- Se você quisesse reaproveitar o cálculo da média em outro programa, qual das duas versões
  permitiria copiar só o que interessa?

## Desafio opcional

Escreva uma função `nota_e_valida` que aceite também os limites como parâmetros, com valores
padrão 0 e 10. Assim ela serve para notas de 0 a 10 **e** para notas de 0 a 100, sem duplicação.

---

Gabarito: [gabaritos/modulo-08-ex02-boletim-com-funcoes/](../../gabaritos/modulo-08-ex02-boletim-com-funcoes/) —
depois de tentar, não antes.
