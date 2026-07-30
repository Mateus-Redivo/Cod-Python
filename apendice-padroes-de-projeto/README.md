# Apêndice — Padrões de projeto

> **Isto está fora da trilha.** Não é lógica de programação para iniciantes, e estudar daqui antes
> de terminar o módulo 14 vai confundir mais que ajudar.
>
> Se você chegou aqui por curiosidade, tudo bem — mas volte para a
> [trilha principal](../README.md) e siga a ordem.

## Para quem terminou o módulo 14

Padrões de projeto são soluções conhecidas para problemas que aparecem repetidamente na organização
de código. Eles não são recursos da linguagem: são **formas de arranjar** o que você já sabe.

Os arquivos aqui usam **classes e objetos**, que a trilha não cobre. Você vai reconhecer as funções
e a lógica, e vai estranhar a sintaxe — isso é esperado.

| Arquivo | Padrão | Resolve |
| --- | --- | --- |
| [Padrao.py](Padrao.py) | visão geral | o que são e quando servem |
| [Factory.py](Factory.py) | Factory | criar objetos sem espalhar a decisão de qual criar |
| [Builder.py](Builder.py) | Builder | montar um objeto complexo por partes |
| [Strategy.py](Strategy.py) | Strategy | trocar um algoritmo sem mexer em quem o usa |

## Antes de estudar isto

O pré-requisito real não está nos módulos: é **orientação a objetos**, que é um assunto inteiro por
si só. Sem ela, os arquivos aqui parecem sintaxe arbitrária.

O caminho honesto é: termine a trilha, estude orientação a objetos em algum material dedicado, e
**então** volte. Padrões fazem sentido quando você já sentiu a dor que eles resolvem.

## Uma ressalva

Padrões de projeto são úteis e são também a fonte de muito código complicado sem necessidade.
A pergunta a fazer diante de cada um é a mesma do módulo 12: *este problema existe no meu código
hoje?* Se não existe, aplicar o padrão só acrescenta cerimônia.

---

Voltar para a [trilha principal](../README.md).
