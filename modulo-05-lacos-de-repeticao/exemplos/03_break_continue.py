"""
Módulo 05 — Laços de repetição
Exemplo 03: break e continue

Este arquivo mostra:
  - break: sair do laço antes da hora
  - continue: pular o resto de uma volta e seguir para a próxima
  - a diferença entre "parar" e "ignorar"

Nada é digitado aqui: os valores estão fixos no código para você
conseguir prever a saída antes de rodar.

Como executar:
  python 03_break_continue.py
"""

# --- break: para assim que a condição especial acontece -------------
# Somamos 1, 2, 3... e queremos saber onde a soma ultrapassa 50.
# Não dá para escrever essa condição no "while": só descobrimos
# depois de somar. Daí o "while True" com break.
soma = 0
numero = 1

while True:
    soma += numero
    print(f"  somei {numero} -> soma = {soma}")

    if soma > 50:
        print(f"  passou de 50 ao somar o {numero}. Parando.")
        break

    numero += 1

print()


# --- continue: ignora esta volta, mas o laço segue ------------------
# Somamos apenas os múltiplos de 3 entre 1 e 12.
soma = 0
quantidade = 0

for numero in range(1, 13):
    if numero % 3 != 0:
        continue        # não é múltiplo de 3: pula para a próxima volta

    soma += numero
    quantidade += 1
    print(f"  {numero} é múltiplo de 3 -> soma parcial = {soma}")

print(f"Total: {soma} em {quantidade} múltiplos.")


# --- Experimento ---------------------------------------------------
# 1. No primeiro laço, apague o "break" e rode.
#    Ctrl + C para interromper. "while True" sem break é loop infinito
#    por construção: o break É a condição de parada.
#
# 2. No segundo laço, mova "soma += numero" para ANTES do if.
#    O resultado muda? Isso mostra exatamente o que o continue pula.
#
# 3. Troque "continue" por "break" no segundo laço. Quantos números
#    aparecem agora? Confira antes de rodar.
