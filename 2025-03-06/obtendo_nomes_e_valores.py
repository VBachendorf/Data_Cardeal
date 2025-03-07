nome_cliente = str(input('Digite o nome do Cliente: '))
total_compra = float(input('Total da Compra: '))
valor_pago = float(input('Total Pagamento do Cliente: '))

#   O Cliente João efetuou uma compra de 455.00 R$
#   João realizou o pagamento de 470.00 R$
#   João receberá de troco 15.00 R$

print(f'O Cliente {nome_cliente} efetuou uma compra de {total_compra} R$') 
print(f'{nome_cliente} realizou o pagamento de {valor_pago} R$')
troco = valor_pago - total_compra 
print(f'{nome_cliente} receberá de troco {troco} R$')