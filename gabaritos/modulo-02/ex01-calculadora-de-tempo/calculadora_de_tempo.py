"""
Gabarito — Módulo 02, Exercício 01: Calculadora de tempo

Enunciado:
  modulo-02-operadores/exercicios/EXERCICIO-01-calculadora-de-tempo.md

Como executar:
  python calculadora_de_tempo.py
"""

SEGUNDOS_POR_HORA = 3600
SEGUNDOS_POR_MINUTO = 60

total_de_segundos = 10000

# O padrão é sempre o mesmo: // pega a unidade maior,
# % guarda o que sobrou para a próxima etapa.
horas = total_de_segundos // SEGUNDOS_POR_HORA
resto = total_de_segundos % SEGUNDOS_POR_HORA

minutos = resto // SEGUNDOS_POR_MINUTO
segundos = resto % SEGUNDOS_POR_MINUTO

print(f"Total: {total_de_segundos} segundos")
print()
print(f"Equivale a: {horas} h, {minutos} min e {segundos} s")
print(f"No relógio:  {horas:02d}:{minutos:02d}:{segundos:02d}")


# --- Por que assim -------------------------------------------------
# 1. A variável "resto" existe para não repetir a mesma conta duas
#    vezes. Daria para escrever tudo em uma linha:
#
#      minutos = (total_de_segundos % 3600) // 60
#
#    Funciona, mas obriga quem lê a desmontar a expressão de dentro
#    para fora. Com o nome no meio, a leitura fica linear.
#
# 2. As constantes no topo eliminam os "números mágicos". Um 3600
#    solto no meio do código exige que o leitor descubra sozinho que
#    aquilo é a quantidade de segundos numa hora.
#
# 3. O "{horas:02d}" preenche com zero à esquerda até dois dígitos.
#    Sem isso, 2 horas sairia como "2:46:40" em vez de "02:46:40".
#    O "d" diz "formate como inteiro decimal".
#
# 4. Nenhum if foi necessário. Todo o trabalho é aritmético — é
#    exatamente para isso que // e % servem.


# --- Conferência ----------------------------------------------------
# 10000 segundos
#   10000 // 3600 = 2        -> 2 horas
#   10000 %  3600 = 2800     -> sobram 2800 segundos
#    2800 //   60 = 46       -> 46 minutos
#    2800 %    60 = 40       -> 40 segundos
#
# Conferindo de volta: 2*3600 + 46*60 + 40 = 7200 + 2760 + 40 = 10000


# --- Solução do desafio opcional ------------------------------------
# Acrescentando dias, o padrão apenas ganha mais um degrau no topo:
#
#   SEGUNDOS_POR_DIA = 86400
#
#   dias = total_de_segundos // SEGUNDOS_POR_DIA
#   resto = total_de_segundos % SEGUNDOS_POR_DIA
#   horas = resto // SEGUNDOS_POR_HORA
#   resto = resto % SEGUNDOS_POR_HORA
#   minutos = resto // SEGUNDOS_POR_MINUTO
#   segundos = resto % SEGUNDOS_POR_MINUTO
#
# E a pergunta: passando de 24 horas, o formato HH:MM:SS estoura.
# Com 100000 segundos, "horas" vale 27 e a saída vira "27:46:40" —
# que não é hora de relógio nenhuma. Um relógio de parede precisaria
# de "horas % 24"; um cronômetro de duração está certo em mostrar 27.
# A escolha depende do que o número significa, e é o tipo de decisão
# que o enunciado não responde por você.
