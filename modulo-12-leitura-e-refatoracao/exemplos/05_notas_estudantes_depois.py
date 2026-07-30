def calcular_nota_estudante(lista_estudantes, configuracoes_curso, politicas_avaliacao,
                            bonus_estudantes=None, limite_participacao=5):
    """
    Calcula a nota média dos estudantes baseado em critérios específicos.

    lista_estudantes: Lista de estudantes com dados [ativo, materia, nota, participacao, trabalho_extra]
    configuracoes_curso: [materias_permitidas, nota_minima, nota_recuperacao]
    politicas_avaliacao: [permite_recuperacao, bonus_recuperacao, bonus_participacao_extra]
    bonus_estudantes: Lista opcional de tipos de bônus por estudante
    limite_participacao: Limite mínimo de participação para bônus (padrão: 5)

    Retorna: Nota média calculada
    """
    if not lista_estudantes or len(lista_estudantes) == 0:
        return 0

    total_pontos = 0

    for indice in range(len(lista_estudantes)):
        estudante = lista_estudantes[indice]

        # Extração dos dados do estudante para melhor legibilidade
        esta_ativo = estudante[0]
        materia = estudante[1]
        nota_base = estudante[2]
        participacao = estudante[3]
        trabalho_extra = estudante[4] if len(estudante) > 4 else None

        # Verificações de elegibilidade
        if not esta_ativo:
            continue

        if not eh_materia_valida(materia, configuracoes_curso):
            continue

        if not atende_nota_minima(nota_base, configuracoes_curso):
            continue

        # Cálculo inicial dos pontos
        pontos_estudante = calcular_pontos_base(nota_base)

        # Adicionar pontos de participação
        pontos_estudante = adicionar_pontos_participacao(
            pontos_estudante, participacao)

        # Adicionar pontos de trabalho extra
        pontos_estudante = adicionar_pontos_trabalho_extra(
            pontos_estudante, trabalho_extra)

        # Aplicar bônus específico do estudante
        pontos_estudante = aplicar_bonus_estudante(
            pontos_estudante, bonus_estudantes, indice
        )

        # Limitar pontuação máxima
        pontos_estudante = min(pontos_estudante, 100)

        # Aplicar políticas de recuperação
        pontos_estudante = aplicar_politicas_recuperacao(
            pontos_estudante, nota_base, participacao,
            configuracoes_curso, politicas_avaliacao, limite_participacao
        )

        total_pontos += pontos_estudante

    # Calcular média e aplicar bônus de desempenho
    nota_media = total_pontos / len(lista_estudantes)
    nota_media = aplicar_bonus_desempenho(nota_media)

    return nota_media


def eh_materia_valida(materia, configuracoes_curso):
    """Verifica se a matéria está na lista de matérias permitidas."""
    materias_permitidas = configuracoes_curso[0]
    return materia in materias_permitidas


def atende_nota_minima(nota, configuracoes_curso):
    """Verifica se a nota atende ao critério mínimo."""
    nota_minima = configuracoes_curso[1]
    return nota >= nota_minima


def calcular_pontos_base(nota_base):
    """Retorna os pontos base igual à nota do estudante."""
    return nota_base


def adicionar_pontos_participacao(pontos_atuais, participacao):
    """
    Adiciona pontos baseado no nível de participação do estudante.

    Retorna: Pontos atualizados com bônus de participação
    """
    BONUS_PARTICIPACAO_ALTA = 15    # Mais de 10 participações
    BONUS_PARTICIPACAO_MEDIA = 10   # 6-10 participações
    BONUS_PARTICIPACAO_BAIXA = 5    # 3-5 participações

    if participacao > 10:
        return pontos_atuais + BONUS_PARTICIPACAO_ALTA
    elif participacao > 5:
        return pontos_atuais + BONUS_PARTICIPACAO_MEDIA
    elif participacao > 2:
        return pontos_atuais + BONUS_PARTICIPACAO_BAIXA
    else:
        return pontos_atuais


def adicionar_pontos_trabalho_extra(pontos_atuais, trabalho_extra):
    """
    Adiciona pontos baseado no trabalho extra realizado pelo estudante.

    Retorna: Pontos atualizados com bônus de trabalho extra
    """
    if not trabalho_extra:
        return pontos_atuais

    tipo_trabalho = trabalho_extra[0]
    nota_trabalho = trabalho_extra[1]

    if tipo_trabalho == 'projeto':
        return calcular_bonus_projeto(pontos_atuais, nota_trabalho)
    elif tipo_trabalho == 'pesquisa':
        return calcular_bonus_pesquisa(pontos_atuais, nota_trabalho)

    return pontos_atuais


def calcular_bonus_projeto(pontos_atuais, nota_projeto):
    """Calcula bônus para projetos baseado na nota obtida."""
    BONUS_PROJETO_EXCELENTE = 20  # Nota > 80
    BONUS_PROJETO_BOM = 15        # Nota > 60
    BONUS_PROJETO_BASICO = 10     # Outras notas

    if nota_projeto > 80:
        return pontos_atuais + BONUS_PROJETO_EXCELENTE
    elif nota_projeto > 60:
        return pontos_atuais + BONUS_PROJETO_BOM
    else:
        return pontos_atuais + BONUS_PROJETO_BASICO


def calcular_bonus_pesquisa(pontos_atuais, nota_pesquisa):
    """Calcula bônus para pesquisas baseado na nota obtida."""
    MULTIPLICADOR_PESQUISA = 0.3
    bonus_pesquisa = nota_pesquisa * MULTIPLICADOR_PESQUISA
    return pontos_atuais + bonus_pesquisa


def aplicar_bonus_estudante(pontos_atuais, bonus_estudantes, indice):
    """
    Aplica bônus específico do estudante baseado no tipo de bônus.

    Retorna: Pontos atualizados com bônus específico
    """
    if not bonus_estudantes or indice >= len(bonus_estudantes) or not bonus_estudantes[indice]:
        return pontos_atuais

    tipo_bonus = bonus_estudantes[indice]

    BONUS_PARTICIPACAO_EXTRA = 8
    MULTIPLICADOR_EXCELENCIA = 1.3
    MULTIPLICADOR_MELHORIA = 1.15

    if tipo_bonus == 'participacao':
        return pontos_atuais + BONUS_PARTICIPACAO_EXTRA
    elif tipo_bonus == 'excelencia':
        return pontos_atuais * MULTIPLICADOR_EXCELENCIA
    elif tipo_bonus == 'melhoria':
        return pontos_atuais * MULTIPLICADOR_MELHORIA

    return pontos_atuais


def aplicar_politicas_recuperacao(pontos_atuais, nota_base, participacao,
                                  configuracoes_curso, politicas_avaliacao,
                                  limite_participacao):
    """
    Aplica políticas de recuperação se habilitadas.

    Retorna: Pontos atualizados considerando políticas de recuperação
    """
    permite_recuperacao = politicas_avaliacao[0]
    nota_limite_recuperacao = configuracoes_curso[2]

    if not (permite_recuperacao and nota_base < nota_limite_recuperacao):
        return pontos_atuais

    # Política de bônus de recuperação
    if len(politicas_avaliacao) > 1 and politicas_avaliacao[1]:
        nota_minima = configuracoes_curso[1]
        nota_recuperacao = min(nota_base + 20, nota_minima)
        pontos_atuais = max(pontos_atuais, nota_recuperacao)

    # Política de bônus por participação extra
    elif (len(politicas_avaliacao) > 2 and
          politicas_avaliacao[2] and
          participacao > limite_participacao):
        BONUS_PARTICIPACAO_RECUPERACAO = 10
        pontos_atuais += BONUS_PARTICIPACAO_RECUPERACAO

    return pontos_atuais


def aplicar_bonus_desempenho(nota_media):
    """
    Aplica bônus de desempenho baseado na nota média obtida.

    Retorna: Nota média ajustada com bônus de desempenho
    """
    MULTIPLICADOR_DESEMPENHO_EXCELENTE = 1.05  # Nota > 95
    MULTIPLICADOR_DESEMPENHO_BOM = 1.02        # Nota > 85
    NOTA_MAXIMA = 100

    if nota_media > 95:
        return min(nota_media * MULTIPLICADOR_DESEMPENHO_EXCELENTE, NOTA_MAXIMA)
    elif nota_media > 85:
        return nota_media * MULTIPLICADOR_DESEMPENHO_BOM
    else:
        return nota_media


if __name__ == "__main__":
    # Dados de teste
    estudantes_teste = [
        # Estudante ativo com projeto
        [True, 'matematica', 75, 8, ['projeto', 85]],
        # Estudante ativo com pesquisa
        [True, 'fisica', 82, 12, ['pesquisa', 90]],
        [False, 'quimica', 60, 3, None],                 # Estudante inativo
        # Estudante com nota baixa mas alta participação
        [True, 'matematica', 45, 15, ['projeto', 70]]
    ]

    # Configurações: [matérias_permitidas, nota_mínima, nota_limite_recuperação]
    configuracoes_teste = [['matematica', 'fisica', 'quimica'], 60, 50]

    # Políticas: [permite_recuperação, bônus_recuperação, bônus_participação_extra]
    politicas_teste = [True, True, True]

    # Bônus específicos por estudante
    bonus_teste = ['excelencia', 'melhoria', None, 'participacao']

    # Execução do teste
    resultado = calcular_nota_estudante(
        estudantes_teste, configuracoes_teste, politicas_teste, bonus_teste
    )

    print(f"Nota média calculada: {resultado:.2f}")

# Estrutura dos parâmetros (mantida para compatibilidade):
# lista_estudantes: [[ativo, materia, nota, participacao, trabalho_extra], ...]
# configuracoes_curso: [materias_permitidas, nota_minima, nota_recuperacao]
# politicas_avaliacao: [permite_recuperacao, bonus_recuperacao, bonus_participacao_extra]
# bonus_estudantes: [tipo_bonus_por_estudante]
