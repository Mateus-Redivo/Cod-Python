def eh_cliente_ativo(cliente):
    return cliente[0]


def eh_cliente_premium(cliente):
    return cliente[1] == 'premium'


def produto_esta_nas_configuracoes(produto, configuracoes):
    return produto[0] in configuracoes[0]


def produto_atende_valor_minimo(produto, configuracoes):
    return produto[1] > configuracoes[1]


def calcular_desconto(cliente):
    anos_cliente = cliente[2]
    compras_total = cliente[3]

    if anos_cliente > 5:
        return 0.2
    elif anos_cliente > 3:
        return 0.15
    elif anos_cliente > 1:
        return 0.1
    elif compras_total > 10:
        return 0.05
    else:
        return 0


def aplicar_desconto(produto, desconto):
    produto[2] = produto[1] * (1 - desconto)


def deve_incluir_produto_alternativo(opcoes, indice_cliente):
    return opcoes[1] and indice_cliente % 2 == 0


def processar_produto(produto, cliente, configuracoes, opcoes):
    if produto_esta_nas_configuracoes(produto, configuracoes):
        if produto_atende_valor_minimo(produto, configuracoes):
            if opcoes[0]:  # aplicar desconto
                desconto = calcular_desconto(cliente)
                aplicar_desconto(produto, desconto)
            return produto
    return None


def processar_dados_cliente(clientes, configuracoes, opcoes):
    resultados = []

    for indice, cliente in enumerate(clientes):
        if not eh_cliente_ativo(cliente):
            continue

        if not eh_cliente_premium(cliente):
            continue

        produtos = cliente[4]
        for produto in produtos:
            produto_processado = processar_produto(
                produto, cliente, configuracoes, opcoes)

            if produto_processado:
                resultados.append(produto_processado)
            elif deve_incluir_produto_alternativo(opcoes, indice):
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
