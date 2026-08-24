"""
Gabarito — Módulo 02, Exercício 03: Anatomia de um número

Enunciado:
  modulo-02-operadores/exercicios/EXERCICIO-03-anatomia-de-um-numero.md

Como executar:
  python anatomia_de_um_numero.py
"""

numero = 4832

# --- Extrair os quatro dígitos ---------------------------------------
# O padrão: // desloca para a direita, % 10 pega o último que sobrou.
unidade = numero % 10                   # 4832 % 10        = 2
dezena = numero // 10 % 10              # 483  % 10        = 3
centena = numero // 100 % 10            # 48   % 10        = 8
milhar = numero // 1000                 # 4                = 4

# --- Contas básicas ---------------------------------------------------
soma = milhar + centena + dezena + unidade
produto = milhar * centena * dezena * unidade

# --- Maior e menor SEM max()/min() -----------------------------------
# (a + b + |a - b|) / 2 devolve o maior dos dois.
# Se a > b, |a-b| = a-b, e a conta vira (a + b + a - b)/2 = a.
# Se b > a, |a-b| = b-a, e a conta vira (a + b + b - a)/2 = b.
# O // 2 no lugar de / 2 mantém o resultado como int.
maior_1 = (milhar + centena + abs(milhar - centena)) // 2
maior_2 = (dezena + unidade + abs(dezena - unidade)) // 2
maior = (maior_1 + maior_2 + abs(maior_1 - maior_2)) // 2

menor_1 = (milhar + centena - abs(milhar - centena)) // 2
menor_2 = (dezena + unidade - abs(dezena - unidade)) // 2
menor = (menor_1 + menor_2 - abs(menor_1 - menor_2)) // 2

# --- Invertido, montado com aritmética --------------------------------
invertido = unidade * 1000 + dezena * 100 + centena * 10 + milhar

# --- As quatro perguntas, todas bool ---------------------------------
e_par = numero % 2 == 0
e_multiplo_de_3 = soma % 3 == 0
e_capicua = numero == invertido

todos_diferentes = (milhar != centena and milhar != dezena and milhar != unidade
                    and centena != dezena and centena != unidade
                    and dezena != unidade)

# --- Saída -------------------------------------------------------------
print(f"Número: {numero}")
print()
print(f"Dígitos: {milhar} {centena} {dezena} {unidade}")
print(f"Soma:     {soma}")
print(f"Produto:  {produto}")
print(f"Maior:    {maior}")
print(f"Menor:    {menor}")
print(f"Invertido: {invertido}")
print()
print(f"É par?                    {e_par}")
print(f"É múltiplo de 3?          {e_multiplo_de_3}")
print(f"É capicua?                {e_capicua}")
print(f"Todos dígitos diferentes? {todos_diferentes}")


# --- Por que assim -------------------------------------------------
# 1. O par // e % é a única forma de entrar num número sem convertê-lo
#    para texto. "numero // 10 % 10" lê-se: descarte a unidade,
#    depois pegue a nova unidade.
#
#    A precedência ajuda: // e % têm a MESMA prioridade e resolvem da
#    esquerda para a direita. Então "numero // 10 % 10" já significa
#    "(numero // 10) % 10" sem precisar de parênteses. Colocá-los
#    mesmo assim não custa nada e evita dúvida.
#
# 2. O truque do maior/menor merece atenção. Ele funciona porque
#    |a - b| é a DISTÂNCIA entre os dois, e somá-la à média puxa o
#    resultado para o maior; subtraí-la puxa para o menor.
#
#    Usei // 2 e não / 2 de propósito: a divisão comum devolveria
#    float, e "Maior: 8.0" ficaria estranho num dígito. Como a soma
#    a+b+|a-b| é sempre par, o // 2 é exato aqui.
#
# 3. "e_par = numero % 2 == 0" já é bool. Escrever isto seria erro:
#
#      if numero % 2 == 0:      <- nem temos if ainda
#          e_par = True
#
#    A comparação PRODUZ o booleano; não é preciso convertê-lo.
#
# 4. O truque do múltiplo de 3 é matemático, não de programação: um
#    número é divisível por 3 se a soma dos seus dígitos for. Dava
#    para fazer "numero % 3 == 0" direto — mas aí a soma dos dígitos
#    não teria serventia, e o exercício perde a graça.
#
# 5. "todos_diferentes" precisa de SEIS comparações, não quatro: são
#    todos os pares possíveis entre 4 dígitos (4x3/2 = 6). Comparar
#    só vizinhos deixaria passar 4832 vs 4238.


# --- Conferência dos três números ------------------------------------
#
# 4832: dígitos 4,8,3,2 | soma 17 | produto 192 | maior 8 | menor 2
#       invertido 2384 | par: sim | múltiplo de 3: 17%3=2, não
#       capicua: 4832 != 2384, não | todos diferentes: sim
#
# 1221: dígitos 1,2,2,1 | soma 6 | produto 4 | maior 2 | menor 1
#       invertido 1221 | par: NÃO (termina em 1) | múltiplo de 3:
#       6%3=0, sim | capicua: 1221 == 1221, SIM | todos diferentes: não
#
#       Repare: todo capicua de 4 dígitos que começa com dígito ímpar
#       termina com o mesmo dígito ímpar — logo é ímpar. Capicua e par
#       só coincidem quando o primeiro dígito é par.
#
# 7777: dígitos 7,7,7,7 | soma 28 | produto 2401 | maior 7 | menor 7
#       invertido 7777 | par: não | múltiplo de 3: 28%3=1, não
#       capicua: SIM | todos diferentes: NÃO


# --- Solução do desafio dentro do desafio ----------------------------
# Depois dos módulos 05 e 06, tudo isto encolhe drasticamente:
#
#   digitos = [int(d) for d in str(numero)]
#
#   soma = sum(digitos)
#   maior = max(digitos)
#   menor = min(digitos)
#   invertido = int(str(numero)[::-1])
#   e_capicua = str(numero) == str(numero)[::-1]
#   todos_diferentes = len(set(digitos)) == len(digitos)
#
#   produto = 1
#   for d in digitos:
#       produto *= d
#
# Cerca de 40 linhas viram 8. E — o mais importante — a versão nova
# funciona para um número de QUALQUER tamanho, enquanto esta só serve
# para exatamente quatro dígitos.
#
# Guarde este arquivo e reabra depois do módulo 06. A diferença entre
# os dois é a melhor medida do que você aprendeu.
