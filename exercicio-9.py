# 9. Uma empresa concederá um aumento de salário aos seus funcionários, variável
# de acordo com o cargo, conforme a tabela abaixo. Faça um algoritmo que leia o
# salário e o cargo de um funcionário (pelo código) e calcule o novo salário. Se o
# cargo do funcionário não estiver na tabela, ele deverá, então, receber 40% de
# aumento. Mostre o salário antigo, o novo salário e a diferença.

codigo_gerente = 101
codigo_engenheiro = 102
codigo_tecnico = 103

codigo = int(input('Digite o codigo:'))
salario = float(input('Digite o salario do funcionario:'))

if codigo == codigo_gerente:
    diferenca = float(((salario * 10) / 100))
elif codigo == codigo_engenheiro:
    diferenca = float(((salario * 20) / 100))
elif codigo == codigo_tecnico:
    diferenca = float(((salario * 30) / 100))
else:
    diferenca = float(((salario * 40) / 100))

novo_salario = salario + diferenca

print('Salario atual: R$ %.2f, Aumento: R$ %.2f, Novo salario R$ %.2f' % (salario,diferenca,novo_salario))
