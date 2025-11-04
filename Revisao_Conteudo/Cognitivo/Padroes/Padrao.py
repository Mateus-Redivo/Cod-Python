# Lista para histórico de comandos (Command Pattern)
HISTORICO_COMANDOS = []


def comando_calcular_nota(estudante_dados, config_avaliacao):
    """Comando para calcular nota"""
    def executar():
        nome, notas = estudante_dados[0], estudante_dados[1]
        nota_final = sum(n * p for n, p in zip(notas,
                         config_avaliacao['pesos']))
        resultado = [nome, nota_final, notas.copy()]
        HISTORICO_COMANDOS.append(['calcular_nota', resultado])
        return resultado

    def desfazer():
        if HISTORICO_COMANDOS and HISTORICO_COMANDOS[-1][0] == 'calcular_nota':
            HISTORICO_COMANDOS.pop()
            print(f"Cálculo de nota desfeito para {estudante_dados[0]}")

    return {'executar': executar, 'desfazer': desfazer}


def comando_aplicar_bonus(estudante_dados, bonus_valor):
    """Comando para aplicar bônus"""
    def executar():
        nome = estudante_dados[0]
        nota_atual = estudante_dados[1] if len(estudante_dados) > 1 else 0
        nova_nota = min(nota_atual + bonus_valor, 100)
        resultado = [nome, nova_nota, bonus_valor]
        HISTORICO_COMANDOS.append(['aplicar_bonus', resultado])
        return resultado

    def desfazer():
        if HISTORICO_COMANDOS and HISTORICO_COMANDOS[-1][0] == 'aplicar_bonus':
            ultimo_comando = HISTORICO_COMANDOS.pop()
            print(f"Bônus removido para {ultimo_comando[1][0]}")

    return {'executar': executar, 'desfazer': desfazer}


def executar_comando(comando):
    """Executa um comando"""
    return comando['executar']()


def desfazer_ultimo_comando():
    """Desfaz o último comando"""
    if HISTORICO_COMANDOS:
        # Encontra o comando correspondente e executa desfazer
        ultimo_tipo = HISTORICO_COMANDOS[-1][0]
        print(f"Desfazendo comando: {ultimo_tipo}")
