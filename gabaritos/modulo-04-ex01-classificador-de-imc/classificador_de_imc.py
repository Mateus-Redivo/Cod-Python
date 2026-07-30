"""
Gabarito — Módulo 04, Exercício 01: Classificador de IMC

Enunciado:
  modulo-04-condicionais/exercicios/EXERCICIO-01-classificador-de-imc.md

Como executar:
  python classificador_de_imc.py
"""

# --- 1. ENTRADA ------------------------------------------------------
# float nos dois: 70.5 kg e 1.75 m são valores normais.
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em m: "))

print()

# --- 2. PROTEÇÃO + PROCESSAMENTO + SAÍDA -----------------------------
# A checagem vem ANTES de qualquer conta. Tudo que depende da divisão
# fica dentro do else, no caminho já sabidamente seguro.
if altura == 0:
    print("Altura inválida: não é possível calcular o IMC.")
else:
    imc = peso / altura ** 2

    # A cadeia vai da faixa mais BAIXA para a mais alta. Poderia ser o
    # contrário; o que não pode é misturar, deixando um ramo coberto
    # por outro que vem antes.
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25.0:
        classificacao = "Peso normal"
    elif imc < 30.0:
        classificacao = "Sobrepeso"
    elif imc < 40.0:
        classificacao = "Obesidade"
    else:
        classificacao = "Obesidade grave"

    print(f"IMC: {imc:.2f}")
    print(f"Classificação: {classificacao}")


# --- Por que assim -------------------------------------------------
# 1. A cadeia usa "<" e vai subindo, em vez de ">=" descendo. As duas
#    formas funcionam. Escolhi esta porque ela deixa as FRONTEIRAS
#    explícitas: "imc < 25.0" diz que 25.0 NÃO é peso normal, que é
#    exatamente o que a tabela do enunciado manda.
#
#    Com ">=" descendo, o mesmo resultado seria:
#
#      if imc >= 40.0:   classificacao = "Obesidade grave"
#      elif imc >= 30.0: classificacao = "Obesidade"
#      elif imc >= 25.0: classificacao = "Sobrepeso"
#      elif imc >= 18.5: classificacao = "Peso normal"
#      else:             classificacao = "Abaixo do peso"
#
# 2. Nenhuma condição repete a faixa anterior. Escrever
#    "elif imc >= 25.0 and imc < 30.0" funciona, mas o "and imc >= 25"
#    é redundante: se o programa chegou nesse elif, é porque
#    "imc < 25.0" já foi falso. O elif carrega o "senão" embutido.
#
# 3. A classificação vai para uma VARIÁVEL e o print acontece uma vez
#    só, no fim. A alternativa — um print dentro de cada ramo —
#    funciona, mas repete cinco vezes uma linha quase igual. Se o
#    formato da saída mudar, você teria que acertar as cinco.
#
# 4. O ** tem precedência sobre o /, então "peso / altura ** 2" já
#    calcula a altura ao quadrado primeiro. Escrever
#    "peso / (altura ** 2)" é igualmente correto e mais explícito.


# --- Conferência das fronteiras -------------------------------------
# O enunciado pede para testar os valores exatos de fronteira.
# Com altura 1.00, o IMC é igual ao peso, o que facilita o teste:
#
#   peso 18.5, altura 1.0  -> IMC 18.50 -> Peso normal      (não "Abaixo")
#   peso 25.0, altura 1.0  -> IMC 25.00 -> Sobrepeso        (não "Normal")
#   peso 30.0, altura 1.0  -> IMC 30.00 -> Obesidade        (não "Sobrepeso")
#   peso 40.0, altura 1.0  -> IMC 40.00 -> Obesidade grave  (não "Obesidade")
#
# Todos batem com a tabela. Se algum tivesse caído na faixa de baixo,
# o operador estaria trocado ("<=" no lugar de "<").
#
# E o caso do enunciado: peso 70, altura 1.75 -> 70 / 3.0625 = 22.857...
# que exibido com duas casas vira 22.86. Peso normal.


# --- Solução do desafio opcional ------------------------------------
# Validando as faixas de entrada:
#
#   if altura <= 0 or altura > 3:
#       print("Altura inválida: informe um valor entre 0 e 3 metros.")
#   elif peso <= 0 or peso > 500:
#       print("Peso inválido: informe um valor entre 0 e 500 kg.")
#   else:
#       ... o cálculo ...
#
# Repare no "or": a faixa PROIBIDA é fora do intervalo, e fora pede
# or — é a armadilha do módulo 02 aparecendo em código de verdade.
#
# E a limitação que o enunciado antecipa: isto só AVISA e encerra. Para
# insistir na pergunta até vir um valor bom, é preciso repetir — e
# repetir é o módulo 05. Lá, a validação vira:
#
#   while altura <= 0 or altura > 3:
#       print("Altura inválida.")
#       altura = float(input("Digite sua altura em m: "))
