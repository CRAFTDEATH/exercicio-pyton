#5. Faça um programa que o usuário informe o salário recebido e o total gasto.
#Deverá ser exibido na tela “Gastos dentro do orçamento” caso o valor gasto não
#ultrapasse o valor do salário e “Orçamento estourado” se o valor gasto
#ultrapassar o valor do salário.

salario = float(input('Digite o valor do salario:'))
gasto = float(input('Digite o total de gastos:'))

if gasto <= salario:
    print('O salário de R$ %.2f, que tem o gasto de R$ %.2f está dentro do orçamento' %(salario,gasto))
else:
    print('O salário de R$ %.2f, que tem o gasto de R$ %.2f não está dentro do orçamento' % (salario, gasto))

