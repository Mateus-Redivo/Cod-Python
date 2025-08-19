"""
Calculadora de IMC (Índice de Massa Corporal)
Programa que calcula o IMC de uma pessoa e informa sua classificação
"""


def calcular_imc(peso, altura):
    """Calcula o IMC baseado no peso e altura"""
    return peso / (altura ** 2)


def classificar_imc(imc):
    """Classifica o IMC de acordo com os padrões da OMS"""
    if imc < 18.5:
        return "Abaixo do peso", "⚠️"
    elif 18.5 <= imc < 25:
        return "Peso normal", "✅"
    elif 25 <= imc < 30:
        return "Sobrepeso", "⚠️"
    elif 30 <= imc < 35:
        return "Obesidade grau I", "❌"
    elif 35 <= imc < 40:
        return "Obesidade grau II", "❌"
    else:
        return "Obesidade grau III (mórbida)", "🚨"


def obter_dados_usuario():
    """Obtém os dados do usuário de forma segura"""
    while True:
        try:
            peso = float(input("Digite seu peso (kg): "))
            if peso <= 0:
                print("❌ Peso deve ser maior que zero!")
                continue
            break
        except ValueError:
            print("❌ Por favor, digite um número válido para o peso!")

    while True:
        try:
            altura = float(input("Digite sua altura (m): "))
            if altura <= 0:
                print("❌ Altura deve ser maior que zero!")
                continue
            if altura > 3:
                print("❌ Altura parece muito alta! Digite em metros (ex: 1.70)")
                continue
            break
        except ValueError:
            print("❌ Por favor, digite um número válido para a altura!")

    return peso, altura


def exibir_resultado(peso, altura, imc, classificacao, emoji):
    """Exibe o resultado de forma formatada"""
    print("\n" + "="*50)
    print("📊 RESULTADO DO CÁLCULO DE IMC")
    print("="*50)
    print(f"💪 Peso: {peso:.1f} kg")
    print(f"📏 Altura: {altura:.2f} m")
    print(f"🧮 IMC: {imc:.2f}")
    print(f"{emoji} Classificação: {classificacao}")
    print("="*50)


def exibir_tabela_referencia():
    """Exibe a tabela de referência dos valores de IMC"""
    print("\n📋 TABELA DE REFERÊNCIA - IMC")
    print("-" * 40)
    print("Abaixo de 18,5    | Abaixo do peso")
    print("18,5 a 24,9       | Peso normal")
    print("25,0 a 29,9       | Sobrepeso")
    print("30,0 a 34,9       | Obesidade grau I")
    print("35,0 a 39,9       | Obesidade grau II")
    print("40,0 ou mais      | Obesidade grau III")
    print("-" * 40)


def dar_dicas(classificacao):
    """Fornece dicas baseadas na classificação do IMC"""
    dicas = {
        "Abaixo do peso": [
            "🍽️ Considere aumentar a ingestão calórica de forma saudável",
            "💪 Pratique exercícios de fortalecimento muscular",
            "👨‍⚕️ Consulte um nutricionista para um plano alimentar adequado"
        ],
        "Peso normal": [
            "🎉 Parabéns! Seu peso está dentro do ideal",
            "🏃‍♂️ Mantenha uma rotina de exercícios regulares",
            "🥗 Continue com uma alimentação equilibrada"
        ],
        "Sobrepeso": [
            "🚶‍♂️ Aumente a atividade física gradualmente",
            "🥗 Reduza o consumo de alimentos processados",
            "💧 Beba mais água e diminua bebidas açucaradas"
        ],
        "Obesidade grau I": [
            "👨‍⚕️ Considere buscar orientação médica",
            "🏋️‍♂️ Inicie um programa de exercícios supervisionado",
            "📊 Monitore sua alimentação com um diário alimentar"
        ],
        "Obesidade grau II": [
            "🚨 É importante buscar acompanhamento médico",
            "👥 Considere grupos de apoio para perda de peso",
            "🎯 Estabeleça metas pequenas e realistas"
        ],
        "Obesidade grau III (mórbida)": [
            "🚨 Procure acompanhamento médico urgente",
            "🏥 Considere tratamentos especializados",
            "👨‍⚕️ Discuta todas as opções disponíveis com seu médico"
        ]
    }

    print(f"\n💡 DICAS PARA: {classificacao.upper()}")
    print("-" * 50)
    for dica in dicas.get(classificacao, []):
        print(f"  {dica}")
    print("-" * 50)


def main():
    """Função principal do programa"""
    print("🏥 BEM-VINDO À CALCULADORA DE IMC!")
    print("="*50)

    while True:
        # Exibir tabela de referência
        exibir_tabela_referencia()

        # Obter dados do usuário
        peso, altura = obter_dados_usuario()

        # Calcular IMC
        imc = calcular_imc(peso, altura)

        # Classificar IMC
        classificacao, emoji = classificar_imc(imc)

        # Exibir resultado
        exibir_resultado(peso, altura, imc, classificacao, emoji)

        # Dar dicas
        dar_dicas(classificacao)

        # Pergunta se quer calcular novamente
        print("\n🔄 Deseja calcular o IMC de outra pessoa?")
        continuar = input(
            "Digite 's' para SIM ou qualquer tecla para SAIR: ").lower().strip()

        if continuar != 's':
            print("\n👋 Obrigado por usar a Calculadora de IMC!")
            print("💙 Cuide bem da sua saúde!")
            break
        else:
            print("\n" + "="*50)


if __name__ == "__main__":
    main()
