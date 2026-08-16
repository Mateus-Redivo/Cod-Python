# Gabarito — Módulo 13, Exercício 02: Estendendo o sistema

Enunciado: [EXERCICIO-02-estendendo-o-sistema.md](../../modulo-13-estudo-de-caso-crud/exercicios/EXERCICIO-02-estendendo-o-sistema.md)

> Este gabarito traz **os trechos** de cada funcionalidade, não o sistema inteiro reescrito. O
> motivo é o próprio exercício: o valor está em encaixar o novo no que já existe, e um arquivo
> pronto para copiar destruiria isso. Compare a sua função com a minha, não o arquivo todo.

---

## 1. Buscar aluno pelo nome

```python
def buscar_aluno():
    if verifica_lista_vazia():
        return

    procurado = input("Digite parte do nome: ").strip().lower()

    encontrados = 0
    for i in range(len(alunos)):
        if procurado in alunos[i].lower():
            media = calcular_media_aluno(i)
            print(f"{i + 1}. {alunos[i]} - Média: {media:.2f}")
            encontrados += 1

    if encontrados == 0:
        print("Nenhum aluno encontrado.")
```

**Decisões:** o `.strip().lower()` nos dois lados é a receita do módulo 07: sem ele, procurar "ana"
não acha "Ana Silva". O `in` funciona com trecho, não só nome exato, que é o que o enunciado pede. E
o contador `encontrados` existe para poder avisar quando não houve resultado: um silêncio deixaria o
usuário sem saber se buscou errado ou se não existe.

## 2. Relatório da turma

```python
def relatorio_da_turma():
    if verifica_lista_vazia():
        return

    medias = []
    for i in range(len(alunos)):
        medias.append(calcular_media_aluno(i))

    media_geral = sum(medias) / len(medias)

    indice_maior = 0
    indice_menor = 0
    for i in range(len(medias)):
        if medias[i] > medias[indice_maior]:
            indice_maior = i
        if medias[i] < medias[indice_menor]:
            indice_menor = i

    acima = 0
    for media in medias:
        if media > media_geral:
            acima += 1

    print(f"Total de alunos:   {len(alunos)}")
    print(f"Média geral:       {media_geral:.2f}")
    print(f"Maior média:       {alunos[indice_maior]} ({medias[indice_maior]:.2f})")
    print(f"Menor média:       {alunos[indice_menor]} ({medias[indice_menor]:.2f})")
    print(f"Acima da média:    {acima}")
```

**Decisões:** as médias são calculadas **uma vez** e guardadas numa lista: recalculá-las em cada
laço seria o defeito que o módulo 12 aponta. E são necessários dois laços: o de "acima da média" só
pode rodar depois de a média existir, exatamente como no boletim do módulo 06.

O `verifica_lista_vazia()` no topo protege as divisões e os índices `[0]`.

## 3. Confirmação antes de excluir

```python
def excluir_aluno():
    if verifica_lista_vazia():
        return

    listar_alunos()
    indice = receber_aluno()
    if indice is None:
        return

    resposta = input(f"Excluir {alunos[indice]}? (s/n): ").strip().lower()
    if resposta != "s":
        print("Exclusão cancelada.")
        return

    alunos.pop(indice)
    notas.pop(indice)
    print("Aluno excluído.")
```

**Decisões:** a confirmação vem **depois** de validar o índice: não faz sentido perguntar "confirma
excluir?" sobre um aluno que não existe. E o teste é `!= "s"`, não `== "n"`: qualquer coisa que não
seja um "sim" explícito cancela. Em operação destrutiva, o silêncio deve significar não.

Repare que os dois `pop` andam juntos. Remover de uma lista e esquecer a outra é o defeito que o
exercício 03 investiga.

## 4. Impedir nome duplicado

```python
def nome_ja_existe(nome):
    for aluno in alunos:
        if aluno.strip().lower() == nome.strip().lower():
            return True
    return False


def cadastrar_aluno():
    nome = input("Nome do aluno: ").strip()

    if len(nome) == 0:
        print("O nome não pode ficar vazio.")
        return

    if nome_ja_existe(nome):
        print(f"Já existe um aluno chamado {nome}.")
        return

    alunos.append(nome)
    notas.append([])
    print("Aluno cadastrado.")
```

**Decisões:** `nome_ja_existe` é função separada porque a pergunta pode reaparecer (na alteração de
nome, por exemplo). A checagem de nome vazio veio junto: ela não estava nos requisitos, mas o
exercício 03 a lista como defeito, e resolvê-la aqui custa duas linhas.

O `notas.append([])` é o que mantém as duas listas do mesmo tamanho. Esquecê-lo é o caminho mais
direto para o desalinhamento.

## 5. Listagem ordenada por média

```python
def listar_por_media():
    if verifica_lista_vazia():
        return

    # Monta pares [media, nome] para poder ordenar sem tocar nas listas originais.
    ranking = []
    for i in range(len(alunos)):
        ranking.append([calcular_media_aluno(i), alunos[i]])

    ranking.sort(reverse=True)

    print("Ranking por média:")
    for posicao in range(len(ranking)):
        media, nome = ranking[posicao]
        print(f"{posicao + 1}. {nome} - {media:.2f}")
```

**Decisões:** a chave do exercício é **não destruir a ordem de cadastro**. Por isso o ranking é uma
estrutura nova, montada a partir das listas originais, que continuam intactas. Um
`alunos.sort()` resolveria a listagem e quebraria todo o resto do sistema, porque os índices
deixariam de casar com `notas`.

Ordenar `[media, nome]` funciona porque listas se comparam elemento a elemento: o Python compara
primeiro as médias e, em caso de empate, os nomes. Empate passa a sair em ordem alfabética, de
graça.

## A função auxiliar que apareceu

Quatro das cinco funcionalidades precisaram calcular a média de um aluno. Em vez de repetir o
cálculo, extraí:

```python
def calcular_media_aluno(indice):
    if len(notas[indice]) == 0:
        return 0
    return sum(notas[indice]) / len(notas[indice])
```

Isso não estava nos requisitos: apareceu porque o código pediu. É o sinal "código repetido" do
módulo 12 aparecendo enquanto você trabalha, e atendê-lo na hora é mais barato do que depois.

> O `return 0` para aluno sem notas está aqui porque é o que o sistema original faz. O exercício 03
> discute se essa é a decisão certa, e eu acho que não é. Mas mudá-la agora violaria a regra de não
> alterar comportamento existente enquanto se acrescenta funcionalidade.

## Sobre o `global`

Nenhuma dessas funções declara `global`, e mesmo assim altera `alunos` e `notas`. Isso funciona
porque `append` e `pop` **modificam** a lista existente em vez de criar uma nova, e o módulo 08
explicou que ler uma global não exige declaração, só reatribuí-la exige.

Se alguma função tentasse `alunos = []`, aí sim precisaria de `global`, e aí sim valeria repensar a
arquitetura.

## Desafio opcional: desfazer a exclusão

```python
ultimo_excluido = None      # [nome, notas] ou None

def excluir_aluno():
    global ultimo_excluido
    ...
    ultimo_excluido = [alunos.pop(indice), notas.pop(indice)]


def desfazer_exclusao():
    global ultimo_excluido
    if ultimo_excluido is None:
        print("Não há exclusão para desfazer.")
        return
    alunos.append(ultimo_excluido[0])
    notas.append(ultimo_excluido[1])
    ultimo_excluido = None
    print("Exclusão desfeita.")
```

Aqui o `global` é inevitável, porque `ultimo_excluido` é **reatribuído**. E repare no detalhe: o
aluno restaurado volta para o **fim** da lista, não para a posição original. Restaurar a posição
exigiria guardar o índice também, e decidir o que fazer se outros alunos tiverem sido cadastrados
no meio-tempo. É mais decisão de projeto do que de código.
