def calcular_premio_seguro(cliente, cobertura, historico):
    premio_base = 500

    if ((cliente[0] > 25 and cliente[0] < 65) or
            (cliente[0] >= 65 and cobertura[0] != 'completo')) and \
            cliente[2] and not historico[0]:
        fator_risco = 1.0
    elif cliente[0] < 25 and cliente[1] == 'masculino' and historico[1] > 0:
        fator_risco = 2.5
    elif cliente[0] < 25 and cliente[1] == 'feminino' and historico[1] > 0:
        fator_risco = 2.0
    elif cliente[0] >= 65 and (historico[0] > 0 or historico[1] > 2):
        if cobertura[0] == 'completo':
            fator_risco = 2.8
        elif cobertura[0] == 'colisao':
            fator_risco = 2.5
        else:
            fator_risco = 2.0
    elif historico[0] > 2:
        if historico[1] > 3:
            fator_risco = 3.0
        elif historico[1] > 1:
            fator_risco = 2.7
        else:
            fator_risco = 2.3
    else:
        if cliente[3] and cliente[4]:
            fator_risco = 0.9
        elif cliente[3] and not cliente[4]:
            fator_risco = 0.95
        else:
            fator_risco = 1.2

    premio_final = premio_base * fator_risco

    if cliente[5] > 5:
        premio_final *= 0.9
    elif cliente[5] > 3:
        premio_final *= 0.95

    if cobertura[1] > 1000:
        premio_final *= 0.85
    elif cobertura[1] > 500:
        premio_final *= 0.9

    return premio_final


if __name__ == "__main__":
    # Teste do código
    cliente_teste = [
        30,        # idade
        'masculino',  # genero
        True,      # possui_licenca
        True,      # casado
        True,      # possui_filhos
        6          # anos_fidelidade
    ]

    cobertura_teste = [
        'completo',  # tipo
        1200         # franquia
    ]

    historico_teste = [
        0,  # acidentes
        0   # violacoes
    ]

    resultado = calcular_premio_seguro(
        cliente_teste, cobertura_teste, historico_teste)
    print("Resultado do teste:")
    print(f"Prêmio calculado: R$ {resultado:.2f}")



