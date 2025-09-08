def processar_dados_cliente(clientes, configuracoes, opcoes):
    resultados = []
    for i, cliente in enumerate(clientes):
        if cliente.get('ativo', False):
            if cliente.get('assinatura') == 'premium':
                for produto in cliente.get('compras', []):
                    if produto['categoria'] in configuracoes['categorias_premium']:
                        if produto['preco'] > configuracoes['limite']:
                            if opcoes['aplicar_desconto']:
                                desconto = 0
                                if cliente['anos_fidelidade'] > 5:
                                    desconto = 0.2
                                elif cliente['anos_fidelidade'] > 3:
                                    desconto = 0.15
                                elif cliente['anos_fidelidade'] > 1:
                                    desconto = 0.1
                                else:
                                    if cliente['quantidade_compras'] > 10:
                                        desconto = 0.05
                                produto['preco_final'] = produto['preco'] * \
                                    (1 - desconto)
                            resultados.append(produto)
                    elif opcoes['incluir_todos'] and i % 2 == 0:
                        resultados.append(produto)
    return resultados
