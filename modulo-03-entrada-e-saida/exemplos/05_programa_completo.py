"""
Módulo 03 — Entrada e saída
Exemplo 05: entrada, processamento e saída

Este arquivo mostra:
  - o esqueleto de três etapas que todo programa daqui em diante segue
  - a escolha entre int e float na hora de converter

Como executar:
  python 05_programa_completo.py
"""

TAXA_DE_SERVICO = 0.10

print("=== Divisor de conta ===")
print()

# --- 1. ENTRADA: pergunte e converta na mesma linha ------------------
# float para o valor: dinheiro tem centavos.
valor_da_conta = float(input("Valor total da conta: R$ "))

# int para as pessoas: meia pessoa não existe.
numero_de_pessoas = int(input("Quantas pessoas: "))


# --- 2. PROCESSAMENTO: só contas, nada de input nem print -----------
servico = valor_da_conta * TAXA_DE_SERVICO
total_com_servico = valor_da_conta + servico
valor_por_pessoa = total_com_servico / numero_de_pessoas


# --- 3. SAÍDA: formatada, com duas casas para dinheiro --------------
print()
print("-" * 32)
print(f"{'Conta:':<20}R$ {valor_da_conta:>8.2f}")
print(f"{'Serviço (10%):':<20}R$ {servico:>8.2f}")
print(f"{'Total:':<20}R$ {total_com_servico:>8.2f}")
print("-" * 32)
print(f"{'Por pessoa:':<20}R$ {valor_por_pessoa:>8.2f}")
print(f"({numero_de_pessoas} pessoas)")


# --- Experimento ---------------------------------------------------
# 1. Rode com conta 100 e 3 pessoas. O valor por pessoa dá 36.67 —
#    e 36.67 x 3 = 110.01, um centavo a mais que o total. Arredondar
#    dinheiro sempre sobra ou falta um trocado. Quem paga o centavo?
#    Não existe resposta técnica: é decisão de quem faz o programa.
#
# 2. Digite 0 no número de pessoas. ZeroDivisionError. No módulo 05
#    você aprende a insistir na pergunta até vir um valor válido.
#
# 3. Troque o int() do número de pessoas por float() e digite 2.5.
#    O programa aceita e calcula. Por que o int() era a escolha certa?
