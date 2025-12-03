"""
=============================
OPERADORES LÓGICOS
=============================
Este arquivo demonstra os operadores lógicos em Python
"""

print("=== OPERADORES LÓGICOS ===")

# =============================
# OPERADOR AND (E)
# =============================
print("=== OPERADOR AND ===")
print("Retorna True apenas quando AMBAS as condições são verdadeiras")

# Exemplos básicos
print(f"True and True: {True and True}")      # True
print(f"True and False: {True and False}")    # False
print(f"False and True: {False and True}")    # False
print(f"False and False: {False and False}")  # False
print()

# Exemplo prático: verificar se pode dirigir
idade = 20
tem_carteira = True
pode_dirigir = idade >= 18 and tem_carteira
print(f"Idade: {idade}, Tem carteira: {tem_carteira}")
print(f"Pode dirigir: {pode_dirigir}")
print()

# =============================
# OPERADOR OR (OU)
# =============================
print("=== OPERADOR OR ===")
print("Retorna True quando PELO MENOS UMA das condições é verdadeira")

print(f"True or True: {True or True}")        # True
print(f"True or False: {True or False}")      # True
print(f"False or True: {False or True}")      # True
print(f"False or False: {False or False}")    # False
print()

# Exemplo prático: desconto especial
eh_cliente_vip = False
compra_acima_100 = True
tem_desconto = eh_cliente_vip or compra_acima_100
print(f"Cliente VIP: {eh_cliente_vip}, Compra > 100: {compra_acima_100}")
print(f"Tem desconto: {tem_desconto}")
print()

# =============================
# OPERADOR NOT (NÃO)
# =============================
print("=== OPERADOR NOT ===")
print("Inverte o valor lógico")

print(f"not True: {not True}")      # False
print(f"not False: {not False}")    # True
print()

# Exemplo prático: verificar se não está logado
usuario_logado = False
precisa_fazer_login = not usuario_logado
print(f"Usuário logado: {usuario_logado}")
print(f"Precisa fazer login: {precisa_fazer_login}")
print()

# =============================
# COMBINANDO OPERADORES
# =============================
print("=== COMBINANDO OPERADORES ===")

# Sistema de acesso a um clube
idade_usuario = 25
eh_socio = True
tem_acompanhante = False
eh_fim_semana = True

# Regras complexas de acesso
pode_entrar = (idade_usuario >= 18 and eh_socio) or (
    eh_fim_semana and not tem_acompanhante)

print(f"Idade: {idade_usuario}")
print(f"É sócio: {eh_socio}")
print(f"Tem acompanhante: {tem_acompanhante}")
print(f"É fim de semana: {eh_fim_semana}")
print(f"Pode entrar no clube: {pode_entrar}")
print()

# =============================
# PRECEDÊNCIA DOS OPERADORES
# =============================
print("=== PRECEDÊNCIA ===")
print("Ordem: not > and > or")

resultado1 = True or False and False    # True or (False and False) = True
resultado2 = (True or False) and False  # (True or False) and False = False

print(f"True or False and False = {resultado1}")
print(f"(True or False) and False = {resultado2}")
print()

# Com not
resultado3 = not True and False    # (not True) and False = False
resultado4 = not (True and False)  # not (True and False) = True

print(f"not True and False = {resultado3}")
print(f"not (True and False) = {resultado4}")
print()

# =============================
# EXEMPLOS PRÁTICOS AVANÇADOS
# =============================
print("=== EXEMPLOS PRÁTICOS ===")

# Sistema de aprovação em curso
nota_prova = 7.5
frequencia = 85
trabalho_entregue = True

# Critérios de aprovação
aprovado = nota_prova >= 6.0 and frequencia >= 75 and trabalho_entregue

print(f"Nota da prova: {nota_prova}")
print(f"Frequência: {frequencia}%")
print(f"Trabalho entregue: {trabalho_entregue}")
print(f"Aprovado: {aprovado}")
print()

# Sistema de alerta meteorológico
temperatura = 35
umidade = 20
vento_forte = True

# Condições de risco
risco_incendio = temperatura > 30 and umidade < 30
risco_tempestade = vento_forte and umidade > 80
alerta_geral = risco_incendio or risco_tempestade

print(f"Temperatura: {temperatura}°C")
print(f"Umidade: {umidade}%")
print(f"Vento forte: {vento_forte}")
print(f"Risco de incêndio: {risco_incendio}")
print(f"Risco de tempestade: {risco_tempestade}")
print(f"Alerta geral: {alerta_geral}")
