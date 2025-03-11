# Operadores em Python

Operadores são símbolos que realizam operações em valores e variáveis. Python oferece diversos tipos de operadores para diferentes propósitos.

## 1. Operadores Aritméticos

Realizam operações matemáticas.

*   `+`: Adição
*   `-`: Subtração
*   `*`: Multiplicação
*   `/`: Divisão
*   `//`: Divisão inteira (retorna o quociente inteiro)
*   `%`: Módulo (retorna o resto da divisão)
*   `**`: Exponenciação

**Exemplos:**

```python
a = 10
b = 3

print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.3333333333333335
print(a // b) # Output: 3
print(a % b)  # Output: 1
print(a ** b) # Output: 1000
```

## 2. Operadores de Comparação

Comparam dois valores e retornam um valor booleano (True ou False).

*   `==`: Igual a
*   `!=`: Diferente de
*   `>`: Maior que
*   `<`: Menor que
*   `>=`: Maior ou igual a
*   `<=`: Menor ou igual a

**Exemplos:**

```python
a = 5
b = 8

print(a == b) # Output: False
print(a != b) # Output: True
print(a > b)  # Output: False
print(a < b)  # Output: True
print(a >= b) # Output: False
print(a <= b) # Output: True
```

## 3. Operadores Lógicos

Realizam operações lógicas em valores booleanos.

*   `and`: E lógico (retorna True se ambos os operandos forem True)
*   `or`: Ou lógico (retorna True se pelo menos um dos operandos for True)
*   `not`: Negação lógica (inverte o valor booleano)

**Exemplos:**

```python
a = True
b = False

print(a and b) # Output: False
print(a or b)  # Output: True
print(not a)  # Output: False
```

## 4. Operadores de Atribuição

Atribuem valores a variáveis.

*   `=`: Atribuição simples
*   `+=`: Adição e atribuição (x += 1 é o mesmo que x = x + 1)
*   `-=`: Subtração e atribuição
*   `*=`: Multiplicação e atribuição
*   `/=`: Divisão e atribuição
*   `//=`: Divisão inteira e atribuição
*   `%=`: Módulo e atribuição
*   `**=`: Exponenciação e atribuição

**Exemplos:**

```python
x = 5
x += 2  # x = x + 2 (x agora é 7)
print(x)  # Output: 7

x -= 1  # x = x - 1 (x agora é 6)
print(x)  # Output: 6
```

## 5. Operadores de Identidade

Verificam se dois objetos são o mesmo objeto (mesmo local na memória).

*   `is`: É o mesmo objeto
*   `is not`: Não é o mesmo objeto

**Exemplos:**

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b) # Output: True (a e b referenciam o mesmo objeto)
print(a is c) # Output: False (a e c são objetos diferentes, mesmo que tenham o mesmo conteúdo)
```

## 6. Operadores de Associação

Verificam se um valor está presente em uma sequência (lista, tupla, string, etc.).

*   `in`: Está presente
*   `not in`: Não está presente

**Exemplos:**

```python
frutas = ["maçã", "banana", "laranja"]

print("banana" in frutas) # Output: True
print("uva" in frutas)    # Output: False