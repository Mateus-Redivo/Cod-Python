"""
Gabarito — Módulo 01, Exercício 01: Ficha cadastral

Enunciado:
  modulo-01-tipos-e-variaveis/exercicios/EXERCICIO-01-ficha-cadastral.md

Como executar:
  python ficha_cadastral.py
"""

# Constante: em maiúsculas para avisar que não deve mudar durante o
# programa. Fica no topo, longe do meio do código, para ser fácil de
# achar quando a regra do negócio mudar.
IDADE_MINIMA = 18

# Uma variável por informação, cada uma com o tipo que faz sentido
# para o dado que guarda.
nome = "Maria Silva"        # str   - texto
idade = 25                  # int   - inteiro, ninguém tem 25.4 anos
altura = 1.75               # float - precisa de casas decimais
ativa = True                # bool  - só há duas respostas possíveis

print("===== FICHA CADASTRAL =====")
print(f"Nome:    {nome}")
print(f"Idade:   {idade} anos")
print(f"Altura:  {altura} m")
print(f"Ativa:   {ativa}")
print()
print(f"Idade mínima exigida: {IDADE_MINIMA}")
print()

print("--- Tipos ---")
print(f"nome   -> {type(nome).__name__}")
print(f"idade  -> {type(idade).__name__}")
print(f"altura -> {type(altura).__name__}")
print(f"ativa  -> {type(ativa).__name__}")


# --- Por que assim -------------------------------------------------
# 1. A escolha do tipo não é decorativa, é uma decisão sobre o dado.
#    Idade como int porque não existe fração de ano no cadastro;
#    altura como float porque 1.75 precisa da casa decimal.
#
# 2. "ativa" é bool, não a string "sim". Guardar True/False permite
#    testar direto no if do módulo 04; guardar "sim" obriga a comparar
#    texto e a decidir se "Sim" e "SIM" também valem.
#
# 3. type(x).__name__ devolve só o nome ("str") em vez do
#    "<class 'str'>" completo. As duas formas estão certas; escolhi a
#    curta porque a saída fica mais limpa.
#
# 4. Tudo formatado com f-string. Concatenar com "+" daria TypeError
#    ao juntar o texto do rótulo com o número da idade — exatamente o
#    problema do exemplo 04.


# --- Solução do desafio opcional ------------------------------------
# O IMC entra como mais um float calculado a partir das outras
# variáveis:
#
#   peso = 68.5
#   imc = peso / altura ** 2
#   print(f"IMC:     {imc:.2f}")
#
# O ":.2f" na f-string arredonda para duas casas na EXIBIÇÃO — a
# variável continua com todas as casas. Sem ele a saída sairia como
# 22.367346938775512, que ninguém quer ler numa ficha.
