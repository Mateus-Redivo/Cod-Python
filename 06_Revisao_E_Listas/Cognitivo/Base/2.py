def processar_dados_cliente(clientes, configuracoes, opcoes):
    resultados = []

    # Itera por cada cliente com seu índice
    for i, cliente in enumerate(clientes):
        # Verifica se o cliente está ativo (índice 0)
        if cliente[0]:  # ativo
            # Verifica se o cliente é premium (índice 1)
            if cliente[1] == 'premium':
                # Processa cada produto do cliente (índice 4)
                for produto in cliente[4]:
                    # Verifica se a categoria do produto está nas categorias permitidas
                    if produto[0] in configuracoes[0]:
                        # Verifica se o valor do produto supera o valor mínimo configurado
                        if produto[1] > configuracoes[1]:
                            # Se a opção de aplicar desconto está ativada
                            if opcoes[0]:
                                desconto = 0
                                # Calcula desconto baseado nos anos como cliente (índice 2)
                                if cliente[2] > 5:
                                    desconto = 0.2  # 20% para clientes com mais de 5 anos
                                elif cliente[2] > 3:
                                    desconto = 0.15  # 15% para clientes com mais de 3 anos
                                elif cliente[2] > 1:
                                    desconto = 0.1   # 10% para clientes com mais de 1 ano
                                else:
                                    # Para clientes novos, verifica valor gasto (índice 3)
                                    if cliente[3] > 10:
                                        desconto = 0.05  # 5% para novos clientes com alto gasto
                                # Aplica o desconto ao preço do produto (índice 2 do produto)
                                produto[2] = produto[1] * (1 - desconto)
                            # Adiciona o produto aos resultados
                            resultados.append(produto)
                    # Caso especial: se incluir_pares está ativo e o índice do cliente é par
                    elif opcoes[1] and i % 2 == 0:
                        resultados.append(produto)

    return resultados


if __name__ == "__main__":
    # Dados de teste: cliente ativo, premium, 6 anos como cliente, gastou R$15
    # com produtos de eletrônicos (R$1000) e livros (R$50)
    clientes_teste = [
        [
            True,        # cliente ativo
            'premium',   # tipo de cliente
            6,           # anos como cliente
            15,          # valor total gasto
            [            # lista de produtos
                # [categoria, preço, preço_com_desconto]
                ['eletronicos', 1000, None],
                ['livros', 50, None]
            ]
        ]
    ]

    # Configurações: categorias permitidas e valor mínimo do produto
    configuracoes_teste = [
        ['eletronicos', 'casa'],  # categorias permitidas
        500                       # valor mínimo do produto
    ]

    # Opções de processamento
    opcoes_teste = [
        True,   # aplicar desconto
        False   # incluir produtos de clientes com índice par
    ]

    # Executa o processamento dos dados de teste
    resultado = processar_dados_cliente(
        clientes_teste, configuracoes_teste, opcoes_teste)

    # Exibe os resultados do processamento
    print("Resultado do teste:")
    print(resultado)
