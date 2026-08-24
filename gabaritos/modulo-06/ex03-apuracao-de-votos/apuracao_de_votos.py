"""
Gabarito — Módulo 06, Exercício 03: Apuração de votos

Enunciado:
  modulo-06-listas/exercicios/EXERCICIO-03-apuracao-de-votos.md

Como executar:
  python apuracao_de_votos.py
"""

VOTO_BRANCO = 0
VOTO_ENCERRAR = -1
LARGURA = 40

candidatos = ["Ana", "Bruno", "Carla", "Diego"]
votos = [0, 0, 0, 0]

brancos = 0
nulos = 0

# --- 1. APURAÇÃO ------------------------------------------------------
while True:
    voto = int(input("Voto (1-4, 0=branco, -1=encerra): "))

    if voto == VOTO_ENCERRAR:
        break

    if voto == VOTO_BRANCO:
        brancos += 1
    elif 1 <= voto <= len(candidatos):
        # O usuário digita 1..4; a lista usa 0..3. A conversão -1
        # acontece AQUI, num lugar só.
        votos[voto - 1] += 1
    else:
        nulos += 1
        print("  Voto NULO registrado.")

# --- 2. TOTAIS --------------------------------------------------------
validos = sum(votos)
total_geral = validos + brancos + nulos

print()
print("=" * LARGURA)
print(f"{'APURAÇÃO ENCERRADA':^{LARGURA}}")
print("=" * LARGURA)

if validos == 0:
    print("Nenhum voto válido foi registrado.")
    print(f"Brancos: {brancos} | Nulos: {nulos} | Total: {total_geral}")
    print("=" * LARGURA)
else:
    # --- 3. TABELA ----------------------------------------------------
    print(f"{'Candidato':<14}{'Votos':>7}{'% válidos':>13}")
    for i in range(len(candidatos)):
        percentual = votos[i] / validos * 100
        print(f"{candidatos[i]:<14}{votos[i]:>7}{percentual:>13.2f}")

    print("-" * LARGURA)
    print(f"{'Votos válidos:':<18}{validos:>4}")
    print(f"{'Brancos:':<18}{brancos:>4}")
    print(f"{'Nulos:':<18}{nulos:>4}")
    print(f"{'Total geral:':<18}{total_geral:>4}")
    print("=" * LARGURA)

    # --- 4. VENCEDOR E EMPATE ----------------------------------------
    mais_votos = max(votos)

    # Achar o maior é fácil. Descobrir QUANTOS têm esse valor exige
    # percorrer de novo — e é isso que detecta o empate.
    empatados = []
    for i in range(len(candidatos)):
        if votos[i] == mais_votos:
            empatados.append(candidatos[i])

    if len(empatados) > 1:
        nomes = ", ".join(empatados)
        print(f"EMPATE entre: {nomes} ({mais_votos} votos cada)")
    else:
        percentual_vencedor = mais_votos / validos * 100
        print(f"Vencedor: {empatados[0]} "
              f"({mais_votos} votos, {percentual_vencedor:.2f}%)")

    if mais_votos / validos > 0.5:
        print("Maioria absoluta.")
    else:
        print("Sem maioria absoluta.")

    print("=" * LARGURA)


# --- Por que assim -------------------------------------------------
# 1. Duas listas PARALELAS: candidatos[i] e votos[i] são a mesma
#    pessoa. Funciona, mas repare no incômodo — nada no código
#    garante que as duas tenham o mesmo tamanho. Se alguém
#    acrescentar um quinto candidato e esquecer o quinto zero, o
#    programa quebra ou conta errado. É exatamente o problema que o
#    módulo 09 resolve com uma matriz.
#
# 2. A conversão "voto - 1" acontece num lugar só, na linha do
#    incremento. Espalhá-la seria repetir a chance de esquecer.
#
# 3. A validação do voto usa "1 <= voto <= len(candidatos)", com
#    len() em vez do 4 fixo. Acrescentar candidato não exige mexer
#    aqui.
#
# 4. A ordem dos ifs importa: encerrar primeiro, depois branco,
#    depois voto válido, e o else pega tudo que sobrou como nulo.
#    Testar "voto válido" antes de "encerrar" faria o -1 cair no
#    nulo.
#
# 5. O empate NÃO sai do max(). O max devolve o maior VALOR (2), não
#    quantos candidatos o têm. Por isso o segundo laço, montando a
#    lista de empatados. Se ela tiver mais de um nome, houve empate.
#
#    Quem usa "votos.index(mais_votos)" pega só o PRIMEIRO empatado e
#    anuncia um vencedor que não existe — é o erro que o enunciado
#    avisa.
#
# 6. O "validos == 0" protege as três divisões (percentual da tabela,
#    do vencedor e da maioria). Sem ele, encerrar sem votos daria
#    ZeroDivisionError.
#
# 7. Maioria absoluta é "> 0.5", não ">= 0.5". Com exatos 50% não há
#    maioria — metade não é mais que a outra metade. Detalhe pequeno
#    que muda o resultado de uma eleição real.


# --- Conferência do exemplo ------------------------------------------
# Votos digitados: 1, 3, 1, 9(nulo), 0(branco), 3, -1(encerra)
#
#   Ana (1)   -> 2 votos
#   Bruno (2) -> 0
#   Carla (3) -> 2 votos
#   Diego (4) -> 0
#   válidos = 4 | brancos = 1 | nulos = 1 | total = 6
#
#   percentuais sobre VÁLIDOS: 2/4 = 50%, 0/4 = 0%
#   (repare: sobre o total geral daria 33%, o que estaria errado)
#
#   max(votos) = 2, e DOIS candidatos têm 2 -> EMPATE
#   2/4 = 0.5, que não é > 0.5 -> sem maioria absoluta


# --- Solução do desafio dentro do desafio ----------------------------
# Desempate por idade, com uma TERCEIRA lista paralela:
#
#   idades = [34, 51, 29, 45]
#
#   if len(empatados) > 1:
#       mais_velho = empatados[0]
#       maior_idade = idades[candidatos.index(empatados[0])]
#       for nome in empatados:
#           idade = idades[candidatos.index(nome)]
#           if idade > maior_idade:
#               maior_idade = idade
#               mais_velho = nome
#       print(f"EMPATE. Vence o mais velho: {mais_velho} ({maior_idade} anos)")
#
# E a resposta à pergunta: com TRÊS listas paralelas, o risco de erro
# não aumenta em 50% — aumenta muito mais. Agora são três ordens que
# precisam coincidir, e o "candidatos.index(nome)" para achar a idade
# é um remendo que só existe porque os dados foram separados.
#
# Com uma matriz do módulo 09:
#
#   candidatos = [
#       ["Ana",   34, 0],
#       ["Bruno", 51, 0],
#   ]
#
# ...nome, idade e votos viajam juntos, e a pergunta "qual a idade de
# quem empatou?" some: você já tem a linha inteira na mão.
