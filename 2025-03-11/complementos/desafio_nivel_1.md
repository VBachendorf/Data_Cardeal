# Desafio Nível 1: Calculadora de Média

**Tópico:** Desafio Nível 1

**Nível:** Amador (para alunos de 14 anos)

**Descrição:**

Crie um programa em Python que calcule a média de três notas inseridas pelo usuário.

**Instruções:**

1.  Peça ao usuário para inserir a primeira nota.
2.  Peça ao usuário para inserir a segunda nota.
3.  Peça ao usuário para inserir a terceira nota.
4.  Calcule a média das três notas.
5.  Exiba a média na tela.

**Exemplo de Saída:**

```
Digite a primeira nota: 7.5
Digite a segunda nota: 8.0
Digite a terceira nota: 9.0
A média é: 8.17
```

**Dicas:**

*   Use a função `input()` para receber as notas do usuário.
*   Lembre-se de converter as notas para números (float) usando a função `float()`.
*   Use a função `print()` para exibir a média na tela.

**Código de Exemplo (completar):**

```python
# Receber as notas do usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcular a média
media = (nota1 + nota2 + nota3) / 3

# Exibir a média
print("A média é:", media)