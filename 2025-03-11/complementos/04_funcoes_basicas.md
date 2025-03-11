# Funções Básicas em Python: print() e input()

## 1. Função print()

**O que é:** A função `print()` é usada para exibir informações na tela (saída padrão).

**Sintaxe:**

```python
print(objeto(s), sep=separador, end=fim, file=arquivo, flush=True/False)
```

*   `objeto(s)`: Um ou mais objetos a serem exibidos.
*   `sep`: Separador entre os objetos (padrão é um espaço).
*   `end`: O que é exibido no final da linha (padrão é uma quebra de linha `\n`).
*   `file`: Onde a saída é escrita (padrão é a tela).
*   `flush`: Força a saída a ser escrita imediatamente (padrão é False).

**Exemplos:**

```python
print("Olá, mundo!")  # Exibe "Olá, mundo!" na tela
nome = "Alice"
print("Olá,", nome)  # Exibe "Olá, Alice" na tela
print(1, 2, 3, sep="-")  # Exibe "1-2-3" na tela
print("Esta linha", end=" ")
print("continua na mesma linha")  # Exibe "Esta linha continua na mesma linha"
```

## 2. Função input()

**O que é:** A função `input()` é usada para receber informações do usuário (entrada padrão).

**Sintaxe:**

```python
input(prompt)
```

*   `prompt`: Uma mensagem opcional exibida ao usuário antes de receber a entrada.

**Exemplos:**

```python
nome = input("Digite seu nome: ")  # Exibe "Digite seu nome: " e armazena a entrada do usuário na variável nome
idade = input("Digite sua idade: ")  # Exibe "Digite sua idade: " e armazena a entrada do usuário na variável idade (como string)
idade = int(input("Digite sua idade: "))  # Converte a entrada do usuário para inteiro
```

**Observação:** A função `input()` sempre retorna uma string. Se você precisar de um tipo diferente (inteiro, float, etc.), você deve converter a string usando as funções apropriadas (int(), float(), etc.).