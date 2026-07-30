"""
Módulo 10 — Tratamento de erros
Exemplo 03: a receita completa (try + while)

Este arquivo mostra:
  - por que validar com while não basta
  - o padrão try dentro de while, que cobre tipo E valor
  - a mesma receita virando função reutilizável

Como executar:
  python 03_entrada_robusta.py
"""

# --- O que o módulo 05 já resolvia -----------------------------------
# while nota < 0 or nota > 10:   ->  pega o VALOR fora da faixa
#
# O que ele NÃO resolvia:
# float("abc")                   ->  o programa morre antes do while


# --- A receita: try por dentro, while por fora -----------------------
print("--- Leitura à prova de tudo ---")

while True:
    try:
        nota = float(input("Nota (0 a 10): "))
    except ValueError:
        print("  Isso não é um número. Tente de novo.")
        continue            # volta ao topo do while, pede de novo

    # Se chegou aqui, o texto virou número. Falta checar a FAIXA.
    if 0 <= nota <= 10:
        break               # tipo certo e valor certo: pode sair
    print("  A nota deve estar entre 0 e 10.")

print(f"  Nota aceita: {nota}")
print()


# --- A mesma receita virando função ----------------------------------
def ler_inteiro(mensagem, minimo, maximo):
    """Insiste até receber um inteiro dentro da faixa."""
    while True:
        try:
            valor = int(input(mensagem))
        except ValueError:
            print("  Digite um número inteiro.")
            continue

        if minimo <= valor <= maximo:
            return valor        # o return sai do while E da função
        print(f"  O valor deve estar entre {minimo} e {maximo}.")


idade = ler_inteiro("Idade (0 a 120): ", 0, 120)
print(f"  Idade aceita: {idade}")
print()

# Agora a mesma função serve para qualquer leitura numérica:
opcao = ler_inteiro("Opção do menu (1 a 4): ", 1, 4)
print(f"  Opção aceita: {opcao}")


# --- Experimento ---------------------------------------------------
# 1. Na primeira leitura, digite nesta ordem: "abc", depois "15",
#    depois "7". Três caminhos diferentes: erro de tipo, erro de
#    valor, sucesso.
#
# 2. Apague o "continue" do primeiro bloco e digite "abc". O programa
#    tenta usar a variável "nota" que nunca foi criada — NameError.
#    Por isso o continue é obrigatório.
#
# 3. Troque o "return valor" da função por "break". O que quebra?
#    (dica: quem recebe o valor de volta?)
