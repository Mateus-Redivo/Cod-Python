# Gabarito — Módulo 13, Exercício 03: Auditoria do sistema

Enunciado: [EXERCICIO-03-auditoria-do-sistema.md](../../../modulo-13-estudo-de-caso-crud/exercicios/EXERCICIO-03-auditoria-do-sistema.md)

> Rode as 11 tentativas antes de ler. Uma auditoria que você leu não treina nada; uma que você fez
> muda a forma como você olha código para sempre.

---

## Parte 1 — O que a exploração revela

O sistema **não quebra** na maioria dos casos: ele tem validações razoáveis, e é por isso que serve
de estudo. Os problemas são mais sutis:

| Tentativa | O que acontece | É defeito? |
| --- | --- | --- |
| Listar sem alunos | avisa "Nenhum aluno cadastrado" | Não: está bem tratado |
| Nome vazio (só Enter) | **cadastra um aluno sem nome** | Sim |
| Nome duplicado | **cadastra os dois** | Discutível |
| Nota 15 ou -3 | depende da versão; frequentemente **aceita** | Sim |
| Nota com letra | tratado com `try/except` | Não |
| Aluno número 99 | avisa "Aluno inválido!" | Não |
| Aluno número 0 | avisa "Aluno inválido!" | Não |
| Excluir o último e listar | avisa que não há alunos | Não |
| Média de aluno sem notas | **mostra 0.00** | Sim |
| Letra na opção do menu | tratado, devolve -1 | Não |
| Fechar e reabrir | **todos os dados somem** | Discutível |

Repare que o autor tratou bem justamente o que dá erro visível (`ValueError`, índice inválido). O
que passou foram os casos em que o programa **aceita** algo e segue em frente.

---

## Parte 2 — A classificação

**Bugs** (faz errado o que promete):

- **Média 0.00 para aluno sem notas.** O sistema promete mostrar a média; um aluno sem notas não tem
  média, e `0.00` é indistinguível de quem tirou zero em tudo. É o mesmo erro que o gabarito do
  módulo 08 discutiu ao decidir o que `calcular_media([])` deveria devolver.

**Falta de validação** (aceita o que não deveria):

- **Nome vazio.** Uma linha (`if len(nome) == 0`) resolveria. O resultado é uma lista com um item
  invisível, impossível de identificar depois.
- **Nota fora de 0 a 10.** O `try/except` protege contra letras, mas não contra `15`. Tipo e faixa
  são problemas diferentes: é a lição do módulo 10.

**Decisões de projeto discutíveis** (funciona assim de propósito):

- **Nome duplicado permitido.** Defensável: pode haver dois "João Silva" numa turma. O problema não
  é permitir: é não haver nenhuma outra forma de distingui-los.
- **Dados somem ao fechar.** Consciente: gravar em arquivo é o que o exemplo 03 faz, e exigiria
  conteúdo além da trilha. Legítimo num sistema didático, inaceitável num real.
- **Exclusão sem confirmação.** Operação destrutiva sem rede de proteção. Não é bug, mas seria a
  primeira reclamação de qualquer usuário.

---

## Parte 3 — Os dados

**a) Como as listas desalinham**

Elas **não** desalinham no fluxo normal, e isso é mérito do autor: `cadastrar` faz `alunos.append`
e `notas.append([])` juntos; `excluir` faz os dois `pop` juntos.

O desalinhamento aparece se alguém **mexer no código**. Basta acrescentar uma funcionalidade e
esquecer metade do par:

```python
def cadastrar_rapido(nome):
    alunos.append(nome)        # esqueceu o notas.append([])
```

A partir daí, `alunos` tem um item a mais. `listar_alunos` percorre `range(len(alunos))` e acessa
`notas[i]`: o último índice não existe, e vem `IndexError`.

**A fragilidade não está no código atual: está no que ele exige de quem for mexer nele.** Toda
alteração precisa lembrar de duas listas. Nada no programa força esse acordo.

**b) A estrutura que impede o problema**

```python
# Cada aluno é uma linha: [nome, [notas]]
alunos = [
    ["Ana",   [8.0, 7.5]],
    ["Bruno", [6.0]],
]
```

Agora cadastrar é uma operação só:

```python
alunos.append([nome, []])
```

Impossível acrescentar o nome e esquecer as notas: eles nascem juntos. É a matriz do módulo 09
resolvendo exatamente o problema que o módulo 08 apontou.

**c) O que precisaria mudar**

Praticamente todas as funções que tocam nos dados:

`listar_alunos`, `cadastrar_aluno`, `lancar_notas`, `alterar_aluno`, `excluir_aluno`,
`calcular_media`, além do `verifica_lista_vazia`, que passa a checar uma lista só.

Na prática, o arquivo inteiro. O acesso muda de `alunos[i]` e `notas[i]` para `alunos[i][0]` e
`alunos[i][1]`.

**d) Vale a pena?**

**Depende de o sistema ainda ir crescer.**

Pelos critérios do módulo 12:

1. *Alguém vai mexer nisso?* Se este sistema vai ganhar as funcionalidades do exercício 02 e virar
   base do projeto do módulo 14: sim, e a fragilidade vai cobrar.
2. *Dá para provar que não quebrei?* Aqui está o problema: o sistema é interativo, e não há como
   rodar um `diff` simples. Seria preciso testar manualmente todo o roteiro. É trabalhoso, mas
   viável.
3. *Eu entendo o que ele faz?* Depois do exercício 01, sim.

**Minha resposta: vale, e antes de acrescentar as cinco funcionalidades do exercício 02**, não
depois. Cada funcionalidade nova escrita sobre a estrutura frágil é mais código para migrar depois.

Repare que essa conclusão contraria a ordem dos exercícios deste módulo. É uma tensão real: a ordem
didática (estender primeiro, auditar depois) não é a ordem que eu recomendaria num projeto de
verdade.

---

## Parte 4 — O relatório

> **Auditoria do Sistema de Notas**
>
> O sistema cumpre o que promete e trata bem os erros mais visíveis: entrada não numérica e índice
> inexistente estão protegidos. Os problemas abaixo estão em ordem de gravidade.
>
> **1. Média de aluno sem notas é exibida como 0.00.**
> Um aluno recém-cadastrado aparece com média zero, igual a quem tirou zero em todas as provas.
> Numa reunião de conselho de classe, os dois casos exigem decisões opostas e o sistema não os
> distingue. É o mais grave porque produz informação **errada** com aparência de correta. Os
> outros dois produzem dados ruins, mas visíveis.
> *Sugestão:* exibir "sem notas" no lugar do número.
>
> **2. Nota fora do intervalo 0 a 10 é aceita.**
> Um `15` digitado por engano entra na média e a distorce silenciosamente. O usuário só percebe se
> conferir na calculadora, e se conferisse, não precisaria do sistema.
> *Sugestão:* validar a faixa com `while`, como já se faz com o tipo.
>
> **3. Nome vazio é aceito no cadastro.**
> Cria um aluno invisível na listagem, que ocupa uma posição e não pode ser identificado para
> alteração ou exclusão. Menos grave que os anteriores porque é visível de imediato: o usuário
> percebe e recadastra.
> *Sugestão:* recusar nome vazio, uma linha no cadastro.
>
> **Por onde começar:** os três se resolvem com validações pontuais, sem tocar na estrutura. Eu
> começaria pelo item 3, que é o mais barato, para pegar o ritmo; depois o 2, que é o mesmo padrão;
> e por fim o 1, que exige decidir como exibir a ausência de média: a única decisão de produto dos
> três.
>
> **Recomendação adicional:** se o sistema for ganhar novas funcionalidades, vale trocar as duas
> listas paralelas por uma lista de registros antes de crescer mais. A mudança é grande, e fica mais
> cara a cada funcionalidade acrescentada.

---

## O que este exercício ensina

Um sistema pode rodar, tratar erros e ainda assim ter defeitos que só aparecem quando alguém o usa
de verdade. Testar é diferente de rodar: rodar confirma que funciona no caminho feliz; testar é
procurar onde ele não funciona.

E a parte mais difícil da auditoria não é achar os problemas: é **ordená-los** e separá-los das
próprias preferências. Um relatório que trata "eu faria diferente" como defeito perde a autoridade
para apontar os defeitos reais.
