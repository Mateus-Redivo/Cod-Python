# Módulo 14 — Projeto integrador

Este é o último módulo, e o único sem conteúdo novo. Tudo que ele pede, você já aprendeu.

O que muda é que agora **ninguém te diz como fazer**. Você escolhe um sistema, decide a estrutura,
escreve do zero e entrega funcionando. É a diferença entre resolver exercícios e construir alguma
coisa.

## Objetivos de aprendizagem

Ao final deste módulo você será capaz de:

- [ ] Planejar um sistema antes de escrever a primeira linha
- [ ] Escolher a estrutura de dados adequada ao problema
- [ ] Construir um CRUD completo do zero
- [ ] Validar toda entrada do usuário
- [ ] Organizar o código em funções com responsabilidade única
- [ ] Entregar um projeto que outra pessoa consiga usar sem você explicando

## Pré-requisitos

**Todos os módulos anteriores**, do 00 ao 13. Este projeto usa cada um deles, e não há como
compensar um que ficou pela metade.

## O cardápio

Escolha **uma** das nove propostas. Todas têm o mesmo peso e a mesma dificuldade: escolha a que te
interessa, porque você vai passar algumas horas com ela.

| Proposta | Do que se trata |
| --- | --- |
| [Sistema de Biblioteca](propostas/Sistema_Biblioteca.md) | acervo, empréstimos e devoluções |
| [Cadastro de Pets](propostas/Sistema_CadastroPets.md) | animais, tutores e histórico |
| [Churrasco](propostas/Sistema_Churrasco.md) | participantes, itens e rateio da conta |
| [Controle de Gastos](propostas/Sistema_ControleGastos.md) | despesas por categoria e relatórios |
| [Loja de Doces](propostas/Sistema_LojaDoces.md) | produtos, vendas e estoque |
| [Sistema de Notas](propostas/Sistema_Notas.md) | alunos, notas e situação |
| [Playlist Musical](propostas/Sistema_PlaylistMusical.md) | músicas, playlists e ordenação |
| [Controle de Produtos](propostas/Sistema_Produtos.md) | estoque, entradas e saídas |
| [Lista de Tarefas](propostas/Sistema_TodoList.md) | tarefas, prioridades e conclusão |

> Se escolher **Sistema de Notas** ou **Controle de Produtos**, saiba que existe uma implementação
> pronta no [módulo 13](../modulo-13-estudo-de-caso-crud/exemplos/). Você pode escolhê-las, mas
> então a entrega precisa ir **além** do que o exemplo faz, e você deve dizer no relatório o que
> acrescentou. Copiar o exemplo não é entrega.

## Requisitos obrigatórios

Independentemente da proposta escolhida, o sistema precisa ter:

**Estrutura**

- [ ] Menu principal em laço, com opção de sair
- [ ] As quatro operações CRUD: cadastrar, listar, alterar e excluir
- [ ] Pelo menos **dois relatórios** com informação calculada (totais, médias, contagens, rankings)
- [ ] Dados guardados em lista de registros, **não** em listas paralelas

**Qualidade**

- [ ] Todo o código em funções; nenhuma com mais de 25 linhas
- [ ] Cada função faz **uma** coisa, e o nome diz qual
- [ ] Nenhum `global` para reatribuir dados
- [ ] Constantes nomeadas no lugar de números e textos soltos
- [ ] Nomes em `snake_case`, em português, sem abreviação críptica

**Robustez**

- [ ] Nenhuma sequência de digitação derruba o programa
- [ ] Toda entrada numérica valida tipo (`try`) **e** faixa (`if`)
- [ ] Operações destrutivas pedem confirmação
- [ ] Listas vazias são tratadas em todas as operações

**Entrega**

- [ ] Um arquivo `.py` que roda com `python nome_do_arquivo.py`
- [ ] Um `README.md` curto: o que o sistema faz, como rodar, quais opções existem
- [ ] Um relatório de decisões (modelo abaixo)

## O roteiro em quatro fases

Não comece escrevendo código. Sério.

### Fase 1 — Desenhe os dados (30 min, no papel)

Antes de qualquer linha, responda:

1. Que informações cada registro guarda? (nome, preço, data…)
2. Que tipo tem cada uma? (`str`, `int`, `float`, `bool`, lista)
3. Como fica um registro de exemplo, escrito em Python?

```python
# Exemplo para uma biblioteca:
livros = [
    ["1984", "Orwell", 1949, True],     # título, autor, ano, disponível
]
```

**Esta é a decisão mais cara de mudar depois.** Meia hora aqui economiza horas na frente.

### Fase 2 — Esqueleto que roda (1 h)

Escreva o menu completo, com todas as opções, e funções vazias que só imprimem "ainda não
implementado". Rode. Navegue por todas as opções.

Você terá um programa que não faz nada, e que **funciona**. A partir daqui, cada função preenchida
é um progresso testável.

### Fase 3 — Uma operação por vez (3–4 h)

Nesta ordem, e testando cada uma antes de passar à seguinte:

1. **Cadastrar**: sem ela, não há o que listar
2. **Listar**: sem ela, você não vê se o cadastro funcionou
3. **Excluir**: mais simples que alterar
4. **Alterar**: a mais trabalhosa
5. **Relatórios**: precisam de dados, que agora existem

Acrescente as validações **junto** com cada operação, não no fim. Deixar para depois significa
revisitar tudo.

### Fase 4 — Acabamento (1–2 h)

- Passe pelos requisitos obrigatórios, um por um
- Tente quebrar o próprio sistema com as 11 tentativas do
  [exercício 03 do módulo 13](../modulo-13-estudo-de-caso-crud/exercicios/EXERCICIO-03-auditoria-do-sistema.md)
- Peça para outra pessoa usar **sem você explicando nada**
- Escreva o README e o relatório de decisões

Aquele momento em que alguém usa e trava é o mais valioso do projeto. Anote onde a pessoa hesitou.

## O relatório de decisões

Uma página, respondendo:

1. **Qual estrutura de dados você escolheu e por quê?** Que alternativa você descartou?
2. **Qual foi a parte mais difícil?** Como você resolveu?
3. **O que você deixou de fora** por falta de tempo ou conhecimento?
4. **Que defeito você sabe que existe** e não consertou? (Responder "nenhum" é quase sempre sinal
   de que você não procurou.)
5. **Se fosse recomeçar, o que faria diferente?**

A pergunta 4 vale mais que as outras. Um aluno que conhece os limites do próprio trabalho está mais
adiantado que um que acha o trabalho perfeito.

## Como será avaliado

Pela [rubrica de avaliação](../material-apoio/rubrica-avaliacao.md), com os pesos de sempre:
funciona (40), lógica (20), legibilidade (20), uso dos conceitos (10), tratamento de entrada (10).

O relatório de decisões entra na nota de legibilidade: ele é parte de comunicar o seu trabalho.

## Auto-avaliação

Marque antes de entregar. Cada caixa em branco é um ponto a perder na rubrica.

- [ ] Desenhei a estrutura de dados **antes** de escrever a primeira linha
- [ ] Meu sistema roda do começo ao fim sem quebrar, faça o usuário o que fizer
- [ ] Nenhuma função minha passa de 25 linhas
- [ ] Consigo explicar por que escolhi esta estrutura de dados, e qual descartei
- [ ] Outra pessoa usou o sistema sem eu explicar nada
- [ ] Sei apontar pelo menos um defeito que deixei no sistema
- [ ] O relatório de decisões está escrito, incluindo a pergunta 4

> Este módulo não tem seção de *Exemplos guiados* nem lista de *Exercícios*, e é a única exceção
> da trilha. O motivo é simples: o projeto **é** o exercício, e os exemplos são os sistemas que
> você leu no [módulo 13](../modulo-13-estudo-de-caso-crud/). A partir daqui, o material sai da
> frente.

## Erros comuns

| Erro | O que está acontecendo |
| --- | --- |
| Começar pelo código, sem desenhar os dados | a estrutura errada custa horas para trocar |
| Escrever tudo antes de rodar qualquer coisa | quando o primeiro erro aparecer, ele pode estar em qualquer lugar |
| Deixar as validações para o fim | você vai ter que revisitar todas as funções |
| Listas paralelas em vez de registros | está nos requisitos, e o módulo 13 mostrou por quê |
| Uma função gigante para o menu inteiro | cada opção chama uma função; o menu só encaminha |
| Não testar com dados vazios | metade dos travamentos aparece na primeira execução limpa |
| Escolher a proposta "mais fácil" | todas têm o mesmo peso; escolha a que te interessa |
| Achar que terminou quando compila | terminou quando outra pessoa usa sem ajuda |

---

## Depois deste módulo

Você terminou a trilha. O que vem a seguir, se quiser continuar:

- **[Banco de exercícios](../banco-de-exercicios/)**: prática extra por nível
- **[Projetos](../projetos/)**: jogos e calculadoras, para se divertir com o que aprendeu
- **[Apêndice: padrões de projeto](../apendice-padroes-de-projeto/)**: fora do escopo de lógica
  básica, e agora ao seu alcance

---

Anterior: [Módulo 13 — Estudo de caso CRUD](../modulo-13-estudo-de-caso-crud/) | [Voltar ao início](../README.md)
