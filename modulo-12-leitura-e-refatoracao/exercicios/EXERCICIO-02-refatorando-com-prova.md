# Exercício 02 — Refatorando com prova

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 2 de 3 | 50 min | refatoração, extração de função, prova por `diff` |

## Objetivo

Refatorar um programa ruim e **provar** que o comportamento não mudou. A prova é parte do
exercício, não um extra.

## O código de partida

Copie para `relatorio_antes.py` e **rode primeiro**, guardando a saída:

```python
v = [["arroz",5,4.5],["feijao",3,8.9],["oleo",12,7.2],["sal",1,2.3],["cafe",8,18.5]]
t=0
c=0
m=0
n=""
for i in range(len(v)):
    s=v[i][1]*v[i][2]
    t=t+s
    if v[i][1]<5:
        c=c+1
    if s>m:
        m=s
        n=v[i][0]
print("=== RELATORIO ===")
for i in range(len(v)):
    s=v[i][1]*v[i][2]
    if v[i][1]<5:
        st="BAIXO"
    else:
        st="OK"
    print(v[i][0]+" "+str(v[i][1])+" "+str(v[i][2])+" "+str(s)+" "+st)
print("Total: "+str(t))
print("Itens baixos: "+str(c))
print("Maior: "+n+" "+str(m))
```

## Requisitos

1. Rode o original e salve a saída:
   ```bash
   python relatorio_antes.py > antiga.txt
   ```
2. Crie `relatorio_depois.py` com a versão refatorada, aplicando:
   - nomes que digam o que guardam
   - funções para os cálculos (`calcular_subtotal`, `classificar_estoque`, `encontrar_maior`…)
   - constantes no lugar dos números soltos
   - f-strings no lugar da concatenação com `+` e `str()`
   - eliminação do cálculo repetido de `s` (ele é feito duas vezes hoje)
3. Prove a equivalência:
   ```bash
   python relatorio_depois.py > nova.txt
   diff antiga.txt nova.txt
   ```
   O `diff` tem que sair **vazio**. No Windows sem `diff`, use `fc antiga.txt nova.txt`.

## A regra que não pode ser quebrada

A saída tem que ficar **byte a byte idêntica**, inclusive os espaços entre as colunas, que hoje
saem tortos por causa da concatenação.

Vai dar vontade de alinhar a tabela. **Não alinhe.** Alinhar é melhorar a saída, e melhorar a saída
é mudar o comportamento. Isso é um segundo passo, depois de a refatoração estar provada.

Essa frustração é o exercício. Refatoração disciplinada é assim: uma coisa de cada vez.

## Parte escrita

Responda em comentários no `relatorio_depois.py`:

**a)** O código original calcula `s` duas vezes para cada produto. Por que isso é um problema, além
de "gasta processamento"?

**b)** A variável `n` guarda o nome do produto de maior subtotal, e `m` guarda o valor. Elas são
atualizadas juntas, sempre. O que isso sugere sobre elas?

**c)** Você conseguiu deixar a saída idêntica? Se algo mudou, o que foi e por quê?

## Critérios de aceitação

- [ ] O `diff` entre as duas saídas é **vazio**
- [ ] Nenhuma variável de uma letra sobrou (exceto contador de laço)
- [ ] Existem pelo menos três funções, todas com `return`
- [ ] O subtotal é calculado uma vez por produto, não duas
- [ ] Nenhuma concatenação com `+` e `str()`: tudo f-string
- [ ] O `5` do "estoque baixo" está numa constante nomeada
- [ ] As três perguntas estão respondidas

## Segundo passo (depois da prova)

Agora que a refatoração está provada, **aí sim** melhore a saída: alinhe as colunas, formate os
valores com duas casas, acrescente cabeçalho. Salve como `relatorio_final.py` e mantenha os três
arquivos.

Repare no que você acabou de fazer: dois commits mentais separados. Primeiro estrutura, com
comportamento congelado. Depois comportamento, com estrutura já limpa.

---

Gabarito: [gabaritos/modulo-12/ex02-refatorando-com-prova/](../../gabaritos/modulo-12/ex02-refatorando-com-prova/), depois de tentar, não antes.
