"""
Gabarito — Módulo 04, Exercício 03: Validador de data

Enunciado:
  modulo-04-condicionais/exercicios/EXERCICIO-03-validador-de-data.md

Como executar:
  python validador_de_data.py
"""

# --- 1. ENTRADA ------------------------------------------------------
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

print()
print(f"Data: {dia:02d}/{mes:02d}/{ano}")

# --- 2. ANO BISSEXTO --------------------------------------------------
# A regra completa, em uma expressão:
#   divisível por 4  E  (não divisível por 100  OU  divisível por 400)
#
# O parêntese é obrigatório: sem ele, o "and" resolveria antes do "or"
# e a regra ficaria errada para 1900.
e_bissexto = ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

# --- 3. NOME E DIAS DO MÊS -------------------------------------------
# match/case porque é comparação com valores exatos, e o "|" agrupa
# os meses que compartilham o mesmo número de dias.
match mes:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        dias_no_mes = 31
    case 4 | 6 | 9 | 11:
        dias_no_mes = 30
    case 2:
        dias_no_mes = 29 if e_bissexto else 28
    case _:
        dias_no_mes = 0         # mês inválido: não há dias

match mes:
    case 1:
        nome_do_mes = "Janeiro"
    case 2:
        nome_do_mes = "Fevereiro"
    case 3:
        nome_do_mes = "Março"
    case 4:
        nome_do_mes = "Abril"
    case 5:
        nome_do_mes = "Maio"
    case 6:
        nome_do_mes = "Junho"
    case 7:
        nome_do_mes = "Julho"
    case 8:
        nome_do_mes = "Agosto"
    case 9:
        nome_do_mes = "Setembro"
    case 10:
        nome_do_mes = "Outubro"
    case 11:
        nome_do_mes = "Novembro"
    case 12:
        nome_do_mes = "Dezembro"
    case _:
        nome_do_mes = "inexistente"

# --- 4. VALIDAÇÃO EM CADEIA ------------------------------------------
# A ordem importa: só dá para perguntar "o dia cabe no mês?" DEPOIS de
# saber que o mês existe.
if ano <= 0:
    valida = False
    motivo = "o ano deve ser positivo"
elif mes < 1 or mes > 12:
    valida = False
    motivo = "o mês deve estar entre 1 e 12"
elif dia < 1:
    valida = False
    motivo = "o dia deve ser positivo"
elif dia > dias_no_mes:
    valida = False
    motivo = f"{nome_do_mes.lower()} de {ano} tem apenas {dias_no_mes} dias"
else:
    valida = True
    motivo = ""

# --- 5. SAÍDA ---------------------------------------------------------
if mes >= 1 and mes <= 12:
    print(f"Mês: {nome_do_mes} ({dias_no_mes} dias)")
else:
    print(f"Mês: {nome_do_mes}")

print(f"Ano bissexto: {'Sim' if e_bissexto else 'Não'}")

if valida:
    print("Data VÁLIDA")
else:
    print(f"Data INVÁLIDA: {motivo}")


# --- Por que assim -------------------------------------------------
# 1. A regra do bissexto em UMA expressão. Rastreie 1900:
#
#      1900 % 4 == 0        -> True
#      1900 % 100 != 0      -> False
#      1900 % 400 == 0      -> False
#      True and (False or False) = True and False = False   ✔ correto
#
#    Sobre o parêntese: aqui ele NÃO muda o resultado. Testei os anos
#    de 1 a 4000 e as duas formas concordam em todos:
#
#      A and (B or C)      <- com parêntese
#      (A and B) or C      <- sem, pois "and" tem precedência
#
#    Elas coincidem por uma razão específica: C ("divisível por 400")
#    só pode ser verdadeiro quando A ("divisível por 4") também é —
#    todo múltiplo de 400 é múltiplo de 4. E o único caso em que as
#    duas formas divergiriam seria justamente C verdadeiro com A
#    falso, que não existe.
#
#    Mesmo assim, escreva o parêntese. Ele não está lá para consertar
#    a conta: está para dizer a INTENÇÃO. A regra em português é
#    "divisível por 4, e além disso (não por 100 ou então por 400)" —
#    e o parêntese é essa frase. Depender de uma coincidência
#    aritmética para o código funcionar é frágil: basta alguém mexer
#    numa das três condições para a sorte acabar.
#
# 2. Dois match separados: um para os dias, outro para o nome. Daria
#    para juntar num só, atribuindo as duas variáveis por case — mas
#    aí o agrupamento "1|3|5|7|8|10|12" se perderia, porque cada mês
#    tem nome diferente. Separar mantém cada match no seu ponto forte.
#
# 3. O "29 if e_bissexto else 28" é um if de uma linha (operador
#    ternário). Equivale a quatro linhas de if/else. Está aqui porque
#    cabe naturalmente numa atribuição — mas se você achou estranho,
#    escreva as quatro linhas: é igualmente correto.
#
# 4. A validação é uma CADEIA de elif, e a ordem não é arbitrária:
#
#      ano  -> mês  -> dia positivo -> dia cabe no mês
#
#    Testar "dia > dias_no_mes" antes de validar o mês compararia o
#    dia com dias_no_mes = 0 (do case _), recusando toda data com mês
#    inválido pelo motivo errado. A mensagem diria "tem apenas 0
#    dias" em vez de "mês inválido".
#
# 5. Cada ramo guarda um "motivo" em texto. É o que permite dizer
#    QUAL regra falhou, em vez do inútil "data inválida".


# --- Conferência dos casos do enunciado ------------------------------
# 29/02/2024 -> bissexto (4 sim, 100 não) -> fev tem 29 -> VÁLIDA
# 29/02/2023 -> 2023%4=3, não bissexto   -> fev tem 28 -> INVÁLIDA
# 29/02/1900 -> 4 sim, 100 sim, 400 não  -> fev tem 28 -> INVÁLIDA
# 29/02/2000 -> 4 sim, 100 sim, 400 SIM  -> fev tem 29 -> VÁLIDA
# 31/04/2024 -> abril tem 30             -> INVÁLIDA
# 31/12/2024 -> dezembro tem 31          -> VÁLIDA
# 10/13/2024 -> mês fora de 1..12        -> INVÁLIDA (motivo do mês)
# 00/05/2024 -> dia < 1                  -> INVÁLIDA (motivo do dia)


# --- Solução do desafio dentro do desafio ----------------------------
# As estações no hemisfério sul, com as fronteiras reais:
#
#   Verão:      21/12 a 20/03
#   Outono:     21/03 a 20/06
#   Inverno:    21/06 a 22/09
#   Primavera:  23/09 a 20/12
#
# Três delas cabem num "and", porque ficam dentro do mesmo ano:
#
#   e_outono = ((mes == 3 and dia >= 21) or (mes == 4) or (mes == 5)
#               or (mes == 6 and dia <= 20))
#
# Mas o VERÃO atravessa a virada do ano: ele começa em dezembro e
# termina em março. Não existe intervalo contínuo de mês que o
# descreva, porque dezembro (12) é MAIOR que março (3).
#
#   e_verao = ((mes == 12 and dia >= 21) or (mes == 1) or (mes == 2)
#              or (mes == 3 and dia <= 20))
#
# É por isso que ele precisa de "or" ligando dois blocos distantes,
# enquanto os outros ligam meses vizinhos. Qualquer tentativa de
# escrever "mes >= 12 and mes <= 3" resulta numa condição que nunca é
# verdadeira — a mesma armadilha do intervalo do módulo 02, agora com
# uma causa geométrica: o calendário é um círculo, não uma reta.
