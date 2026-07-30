# Exercício 02 — Decifrando erros

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 2 de 3 | 30 min | leitura de mensagem de erro, depuração |

## Objetivo

Ler cinco mensagens de erro e consertar os programas que as produziram. É a habilidade mais útil da
primeira semana — e a que ninguém ensina de propósito.

> **Este é o último exercício do módulo.** Ele não tem nível 3: o módulo 00 só ensina `print`,
> comentários e leitura de erro, e um terceiro exercício aqui seria enchimento. Os níveis 3 começam
> no módulo 01.

## Como fazer

Para cada programa abaixo:

1. **Antes de rodar**, leia o código e escreva o que você acha que vai acontecer.
2. Copie para um arquivo e rode.
3. Anote: **qual linha** o Python apontou e **qual o tipo** do erro (a última linha da mensagem).
4. Conserte e rode de novo.

Entregue um arquivo `decifrando_erros.md` (ou o formato que o professor pedir) com as cinco
respostas, e os cinco programas corrigidos.

---

## Programa A

```python
print("Bem-vindo ao sistema)
print("Digite seus dados")
```

## Programa B

```python
nome = "Maria"
print("Olá, " + nome)
print("Você tem " + 25 + " anos")
```

## Programa C

```python
print("Calculando...")
print(totall)
```

## Programa D

```python
print("Linha 1")
   print("Linha 2")
print("Linha 3")
```

## Programa E

```python
primt("Olá!")
```

---

## Para cada um, responda

| Pergunta | O que você deve anotar |
| --- | --- |
| Que linha o Python apontou? | o número que aparece depois de `line` |
| Qual o tipo do erro? | a primeira palavra da última linha da mensagem |
| O que a mensagem quer dizer? | com suas palavras, não copiando |
| Como consertar? | a linha corrigida |

## A pergunta que amarra o exercício

Dois desses cinco erros têm uma característica que os outros três não têm: **nenhuma linha do
programa chega a rodar**, nem as que estão antes do erro.

**Quais são os dois? E por que isso acontece?**

Descubra observando: em quais programas a mensagem `"Calculando..."` ou `"Linha 1"` apareceu na tela
antes do erro, e em quais não apareceu.

## Critérios de aceitação

- [ ] As cinco previsões foram escritas **antes** de rodar
- [ ] Os cinco tipos de erro estão identificados corretamente
- [ ] As explicações estão com suas palavras, não copiadas da mensagem
- [ ] Os cinco programas corrigidos rodam sem erro
- [ ] A pergunta dos "dois erros diferentes" está respondida com a observação que a comprova

## Dica sobre o Programa E

O Python 3.14 é gentil neste caso: além de dizer o que está errado, ele **sugere** o que você
provavelmente quis escrever. Leia a mensagem inteira, até o fim — muita gente para na primeira
linha e perde a ajuda.

---

Gabarito: [gabaritos/modulo-00-ex02-decifrando-erros/](../../gabaritos/modulo-00-ex02-decifrando-erros/) —
depois de tentar, não antes.
