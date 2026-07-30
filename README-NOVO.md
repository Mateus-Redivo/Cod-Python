# Lógica de Programação com Python

> **Este arquivo é uma proposta.** Se aprovado, ele substitui o `README.md` da raiz e este
> `README-NOVO.md` é apagado. Nada foi trocado ainda.

---

Uma trilha de estudo do zero até um sistema completo, feita para ser percorrida **em ordem**. Cada
módulo é uma aula: a explicação mora no `README.md`, os exemplos rodáveis em `exemplos/` e os
enunciados em `exercicios/`. As respostas ficam em [gabaritos/](gabaritos/) — longe dos enunciados,
de propósito.

**Nunca programou antes?** Comece pelo [Guia do aluno](GUIA-DO-ALUNO.md): instalar o Python, rodar
o primeiro arquivo e como estudar cada módulo.

---

## A trilha

```mermaid
flowchart LR
    M00["00 · Preparação"] --> M01

    subgraph F ["Fundamentos"]
        direction LR
        M01["01 · Tipos e variáveis"] --> M02["02 · Operadores"] --> M03["03 · Entrada e saída"] --> M04["04 · Condicionais"] --> M05["05 · Laços"]
    end

    subgraph D ["Dados e organização"]
        direction LR
        M06["06 · Listas"] --> M07["07 · Strings"] --> M08["08 · Funções"] --> M09["09 · Matrizes"]
    end

    subgraph R ["Robustez e algoritmos"]
        direction LR
        M10["10 · Tratamento de erros"] --> M11["11 · Ordenação"] --> M12["12 · Leitura e refatoração"]
    end

    subgraph C ["Fechamento"]
        direction LR
        M13["13 · Estudo de caso CRUD"] --> M14["14 · Projeto integrador"]
    end

    M05 --> M06
    M09 --> M10
    M12 --> M13
```

---

## Módulos

| # | Módulo | O que você sai sabendo |
| --- | --- | --- |
| 00 | Preparação | instalar Python, usar o VS Code, rodar o primeiro `.py` |
| 01 | Tipos e variáveis | guardar valores e saber com que tipo de dado você está lidando |
| 02 | Operadores | calcular, comparar e combinar condições |
| 03 | Entrada e saída | conversar com o usuário: `input`, `print`, f-strings e conversões |
| 04 | Condicionais | fazer o programa decidir, com `if/elif/else` e `match/case` |
| 05 | **[Laços de repetição](modulo-05-lacos-de-repeticao/)** | repetir sem copiar e colar: `while`, `for`, `range`, acumuladores |
| 06 | Listas | guardar muitos valores em uma variável só |
| 07 | Strings | tratar texto: buscar, fatiar, comparar e transformar |
| 08 | Funções | escrever uma vez e reaproveitar; parâmetros, retorno e escopo |
| 09 | Matrizes | listas de listas para representar tabelas e grades |
| 10 | Tratamento de erros | impedir que uma digitação errada derrube o programa |
| 11 | Algoritmos de ordenação | Bubble, Selection, Insertion e Quick Sort por dentro |
| 12 | Leitura e refatoração | ler código dos outros e melhorar o seu sem quebrá-lo |
| 13 | Estudo de caso CRUD | um sistema completo, comentado linha a linha |
| 14 | Projeto integrador | seu próprio sistema, do enunciado à entrega |

> **Migração em andamento.** Só o módulo 05 está no formato novo — ele é o piloto. Os demais
> continuam nas pastas antigas listadas abaixo e seguem plenamente utilizáveis. A ordem de
> conversão está em [PLANO-REESTRUTURACAO.md](PLANO-REESTRUTURACAO.md).

### Onde está cada conteúdo hoje

| Pasta atual | Vira |
| --- | --- |
| [01_Fundamentos_Python/](01_Fundamentos_Python/) | módulos 01 a 07 e 10 |
| [02_Estruturas_De_Controle/](02_Estruturas_De_Controle/) | módulos 04 e 05 |
| [03_Estruturas_De_Dados/](03_Estruturas_De_Dados/) | módulos 06, 07, 09 e 11 |
| [04_Funcoes/](04_Funcoes/) | módulo 08 |
| [05_Exercicios_Praticos/](05_Exercicios_Praticos/) | `banco-de-exercicios/` |
| [06_Projetos_Praticos/](06_Projetos_Praticos/) | `projetos/` e módulos 13 e 14 |
| [07_Revisao_E_Listas/](07_Revisao_E_Listas/) | módulos 08 e 12 |
| [08_Avancado/](08_Avancado/) | `apendice-padroes-de-projeto/` |

---

## Além da trilha

| Pasta | Para que serve |
| --- | --- |
| [gabaritos/](gabaritos/) | resoluções comentadas de todos os exercícios |
| `banco-de-exercicios/` | prática extra por nível, quando um módulo não bastou |
| `projetos/` | jogos e calculadoras — desafios opcionais, e os mais divertidos |
| [material-apoio/](material-apoio/) | [resumo de sintaxe](material-apoio/resumo-sintaxe.md), [guia de comentários](material-apoio/guia-de-comentarios.md) e [rubrica de avaliação](material-apoio/rubrica-avaliacao.md) |
| `apendice-padroes-de-projeto/` | fora do escopo de lógica básica; só depois do módulo 14 |

Documentos de referência: [Guia do aluno](GUIA-DO-ALUNO.md) · [Glossário](GLOSSARIO.md)

---

## Como estudar

1. **Leia o README do módulo inteiro** antes de abrir qualquer `.py`. A aula está lá.
2. **Rode os exemplos na ordem numerada** e faça o *Experimento* que fecha cada arquivo — mexer no
   código ensina o que ler não ensina.
3. **Faça os exercícios sem gabarito.** Vinte minutos travado valem mais que a resposta pronta.
4. **Marque a auto-avaliação** no fim do README. Caixinha em branco é sinal de voltar, não de seguir.

Um módulo por sessão de estudo. Dois no mesmo dia rende menos do que parece — o segundo depende do
primeiro estar assentado.

## Requisitos

Python **3.14 ou superior**. O mínimo absoluto para o material rodar é a 3.10, por causa do
`match/case` do módulo 04 — mas instale a versão mais recente, que é a usada em aula.

Nenhuma biblioteca externa é necessária na trilha principal; a única exceção é o NumPy, opcional,
na seção "Para ir além" do módulo 09.

Como avaliar e ser avaliado: [rubrica de avaliação](material-apoio/rubrica-avaliacao.md).

---

## Sobre

Material de aula de lógica de programação, mantido por
[Mateus Redivo](https://github.com/Mateus-Redivo). Use, adapte e leve para a sua turma.
