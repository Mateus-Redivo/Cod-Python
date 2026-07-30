"""
Módulo 10 — Tratamento de erros
Exemplo 04: else, finally e quando NÃO capturar

Este arquivo mostra:
  - o else, que só roda quando deu certo
  - o finally, que roda sempre
  - dois casos em que capturar é pior do que não capturar

Como executar:
  python 04_else_finally.py
"""


def testar(texto):
    """Mostra a ordem de execução de try, except, else e finally."""
    print(f"  entrada: {texto!r}")
    try:
        numero = int(texto)
    except ValueError:
        print("    except: não era número")
    else:
        print(f"    else:   deu certo, numero = {numero}")
    finally:
        print("    finally: isto roda sempre")


print("--- Caso que dá certo ---")
testar("42")
print()

print("--- Caso que dá erro ---")
testar("abc")
print()

print("Repare: o finally rodou nos DOIS casos. O else, só no primeiro.")
print()


# --- Por que o else deixa o código melhor ----------------------------
print("--- try curto vs try inchado ---")
print()
print("  RUIM — o try engloba coisas que não podem falhar:")
print("""
    try:
        numero = int(texto)
        dobro = numero * 2
        print(f"O dobro é {dobro}")
    except ValueError:
        print("Erro")
""")
print("  Se o print tivesse um bug, o except o esconderia como se")
print("  fosse problema de conversão.")
print()
print("  BOM — no try, só a linha que pode falhar:")
print("""
    try:
        numero = int(texto)
    except ValueError:
        print("Erro")
    else:
        dobro = numero * 2
        print(f"O dobro é {dobro}")
""")
print()


# --- Quando NÃO capturar ---------------------------------------------
print("--- Dois casos em que capturar é pior ---")
print()

print("  Caso 1: inventar um valor para esconder o problema")
soma = 0
quantidade = 0
try:
    media = soma / quantidade
except ZeroDivisionError:
    media = 0                       # mentira!

print(f"    média de uma turma vazia: {media}")
print("    Isso é indistinguível de uma turma que tirou zero em tudo.")
print("    O erro foi escondido, não resolvido.")
print()

print("  Caso 2: dava para PREVENIR com um if")
print("""
    if quantidade > 0:              # melhor
        media = soma / quantidade
    else:
        print("Nenhuma nota informada.")
""")
print("    Prevenir lê melhor que remediar. Use try quando o erro")
print("    depende de algo fora do seu controle — o que o usuário")
print("    digitou, um arquivo que pode não existir. Para o que está")
print("    sob seu controle, use if.")


# --- Experimento ---------------------------------------------------
# 1. Em testar(), acrescente um "return" dentro do except. O finally
#    ainda roda? (Sim — e é justamente para isso que ele existe.)
#
# 2. Reescreva o "Caso 1" de forma honesta: em vez de media = 0,
#    avise que não há média. Qual das duas versões você gostaria de
#    encontrar num relatório?
#
# 3. Pense num erro do seu dia a dia que você NÃO deveria capturar.
#    Escreva por quê num comentário.
