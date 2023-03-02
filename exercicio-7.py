#7. Elabore um algoritmo que dada a idade de um nadador classifica-o em uma das
#seguintes categorias:
#infantil A = 5 - 7 anos
#infantil B = 8-10 anos
#juvenil A = 11-13 anos
#juvenil B = 14-17 anos
#adulto = maiores de 18 anos

idade = int(input('Digite a idade:'))
if idade >= 5 and idade <= 7:
    print('Categoria infantil A')
if idade >= 8 and idade <= 10:
    print('Categoria infantil B')
if idade >= 11 and idade <= 13:
    print('Categoria juvenil A')
if idade >= 14 and idade <= 17:
    print('Categoria juvenil B ')
if idade >= 18:
    print('Categoria adulto')

