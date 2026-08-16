# Exercício 02 — Validador de cadastro

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 2 de 3 | 40 min | `strip`, `lower`, `in`, `find`, `split`, `startswith`, validação |

## Objetivo

Limpar e conferir dados digitados por uma pessoa real, que erra o tamanho da caixa, deixa espaços
sobrando e digita de qualquer jeito.

## Requisitos

1. Crie um arquivo `validador_de_cadastro.py`.
2. Peça: **nome completo**, **e-mail** e **telefone**.
3. Limpe cada campo com `.strip()` antes de qualquer verificação.
4. Valide o **nome**:
   - não pode estar vazio
   - deve ter pelo menos duas palavras (nome e sobrenome)
   - exiba-o formatado com `.title()`
5. Valide o **e-mail**:
   - deve conter exatamente um `@`
   - deve ter algo antes e algo depois do `@`
   - a parte depois do `@` deve conter um `.`
   - exiba-o em minúsculas
6. Valide o **telefone**:
   - remova espaços, parênteses e hifens com `.replace()`
   - o que sobrar deve ter 10 ou 11 dígitos
   - use `.isdigit()` para conferir que sobraram apenas números
7. Ao final, exiba um resumo dizendo o que passou e o que falhou.

**Restrição:** não use `try/except` (módulo 10) nem funções (módulo 08).

## Exemplo de saída

```text
Nome completo:   maria  DA silva
E-mail:  MARIA@Email.COM
Telefone: (45) 99999-1234

===== VALIDAÇÃO =====
Nome:     Maria Da Silva            [OK]
E-mail:   maria@email.com           [OK]
Telefone: 45999991234               [OK]

Cadastro válido.
```

E com dados ruins:

```text
Nome completo: maria
E-mail: maria.email.com
Telefone: 123

===== VALIDAÇÃO =====
Nome:     Maria                     [ERRO] informe nome e sobrenome
E-mail:   maria.email.com           [ERRO] falta o @
Telefone: 123                       [ERRO] precisa ter 10 ou 11 dígitos

Cadastro inválido.
```

## Dicas

```python
email.count("@")            # quantos @ existem
email.find("@")             # onde está o @
partes = email.split("@")   # ['maria', 'email.com']
telefone.replace(" ", "")   # encadeie um replace para cada caractere
"45999991234".isdigit()     # True se só tiver dígitos
```

Para o resumo final, guarde o resultado de cada validação em uma variável `bool` e junte tudo com
`and`: é o módulo 02 voltando.

## Critérios de aceitação

- [ ] Espaços sobrando nas pontas nunca causam erro de validação
- [ ] `MARIA@Email.COM` é aceito e exibido como `maria@email.com`
- [ ] Um e-mail com dois `@` é recusado
- [ ] Um e-mail sem `.` depois do `@` é recusado
- [ ] `(45) 99999-1234` é aceito e vira `45999991234`
- [ ] Cada erro tem sua própria mensagem, dizendo o que corrigir
- [ ] O resumo final só diz "válido" se **todos** os campos passaram

## Sobre validar e-mail de verdade

O que você vai escrever aqui é uma verificação simplificada, e é assim de propósito. Validar e-mail
corretamente é notoriamente difícil: `a@b` é tecnicamente válido, e endereços reais podem ter
caracteres que surpreendem. Em programa de verdade, o teste que vale é mandar uma mensagem de
confirmação. O objetivo aqui é treinar `find`, `split` e `count`, não escrever um validador para
produção.

## Desafio opcional

Você validou, mas não consegue **pedir de novo**. Escreva em um comentário como esse programa
mudaria se você pudesse repetir a pergunta até o dado ficar bom, e diga qual estrutura do módulo
05 faria isso.

---

Gabarito: [gabaritos/modulo-07-ex02-validador-de-cadastro/](../../gabaritos/modulo-07-ex02-validador-de-cadastro/), depois de tentar, não antes.
