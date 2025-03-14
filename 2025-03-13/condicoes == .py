# Verifique se o nome digitado será Tomas
nome = str(input('Digite um nome: '))
nome_procurado = 'Tomas'

if (nome == nome_procurado):
    print('os nomes são iguais')

else:
    print(f'O nome não é {nome_procurado}')