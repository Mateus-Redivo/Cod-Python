def processar_dados_cliente(clientes, configuracoes, opcoes):
    resultados = []
    for i, cliente in enumerate(clientes):
        if cliente[0]:  # ativo
            if cliente[1] == 'premium':
                for produto in cliente[4]:
                    if produto[0] in configuracoes[0]:
                        if produto[1] > configuracoes[1]:
                            if opcoes[0]:
                                desconto = 0
                                if cliente[2] > 5:
                                    desconto = 0.2
                                elif cliente[2] > 3:
                                    desconto = 0.15
                                elif cliente[2] > 1:
                                    desconto = 0.1
                                else:
                                    if cliente[3] > 10:
                                        desconto = 0.05
                                produto[2] = produto[1] * \
                                    (1 - desconto)
                            resultados.append(produto)
                    elif opcoes[1] and i % 2 == 0:
                        resultados.append(produto)
    return resultados


if __name__ == "__main__":
    clientes_teste = [
        [
            True,
            'premium',
            6,
            15,
            [
                ['eletronicos', 1000, None],
                ['livros', 50, None]
            ]
        ]
    ]

    configuracoes_teste = [
        ['eletronicos', 'casa'],
        500
    ]

    opcoes_teste = [
        True,
        False
    ]

    resultado = processar_dados_cliente(
        clientes_teste, configuracoes_teste, opcoes_teste)
    print("Resultado do teste:")
    print(resultado)
