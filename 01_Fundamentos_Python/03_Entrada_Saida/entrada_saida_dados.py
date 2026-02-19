"""
=============================
ENTRADA E SAÍDA DE DADOS
=============================
Este arquivo demonstra como receber dados do usuário e exibir informações
"""

# =============================
# FUNÇÃO PRINT() - SAÍDA DE DADOS
# =============================
print("=== FUNÇÃO PRINT ===")

# Print simples
print("Olá, mundo!")
print("Esta é uma segunda linha")
print()

# Print com múltiplos valores
nome = "João"
idade = 25
print("Nome:", nome, "| Idade:", idade , 5)
print()

# Controlando o separador
print("A", "B", "C", sep="-")           # A-B-C
print("A", "B", "C", sep=" | ")         # A | B | C
print("A", "B", "C", sep="")            # ABC
print()

# Controlando o final da linha
print("Esta linha", end="")
print(" continua aqui")
print("Esta é uma nova linha")
print()

# =============================
# FORMATAÇÃO DE STRINGS
# =============================
print("=== FORMATAÇÃO DE STRINGS ===")

nome = "Maria"
salario = 3500.75

# Método .format()
print("Nome: {} | Salário: R$ {:.2f}".format(nome, salario))

# F-strings (mais moderno e recomendado)
print(f"Nome: {nome} | Salário: R$ {salario:.2f}")

# Formatação de números
pi = 3.14159
print(f"Pi com 2 casas: {pi:.2f}")
print(f"Pi com 4 casas: {pi:.4f}")

numero = 1234
print(f"Número com zeros: {numero:06d}")    # 001234
print()

# =============================
# FUNÇÃO INPUT() - ENTRADA DE DADOS
# =============================
print("=== FUNÇÃO INPUT ===")
print("Vamos coletar algumas informações:")

# Input básico (sempre retorna string)
nome_usuario = input("Digite seu nome: ")
print(f"Olá, {nome_usuario}!")
print()

# Mostrando que input sempre retorna string
idade_texto = input("Digite sua idade: ")
print(f"Você digitou: '{idade_texto}' (tipo: {type(idade_texto)})")
print()

# =============================
# EXEMPLOS PRÁTICOS
# =============================
print("=== EXEMPLO PRÁTICO ===")

# Coletando dados pessoais
print("--- Cadastro de Usuário ---")
nome = input("Nome completo: ")
cidade = input("Cidade: ")
profissao = input("Profissão: ")

# Exibindo os dados coletados
print("\n--- DADOS CADASTRADOS ---")
print(f"Nome: {nome}")
print(f"Cidade: {cidade}")
print(f"Profissão: {profissao}")
print()

# =============================
# DICAS IMPORTANTES
# =============================
print("=== DICAS IMPORTANTES ===")

print("1. A função input() sempre retorna uma string")
print("2. Use f-strings para formatação moderna")
print("3. Use {:.2f} para mostrar 2 casas decimais")
print("4. O parâmetro 'sep' do print controla o separador")
print("5. O parâmetro 'end' do print controla o fim da linha")
print()

# Exemplo de formatação avançada
produto = "Notebook"
preco = 2499.99
desconto = 15

print(f"Produto: {produto}")
print(f"Preço original: R$ {preco:.2f}")
print(f"Desconto: {desconto}%")
print(f"Preço final: R$ {preco * (1 - desconto/100):.2f}")
