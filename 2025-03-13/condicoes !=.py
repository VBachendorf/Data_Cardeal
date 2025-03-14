# Verifique se o nome digitado será Tomas
nome = str(input('Digite um nome: '))
nome_procurado = 'Tomas'

# o nome não pode ser Tomas!
if nome != nome_procurado:
    print(f'Nome {nome} Permitido')
else:
    (f'Nome {nome} não permitido')