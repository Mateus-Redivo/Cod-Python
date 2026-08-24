"""
Gabarito — Módulo 07, Exercício 03: Cifra de César

Enunciado:
  modulo-07-strings/exercicios/EXERCICIO-03-cifra-de-cesar.md

Como executar:
  python cifra_de_cesar.py
"""

LETRAS_NO_ALFABETO = 26
BASE_MAIUSCULA = ord("A")       # 65
BASE_MINUSCULA = ord("a")       # 97


def cifrar(texto, deslocamento):
    """Desloca cada letra, preservando caixa e deixando o resto intacto."""
    resultado = ""

    for caractere in texto:
        if "A" <= caractere <= "Z":
            base = BASE_MAIUSCULA
        elif "a" <= caractere <= "z":
            base = BASE_MINUSCULA
        else:
            # Não é letra: espaço, pontuação, número, acento.
            resultado += caractere
            continue

        # Os três passos. A ordem importa:
        posicao = ord(caractere) - base                             # 0..25
        nova_posicao = (posicao + deslocamento) % LETRAS_NO_ALFABETO
        resultado += chr(nova_posicao + base)

    return resultado


def decifrar(texto, deslocamento):
    """Cifrar no sentido contrário é o mesmo que cifrar com 26 - n."""
    return cifrar(texto, LETRAS_NO_ALFABETO - deslocamento)


# --- 1. ENTRADA -------------------------------------------------------
mensagem = input("Mensagem: ")

deslocamento = int(input("Deslocamento (1-25): "))
while deslocamento < 1 or deslocamento > 25:
    print("  O deslocamento deve estar entre 1 e 25.")
    deslocamento = int(input("Deslocamento (1-25): "))

# --- 2. CIFRAR E DECIFRAR --------------------------------------------
cifrada = cifrar(mensagem, deslocamento)
decifrada = decifrar(cifrada, deslocamento)

print()
print(f"Original:  {mensagem}")
print(f"Cifrada:   {cifrada}")
print(f"Decifrada: {decifrada}")
print()

# --- 3. TESTE DOS 25 DESLOCAMENTOS ------------------------------------
passaram = 0
for teste in range(1, 26):
    if decifrar(cifrar(mensagem, teste), teste) == mensagem:
        passaram += 1

print(f"Teste dos 25 deslocamentos: {passaram}/25 passaram.")


# --- Por que assim -------------------------------------------------
# 1. Os três passos, na ordem certa:
#
#      posicao      = ord(letra) - base    -> traz para a faixa 0..25
#      nova_posicao = (posicao + n) % 26   -> desloca e dá a volta
#      nova_letra   = chr(nova + base)     -> devolve para a tabela
#
#    Aplicar o "% 26" direto sobre o ord() não funciona: ord("A") é
#    65, e 65 % 26 = 13, que não significa nada. É preciso zerar a
#    origem antes e restaurá-la depois.
#
# 2. A comparação de faixa usa os próprios caracteres:
#
#      if "A" <= caractere <= "Z":
#
#    Funciona porque strings se comparam pela tabela de caracteres —
#    a mesma propriedade que fazia "Zebra" < "ana" no módulo 02.
#    Poderia ser "if caractere.isupper()", que lê melhor; escolhi a
#    comparação para deixar visível que tudo aqui é aritmética de
#    posições.
#
# 3. O "continue" no else trata o caso "não é letra": acrescenta o
#    caractere como está e pula para o próximo. Espaço, vírgula e
#    número passam intactos, como o enunciado pede.
#
# 4. "decifrar" não tem lógica própria: cifrar com 26 - n desfaz o
#    deslocamento de n, porque (x + n + 26 - n) % 26 = x. Escrever uma
#    segunda função de deslocamento inverso seria duplicar código com
#    chance de divergir.
#
# 5. O resultado é montado com "resultado += caractere", criando uma
#    string nova a cada volta — porque string é IMUTÁVEL e não dá
#    para alterar no lugar. Para textos longos isso é ineficiente
#    (existe o "".join(), mais rápido), mas para uma mensagem é
#    irrelevante e assim fica mais claro.


# --- Conferência ------------------------------------------------------
# "PYTHON" com deslocamento 3:
#   P(15) + 3 = 18 -> S
#   Y(24) + 3 = 27 % 26 = 1  -> B     <- aqui o % 26 deu a volta
#   T(19) + 3 = 22 -> W
#   H(7)  + 3 = 10 -> K
#   O(14) + 3 = 17 -> R
#   N(13) + 3 = 16 -> Q
#   Resultado: SBWKRQ  ✔ bate com o enunciado
#
# "Z" + 3: Z(25) + 3 = 28 % 26 = 2 -> C  ✔
# "z" + 3: mesma conta, base minúscula -> c  ✔


# --- Sobre acentos ----------------------------------------------------
# Letras acentuadas NÃO são cifradas: "ç" e "ã" caem no else e passam
# intactas. Isso é uma limitação honesta desta implementação, e não um
# bug escondido — a cifra de César clássica trabalha com o alfabeto de
# 26 letras.
#
# Cifrá-las exigiria decidir onde encaixá-las no alfabeto, e não há
# resposta padrão. Repare no efeito colateral: uma mensagem cifrada
# que ainda mostra os acentos entrega informação sobre o texto
# original — mais um motivo para esta cifra não servir para nada
# sério.


# --- Solução do desafio dentro do desafio ----------------------------
# Modo "quebrar": mostrar as 25 possibilidades.
#
#   for chave in range(1, 26):
#       print(f"{chave:2}: {decifrar(cifrada, chave)}")
#
# Com 25 chaves possíveis, a cifra de César cai em segundos — por isso
# ela é material didático, não segurança de verdade.
#
# E a pergunta do enunciado: como o programa escolheria sozinho?
#
# Por ANÁLISE DE FREQUÊNCIA. Em português, "a" e "e" aparecem em torno
# de 14% e 12% do texto, enquanto "w" e "k" quase não aparecem. O
# programa poderia:
#
#   1. decifrar com cada uma das 25 chaves
#   2. contar a frequência das letras em cada resultado
#   3. comparar com a frequência esperada do português
#   4. escolher a decifragem cuja distribuição mais se parece
#
# É a mesma técnica que quebrou cifras reais por séculos — e o motivo
# de a criptografia moderna não se basear em substituição de letras.
