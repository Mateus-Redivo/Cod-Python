# Guia de Comentários de Código - Python

Este arquivo contém exemplos de diferentes tipos de comentários que podem ser usados para anotar e documentar código Python.

## **Comentários de Tarefas Pendentes**

```python
# TODO: Implementar validação de email
# TODO: Adicionar logging para debug
# TODO: Criar testes unitários para esta função
# TODO: Refatorar esta função para ser mais legível
# TODO: Implementar cache para melhorar performance
```

## **Comentários de Problemas**

```python
# FIXME: Corrigir divisão por zero quando lista está vazia
# FIXME: Bug na validação de entrada de dados
# FIXME: Problema de encoding com caracteres especiais
# FIXME: Memory leak nesta função
# FIXME: Atualizar números do menu (opções estão trocadas)
```

## **Comentários de Bugs Conhecidos**

```python
# BUG: Função retorna None em casos específicos
# BUG: Não funciona corretamente com strings unicode
# BUG: Falha ao processar arquivos grandes
# BUG: Inconsistência nos resultados em ambiente Windows
```

## **Comentários de Soluções Temporárias**

```python
# HACK: Solução temporária - remover na próxima versão
# HACK: Gambiarra para contornar limitação da biblioteca
# HACK: Quick fix para resolver problema urgente
# HACK: Workaround para bug da versão atual do framework
```

## **Comentários de Código Problemático**

```python
# XXX: Este código precisa ser revisado urgentemente
# XXX: Lógica complexa - considerar simplificar
# XXX: Possível problema de segurança aqui
# XXX: Performance ruim - otimizar
```

## **Comentários Informativos**

```python
# NOTE: Esta função assume que os dados estão ordenados
# NOTE: Usar apenas com Python 3.8 ou superior
# NOTE: Dependente da biblioteca requests estar instalada
# NOTE: Formato de data deve ser DD/MM/YYYY
```

## **Comentários de Aviso**

```python
# WARNING: Não usar esta função em produção
# WARNING: Esta operação é irreversível
# WARNING: Pode consumir muita memória com datasets grandes
# WARNING: Thread-unsafe - usar apenas em contexto single-thread
```

## **Comentários de Funcionalidade Obsoleta**

```python
# DEPRECATED: Esta função será removida na versão 2.0
# DEPRECATED: Usar nova_funcao() ao invés desta
# DEPRECATED: Mantido apenas para compatibilidade
# DEPRECATED: Substituído por implementação mais eficiente
```

## **Comentários de Otimização**

```python
# OPTIMIZE: Usar list comprehension ao invés de loop
# OPTIMIZE: Cachear resultado desta operação custosa
# OPTIMIZE: Considerar usar numpy para cálculos matemáticos
# OPTIMIZE: Implementar lazy loading para melhor performance
```

## **Comentários de Revisão**

```python
# REVIEW: Verificar se esta lógica está correta
# REVIEW: Confirmar se tratamento de erro está adequado
# REVIEW: Validar se os tipos de dados estão corretos
# REVIEW: Checar se documentação está atualizada
```

## **Comentários de Mudanças**

```python
# CHANGED: Alterado para usar f-strings ao invés de format()
# CHANGED: Migrado de requests para httpx
# CHANGED: Atualizado para usar pathlib ao invés de os.path
# CHANGED: Modificado para suportar async/await
```

## **Comentários de Ideias**

```python
# IDEA: Implementar sistema de plugins
# IDEA: Adicionar suporte a múltiplos formatos de arquivo
# IDEA: Criar dashboard para visualização de dados
# IDEA: Integrar com API externa para dados em tempo real
```

## **Comentários de Questionamentos**

```python
# QUESTION: Devemos validar entrada ou confiar no input?
# QUESTION: É necessário suporte a Python 2.7?
# QUESTION: Qual a melhor estrutura de dados para este caso?
# QUESTION: Devemos usar threading ou asyncio?
```

## **Comentários de Refatoração**

```python
# REFACTOR: Extrair esta lógica para classe separada
# REFACTOR: Dividir esta função em funções menores
# REFACTOR: Mover constantes para arquivo de configuração
# REFACTOR: Simplificar estrutura condicional complexa
```

## **Comentários de Testes**

```python
# TEST: Adicionar teste para caso extremo
# TEST: Verificar comportamento com entrada inválida
# TEST: Testar performance com grande volume de dados
# TEST: Criar mock para dependências externas
```

## **Comentários de Documentação**

```python
# DOC: Adicionar docstring para esta função
# DOC: Atualizar README com novos exemplos
# DOC: Documentar parâmetros e valores de retorno
# DOC: Criar tutorial para uso da API
```

## **Comentários de Segurança**
```python
# SECURITY: Sanitizar input antes de usar
# SECURITY: Usar HTTPS em vez de HTTP
# SECURITY: Revisar autenticação - possível vulnerabilidade
# SECURITY: Senhas não devem ser logadas
```
