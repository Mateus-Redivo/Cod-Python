# Módulo 12 — Leitura e refatoração

Você passou onze módulos aprendendo a **escrever** código. Na vida profissional, você vai gastar
muito mais tempo **lendo**: código dos outros, e código seu de seis meses atrás, que dá no mesmo.

Este módulo é sobre as duas habilidades que decorrem disso: entender um código que você não
escreveu, e melhorá-lo **sem quebrá-lo**.

## Objetivos de aprendizagem

Ao final deste módulo você será capaz de:

- [ ] Ler um código ruim e descrever o que ele faz, sem executá-lo
- [ ] Nomear os sinais de código que pede refatoração
- [ ] Refatorar preservando comportamento, e provar que preservou
- [ ] Explicar por que refatorar e corrigir bugs não devem andar juntos
- [ ] Escrever comentários que envelhecem bem
- [ ] Decidir quando **não** vale a pena refatorar

## Pré-requisitos

[Módulo 11 — Ordenação](../modulo-11-algoritmos-de-ordenacao/) concluído. Na prática, este módulo
usa tudo: você não consegue melhorar um código sem entender listas, laços, condicionais e funções.

## Conceito

### O que é refatorar

> **Refatorar é mudar a estrutura do código sem mudar o que ele faz.**

As duas metades importam igualmente. Se o código não melhorou, você perdeu tempo. Se o
comportamento mudou, você não refatorou: introduziu uma alteração, possivelmente um bug.

Isso leva à regra mais importante do módulo:

> **Nunca refatore e conserte na mesma passada.**

Se você mexe na estrutura e no comportamento ao mesmo tempo e algo quebra, não há como saber qual
das duas mudanças causou. Refatore primeiro, com a saída idêntica; conserte depois, num passo
separado.

### Como se prova que o comportamento não mudou

Não se prova por leitura. Prova-se comparando saídas:

```bash
python versao_antiga.py > antiga.txt
python versao_nova.py > nova.txt
diff antiga.txt nova.txt
```

`diff` sem saída significa arquivos idênticos. No Windows sem `diff`, use `fc antiga.txt nova.txt`.

Você já fez isso no módulo 08, no exercício do monólito. Aqui vira método.

### Os sinais de que um código pede refatoração

| Sinal | O que indica |
| --- | --- |
| Nomes de uma letra (`d`, `p`, `tx`) | ninguém sabe o que a variável guarda sem rastrear o código |
| Função gigante | ela faz coisas demais; cada bloco quer virar uma função |
| Código repetido | mudar a regra exige achar todas as cópias |
| Indentação profunda | três níveis de `if` dentro de `for` dentro de `if` |
| Números soltos (`0.1`, `100`, `46`) | ninguém sabe de onde vieram |
| Comentário explicando *o que* a linha faz | se precisa explicar, o nome está ruim |
| Precisa de comentário para separar blocos | cada bloco quer ser uma função |

Nenhum é erro. Todos são **atrito**: o código funciona, mas custa caro para entender e mudar.

### O que a refatoração não é

- **Não é reescrever do zero.** Reescrever joga fora todas as correções silenciosas que o código
  acumulou, inclusive as que ninguém lembra por que existem.
- **Não é deixar mais curto.** Menos linhas nem sempre é mais claro.
- **Não é adicionar recursos.** Isso é outra tarefa, em outro commit.

### O caso dos cinco pares

A pasta `exemplos/` tem cinco programas em duas versões: `_antes.py` e `_depois.py`. Eles vieram do
material antigo deste repositório e são reais, não foram fabricados para a aula.

Rodando o `diff` nos cinco pares, o resultado surpreende:

| Par | Saída idêntica? |
| --- | --- |
| 01 cálculo de preços | Sim |
| 02 processamento de clientes | **Não** |
| 03 cálculo de seguro | Sim |
| 04 status de pets | **Não** |
| 05 notas de estudantes | **Não** |

Três dos cinco mudaram a saída. **Isso significa que não foram refatorações?**

Não necessariamente, e é aí que o módulo fica interessante. Olhando de perto:

- No **05**, a função devolve exatamente `50.0` nas duas versões. O que mudou foi o `print` final,
  que passou a usar `:.2f` e exibe `50.00`. O **cálculo** é idêntico; a **apresentação** mudou.
- No **04**, o valor também é o mesmo (`30.05`). Mudou o texto do rótulo.
- No **02**, a versão nova acrescentou casos de teste que não existiam antes.

Ou seja: as **funções** foram refatoradas de verdade. O que mudou foi o bloco de demonstração no fim
do arquivo, que não é o programa, é o teste dele.

Isso levanta a pergunta que você vai levar para o resto da carreira: **o que exatamente conta como
"comportamento"?** A resposta prática é: o que o usuário do seu código observa. Se ele chama uma
função, o comportamento é o valor devolvido. Se ele roda um programa, é a saída na tela.

### Comentários que envelhecem bem

```python
# Ruim: explica o QUE, e vira mentira quando alguém mexe na linha
total = preco * 1.1        # multiplica o preço por 1.1

# Bom: explica o PORQUÊ, e continua verdadeiro
total = preco * 1.1        # 10% de taxa de serviço, definida em contrato
```

O melhor comentário costuma ser um nome:

```python
TAXA_DE_SERVICO = 1.1
total = preco * TAXA_DE_SERVICO
```

Agora não é preciso comentário nenhum. **Nome bom é comentário que não apodrece.**

Para os marcadores padronizados (`TODO`, `FIXME`, `NOTE`…), veja o
[guia de comentários](../material-apoio/guia-de-comentarios.md).

### Quando não refatorar

- **Código que você não entende ainda.** Entenda primeiro; mexer no escuro é como andar de olhos
  fechados.
- **Código sem forma de testar.** Sem comparar a saída, você não tem como saber se quebrou.
- **Código que ninguém mais toca.** Se funciona e nunca muda, o atrito não custa nada.
- **Na véspera da entrega.** Refatoração é investimento; investimento tem hora.

## Exemplos guiados

Cinco pares reais, cada um com o código original e a versão melhorada:

| Par | O que o "antes" tem de ruim |
| --- | --- |
| [01_calculo_precos](exemplos/01_calculo_precos_antes.py) / [depois](exemplos/01_calculo_precos_depois.py) | nomes de uma letra, função recursiva ilegível |
| [02_processamento_clientes](exemplos/02_processamento_clientes_antes.py) / [depois](exemplos/02_processamento_clientes_depois.py) | condicionais aninhadas fundas |
| [03_calculo_seguro](exemplos/03_calculo_seguro_antes.py) / [depois](exemplos/03_calculo_seguro_depois.py) | números mágicos por toda parte |
| [04_status_pets](exemplos/04_status_pets_antes.py) / [depois](exemplos/04_status_pets_depois.py) | uma função fazendo cinco coisas |
| [05_notas_estudantes](exemplos/05_notas_estudantes_antes.py) / [depois](exemplos/05_notas_estudantes_depois.py) | parâmetros crípticos (`e`, `c`, `p`, `b`, `d`) |

Para comparar um par:

```bash
cd modulo-12-leitura-e-refatoracao/exemplos
python 05_notas_estudantes_antes.py
python 05_notas_estudantes_depois.py
```

Leia o `_antes` **primeiro**, e tente descrever o que ele faz antes de abrir o `_depois`. É
desconfortável de propósito: é assim que se chega num código na vida real.

## Exercícios

1. [EXERCICIO-01-lendo-codigo-alheio.md](exercicios/EXERCICIO-01-lendo-codigo-alheio.md) (nível 1): descrever o que um código faz sem rodá-lo.
2. [EXERCICIO-02-refatorando-com-prova.md](exercicios/EXERCICIO-02-refatorando-com-prova.md) (nível 2): refatorar e provar que a saída não mudou.
3. [EXERCICIO-03-auditoria-de-refatoracao.md](exercicios/EXERCICIO-03-auditoria-de-refatoracao.md) (nível 3): julgar refatorações alheias, incluindo as deste módulo.

## Auto-avaliação

- [ ] Sei definir refatoração citando as duas metades da definição
- [ ] Sei provar que uma refatoração preservou o comportamento
- [ ] Sei por que refatorar e corrigir não devem andar juntos
- [ ] Reconheço pelo menos cinco sinais de código que pede refatoração
- [ ] Escrevo comentários que explicam o porquê
- [ ] Sei dar um exemplo de código que **não** vale a pena refatorar

## Erros comuns

| Erro | O que está acontecendo |
| --- | --- |
| Refatorar e corrigir junto | se quebrar, não há como saber qual mudança causou |
| "Melhorei" sem comparar a saída | sem prova, é só esperança |
| Reescrever do zero | joga fora as correções que ninguém lembra por que existem |
| Encurtar em vez de esclarecer | uma linha densa pode ser pior que cinco claras |
| Renomear tudo de uma vez | mudanças grandes escondem o erro; vá em passos pequenos |
| Comentar o óbvio | `# soma 1 ao contador` não ajuda ninguém |
| Refatorar código que você não entendeu | entenda primeiro, sempre |
| Achar que menos funções é mais simples | uma função de 200 linhas não é "simples", é indivisível |

---

Anterior: [Módulo 11 — Algoritmos de ordenação](../modulo-11-algoritmos-de-ordenacao/) | Próximo: [Módulo 13 — Estudo de caso CRUD](../modulo-13-estudo-de-caso-crud/)
