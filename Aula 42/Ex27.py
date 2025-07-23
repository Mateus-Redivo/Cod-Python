# Comparação de strings em Python - Versão Expandida

# Strings para comparação
texto1 = "Python"
texto2 = "python"
texto3 = "Python"
texto4 = "Java"
texto5 = "    Python    "
texto6 = "Python é incrível!"

# 1. Comparações básicas
print("=== Comparações básicas ===")
print(f"'Python' == 'python': {texto1 == texto2}")
print(f"'Python' == 'Python': {texto1 == texto3}")
print(f"'Python' != 'Java': {texto1 != texto4}")

# 2. Comparação ignorando maiúsculas/minúsculas
print("\n=== Comparação ignorando case ===")
print(
    f"'Python'.lower() == 'python'.lower(): {texto1.lower() == texto2.lower()}")
print(
    f"'Python'.casefold() == 'python'.casefold(): {texto1.casefold() == texto2.casefold()}")

# 3. Comparação de ordem alfabética
print("\n=== Comparação alfabética ===")
print(f"'Python' < 'Java': {texto1 < texto4}")
print(f"'Java' < 'Python': {texto4 < texto1}")
print(f"Ordem alfabética: {sorted([texto1, texto2, texto4])}")

# 4. Métodos de verificação
palavra = "Hello World"
print("\n=== Métodos de verificação ===")
print(f"Começa com 'He': {palavra.startswith('He')}")
print(f"Termina com 'rld': {palavra.endswith('rld')}")
print(f"'World' está contido: {'World' in palavra}")
print(f"Posição de 'World': {palavra.find('World')}")

# 5. Comparação de tamanhos
print("\n=== Comparação de tamanhos ===")
print(f"Tamanho de '{texto1}': {len(texto1)}")
print(f"Tamanho de '{texto4}': {len(texto4)}")
print(f"'{texto1}' tem mais caracteres que '{texto4}': {len(texto1) > len(texto4)}")

# 6. Manipulação de espaços
print("\n=== Manipulação de espaços ===")
print(f"String original: '{texto5}'")
print(f"Removendo espaços à direita: '{texto5.rstrip()}'")
print(f"Removendo espaços à esquerda: '{texto5.lstrip()}'")
print(f"Removendo espaços dos dois lados: '{texto5.strip()}'")

# 7. Métodos de substituição
print("\n=== Métodos de substituição ===")
print(f"Substituindo 'Python' por 'Java': {texto6.replace('Python', 'Java')}")
print(f"Substituindo espaços por hífen: {texto6.replace(' ', '-')}")

# 8. Verificação de conteúdo
print("\n=== Verificação de conteúdo ===")

# Verifica se todos os caracteres são alfanuméricos (letras ou números)
# Retorna False se contiver espaços ou caracteres especiais
print(f"É alfanumérico? {texto1.isalnum()}")

# Verifica se todos os caracteres são letras do alfabeto
# Retorna False se contiver números, espaços ou caracteres especiais
print(f"É alfabético? {texto1.isalpha()}")

# Verifica se a string contém apenas dígitos decimais (0-9)
# Retorna False para números em outros formatos (hex, binary) ou caracteres não numéricos
print(f"É decimal? {texto1.isdecimal()}")

# Verifica se a string está formatada como título
# Exemplo de título: "Hello World" (primeira letra de cada palavra em maiúsculo)
print(f"É título? {texto1.istitle()}")

# Verifica se todos os caracteres estão em minúsculo
# Retorna False se houver qualquer caractere em maiúsculo
print(f"É minúsculo? {texto1.islower()}")

# Verifica se todos os caracteres estão em maiúsculo
# Retorna False se houver qualquer caractere em minúsculo
print(f"É maiúsculo? {texto1.isupper()}")

# 9. Comparação usando operadores de cadeia
print("\n=== Comparação encadeada ===")
print(f"'A' <= 'Python' <= 'Z': {'A' <= texto1 <= 'Z'}")
print(f"Comparação múltipla: {3 < len(texto1) < 10}")
<<<<<<< HEAD

=======
>>>>>>> 680283a4c776b59b73511f223aa6e8984191356d
