"""
Gabarito — Módulo 03, Exercício 01: Conversor de medidas

Enunciado:
  modulo-03-entrada-e-saida/exercicios/EXERCICIO-01-conversor-de-medidas.md

Como executar:
  python conversor_de_medidas.py
"""

# Constantes das fórmulas. Sem elas, 9, 5, 32 e 273.15 ficariam soltos
# no meio da conta e ninguém saberia de onde vieram.
FATOR_FAHRENHEIT = 9 / 5
AJUSTE_FAHRENHEIT = 32
ZERO_ABSOLUTO = 273.15

# --- 1. ENTRADA ------------------------------------------------------
# float, não int: 36.6 é uma temperatura perfeitamente normal.
celsius = float(input("Digite a temperatura em Celsius: "))

# --- 2. PROCESSAMENTO ------------------------------------------------
fahrenheit = celsius * FATOR_FAHRENHEIT + AJUSTE_FAHRENHEIT
kelvin = celsius + ZERO_ABSOLUTO

# --- 3. SAÍDA --------------------------------------------------------
print()
print(f"{celsius:.1f} °C equivale a:")
print(f"  {fahrenheit:.1f} °F")
print(f"  {kelvin:.1f} K")


# --- Por que assim -------------------------------------------------
# 1. float() e não int(). Se fosse int, digitar 36.6 daria ValueError:
#    int() não aceita a escrita de um decimal. Temperatura é uma
#    grandeza contínua — a pergunta "faz sentido meio disso?" responde
#    sim, então é float.
#
# 2. A ordem das operações não precisa de parênteses aqui: * vem antes
#    de + na precedência, então "celsius * FATOR + AJUSTE" já calcula
#    na ordem certa. Escrever "(celsius * FATOR) + AJUSTE" também está
#    certo e não custa nada — na dúvida, use.
#
# 3. FATOR_FAHRENHEIT guarda 9/5, que dá 1.8. Escrever a divisão em
#    vez do 1.8 preserva a fórmula original, que é como ela aparece em
#    qualquer tabela de conversão. Quem for conferir reconhece.


# --- Sobre o arredondamento de 298.15 --------------------------------
# Com 25 °C, o Kelvin dá exatamente 298.15 — e a exibição com uma casa
# mostra 298.1, não 298.2. Parece erro, não é.
#
# O 298.15 guardado na memória não é exatamente 298.15: é um valor
# binário pouquinho MENOR. Como está abaixo do ponto médio, arredonda
# para baixo. É a mesma poeirinha do 0.1 + 0.2 do módulo 02.
#
# Confira você mesmo:
#
#   print(f"{298.15:.20f}")   ->  298.14999999999997726263
#
# Para material didático isso é curiosidade. Para dinheiro, é o motivo
# de existirem bibliotecas especializadas (decimal) — assunto muito
# além desta trilha, mas vale saber que o problema tem nome.


# --- Conferência ----------------------------------------------------
# Entrada 25:
#   F = 25 * 1.8 + 32 = 45 + 32 = 77.0
#   K = 25 + 273.15   = 298.15  -> exibido 298.1
#
# Entrada -40 (o ponto onde as duas escalas se cruzam):
#   F = -40 * 1.8 + 32 = -72 + 32 = -40.0   <- iguais!
#   K = -40 + 273.15   = 233.15  -> exibido 233.1


# --- Solução do desafio opcional ------------------------------------
# O caminho inverso, Fahrenheit para Celsius, é a fórmula isolada:
#
#   celsius = (fahrenheit - AJUSTE_FAHRENHEIT) / FATOR_FAHRENHEIT
#
# Repare que agora os parênteses são OBRIGATÓRIOS: sem eles, a divisão
# aconteceria antes da subtração e o resultado sairia errado — sem
# nenhum aviso do Python.
#
# E a pergunta que o enunciado deixou no ar — "como eu escolheria
# entre os dois programas?" — é exatamente o que o módulo 04 responde,
# com if/elif/else.
