# Tipos de Variáveis em Python

Em Python, os tipos de variáveis são dinâmicos, o que significa que você não precisa declarar o tipo de uma variável explicitamente. O interpretador Python infere o tipo com base no valor atribuído à variável.

## 1. Tipos Numéricos

*   **int:** Inteiros (números inteiros).
*   **float:** Números de ponto flutuante (números decimais).
*   **complex:** Números complexos.

**Exemplos:**

```python
idade = 30  # int
preco = 99.90  # float
complexo = 2 + 3j  # complex
```

## 2. Tipo Booleano

*   **bool:** Representa valores booleanos (True ou False).

**Exemplo:**

```python
verdadeiro = True
falso = False
```

## 3. Tipo String

*   **str:** Representa sequências de caracteres (texto).

**Exemplo:**

```python
nome = "Alice"
mensagem = "Olá, mundo!"
```

## 4. Tipos de Sequência

*   **list:** Listas (coleções ordenadas e mutáveis de itens).
*   **tuple:** Tuplas (coleções ordenadas e imutáveis de itens).
*   **range:** Sequência de números.

**Exemplos:**

```python
frutas = ["maçã", "banana", "laranja"]  # list
cores = ("vermelho", "verde", "azul")  # tuple
numeros = range(5)  # range (0, 1, 2, 3, 4)
```

## 5. Tipos de Mapeamento

*   **dict:** Dicionários (coleções de pares chave-valor).

**Exemplo:**

```python
pessoa = {"nome": "Alice", "idade": 30}  # dict
```

## 6. Tipos de Conjunto

*   **set:** Conjuntos (coleções não ordenadas de itens únicos).
*   **frozenset:** Conjuntos imutáveis.

**Exemplos:**

```python
numeros = {1, 2, 3, 4, 5}  # set
conjunto_imutavel = frozenset({1, 2, 3})  # frozenset
```

## 7. Tipo None

*   **NoneType:** Representa a ausência de um valor.

**Exemplo:**

```python
nulo = None