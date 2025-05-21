# Enunciado 1: Escreva um programa que receba 5 notas e calcule a média delas.

# Cria uma lista com 5 notas usando list comprehension
# O loop range(5) executa 5 vezes
# float() converte a entrada do usuário (string) para número decimal
# input() solicita que o usuário digite uma nota
notas = [float(input("Digite uma nota: ")) for _ in range(5)]

# Calcula a média das notas
# sum() soma todos os valores da lista
# len() retorna o tamanho da lista (quantidade de notas)
# A divisão resulta na média aritmética
media = sum(notas) / len(notas)

# Exibe a média formatada com 2 casas decimais
# f-string permite inserir variáveis dentro da string
# :.2f formata o número com 2 casas decimais
print(f"Média das notas: {media:.2f}")
