# Diferentes estratégias de cálculo de bônus
def bonus_participacao(dados_estudante):
    """Bônus baseado em participação"""
    participacao = dados_estudante[3]  # índice para participação
    return min(participacao * 0.1, 5.0)


def bonus_projeto(dados_estudante):
    """Bônus baseado em projetos extras"""
    projetos = dados_estudante[4] if len(dados_estudante) > 4 else 0
    return projetos * 2.0


def bonus_frequencia(dados_estudante):
    """Bônus baseado em frequência"""
    frequencia = dados_estudante[5] if len(dados_estudante) > 5 else 90
    return 3.0 if frequencia >= 95 else 0


# Dicionário com estratégias de bônus (Strategy Pattern)
ESTRATEGIAS_BONUS = {
    'participacao': bonus_participacao,
    'projeto': bonus_projeto,
    'frequencia': bonus_frequencia
}


def calcular_bonus_com_strategy(dados_estudante, tipos_bonus):
    """Aplica múltiplas estratégias de bônus"""
    bonus_total = 0
    for tipo in tipos_bonus:
        if tipo in ESTRATEGIAS_BONUS:
            bonus_total += ESTRATEGIAS_BONUS[tipo](dados_estudante)
    return min(bonus_total, 10.0)  # Limite máximo de bônus
