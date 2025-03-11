# Tipos de Dados em Python: Chaves, Listas e Tuplas

## 1. Chaves (Dicionários)

**O que são:** Dicionários são estruturas de dados que armazenam pares de chave-valor. As chaves são únicas dentro de um dicionário e são usadas para acessar os valores correspondentes.

**Características:**
*   Mutáveis (podem ser alterados após a criação).
*   Não ordenados (a ordem dos elementos não é garantida).
*   Chaves devem ser imutáveis (strings, números, tuplas).
*   Valores podem ser de qualquer tipo.

**Exemplo:**

```python
pessoa = {"nome": "Alice", "idade": 30, "cidade": "São Paulo"}
print(pessoa["nome"])  # Output: Alice
```

**Explicação:** Neste exemplo, `nome`, `idade` e `cidade` são as chaves, e `"Alice"`, `30` e `"São Paulo"` são os valores correspondentes.

## 2. Listas

**O que são:** Listas são coleções ordenadas de itens.

**Características:**
*   Mutáveis (podem ser alteradas após a criação).
*   Ordenadas (a ordem dos elementos é preservada).
*   Podem conter itens de diferentes tipos.

**Exemplo:**

```python
frutas = ["maçã", "banana", "laranja"]
print(frutas[0])  # Output: maçã
```

**Explicação:** Neste exemplo, `frutas` é uma lista de strings. Podemos acessar os elementos da lista usando seus índices (a partir de 0).

## 3. Tuplas

**O que são:** Tuplas são coleções ordenadas de itens, semelhantes às listas, mas imutáveis.

**Características:**
*   Imutáveis (não podem ser alteradas após a criação).
*   Ordenadas (a ordem dos elementos é preservada).
*   Podem conter itens de diferentes tipos.

**Exemplo:**

```python
cores = ("vermelho", "verde", "azul")
print(cores[1])  # Output: verde
```

**Explicação:** Neste exemplo, `cores` é uma tupla de strings. Assim como nas listas, podemos acessar os elementos da tupla usando seus índices. A principal diferença é que não podemos modificar uma tupla depois de criada.