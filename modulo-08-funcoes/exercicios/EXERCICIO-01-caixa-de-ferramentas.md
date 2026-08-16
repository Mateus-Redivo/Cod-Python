# Exercício 01 — Caixa de ferramentas

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 1 de 3 | 30 min | `def`, parâmetros, `return` |

## Objetivo

Escrever oito funções pequenas, cada uma fazendo uma coisa só. É o exercício de fixação: nenhuma
delas passa de quatro linhas.

## Requisitos

1. Crie um arquivo `caixa_de_ferramentas.py`.
2. Escreva as funções da tabela abaixo. **Todas devem `return`, nenhuma deve `print`.**
3. Depois de defini-las, chame cada uma pelo menos duas vezes e mostre os resultados.
4. Todo nome de função começa com um verbo.

| Função | Recebe | Devolve |
| --- | --- | --- |
| `dobrar` | um número | o dobro dele |
| `calcular_media` | uma lista de números | a média |
| `e_par` | um número | `True` ou `False` |
| `converter_para_celsius` | temperatura em Fahrenheit | o valor em Celsius |
| `contar_vogais` | um texto | quantas vogais tem |
| `inverter_texto` | um texto | o texto de trás para frente |
| `maior_de_tres` | três números | o maior deles |
| `aplicar_desconto` | preço e percentual (padrão 10) | o preço com desconto |

## Exemplo de saída

```text
dobrar(5)                      -> 10
calcular_media([7, 8, 9])      -> 8.0
e_par(4)                       -> True
e_par(7)                       -> False
converter_para_celsius(212)    -> 100.0
contar_vogais('programacao')   -> 5
inverter_texto('Python')       -> nohtyP
maior_de_tres(3, 9, 5)         -> 9
aplicar_desconto(100)          -> 90.0
aplicar_desconto(100, 25)      -> 75.0
```

## Critérios de aceitação

- [ ] As oito funções existem e todas usam `return`
- [ ] Nenhuma função tem `print` dentro
- [ ] `aplicar_desconto` funciona com um e com dois argumentos
- [ ] `e_par` devolve um `bool`, não a string `"sim"`
- [ ] Cada nome começa com verbo (ou é uma pergunta, como `e_par`)
- [ ] Nenhuma função passa de quatro linhas de corpo

## Armadilha conhecida

Vai dar vontade de escrever assim:

```python
def e_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
```

Funciona. Mas repare que `numero % 2 == 0` **já é** `True` ou `False`: o `if` está comparando um
booleano para devolver o mesmo booleano. A versão direta é:

```python
def e_par(numero):
    return numero % 2 == 0
```

## Desafio opcional

Escreva `calcular_media` de forma que ela não quebre com uma lista vazia. O que ela deveria devolver
nesse caso? Não existe resposta única: escolha uma e justifique em um comentário.

---

Gabarito: [gabaritos/modulo-08-ex01-caixa-de-ferramentas/](../../gabaritos/modulo-08-ex01-caixa-de-ferramentas/), depois de tentar, não antes.
