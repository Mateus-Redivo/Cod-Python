# Seção 1: Manipulação de Strings
# Limpeza de Texto: Crie uma função que remova espaços em branco extras no início e fim de uma string, e entre palavras deixe apenas um espaço.
def limpar_texto(texto):
    """Remove espaços extras no início, fim e entre palavras."""
    # Remove espaços no início e fim, depois substitui múltiplos espaços por um só
    return " ".join(texto.strip().split())

# Teste da função limpar_texto
texto_sujo = "   Olá,    mundo  !    "
print(f"Original: '{texto_sujo}'")
print(f"Limpo: '{limpar_texto(texto_sujo)}'")


# Extração de Substrings: Escreva um programa que extrai partes específicas de uma string usando fatiamento (slicing).
def extrair_substrings(texto):
    """Demonstra diferentes técnicas de fatiamento de strings."""
    print(f"Texto original: '{texto}'")
    print(f"Primeiros 5 caracteres: '{texto[:5]}'")
    print(f"Últimos 5 caracteres: '{texto[-5:]}'")
    print(f"Do 6º ao 10º caractere: '{texto[5:10]}'")
    print(f"Caracteres em posições pares: '{texto[::2]}'")
    print(f"Texto reverso: '{texto[::-1]}'")

# Teste da função extrair_substrings
texto_exemplo = "O aprendizado é uma jornada, não um destino"
extrair_substrings(texto_exemplo)


# Comparação Insensível a Caso: Implemente uma função que verifica se duas strings são iguais, ignorando diferenças entre maiúsculas e minúsculas.
def comparar_strings_insensivel(str1, str2):
    """Verifica se duas strings são iguais, ignorando maiúsculas e minúsculas."""
    return str1.lower() == str2.lower()

# Teste da função comparar_strings_insensivel
string1 = "Python"
string2 = "PYTHON"
string3 = "python!"
print(f"'{string1}' == '{string2}' (ignorando caso): {comparar_strings_insensivel(string1, string2)}")
print(f"'{string1}' == '{string3}' (ignorando caso): {comparar_strings_insensivel(string1, string3)}")


# Validação de Texto: Crie um programa que verifica se uma string contém apenas letras do alfabeto.
def contem_apenas_letras(texto):
    """Verifica se uma string contém apenas letras do alfabeto."""
    return texto.isalpha()

# Teste da função contem_apenas_letras
texto1 = "Teste"
texto2 = "Teste3"
texto3 = "Teste!"
print(f"'{texto1}' contém apenas letras? {contem_apenas_letras(texto1)}")
print(f"'{texto2}' contém apenas letras? {contem_apenas_letras(texto2)}")
print(f"'{texto3}' contém apenas letras? {contem_apenas_letras(texto3)}")


# Substituição de Texto: Escreva uma função que substitui todas as ocorrências de uma palavra por outra em um texto.
def substituir_palavra(texto, palavra_antiga, palavra_nova):
    """Substitui todas as ocorrências de uma palavra por outra em um texto."""
    return texto.replace(palavra_antiga, palavra_nova)

# Teste da função substituir_palavra
frase = "Não se trata de saber tudo, mas de saber onde encontrar as respostas."
nova_frase = substituir_palavra(frase, "respostas", "perguntas")
print(f"Original: '{frase}'")
print(f"Substituída: '{nova_frase}'") 