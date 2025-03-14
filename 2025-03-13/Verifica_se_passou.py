nome_aluno = str(input('Nome do Aluno(a): '))
nota_1 = float(input('Digite a primeira Nota: '))
nota_2 = float(input('Digite a segunda Nota: '))
nota_3 = float(input('Digite a terceira Nota: '))
soma = nota_1 + nota_2 + nota_3 
media = soma / 3

if media >= 6:
    print(f'O aluno(a) {nome_aluno} está Aprovado(a) com média de {media}')
else:
    print(f'O aluno(a) {nome_aluno} está Reprovado(a) com média de {media}')
    
# O aluno(a) Jaburu está Aprovado(a) com média de 7.15
