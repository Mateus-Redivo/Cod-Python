"""
Gabarito — Módulo 08, Exercício 01: Caixa de ferramentas

Enunciado:
  modulo-08-funcoes/exercicios/EXERCICIO-01-caixa-de-ferramentas.md

Como executar:
  python caixa_de_ferramentas.py
"""

VOGAIS = "aeiou"


def dobrar(numero):
    return numero * 2


def calcular_media(numeros):
    return sum(numeros) / len(numeros)


def e_par(numero):
    # "numero % 2 == 0" JÁ é True ou False. Um if aqui compararia um
    # booleano para devolver o mesmo booleano.
    return numero % 2 == 0


def converter_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def contar_vogais(texto):
    total = 0
    for letra in texto.lower():
        if letra in VOGAIS:
            total += 1
    return total


def inverter_texto(texto):
    return texto[::-1]


def maior_de_tres(a, b, c):
    return max(a, b, c)


def aplicar_desconto(preco, percentual=10):
    return preco - preco * percentual / 100


# --- Uso -------------------------------------------------------------
print(f"dobrar(5)                      -> {dobrar(5)}")
print(f"dobrar(-3)                     -> {dobrar(-3)}")
print(f"calcular_media([7, 8, 9])      -> {calcular_media([7, 8, 9])}")
print(f"calcular_media([10, 0])        -> {calcular_media([10, 0])}")
print(f"e_par(4)                       -> {e_par(4)}")
print(f"e_par(7)                       -> {e_par(7)}")
print(f"converter_para_celsius(212)    -> {converter_para_celsius(212)}")
print(f"converter_para_celsius(32)     -> {converter_para_celsius(32)}")
print(f"contar_vogais('programacao')   -> {contar_vogais('programacao')}")
print(f"contar_vogais('XYZ')           -> {contar_vogais('XYZ')}")
print(f"inverter_texto('Python')       -> {inverter_texto('Python')}")
print(f"inverter_texto('arara')        -> {inverter_texto('arara')}")
print(f"maior_de_tres(3, 9, 5)         -> {maior_de_tres(3, 9, 5)}")
print(f"maior_de_tres(-1, -9, -5)      -> {maior_de_tres(-1, -9, -5)}")
print(f"aplicar_desconto(100)          -> {aplicar_desconto(100)}")
print(f"aplicar_desconto(100, 25)      -> {aplicar_desconto(100, 25)}")


# --- Por que assim -------------------------------------------------
# 1. Nenhuma função tem print. Todas devolvem. Quem chama é que
#    decide exibir — por isso os prints estão todos aqui embaixo,
#    num bloco só. Se amanhã você quiser somar dois resultados em vez
#    de mostrá-los, nada precisa mudar nas funções.
#
# 2. "e_par" devolve bool, não a string "sim". Um bool cabe direto num
#    if; a string obriga quem chama a comparar texto.
#
# 3. maior_de_tres usa max() em vez de dois ifs encadeados. As duas
#    versões estão certas; esta lê melhor e não tem onde errar. Se o
#    exercício fosse sobre if, valeria escrever à mão.
#
# 4. aplicar_desconto tem o percentual como parâmetro OPCIONAL, com
#    padrão 10. Assim uma função serve para o caso comum e para o
#    caso especial, sem duplicar nada.
#
# 5. VOGAIS é constante no topo, não uma string solta dentro da
#    função. Mesmo argumento do módulo 07.


# --- Solução do desafio opcional ------------------------------------
# calcular_media([]) hoje quebra com ZeroDivisionError. Três saídas
# possíveis, e nenhuma é obviamente certa:
#
#   a) devolver 0
#      def calcular_media(numeros):
#          if len(numeros) == 0:
#              return 0
#          return sum(numeros) / len(numeros)
#
#      Simples, mas MENTE: uma turma sem notas passa a ter média zero,
#      que é indistinguível de uma turma que tirou zero em tudo.
#
#   b) devolver None
#      Honesto — "não há média" é diferente de "a média é 0". Mas
#      obriga quem chama a testar antes de usar, e esquecer disso dá
#      TypeError lá na frente.
#
#   c) deixar quebrar
#      Também é uma escolha: lista vazia é erro de quem chamou, e o
#      ZeroDivisionError avisa alto. O módulo 10 mostra como
#      transformar isso numa mensagem decente.
#
# Escolho a (b). O motivo: "não sei" é uma resposta legítima, e
# fingir um número inventado é o tipo de decisão que vira bug de
# relatório seis meses depois.
