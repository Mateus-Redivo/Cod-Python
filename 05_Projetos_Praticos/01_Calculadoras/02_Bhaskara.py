import math


def calcular_bhaskara(a, b, c):
    """
    Calcula as raízes de uma equação quadrática usando a fórmula de Bhaskara.
    Para uma equação na forma ax² + bx + c = 0
    """
    # Verificar se a equação é quadrática
    if a == 0:
        return "Não é uma equação quadrática (a = 0)"

    # Calcular o discriminante (delta)
    delta = b**2 - 4*a*c

    # Verificar casos possíveis
    if delta < 0:
        # Raízes complexas
        parte_real = -b / (2*a)
        parte_imaginaria = math.sqrt(abs(delta)) / (2*a)
        return f"Raízes complexas: x1 = {parte_real:.2f}+{parte_imaginaria:.2f}i e x2 = {parte_real:.2f}-{parte_imaginaria:.2f}i"
    elif delta == 0:
        # Raiz única (repetida)
        x = -b / (2*a)
        return f"Raiz única: x = {x:.2f}"
    else:
        # Duas raízes reais distintas
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Duas raízes reais: x1 = {x1:.2f} e x2 = {x2:.2f}"


# Exemplo de uso
if __name__ == "__main__":
    print("Resolução de equações quadráticas usando a fórmula de Bhaskara")
    print("Formato: ax² + bx + c = 0")

    try:
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        c = float(input("Digite o valor de c: "))

        resultado = calcular_bhaskara(a, b, c)
        print(resultado)
    except ValueError:
        print("Entrada inválida. Por favor, digite valores numéricos.")
