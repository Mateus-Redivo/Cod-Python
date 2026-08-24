"""
Gabarito — Módulo 03, Exercício 03: Planejador de viagem

Enunciado:
  modulo-03-entrada-e-saida/exercicios/EXERCICIO-03-planejador-de-viagem.md

Escolha dos tipos, justificada:
  destino          -> str,   é texto
  distancia        -> float, 480.5 km é possível
  consumo          -> float, 12.5 km/l é comum
  preco_do_litro   -> float, dinheiro tem centavos
  velocidade       -> float, média não precisa ser inteira
  pedagios         -> float, dinheiro de novo
  pessoas          -> int,   meia pessoa não existe

Como executar:
  python planejador_de_viagem.py
"""

TANQUE_LITROS = 50
MINUTOS_POR_HORA = 60
LARGURA = 50
COL_ROTULO = 33
COL_VALOR = 9

# --- 1. ENTRADA ------------------------------------------------------
print("=== PLANEJADOR DE VIAGEM ===")
destino = input("Destino: ")
distancia = float(input("Distância (km): "))
consumo = float(input("Consumo do carro (km/l): "))
preco_do_litro = float(input("Preço do litro (R$): "))
velocidade = float(input("Velocidade média (km/h): "))
pedagios = float(input("Total de pedágios (R$): "))
pessoas = int(input("Número de pessoas: "))

# --- 2. PROCESSAMENTO ------------------------------------------------
litros = distancia / consumo
custo_combustivel = litros * preco_do_litro
custo_total = custo_combustivel + pedagios
custo_por_pessoa = custo_total / pessoas

duracao_horas = distancia / velocidade

# Converte para minutos TOTAIS e arredonda uma vez só. Ver a nota
# "A armadilha da truncagem", no fim do arquivo — este trecho parece
# trivial e não é.
duracao_minutos_totais = round(duracao_horas * MINUTOS_POR_HORA)
horas_inteiras = duracao_minutos_totais // MINUTOS_POR_HORA
minutos = duracao_minutos_totais % MINUTOS_POR_HORA

custo_por_km = custo_total / distancia
percentual_pedagio = pedagios / custo_total * 100
sobra_no_tanque = TANQUE_LITROS - litros

# --- 3. SAÍDA --------------------------------------------------------
print()
print("=" * LARGURA)
print(f"{'VIAGEM PARA ' + destino.upper():^{LARGURA}}")
print("=" * LARGURA)

# Toda linha de valor tem: rótulo + prefixo de 3 caracteres + número.
# O prefixo é "R$ " quando é dinheiro e "   " quando não é. É isso que
# mantém TODOS os números na mesma coluna, com ou sem cifrão.
SEM_CIFRAO = "   "

print("--- ROTA ---")
print(f"{'Distância':<{COL_ROTULO}}{SEM_CIFRAO}{distancia:>{COL_VALOR}.1f} km")
print(f"{'Velocidade média':<{COL_ROTULO}}{SEM_CIFRAO}{velocidade:>{COL_VALOR}.1f} km/h")
print(f"{'Duração':<{COL_ROTULO}}{SEM_CIFRAO}{str(horas_inteiras) + 'h' + str(minutos) + 'min':>{COL_VALOR}}")
print(f"{'Duração (decimal)':<{COL_ROTULO}}{SEM_CIFRAO}{duracao_horas:>{COL_VALOR}.2f} h")
print()

print("--- CUSTOS ---")
print(f"{'Combustível necessário':<{COL_ROTULO}}{SEM_CIFRAO}{litros:>{COL_VALOR}.2f} L")
print(f"{'Custo do combustível':<{COL_ROTULO}}R$ {custo_combustivel:>{COL_VALOR}.2f}")
print(f"{'Pedágios':<{COL_ROTULO}}R$ {pedagios:>{COL_VALOR}.2f}")
print(f"{'CUSTO TOTAL':<{COL_ROTULO}}R$ {custo_total:>{COL_VALOR}.2f}")
print()
print(f"{'Custo por km':<{COL_ROTULO}}R$ {custo_por_km:>{COL_VALOR}.2f}")
print(f"{'Pedágio representa':<{COL_ROTULO}}{SEM_CIFRAO}{percentual_pedagio:>{COL_VALOR}.2f} % do total")
print()

print("--- RATEIO ---")
print(f"{'Pessoas':<{COL_ROTULO}}{SEM_CIFRAO}{pessoas:>{COL_VALOR}}")
print(f"{'Cada um paga':<{COL_ROTULO}}R$ {custo_por_pessoa:>{COL_VALOR}.2f}")
print()

print(f"--- TANQUE ({TANQUE_LITROS} L) ---")
print(f"{'Sobram após a viagem':<{COL_ROTULO}}{SEM_CIFRAO}{sobra_no_tanque:>{COL_VALOR}.2f} L")
print("=" * LARGURA)


# --- Por que assim -------------------------------------------------
# 1. A escolha dos tipos está no docstring do topo, como o enunciado
#    pediu. A regra é sempre a mesma: "faz sentido meio disso?" Meia
#    pessoa não; meio litro sim.
#
# 2. A duração converte para MINUTOS TOTAIS e arredonda uma vez só.
#    Ver a nota sobre truncagem, no fim — a versão "óbvia" erra.
#
# 3. O percentual é calculado com "* 100" e exibido com ":.2f". A
#    alternativa seria não multiplicar e usar ":.2%" — mas fazer as
#    DUAS coisas daria 1277%, que é o erro comum que o enunciado
#    avisa.
#
# 4. As larguras estão em constantes e as f-strings as leem com chaves
#    aninhadas. Mudar COL_ROTULO de 33 para 40 realinha o relatório
#    inteiro sem tocar em mais nada.
#
#    O truque do alinhamento: toda linha de valor tem um prefixo de
#    EXATAMENTE 3 caracteres entre o rótulo e o número — "R$ " quando
#    é dinheiro, "   " quando não é. Sem isso, as linhas com cifrão
#    empurram o número 3 colunas para a direita e a tabela entorta.
#    Foi o que aconteceu na primeira versão deste gabarito.
#
# 5. O ":^" centraliza o título. É o terceiro alinhamento, junto de
#    < e >.
#
# 6. O .upper() no destino atende ao requisito de exibi-lo em
#    maiúsculas sem obrigar o usuário a digitar assim. É o método do
#    módulo 07 sendo antecipado — mas o .upper() é simples o bastante
#    para aparecer aqui.


# --- Conferência (dados do enunciado) --------------------------------
# distância 480, consumo 12, litro 5.89, velocidade 90, pedágio 34.50,
# 3 pessoas:
#
#   litros    = 480 / 12       = 40.00 L
#   combustív = 40 * 5.89      = 235.60
#   total     = 235.60 + 34.50 = 270.10
#   por pessoa= 270.10 / 3     = 90.0333... -> 90.03
#   duração   = 480 / 90       = 5.333... h -> 5h20min
#   por km    = 270.10 / 480   = 0.5627...  -> 0.56
#   % pedágio = 34.50 / 270.10 = 0.12772... -> 12.77 %
#   sobra     = 50 - 40        = 10.00 L


# --- A armadilha da truncagem ----------------------------------------
# A forma "óbvia" de separar horas e minutos ERRA neste caso:
#
#   horas   = int(duracao_horas)                        # 5
#   minutos = int((duracao_horas % 1) * 60)             # 19, não 20!
#
# Por quê? Rastreie:
#
#   480 / 90            = 5.333333333333333
#   5.3333... % 1       = 0.33333333333333304
#   0.3333... * 60      = 19.999999999999982
#   int(19.99999...)    = 19          <- int() TRUNCA, não arredonda
#
# A poeirinha dos decimais do módulo 02 aparece aqui com consequência
# visível: a viagem passa a durar "5h19min". Um minuto a menos, sem
# nenhum erro na tela.
#
# Duas correções possíveis:
#
#   a) arredondar em vez de truncar:  round(...) em vez de int(...)
#   b) converter para minutos totais e arredondar UMA vez (o que este
#      gabarito faz):
#
#        total = round(duracao_horas * 60)   # 320
#        horas = total // 60                 # 5
#        minutos = total % 60                # 20
#
# Prefiro a (b) por um motivo geral: **arredonde uma vez só, o mais
# tarde possível.** Cada arredondamento intermediário é uma chance de
# a diferença se acumular. É o mesmo princípio do centavo do rateio,
# logo abaixo.
#
# Se a sua solução deu 5h19min, ela não estava "quase certa" — estava
# errada de um jeito difícil de notar. Esses são os piores.


# --- Sobre o centavo que sobra ---------------------------------------
# 90.03 x 3 = 270.09, um centavo a menos que os 270.10 reais.
#
# Na prática, quem organiza a viagem costuma absorver a diferença — e
# é a solução que eu adotaria: o custo de discutir um centavo é maior
# que o centavo.
#
# Mas repare que a decisão é de PRODUTO, não de programação. Um
# sistema de cobrança sério faria diferente: distribuiria os centavos
# restantes um a um entre os primeiros pagadores, para que a soma
# fechasse exata. Existe até nome para isso — "arredondamento com
# distribuição de resto".
#
# O que não vale é fingir que o problema não existe. Todo sistema que
# divide dinheiro topa com ele.
