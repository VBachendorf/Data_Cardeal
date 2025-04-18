numero_digitado = int(input('Digite um numero para saber se ele é primo!!'))
 # é preciso saber se ele é divisível por ele mesmo ou por 1
print(numero_digitado % 1 == 0 )

for i in range(numero_digitado):
    print(numero_digitado % i )