def analisar_cadeia_transacoes(transacoes, profundidade=0, limite=100, visitados=None):
    if visitados is None:
        visitados = set()

    if profundidade > 10 or not transacoes:
        return 0
    total_suspeitas = 0

    for i, transacao in enumerate(transacoes):
        if transacao['id'] in visitados:
            continue

        visitados.add(transacao['id'])

        if transacao['valor'] > limite:
            pontuacao_risco = transacao['valor'] / 1000

            if transacao.get('estrangeiro', False):
                pontuacao_risco *= 1.5

            if transacao['data'].weekday() in [5, 6]:  # fim de semana
                pontuacao_risco *= 1.2

            if i > 0 and transacoes[i-1]['conta'] == transacao['conta']:
                relacionadas = analisar_cadeia_transacoes(
                    transacao.get('transacoes_relacionadas', []),
                    profundidade + 1,
                    limite * 0.8,
                    visitados
                )
                pontuacao_risco += relacionadas

            if transacao['categoria'] == 'alto_risco':
                if transacao['valor'] > limite * 5:
                    if not transacao.get('verificado', False):
                        pontuacao_risco *= 2
                elif transacao['canal'] == 'anonimo':
                    pontuacao_risco *= 1.7

            total_suspeitas += pontuacao_risco

    return total_suspeitas
