def calcular_premio_seguro(cliente, cobertura, historico):
    premio_base = 500

    if ((cliente['idade'] > 25 and cliente['idade'] < 65) or
            (cliente['idade'] >= 65 and cobertura['tipo'] != 'completo')) and \
            cliente['possui_licenca'] and not historico['acidentes']:
        fator_risco = 1.0
    elif cliente['idade'] < 25 and cliente['genero'] == 'masculino' and historico['violacoes'] > 0:
        fator_risco = 2.5
    elif cliente['idade'] < 25 and cliente['genero'] == 'feminino' and historico['violacoes'] > 0:
        fator_risco = 2.0
    elif cliente['idade'] >= 65 and (historico['acidentes'] > 0 or historico['violacoes'] > 2):
        if cobertura['tipo'] == 'completo':
            fator_risco = 2.8
        elif cobertura['tipo'] == 'colisao':
            fator_risco = 2.5
        else:
            fator_risco = 2.0
    elif historico['acidentes'] > 2:
        if historico['violacoes'] > 3:
            fator_risco = 3.0
        elif historico['violacoes'] > 1:
            fator_risco = 2.7
        else:
            fator_risco = 2.3
    else:
        if cliente['casado'] and cliente['possui_filhos']:
            fator_risco = 0.9
        elif cliente['casado'] and not cliente['possui_filhos']:
            fator_risco = 0.95
        else:
            fator_risco = 1.2

    premio_final = premio_base * fator_risco

    if cliente['anos_fidelidade'] > 5:
        premio_final *= 0.9
    elif cliente['anos_fidelidade'] > 3:
        premio_final *= 0.95

    if cobertura['franquia'] > 1000:
        premio_final *= 0.85
    elif cobertura['franquia'] > 500:
        premio_final *= 0.9

    return premio_final
