#8. Escrever um algoritmo que leia o código do item pedido, a quantidade e calcule
#o valor a ser pago por aquele lanche. Considere que a cada execução somente
#será calculado um item.

codigo_cachoro_quente = 100
codigo_bauru_simples = 101
codigo_bauro_ovo = 102
codigo_hamburger = 103
codigo_cheesseburguer = 104
codigo_refrigerante = 105

codigo = int(input('Digite o codigo do produto:'))
quantidade = int(input('Digite quantia de produtos:'))

if codigo == codigo_cachoro_quente:
    calculo = float(quantidade * 1.20)
    print('O valor cachoro quente é %.2f:' % calculo)
if codigo == codigo_bauru_simples:
    calculo = float(quantidade * 1.30)
    print('O valor bauru simples é %.2f:' % calculo)
if codigo == codigo_bauro_ovo:
    calculo = float(quantidade * 1.50)
    print('O valor bauru com ovo é %.2f:' % calculo)
if codigo == codigo_hamburger:
    calculo = float(quantidade * 1.20)
    print('O valor hamburguer é %.2f:' % calculo)
if codigo == codigo_cheesseburguer:
    calculo = float(quantidade * 1.30)
    print('O valor cheesseburguer é %.2f:' % calculo)
if codigo == codigo_refrigerante:
    calculo = float(quantidade * 1.00)
    print('O valor refrigerante é %.2f:' % calculo)