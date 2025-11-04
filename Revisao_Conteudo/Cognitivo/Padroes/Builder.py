def criar_estudante_base(nome, matricula):
    """Inicia construção do estudante (Builder Pattern)"""
    return [nome, matricula, [], [], []]  # [nome, matricula, notas, bonus, historico]

def adicionar_nota(estudante, tipo_avaliacao, nota):
    """Adiciona nota ao estudante"""
    estudante[2].append([tipo_avaliacao, nota])
    return estudante

def adicionar_bonus(estudante, tipo_bonus, valor):
    """Adiciona bônus ao estudante"""
    estudante[3].append([tipo_bonus, valor])
    return estudante

def adicionar_historico(estudante, evento, data):
    """Adiciona evento ao histórico"""
    estudante[4].append([evento, data])
    return estudante

def finalizar_estudante(estudante):
    """Finaliza e valida construção do estudante"""
    if not estudante[0] or not estudante[1]:  # Nome e matrícula obrigatórios
        raise ValueError("Nome e matrícula são obrigatórios")
    return estudante

# Exemplo de uso do Builder
def construir_estudante_completo():
    estudante = criar_estudante_base("João Silva", "2023001")
    estudante = adicionar_nota(estudante, "P1", 85)
    estudante = adicionar_nota(estudante, "T1", 90)
    estudante = adicionar_bonus(estudante, "participacao", 3)
    estudante = adicionar_historico(estudante, "matricula", "2023-03-01")
    estudante = finalizar_estudante(estudante)
    return estudante