# Conceitos avançados de manipulação de strings
texto = "Python Programming"
texto_espacado = "    Python com espaços    "


# 1. Acessando caracteres por índice
primeiro_caractere = texto[0]  # P
ultimo_caractere = texto[-1]   # g

# 2. Fatiamento (slicing)
primeiras_letras = texto[0:6]  # Python

# 3. Métodos básicos de string
texto_maiusculo = texto.upper()      # Converte para maiúsculo
texto_minusculo = texto.lower()      # Converte para minúsculo
texto_titulo = texto.title()         # Primeira letra de cada palavra em maiúsculo

# 4. Verificação de conteúdo
contem_python = "Python" in texto    # Verifica se contém a palavra
comeca_com = texto.startswith("Py")  # Verifica se começa com
 
# 5. Remoção de espaços em branco
texto_sem_espacos = texto_espacado.strip()       # Remove espaços no início e fim
texto_sem_espacos_esq = texto_espacado.lstrip()  # Remove espaços à esquerda
texto_sem_espacos_dir = texto_espacado.rstrip()  # Remove espaços à direita

# 6. Substituição de caracteres
texto_substituido = texto.replace("Python", "Java")

# 7. Dividindo strings
palavras = texto.split()  # Divide por espaços
caracteres = list(texto)  # Converte string em lista de caracteres

# 8. Encontrando posições
# Retorna o índice onde começa "Programming"
posicao = texto.find("Programming")
contagem = texto.count("m")          # Conta quantas vezes 'm' aparece

# 9. Junção de strings
lista_palavras = ["Python", "é", "incrível"]
texto_junto = " ".join(lista_palavras)

# 10. Verificações adicionais
e_alfanumerico = texto.isalnum()     # Verifica se são só letras e números
e_alfabetico = texto.isalpha()       # Verifica se são só letras
e_decimal = "123".isdecimal()        # Verifica se são só números decimais

# Exibindo os resultados
print(f"Texto original: {texto}")
print(f"Primeiro caractere: {primeiro_caractere}")
print(f"Último caractere: {ultimo_caractere}")
print(f"Primeiras letras: {primeiras_letras}")
print(f"Maiúsculas: {texto_maiusculo}")
print(f"Minúsculas: {texto_minusculo}")
print(f"Título: {texto_titulo}")
print(f"Contém 'Python'?: {contem_python}")
print(f"Começa com 'Py'?: {comeca_com}")

# Exibindo os novos resultados
print("\nResultados adicionais:")
print(f"Texto sem espaços: '{texto_sem_espacos}'")
print(f"Texto substituído: {texto_substituido}")
print(f"Palavras separadas: {palavras}")
print(f"Lista de caracteres: {caracteres}")
print(f"Posição de 'Programming': {posicao}")
print(f"Quantidade de 'm': {contagem}")
print(f"Palavras unidas: {texto_junto}")
print(f"É alfanumérico?: {e_alfanumerico}")
print(f"É alfabético?: {e_alfabetico}")
print(f"'123' é decimal?: {e_decimal}")
