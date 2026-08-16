# Rubrica de avaliação

Como os exercícios e projetos deste repositório são corrigidos. Está aqui, aberto, **antes** de você
entregar: nota não deve ser surpresa.

A rubrica vale para qualquer entrega: exercício de módulo, sistema do banco de exercícios ou o
projeto integrador. O que muda é o peso, não os critérios.

---

## Os cinco critérios

### 1. Funciona (peso 40)

O programa faz o que o enunciado pediu, para qualquer entrada válida, não só para o exemplo.

| Nível | O que significa |
| --- | --- |
| **Excelente (36–40)** | Atende todos os requisitos. Funciona também nos casos-limite (lista vazia, zero, valor no limite do intervalo). |
| **Bom (28–35)** | Atende todos os requisitos do enunciado. Falha em algum caso-limite. |
| **Suficiente (20–27)** | Atende a maior parte. Um requisito ficou de fora ou funciona só para o exemplo dado. |
| **Insuficiente (0–19)** | Não roda, ou o resultado está errado no caso principal. |

> Um programa que não executa não é avaliado nos outros critérios. **Rode antes de entregar.**

### 2. Corretude da lógica (peso 20)

A solução resolve o problema pelo raciocínio certo, não por coincidência.

| Nível | O que significa |
| --- | --- |
| **Excelente (18–20)** | Escolhas coerentes: `for` onde o número de repetições é conhecido, `while` onde depende de condição. Sem cálculo redundante. |
| **Bom (14–17)** | Lógica correta, com alguma volta desnecessária. |
| **Suficiente (10–13)** | Chega ao resultado, mas por caminho confuso (valores fixos onde deveria ter variável, por exemplo). |
| **Insuficiente (0–9)** | O resultado certo sai por acaso, ou só para a entrada de exemplo. |

### 3. Legibilidade (peso 20)

Outra pessoa consegue ler o seu código sem você do lado explicando.

| Nível | O que significa |
| --- | --- |
| **Excelente (18–20)** | Nomes em `snake_case` que dizem o que a variável guarda. Indentação consistente. Comentários explicam o *porquê*, nunca o óbvio. |
| **Bom (14–17)** | Nomes claros na maior parte. Um ou outro `x`, `a1`, `aux`. |
| **Suficiente (10–13)** | Nomes genéricos frequentes. Código funciona, mas exige esforço para acompanhar. |
| **Insuficiente (0–9)** | Variáveis de uma letra em todo lugar, código sem espaçamento, impossível de acompanhar. |

### 4. Uso dos conceitos do módulo (peso 10)

O exercício existe para exercitar alguma coisa específica. Se o enunciado pede `for` com `range`,
resolver com dez `print` copiados atende o resultado e falha o objetivo.

| Nível | O que significa |
| --- | --- |
| **Excelente (9–10)** | Usa os recursos que o módulo ensinou, do jeito que o módulo ensinou. |
| **Bom (7–8)** | Usa os recursos, com alguma escolha discutível. |
| **Suficiente (5–6)** | Usa parcialmente, ou contorna o conceito exigido. |
| **Insuficiente (0–4)** | Ignora a restrição do enunciado. |

### 5. Tratamento de entrada (peso 10)

O programa não morre por causa de uma digitação. A partir do módulo 05, validar com `while` já é
esperado; a partir do módulo 10, `try/except` também.

| Nível | O que significa |
| --- | --- |
| **Excelente (9–10)** | Valida faixa e tipo. Mensagem de erro diz ao usuário o que fazer. |
| **Bom (7–8)** | Valida o principal. Mensagem genérica. |
| **Suficiente (5–6)** | Valida só um caso, ou avisa mas segue em frente com o dado ruim. |
| **Insuficiente (0–4)** | Nenhuma validação, e o programa quebra com entrada previsível. |

---

## Como a nota fecha

```text
Nota = Funciona (40) + Lógica (20) + Legibilidade (20) + Conceitos (10) + Entrada (10)
```

| Faixa | Significado |
| --- | --- |
| 90–100 | Entrega exemplar; serve de referência para a turma. |
| 75–89 | Boa entrega. Ajustes pontuais. |
| 60–74 | Aprovado com ressalvas. Vale refazer. |
| < 60 | Refazer. A correção vem com o apontamento do que revisar. |

---

## Zeramentos automáticos

Três situações que anulam a entrega, independentemente da qualidade do código:

- **Código copiado de `gabaritos/`** sem tentativa própria. O gabarito existe para conferir, e a
  correção reconhece a cópia: as decisões arbitrárias do gabarito reaparecem idênticas.
- **Arquivo que não executa** por erro de sintaxe. Isso é conferível em cinco segundos, antes de
  entregar.
- **Entrega em branco** ou fora do formato pedido (`.py` executável, não print de tela, não `.docx`).

---

## Antes de entregar, confira

- [ ] O programa roda do começo ao fim sem erro
- [ ] Testei com pelo menos três entradas diferentes, incluindo uma esquisita
- [ ] Nenhuma variável tem nome de uma letra só (exceto contador de laço)
- [ ] A saída está formatada como o enunciado pediu
- [ ] Marquei todos os *critérios de aceitação* do enunciado
- [ ] Não sobrou código comentado nem `print` de depuração
- [ ] Consigo explicar cada linha se me perguntarem
