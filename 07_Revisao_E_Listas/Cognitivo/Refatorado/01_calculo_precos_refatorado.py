def processar_dados(lista_dados, taxa_imposto=0.1, nivel_recursao=10):
    """
    lista_dados: Lista contendo números ou dicionários para processamento
    taxa_imposto: Taxa a ser aplicada nos cálculos (padrão: 0.1)
    nivel_recursao: Controla a profundidade da recursão (padrão: 10)
   
    Lista com os valores processados
    """
    resultados = []
    
    for indice in range(len(lista_dados)):
        item = lista_dados[indice]
        
        if isinstance(item, dict):
            # Processamento para itens do tipo dicionário
            valor_total = 0
            
            # Soma todos os valores de chaves que começam com 'val'
            for chave in item:
                if chave.startswith('val'):
                    valor_total += item[chave]
                elif chave == 'mult' and indice > 0:
                    # Cálculo recursivo para multiplicador
                    if nivel_recursao > 0:
                        valor_anterior = processar_dados(lista_dados[:indice], taxa_imposto, nivel_recursao-1)[0]
                        valor_total += item[chave] * valor_anterior
            
            # Aplicação de taxas e regras especiais
            if valor_total > 0:
                # Taxa diferenciada baseada na posição do item
                imposto = valor_total * taxa_imposto if indice % 3 == 0 else valor_total * (taxa_imposto/2)
                
                # Redução do valor com base no valor total
                if valor_total > 100:
                    valor_total = valor_total - imposto
                else:
                    valor_total = valor_total - (imposto/2)
                
                # Aplicação de bônus para itens especiais
                if 'special' in item and item['special']:
                    if item.get('type') == 'A':
                        valor_total *= 1.5  # Bônus de 50% para tipo A
                    elif item.get('type') == 'B':
                        valor_total *= 1.2  # Bônus de 20% para tipo B
                    else:
                        valor_total *= 1.1  # Bônus padrão de 10%
            
            resultados.append(valor_total)
        else:
            # Processamento para itens numéricos
            if item > 50:
                resultados.append(item * 0.8)  # Desconto maior para valores altos
            else:
                resultados.append(item * 0.9)  # Desconto menor para valores baixos
    
    return resultados


# Teste da função
resultado = processar_dados([30, 60, 100])
print(resultado)