# 4. A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários
# estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
# bruto. Fazer um algoritmo que permita entrar com o salário bruto e o valor da
# prestação e informar se o empréstimo pode ou não ser concedido.

limite = float(30)
salario_bruto = float(input('Digite o salario bruto:'))
prestacao = float(input('Digite a prestação:'))

calculo_limite = float(((salario_bruto * limite) / 100))

if prestacao <= calculo_limite:
    print('Essa prestação de %.2f R$ é posivel na regra de limite de credito de %.2f %%' % (prestacao, limite))
else:
    print('Essa prestação de %.2f R$ não é posivel na regra de limite de credito de %.2f %%' % (prestacao, limite))
