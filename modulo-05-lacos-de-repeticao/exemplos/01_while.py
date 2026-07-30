"""
Módulo 05 — Laços de repetição
Exemplo 01: as três partes do while

Este arquivo mostra:
  - inicializar, testar e atualizar a variável de controle
  - o que muda quando você mexe em cada uma das três partes

Como executar:
  python 01_while.py
"""

# 1. INICIALIZAR a variável de controle, antes do laço
contador = 1

# 2. TESTAR: enquanto a condição for verdadeira, o bloco se repete
while contador <= 5:
    print(f"Volta número {contador}")

    # 3. ATUALIZAR: sem esta linha, contador vale 1 para sempre
    contador += 1

print(f"O laço terminou com contador = {contador}")
print()


# --- Contagem regressiva: mesma estrutura, sentido contrário --------
numero = 5

while numero >= 1:
    print(f"{numero}...")
    numero -= 1

print("FOGO!")


# --- Experimento ---------------------------------------------------
# 1. Comente a linha "contador += 1" e rode de novo.
#    O programa vai imprimir "Volta número 1" para sempre: é o loop
#    infinito. Interrompa com Ctrl + C. Descomente depois.
#
# 2. Troque "contador = 1" por "contador = 10" e rode.
#    Quantas voltas o laço deu? Por que a condição nunca foi verdadeira?
#
# 3. Troque "contador <= 5" por "contador < 5".
#    Quantas voltas o laço dá agora? Confira antes de rodar.
