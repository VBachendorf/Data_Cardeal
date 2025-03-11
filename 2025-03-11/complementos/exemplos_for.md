# Exemplos de Laços `for` em Python

## 1. Imprimindo Números Sequencialmente

```python
for i in range(5):
    print(i)
```

**Explicação:** Este exemplo demonstra como usar o loop `for` com a função `range()` para imprimir números de 0 a 4.

## 2. Iterando sobre uma Lista

```python
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)
```

**Explicação:** Este exemplo demonstra como iterar sobre cada elemento de uma lista. A variável `fruta` assume o valor de cada item na lista `frutas` a cada iteração do loop.

## 3. Iterando sobre uma String

```python
mensagem = "Olá"
for letra in mensagem:
    print(letra)
```

**Explicação:** Strings em Python podem ser iteradas como listas de caracteres. Este loop imprime cada letra da string "Olá" em uma linha separada.

## 4. Iterando sobre um Dicionário (Chaves)

```python
pessoa = {"nome": "Alice", "idade": 30, "cidade": "São Paulo"}
for chave in pessoa:
    print(chave)
```

**Explicação:** Por padrão, a iteração sobre um dicionário itera sobre suas chaves. Este exemplo imprime cada chave do dicionário `pessoa`.

## 5. Iterando sobre um Dicionário (Valores)

```python
pessoa = {"nome": "Alice", "idade": 30, "cidade": "São Paulo"}
for valor in pessoa.values():
    print(valor)
```

**Explicação:** Para iterar sobre os valores de um dicionário, usamos o método `.values()`. Este loop imprime cada valor do dicionário `pessoa`.

## 6. Iterando sobre um Dicionário (Chaves e Valores)

```python
pessoa = {"nome": "Alice", "idade": 30, "cidade": "São Paulo"}
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
```

**Explicação:** Para iterar tanto sobre as chaves quanto sobre os valores de um dicionário simultaneamente, usamos o método `.items()`. Este loop imprime cada par chave-valor do dicionário `pessoa`.