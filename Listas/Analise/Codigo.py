def calcular_nota_estudante(e, c, p, b=None, d=5):
    estudantes = [
        ["João", 85, 90, 78, "presencial", True],
        ["Maria", 92, 88, 95, "online", False],
        ["Pedro", 70, 65, 80, "presencial", True],
        ["Ana", 88, 91, 85, "online", False]
    ]

    notas_finais = []

    for i in range(len(estudantes)):
        if estudantes[i][0] == e:
            n1 = estudantes[i][1]
            n2 = estudantes[i][2]
            n3 = estudantes[i][3]
            modalidade = estudantes[i][4]
            veterano = estudantes[i][5]

            if n1 < 0 or n2 < 0 or n3 < 0:
                continue

            media = (n1 * 0.3 + n2 * 0.4 + n3 * 0.3)

            if c == "matematica":
                if p >= 15:
                    bonus = 5
                elif p >= 10:
                    bonus = 3
                elif p >= 5:
                    bonus = 1
                else:
                    bonus = 0
            elif c == "portugues":
                if p >= 20:
                    bonus = 4
                elif p >= 15:
                    bonus = 2
                elif p >= 10:
                    bonus = 1
                else:
                    bonus = 0
            elif c == "ciencias":
                if p >= 12:
                    bonus = 6
                elif p >= 8:
                    bonus = 3
                else:
                    bonus = 0
            else:
                bonus = 0

            if veterano:
                bonus += 2

            if modalidade == "online":
                bonus += 1

            if b and b == "olimpiada":
                bonus += 10
            elif b and b == "concurso":
                bonus += 5

            nota_final = media + bonus

            if nota_final > 100:
                nota_final = 100

            if d > 5:
                nota_final -= (d - 5) * 0.5

            if nota_final >= 80:
                status = "Aprovado com Distinção"
            elif nota_final >= 60:
                status = "Aprovado"
            else:
                status = "Reprovado"

            notas_finais.append([estudantes[i][0], nota_final, status])

            print(f"Estudante: {estudantes[i][0]}")
            print(f"Média Base: {media:.2f}")
            print(f"Bônus Total: {bonus}")
            print(f"Nota Final: {nota_final:.2f}")
            print(f"Status: {status}")
            print("-" * 30)

    return notas_finais


# Exemplo de uso
resultado = calcular_nota_estudante("João", "matematica", 12, "olimpiada", 3)
