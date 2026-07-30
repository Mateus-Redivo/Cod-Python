def criar_avaliacao_tradicional():
    """Factory para avaliação tradicional"""
    return {
        # [prova, trabalho, participacao, bonus]
        'pesos': [0.4, 0.5, 0.3, 0.0],
        'nota_minima': 60,
        'bonus_maximo': 5
    }


def criar_avaliacao_moderna():
    """Factory para avaliação moderna"""
    return {
        'pesos': [0.3, 0.4, 0.2, 0.1],  # Mais peso em trabalhos
        'nota_minima': 70,
        'bonus_maximo': 10
    }


def criar_avaliacao_intensiva():
    """Factory para curso intensivo"""
    return {
        'pesos': [0.6, 0.2, 0.1, 0.1],  # Mais peso em provas
        'nota_minima': 75,
        'bonus_maximo': 8
    }


# Factory principal (Factory Pattern)
TIPOS_AVALIACAO = {
    'tradicional': criar_avaliacao_tradicional,
    'moderna': criar_avaliacao_moderna,
    'intensiva': criar_avaliacao_intensiva
}


def criar_configuracao_avaliacao(tipo):
    """Factory method para criar configurações"""
    if tipo in TIPOS_AVALIACAO:
        return TIPOS_AVALIACAO[tipo]()
    return criar_avaliacao_tradicional()  # Padrão
