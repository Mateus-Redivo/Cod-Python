# Sistemas

Essa pasta contém dois tipos de material: implementações prontas para estudo e propostas para você implementar do zero.

## Estrutura

```
Implementacoes/
    Vetor/      — sistemas que guardam dados em listas (memória)
    Txt/        — sistemas que guardam dados em arquivo .txt (disco)

Propostas/      — especificações de sistemas para implementar
```

## Implementacoes

Há dois sistemas implementados com a mesma funcionalidade (cadastro e controle de produtos), mas com abordagens diferentes de armazenamento:

### Vetor (em memória)

`Vetor/Sistema_Produtos.py` guarda os dados em listas Python enquanto o programa está rodando. Quando o programa fecha, os dados são perdidos.

Use para estudar: menus, funções, listas, lógica de CRUD básico.

### Txt (em arquivo)

`Txt/Prod_TXT.py` lê e salva os dados em um arquivo `.txt` a cada operação. Os dados persistem entre execuções.

Use para estudar: leitura e escrita de arquivos, `open()`, `split()`, tratamento de `FileNotFoundError`.

### Por que os dois?

Mostrar a mesma lógica com duas formas de persistência diferentes é intencional. Primeiro entenda o funcionamento com a versão Vetor. Depois veja como a versão Txt resolve o problema de dados que somem ao fechar o programa.

## Propostas

Cada arquivo `.md` em `Propostas/` descreve um sistema diferente para você implementar. Leia a proposta, entenda os requisitos e implemente antes de consultar qualquer implementação pronta.

Comece pela proposta mais simples e avance conforme ganha confiança.
