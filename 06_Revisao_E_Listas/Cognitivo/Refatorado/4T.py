def calcular_status_pets(lista_pets, configuracoes_clinica, regras_avaliacao,
                         bonus_pets=None, limite_vacinas=3):
    """
    Calcula o status médio dos pets baseado em critérios específicos.

    lista_pets: Lista de pets com dados [ativo, especie, idade, vacinas, dono, atividade_extra]
    configuracoes_clinica: [especies_permitidas, idade_minima]
    regras_avaliacao: [permite_recuperacao, bonus_recuperacao, bonus_vacinas_extra]
    bonus_pets: Lista opcional de tipos de bônus por pet
    limite_vacinas: Limite mínimo de vacinas para bônus (padrão: 3)

    Retorna: Status médio calculado
    """
    if not lista_pets or len(lista_pets) == 0:
        return 0

    total_pontos = 0

    for indice in range(len(lista_pets)):
        pet = lista_pets[indice]

        # Extração dos dados do pet para melhor legibilidade
        esta_ativo = pet[0]
        especie = pet[1]
        idade = pet[2]
        quantidade_vacinas = pet[3]
        atividade_extra = pet[5] if len(pet) > 5 else None

        # Verificações de elegibilidade
        if not esta_ativo:
            continue

        if not eh_especie_valida(especie, configuracoes_clinica):
            continue

        if not atende_idade_minima(idade, configuracoes_clinica):
            continue

        # Cálculo inicial dos pontos
        pontos_pet = calcular_pontos_base(idade)

        # Adicionar pontos de vacinação
        pontos_pet = adicionar_pontos_vacinas(pontos_pet, quantidade_vacinas)

        # Adicionar pontos de atividade extra
        pontos_pet = adicionar_pontos_atividade_extra(
            pontos_pet, atividade_extra)

        # Aplicar bônus específico do pet
        pontos_pet = aplicar_bonus_pet(pontos_pet, bonus_pets, indice)

        # Limitar pontuação máxima
        pontos_pet = min(pontos_pet, 100)

        # Aplicar regras de recuperação
        pontos_pet = aplicar_regras_recuperacao(
            pontos_pet, idade, quantidade_vacinas,
            configuracoes_clinica, regras_avaliacao, limite_vacinas
        )

        total_pontos += pontos_pet

    # Calcular média e aplicar bônus de desempenho
    status_medio = total_pontos / len(lista_pets)
    status_medio = aplicar_bonus_desempenho(status_medio)

    return status_medio


def eh_especie_valida(especie, configuracoes_clinica):
    """Verifica se a espécie está na lista de espécies permitidas."""
    especies_permitidas = configuracoes_clinica[0]
    return especie in especies_permitidas


def atende_idade_minima(idade, configuracoes_clinica):
    """Verifica se a idade atende ao critério mínimo."""
    idade_minima = configuracoes_clinica[1]
    return idade >= idade_minima


def calcular_pontos_base(idade):
    """Retorna os pontos base igual à idade do pet."""
    return idade


def adicionar_pontos_vacinas(pontos_atuais, quantidade_vacinas):
    """
    Adiciona pontos baseado no número de vacinas do pet.

    Retorna: Pontos atualizados com bônus de vacinação
    """
    BONUS_VACINAS_ALTA = 25    # Mais de 10 vacinas
    BONUS_VACINAS_MEDIA = 15   # 6-10 vacinas
    BONUS_VACINAS_BAIXA = 8    # 3-5 vacinas

    if quantidade_vacinas > 10:
        return pontos_atuais + BONUS_VACINAS_ALTA
    elif quantidade_vacinas > 5:
        return pontos_atuais + BONUS_VACINAS_MEDIA
    elif quantidade_vacinas > 2:
        return pontos_atuais + BONUS_VACINAS_BAIXA
    else:
        return pontos_atuais


def adicionar_pontos_atividade_extra(pontos_atuais, atividade_extra):
    """
    Adiciona pontos baseado na atividade extra realizada pelo pet.

    Retorna: Pontos atualizados com bônus de atividade extra
    """
    if not atividade_extra:
        return pontos_atuais

    tipo_atividade = atividade_extra[0]
    nota_atividade = atividade_extra[1]

    if tipo_atividade == 'adestramento':
        return calcular_bonus_adestramento(pontos_atuais, nota_atividade)
    elif tipo_atividade == 'competicao':
        return calcular_bonus_competicao(pontos_atuais, nota_atividade)

    return pontos_atuais


def calcular_bonus_adestramento(pontos_atuais, nota_adestramento):
    """Calcula bônus para adestramento baseado na nota obtida."""
    BONUS_ADESTRAMENTO_EXCELENTE = 20  # Nota > 80
    BONUS_ADESTRAMENTO_BOM = 10        # Nota > 60
    BONUS_ADESTRAMENTO_BASICO = 5      # Outras notas

    if nota_adestramento > 80:
        return pontos_atuais + BONUS_ADESTRAMENTO_EXCELENTE
    elif nota_adestramento > 60:
        return pontos_atuais + BONUS_ADESTRAMENTO_BOM
    else:
        return pontos_atuais + BONUS_ADESTRAMENTO_BASICO


def calcular_bonus_competicao(pontos_atuais, nota_competicao):
    """Calcula bônus para competições baseado na nota obtida."""
    MULTIPLICADOR_COMPETICAO = 0.2
    bonus_competicao = nota_competicao * MULTIPLICADOR_COMPETICAO
    return pontos_atuais + bonus_competicao


def aplicar_bonus_pet(pontos_atuais, bonus_pets, indice):
    """
    Aplica bônus específico do pet baseado no tipo de bônus.

    Retorna: Pontos atualizados com bônus específico
    """
    if not bonus_pets or indice >= len(bonus_pets) or not bonus_pets[indice]:
        return pontos_atuais

    tipo_bonus = bonus_pets[indice]

    BONUS_ADOCAO = 10
    MULTIPLICADOR_PREMIADO = 1.3
    MULTIPLICADOR_RESGATE = 1.1

    if tipo_bonus == 'premiado':
        return pontos_atuais * MULTIPLICADOR_PREMIADO
    elif tipo_bonus == 'adocao':
        return pontos_atuais + BONUS_ADOCAO
    elif tipo_bonus == 'resgate':
        return pontos_atuais * MULTIPLICADOR_RESGATE

    return pontos_atuais


def aplicar_regras_recuperacao(pontos_atuais, idade, quantidade_vacinas,
                               configuracoes_clinica, regras_avaliacao,
                               limite_vacinas):
    """
    Aplica regras de recuperação se habilitadas.

    Retorna: Pontos atualizados considerando regras de recuperação
    """
    permite_recuperacao = regras_avaliacao[0]
    idade_minima = configuracoes_clinica[1]

    if not (permite_recuperacao and idade < idade_minima):
        return pontos_atuais

    # Regra de bônus de recuperação por idade
    if len(regras_avaliacao) > 1 and regras_avaliacao[1]:
        idade_bonus = min(idade + 5, idade_minima)
        pontos_atuais = max(pontos_atuais, idade_bonus)

    # Regra de bônus por vacinas extra
    elif (len(regras_avaliacao) > 2 and
          regras_avaliacao[2] and
          quantidade_vacinas > limite_vacinas):
        BONUS_VACINAS_RECUPERACAO = 5
        pontos_atuais += BONUS_VACINAS_RECUPERACAO

    return pontos_atuais


def aplicar_bonus_desempenho(status_medio):
    """
    Aplica bônus de desempenho baseado no status médio obtido.

    Retorna: Status médio ajustado com bônus de desempenho
    """
    MULTIPLICADOR_DESEMPENHO_EXCELENTE = 1.05  # Status > 90
    MULTIPLICADOR_DESEMPENHO_BOM = 1.02        # Status > 70
    STATUS_MAXIMO = 100

    if status_medio > 90:
        return min(status_medio * MULTIPLICADOR_DESEMPENHO_EXCELENTE, STATUS_MAXIMO)
    elif status_medio > 70:
        return status_medio * MULTIPLICADOR_DESEMPENHO_BOM
    else:
        return status_medio


if __name__ == "__main__":
    # Dados de teste
    pets_teste = [
        # Pet ativo com adestramento
        [True, 'cachorro', 5, 8, 'Carlos', ['adestramento', 90]],
        # Pet ativo com competição
        [True, 'gato', 3, 12, 'Ana', ['competicao', 70]],
        [False, 'passaro', 1, 2, 'Joao', None],              # Pet inativo
        # Pet com idade baixa mas sem vacinas
        [True, 'cachorro', 2, 0, 'Marina', ['adestramento', 65]]
    ]

    # Configurações: [especies_permitidas, idade_minima]
    configuracoes_teste = [['cachorro', 'gato', 'passaro'], 2]

    # Regras: [permite_recuperacao, bonus_recuperacao, bonus_vacinas_extra]
    regras_teste = [True, True, True]

    # Bônus específicos por pet
    bonus_teste = ['premiado', 'resgate', None, 'adocao']

    # Execução do teste
    resultado = calcular_status_pets(
        pets_teste, configuracoes_teste, regras_teste, bonus_teste
    )

    print(f"Status médio calculado: {resultado:.2f}")

# Estrutura dos parâmetros (mantida para compatibilidade):
# lista_pets: [[ativo, especie, idade, vacinas, dono, atividade_extra], ...]
# configuracoes_clinica: [especies_permitidas, idade_minima]
# regras_avaliacao: [permite_recuperacao, bonus_recuperacao, bonus_vacinas_extra]
# bonus_pets: [tipo_bonus_por_pet]
