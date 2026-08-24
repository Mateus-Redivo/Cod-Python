# Exercício 03 — Planejador de viagem (desafio)

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 3 de 3 | 50 min | `input`, escolha de tipos, `//` e `%`, f-strings avançadas |

## Objetivo

Um programa que lê sete dados, faz nove cálculos encadeados e produz um relatório formatado em três
blocos. É o maior programa da trilha até aqui, e o teste real de se você consegue organizar
entrada, processamento e saída sem se perder.

## Requisitos

1. Crie um arquivo `planejador_de_viagem.py`.
2. Leia, nesta ordem: destino, distância em km, consumo do carro em km/l, preço do litro,
   velocidade média em km/h, total de pedágios em reais, e número de pessoas.
3. **Escolha o tipo certo em cada leitura** e justifique as escolhas em um comentário no topo.
4. Calcule:
   - litros necessários
   - custo do combustível
   - custo total (combustível + pedágios)
   - custo por pessoa
   - duração da viagem em horas decimais
   - a mesma duração em **horas e minutos inteiros**
   - custo por quilômetro
   - percentual do custo que é pedágio
   - quantos litros sobram de um tanque de 50 litros
5. Exiba um relatório em três blocos: **Rota**, **Custos** e **Rateio**, com valores alinhados à
   direita e duas casas decimais no dinheiro.
6. Use constantes para o tamanho do tanque e para os minutos por hora.

**Restrição:** sem `if`, sem laços, sem listas. Só o que os módulos 01 a 03 deram.

## Exemplo de saída

```text
=== PLANEJADOR DE VIAGEM ===
Destino: Florianópolis
Distância (km): 480
Consumo do carro (km/l): 12
Preço do litro (R$): 5.89
Velocidade média (km/h): 90
Total de pedágios (R$): 34.50
Número de pessoas: 3

==================================================
            VIAGEM PARA FLORIANÓPOLIS             
==================================================
--- ROTA ---
Distância                               480.0 km
Velocidade média                         90.0 km/h
Duração                               5h20min
Duração (decimal)                        5.33 h

--- CUSTOS ---
Combustível necessário                  40.00 L
Custo do combustível             R$    235.60
Pedágios                         R$     34.50
CUSTO TOTAL                      R$    270.10

Custo por km                     R$      0.56
Pedágio representa                      12.77 % do total

--- RATEIO ---
Pessoas                                     3
Cada um paga                     R$     90.03

--- TANQUE (50 L) ---
Sobram após a viagem                    10.00 L
==================================================
```

## As três partes difíceis

**Horas e minutos.** A duração dá `5.333...` horas, que deve virar `5h20min`. Duas armadilhas aqui:
o resto de uma divisão com `float` também é `float` (e `20.0min` fica feio), e `int()` **trunca em
vez de arredondar**.

Depois de pronto, confira: sua resposta deu `5h20min` ou `5h19min`? Se deu 19, não está "quase
certo": está errado, e vale descobrir por quê antes de olhar o gabarito. Rastreie a conta passo a
passo imprimindo cada resultado intermediário.

**O percentual.** `pedagio / total * 100` dá `12.769...`. A f-string tem um formato próprio para
porcentagem (`:.1%`), mas ele **multiplica por 100 sozinho**: usar os dois é erro comum. Escolha
um.

**O alinhamento.** Os três blocos precisam ficar retos na vertical, com rótulos de tamanhos bem
diferentes. Defina uma largura para o rótulo e outra para o valor, e use as mesmas em todas as
linhas.

## Critérios de aceitação

- [ ] Os sete dados são lidos com o tipo certo, e a escolha está justificada em comentário
- [ ] Todos os cálculos conferem (refaça três deles na calculadora)
- [ ] A duração aparece nos dois formatos, e os minutos são inteiros
- [ ] O rateio bate: `custo por pessoa × pessoas` volta ao custo total (com até 1 centavo de
      diferença por arredondamento)
- [ ] As colunas ficam alinhadas nos três blocos
- [ ] O destino aparece em maiúsculas no título, sem você digitá-lo em maiúsculas
- [ ] Nenhum `if`, laço ou lista no arquivo

## Sobre o centavo que sobra

`270.10 / 3 = 90.0333...`, que arredonda para `90.03`. Mas `90.03 × 3 = 270.09`: falta um centavo.

Isso não é bug: é a mesma questão do gabarito da nota fiscal. Escreva em um comentário quem, na sua
opinião, deveria pagar esse centavo a mais, e por quê. Não há resposta técnica.

---

Gabarito: [gabaritos/modulo-03/ex03-planejador-de-viagem/](../../gabaritos/modulo-03/ex03-planejador-de-viagem/), depois de tentar, não antes.
