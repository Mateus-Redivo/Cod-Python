def calcular_premio_seguro(dados_cliente, tipo_cobertura, historico_condutor):
    """
    Calcula o prêmio do seguro baseado no perfil do cliente, cobertura e histórico.

    dados_cliente: [idade, genero, possui_licenca, casado, possui_filhos, anos_fidelidade]
    tipo_cobertura: [tipo_cobertura, valor_franquia]
    historico_condutor: [numero_acidentes, numero_violacoes]

    Retorna: Valor do prêmio calculado
    """
    PREMIO_BASE = 500

    # Extração dos dados do cliente para melhor legibilidade
    idade = dados_cliente[0]
    genero = dados_cliente[1]
    possui_licenca = dados_cliente[2]
    casado = dados_cliente[3]
    possui_filhos = dados_cliente[4]
    anos_fidelidade = dados_cliente[5]

    # Extração dos dados de cobertura
    tipo_cobertura_seguro = tipo_cobertura[0]
    valor_franquia = tipo_cobertura[1]

    # Extração do histórico
    numero_acidentes = historico_condutor[0]
    numero_violacoes = historico_condutor[1]

    # Cálculo do fator de risco
    fator_risco = calcular_fator_risco_cliente(
        idade, genero, possui_licenca, numero_acidentes, numero_violacoes,
        tipo_cobertura_seguro, casado, possui_filhos
    )

    # Cálculo do prêmio base
    premio_final = PREMIO_BASE * fator_risco

    # Aplicação de desconto por fidelidade
    premio_final = aplicar_desconto_fidelidade(premio_final, anos_fidelidade)

    # Aplicação de desconto por franquia
    premio_final = aplicar_desconto_franquia(premio_final, valor_franquia)

    return premio_final


def calcular_fator_risco_cliente(idade, genero, possui_licenca, acidentes, violacoes,
                                 tipo_cobertura, casado, possui_filhos):
    """
    Calcula o fator de risco baseado no perfil do cliente.

    Retorna: Fator multiplicador de risco
    """
    # Perfil de baixo risco: idade adequada, licenciado, sem acidentes
    if eh_perfil_baixo_risco(idade, possui_licenca, acidentes, tipo_cobertura):
        return 1.0

    # Jovem do sexo masculino com violações
    elif idade < 25 and genero == 'masculino' and violacoes > 0:
        return 2.5

    # Jovem do sexo feminino com violações
    elif idade < 25 and genero == 'feminino' and violacoes > 0:
        return 2.0

    # Idoso com histórico problemático
    elif idade >= 65 and (acidentes > 0 or violacoes > 2):
        return calcular_fator_risco_idoso(tipo_cobertura)

    # Muitos acidentes
    elif acidentes > 2:
        return calcular_fator_risco_acidentes(violacoes)

    # Perfil padrão com possíveis descontos familiares
    else:
        return calcular_fator_risco_familia(casado, possui_filhos)


def eh_perfil_baixo_risco(idade, possui_licenca, acidentes, tipo_cobertura):
    """Verifica se o cliente se enquadra no perfil de baixo risco."""
    idade_adequada = (25 <= idade < 65) or (
        idade >= 65 and tipo_cobertura != 'completo')
    sem_acidentes = acidentes == 0

    return idade_adequada and possui_licenca and sem_acidentes


def calcular_fator_risco_idoso(tipo_cobertura):
    """Calcula fator de risco para clientes idosos."""
    FATOR_COBERTURA_COMPLETA = 2.8
    FATOR_COBERTURA_COLISAO = 2.5
    FATOR_COBERTURA_BASICA = 2.0

    if tipo_cobertura == 'completo':
        return FATOR_COBERTURA_COMPLETA
    elif tipo_cobertura == 'colisao':
        return FATOR_COBERTURA_COLISAO
    else:
        return FATOR_COBERTURA_BASICA


def calcular_fator_risco_acidentes(violacoes):
    """Calcula fator de risco baseado no número de acidentes e violações."""
    FATOR_ALTO_RISCO = 3.0
    FATOR_MEDIO_ALTO = 2.7
    FATOR_MEDIO = 2.3

    if violacoes > 3:
        return FATOR_ALTO_RISCO
    elif violacoes > 1:
        return FATOR_MEDIO_ALTO
    else:
        return FATOR_MEDIO


def calcular_fator_risco_familia(casado, possui_filhos):
    """Calcula fator de risco considerando situação familiar."""
    DESCONTO_FAMILIA_COMPLETA = 0.9
    DESCONTO_CASADO = 0.95
    FATOR_PADRAO = 1.2

    if casado and possui_filhos:
        return DESCONTO_FAMILIA_COMPLETA
    elif casado and not possui_filhos:
        return DESCONTO_CASADO
    else:
        return FATOR_PADRAO


def aplicar_desconto_fidelidade(premio, anos_fidelidade):
    """Aplica desconto baseado nos anos de fidelidade."""
    DESCONTO_FIDELIDADE_ALTA = 0.9  # 10% desconto
    DESCONTO_FIDELIDADE_MEDIA = 0.95  # 5% desconto

    if anos_fidelidade > 5:
        return premio * DESCONTO_FIDELIDADE_ALTA
    elif anos_fidelidade > 3:
        return premio * DESCONTO_FIDELIDADE_MEDIA
    else:
        return premio


def aplicar_desconto_franquia(premio, valor_franquia):
    """Aplica desconto baseado no valor da franquia."""
    DESCONTO_FRANQUIA_ALTA = 0.85  # 15% desconto
    DESCONTO_FRANQUIA_MEDIA = 0.9   # 10% desconto

    if valor_franquia > 1000:
        return premio * DESCONTO_FRANQUIA_ALTA
    elif valor_franquia > 500:
        return premio * DESCONTO_FRANQUIA_MEDIA
    else:
        return premio


if __name__ == "__main__":
    # Teste do código refatorado
    cliente_teste = [
        30,           # idade
        'masculino',  # genero
        True,         # possui_licenca
        True,         # casado
        True,         # possui_filhos
        6             # anos_fidelidade
    ]

    cobertura_teste = [
        'completo',   # tipo_cobertura
        1200          # valor_franquia
    ]

    historico_teste = [
        0,  # numero_acidentes
        0   # numero_violacoes
    ]

    resultado = calcular_premio_seguro(
        cliente_teste, cobertura_teste, historico_teste
    )

    print("Resultado do teste:")
    print(f"Prêmio calculado: R$ {resultado:.2f}")

# Estrutura dos parâmetros (mantida para compatibilidade):
# dados_cliente: [idade, genero, possui_licenca, casado, possui_filhos, anos_fidelidade]
# tipo_cobertura: [tipo_cobertura, valor_franquia]
# historico_condutor: [numero_acidentes, numero_violacoes]
