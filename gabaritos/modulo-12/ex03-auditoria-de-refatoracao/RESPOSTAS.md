# Gabarito — Módulo 12, Exercício 03: Auditoria de refatoração

Enunciado: [EXERCICIO-03-auditoria-de-refatoracao.md](../../../modulo-12-leitura-e-refatoracao/exercicios/EXERCICIO-03-auditoria-de-refatoracao.md)

> Este exercício é sobre julgamento. Ler a minha resposta antes de formar a sua troca o aprendizado
> por uma opinião emprestada.

---

## Parte 1 — A auditoria dos cinco pares

Resultado medido, rodando `diff` em cada par:

| Par | `diff` vazio? | O que mudou | Refatoração legítima? |
| --- | --- | --- | --- |
| 01 cálculo de preços | **Sim** | nada | Sim, sem ressalva |
| 02 processamento de clientes | Não | o bloco de teste ganhou casos novos e mensagens diferentes | Sim, com ressalva |
| 03 cálculo de seguro | **Sim** | nada | Sim, sem ressalva |
| 04 status de pets | Não | o rótulo do `print` final mudou de "Média calculada" para "Status médio calculado" | Sim, com ressalva |
| 05 notas de estudantes | Não | o `print` passou a usar `:.2f`, exibindo `50.00` em vez de `50.0` | Sim, com ressalva |

### Cálculo ou apresentação?

Nos três casos que divergem, a mudança é de **apresentação**. A prova é chamar as funções
diretamente:

```python
# 05 — mesma entrada nas duas versões
antes.calcular_nota_estudante(estudantes, config, politicas, bonus)   # 50.0
depois.calcular_nota_estudante(estudantes, config, politicas, bonus)  # 50.0
```

Idênticos. O `50.00` da tela é o `:.2f` do `print`, não um cálculo diferente.

O mesmo vale para o 04: o valor é `30.05` nas duas versões; mudou a palavra do rótulo.

O 02 é o caso mais discutível: a versão nova não só mudou mensagens, como **acrescentou casos de
teste**. Isso não é refatoração: é escrever testes, que é outra tarefa boa, feita no mesmo commit.

**Veredito geral:** as cinco funções foram refatoradas de verdade. Três autores aproveitaram a
passagem para mexer também no bloco de demonstração, o que é compreensível e mesmo assim
indisciplinado, porque destrói a possibilidade de provar a equivalência com `diff`.

---

## Parte 2 — O que conta como "comportamento"

**a) A função devolve `50.0` antes e depois, mas o print mudou de `50.0` para `50.00`.**

Depende de quem é o usuário, e essa é a resposta, não uma evasiva.

Se o usuário é **outro programa**, que chama a função e usa o valor devolvido, nada mudou: ele
recebe `50.0` nos dois casos.

Se o usuário é uma **pessoa lendo a tela**, o comportamento mudou. E pode importar: se alguém copia
esse número para uma planilha, ou se um script lê essa saída, `50.00` e `50.0` são textos
diferentes.

Na prática: para a função, foi refatoração. Para o programa como um todo, não.

**b) Mesmos valores, 40% mais lenta.**

Mudou o comportamento? Formalmente não: a resposta é a mesma para toda entrada.

Na prática, depende da escala. Numa função chamada uma vez com cinco itens, 40% de nada é nada.
Numa chamada num laço sobre um milhão de registros, é a diferença entre um relatório que sai e um
que não sai.

Desempenho é um requisito como qualquer outro: só é problema quando alguém percebe. Mas piorar
40% "sem querer" durante uma refatoração é sinal de que você mudou mais do que pretendia: vale
investigar o que aconteceu.

**c) Mesmos valores nos casos testados, mas divergem em lista vazia, que ninguém testou.**

**Não foi refatoração**: foi uma mudança de comportamento que passou despercebida.

O fato de ninguém ter testado não muda o que o código faz; muda só o que se sabe sobre ele. O bug
já está lá, esperando o primeiro usuário com lista vazia.

Isto é o argumento mais forte a favor de testar casos-limite antes de refatorar: sem eles, a
"prova" de equivalência prova apenas que os casos que você lembrou continuam funcionando.

---

## Parte 3 — Refatorando uma refatoração

O par que eu escolheria é o **02 (processamento de clientes)**, e não por ele estar mal escrito: por
ele ser o único cuja mudança de saída **não dá para justificar como apresentação**.

A melhoria que eu faria não é no código da função, é na disciplina: separar o que virou dois
trabalhos em um. A versão `_depois2.py` seria idêntica ao `_depois.py` na função, com o bloco de
demonstração **restaurado ao original**. Aí sim, os casos de teste novos entrariam num segundo
arquivo ou num segundo commit.

Se a sua resposta foi "a versão oficial já está boa e não há o que melhorar", ela é aceitável, mas
precisa enfrentar a pergunta: como você provaria isso, se o `diff` não fecha?

---

## Parte 4 — Existe código que não vale refatorar?

Existe, e o critério não é a qualidade do código: é **quanto ele ainda vai mudar**.

Exemplo concreto deste próprio repositório: o `01_calculo_precos_antes.py`. Ele é péssimo: nomes
de uma letra, cinco níveis de indentação, uma recursão ilegível. E não vale a pena refatorá-lo,
porque a única função dele hoje é **ser péssimo**: é material didático, existe para ser lido como
exemplo negativo. Refatorá-lo destruiria o motivo de ele existir.

O critério geral que eu uso, em três perguntas:

1. **Alguém vai mexer nisso de novo?** Se não, o atrito custa zero.
2. **Eu consigo provar que não quebrei?** Se não há como comparar a saída, o risco supera o ganho.
3. **Eu entendo o que ele faz?** Se não, o primeiro trabalho é entender, e às vezes esse trabalho
   já resolve a necessidade, sem tocar numa linha.

Refatoração é investimento, e investimento se avalia pelo retorno. Código estável, que ninguém lê e
ninguém muda, tem retorno zero por definição (por pior que seja).
