"""
Módulo 04 — Condicionais
Exemplo 03: aninhar, achatar e proteger

Este arquivo mostra:
  - condicionais dentro de condicionais
  - como achatar um aninhamento com and
  - o padrão "proteger antes de agir", que fecha a promessa do módulo 03

Como executar:
  python 03_aninhadas_e_protecao.py
"""

# --- Aninhamento que faz sentido ------------------------------------
# Aqui o segundo teste só existe DENTRO do primeiro caso: perguntar
# se é par só interessa depois de saber que é positivo.
numero = 10
print(f"numero = {numero}")

if numero > 0:
    print("  Positivo")
    if numero % 2 == 0:
        print("  E par")
    else:
        print("  E ímpar")
elif numero < 0:
    print("  Negativo")
else:
    print("  Zero")
print()


# --- Aninhamento que pede para ser achatado -------------------------
tem_conta = True
saldo = 150.00

print("Versão aninhada:")
if tem_conta:
    if saldo > 0:
        print("  Pode sacar")

print("Versão achatada (mesma coisa, uma leitura só):")
if tem_conta and saldo > 0:
    print("  Pode sacar")

print()
print("Quando o if de dentro é a ÚNICA coisa dentro do if de fora,")
print("os dois viram um só com 'and'. Se você chegou no terceiro")
print("nível de indentação, quase sempre dá para simplificar.")
print()


# --- Proteger antes de agir -----------------------------------------
# Este é o padrão que resolve o ZeroDivisionError do módulo 03.
total = 100.00

numero_de_pessoas = 4
print(f"Dividindo R$ {total:.2f} entre {numero_de_pessoas} pessoas:")
if numero_de_pessoas == 0:
    print("  Não dá para dividir por zero pessoas.")
else:
    # A divisão está DENTRO do else: só roda no caminho seguro.
    print(f"  Cada um paga R$ {total / numero_de_pessoas:.2f}")
print()

numero_de_pessoas = 0
print(f"Dividindo R$ {total:.2f} entre {numero_de_pessoas} pessoas:")
if numero_de_pessoas == 0:
    print("  Não dá para dividir por zero pessoas.")
else:
    print(f"  Cada um paga R$ {total / numero_de_pessoas:.2f}")
print()

print("Testar não basta: a operação perigosa precisa ficar no ramo")
print("onde já se sabe que ela é segura.")


# --- Experimento ---------------------------------------------------
# 1. Tire a divisão de dentro do else e coloque-a depois do if,
#    sem indentação. Rode. Você recupera o ZeroDivisionError — o if
#    avisa, mas não protege mais nada.
#
# 2. No bloco aninhado, troque numero por -4 e depois por 0.
#    Os três caminhos são cobertos?
#
# 3. Reescreva o bloco "tem_conta / saldo" invertendo a lógica: saia
#    cedo quando NÃO puder sacar. Qual das três versões você acharia
#    mais fácil de ler daqui a um mês?
