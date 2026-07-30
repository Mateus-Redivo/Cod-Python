"""
Gabarito — Módulo 07, Exercício 02: Validador de cadastro

Enunciado:
  modulo-07-strings/exercicios/EXERCICIO-02-validador-de-cadastro.md

Como executar:
  python validador_de_cadastro.py
"""

LARGURA_VALOR = 26

# --- 1. ENTRADA: strip() já na leitura -------------------------------
nome = input("Nome completo: ").strip()
email = input("E-mail: ").strip()
telefone = input("Telefone: ").strip()


# --- 2. VALIDAÇÃO DO NOME --------------------------------------------
partes_do_nome = nome.split()

# split() + join() normaliza os espaços INTERNOS. O .strip() só limpa
# as pontas: "maria  DA silva" continuaria com dois espaços no meio.
# Como split() ignora espaços repetidos, juntar de volta com um único
# espaço resolve. Só depois disso vale aplicar o .title().
nome_formatado = " ".join(partes_do_nome).title()

if len(nome) == 0:
    nome_ok = False
    erro_nome = "campo vazio"
elif len(partes_do_nome) < 2:
    nome_ok = False
    erro_nome = "informe nome e sobrenome"
else:
    nome_ok = True
    erro_nome = ""


# --- 3. VALIDAÇÃO DO E-MAIL ------------------------------------------
email_formatado = email.lower()

# A ordem dos testes importa: só dá para dividir pelo "@" depois de
# saber que existe exatamente um.
if email_formatado.count("@") == 0:
    email_ok = False
    erro_email = "falta o @"
elif email_formatado.count("@") > 1:
    email_ok = False
    erro_email = "mais de um @"
else:
    antes, depois = email_formatado.split("@")

    if len(antes) == 0:
        email_ok = False
        erro_email = "falta o nome antes do @"
    elif len(depois) == 0:
        email_ok = False
        erro_email = "falta o domínio depois do @"
    elif "." not in depois:
        email_ok = False
        erro_email = "o domínio precisa de um ponto"
    else:
        email_ok = True
        erro_email = ""


# --- 4. VALIDAÇÃO DO TELEFONE ----------------------------------------
# Cada replace devolve uma string nova, que recebe o próximo replace.
telefone_limpo = telefone.replace(" ", "").replace("(", "").replace(")", "").replace("-", "")

if not telefone_limpo.isdigit():
    telefone_ok = False
    erro_telefone = "só pode conter números"
elif len(telefone_limpo) < 10 or len(telefone_limpo) > 11:
    telefone_ok = False
    erro_telefone = "precisa ter 10 ou 11 dígitos"
else:
    telefone_ok = True
    erro_telefone = ""


# --- 5. RESUMO -------------------------------------------------------
print()
print("===== VALIDAÇÃO =====")

if nome_ok:
    print(f"Nome:     {nome_formatado:<{LARGURA_VALOR}}[OK]")
else:
    print(f"Nome:     {nome_formatado:<{LARGURA_VALOR}}[ERRO] {erro_nome}")

if email_ok:
    print(f"E-mail:   {email_formatado:<{LARGURA_VALOR}}[OK]")
else:
    print(f"E-mail:   {email_formatado:<{LARGURA_VALOR}}[ERRO] {erro_email}")

if telefone_ok:
    print(f"Telefone: {telefone_limpo:<{LARGURA_VALOR}}[OK]")
else:
    print(f"Telefone: {telefone_limpo:<{LARGURA_VALOR}}[ERRO] {erro_telefone}")

print()

# O "and" do módulo 02: só é válido se TODOS passaram.
cadastro_valido = nome_ok and email_ok and telefone_ok

if cadastro_valido:
    print("Cadastro válido.")
else:
    print("Cadastro inválido.")


# --- Por que assim -------------------------------------------------
# 1. O .strip() acontece na LEITURA, não depois. Assim nenhuma
#    validação seguinte precisa se preocupar com espaço sobrando —
#    o dado já entra limpo no programa. Limpar cedo é mais barato do
#    que lembrar de limpar em cada uso.
#
# 2. Cada campo guarda DUAS coisas: um bool ("passou?") e um texto
#    ("por que não?"). Isso permite uma mensagem específica por erro,
#    em vez de um genérico "dados inválidos" que não ajuda ninguém a
#    consertar.
#
# 3. A ordem dos testes do e-mail não é arbitrária. O split("@") só
#    é seguro DEPOIS de confirmar que existe exatamente um "@" —
#    com dois, o split devolveria três partes e o desempacotamento
#    "antes, depois = ..." quebraria com ValueError.
#
#    Testar o caso mais grosseiro primeiro e ir refinando é o padrão
#    de toda validação em cadeia.
#
# 4. Os replace encadeados removem um caractere por vez. Fica
#    repetitivo, e é o preço de não usar recursos que a trilha ainda
#    não apresentou. Com o módulo 08 (funções) isso viraria uma
#    função "limpar_telefone" chamada uma vez.
#
# 5. isdigit() é testado ANTES do tamanho. Se o usuário digitar
#    "abcdefghij", ele tem 10 caracteres — passaria no teste de
#    tamanho e seria aceito como telefone. A ordem protege.
#
# 6. "cadastro_valido = nome_ok and email_ok and telefone_ok" é o
#    módulo 02 aparecendo em código real: três condições que precisam
#    ser verdadeiras ao mesmo tempo pedem "and".


# --- Conferência ----------------------------------------------------
# Entrada boa:
#   "  maria  DA silva  " -> strip -> "maria  DA silva"
#                         -> split -> ['maria','DA','silva'] (3 partes, ok)
#                         -> join  -> "maria DA silva"  (espaço duplo sumiu)
#                         -> title -> "Maria Da Silva"
#
#   Sem o passo do join, a saída sairia "Maria  Da Silva", com dois
#   espaços — porque .strip() limpa só as pontas e .title() não mexe
#   em espaçamento. Esse é o tipo de detalhe que só aparece quando
#   você testa com uma entrada de verdade, digitada por gente.
#
#   "MARIA@Email.COM"     -> lower -> "maria@email.com"
#                         -> count("@") = 1, antes="maria",
#                            depois="email.com" tem "." -> ok
#
#   "(45) 99999-1234"     -> replaces -> "45999991234"
#                         -> isdigit() True, 11 dígitos -> ok
#
# Repare que o .title() transforma "DA" em "Da". Para nomes com
# preposição isso é discutível — "Maria da Silva" seria o correto em
# português. Corrigir isso exigiria uma lista de exceções ("da",
# "de", "dos"...), o que já é bem mais trabalho do que parece.


# --- Solução do desafio opcional ------------------------------------
# Hoje o programa avisa e desiste. Com o while do módulo 05, ele
# insistiria até o dado ficar bom:
#
#   nome = input("Nome completo: ").strip()
#   while len(nome.split()) < 2:
#       print("Informe nome e sobrenome.")
#       nome = input("Nome completo: ").strip()
#
# É o mesmo par "ler antes / ler dentro" da validação de notas do
# módulo 05. A diferença é que agora a condição de parada envolve
# split() e len() em vez de uma comparação numérica — mas a estrutura
# é idêntica.
#
# E note o que isso muda no desenho do programa: as variáveis
# "nome_ok" e "erro_nome" deixariam de ser necessárias, porque o
# programa nunca seguiria adiante com um dado ruim.
