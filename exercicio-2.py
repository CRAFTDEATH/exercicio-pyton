# 2. Uma loja fornece 10% de desconto para funcionários e 5% de desconto para
# clientes vips. Faça um programa que calcule o valor total a ser pago por uma
# pessoa. O programa deverá ler o valor total da compra efetuada e um código que
# identifique se o comprador é um cliente comum (1), funcionário (2) ou vip (3).

cod_cliente_comum = int(1)
cod_funcionario = int(2)
cod_cliente_vip = int(3)

desconto_funcionario = float(10)
desconto_cliente_vip = float(5)

codigo = int(input('digite o codigo (1) para cliente comum e (2) para funcionario ou (3) para cliente vip:'))
valor = float(input('Digite o valor da compra:'))

desconto = float(0)

if codigo == cod_funcionario:
    desconto = float(((valor * desconto_funcionario) / 100))
if codigo == cod_cliente_vip:
    desconto = float(((valor * desconto_cliente_vip) / 100))

calculo = float(valor - desconto)

print('A compra de %.2f R$ com desconto de %.2f R$ é %.2f R$' % (valor, desconto, calculo))
