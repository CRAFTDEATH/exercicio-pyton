# 3. Escrever um programa para ler um número inteiro e informar se ele é divisível por 5.

divisivel = int(5);
numero = int(input('Digite um numero:'))

if numero % 5 == 0:
    print('O numero %d é divisvel por %d' % (numero, divisivel))
else:
    print('O numero %d não é divisvel por %d' % (numero, divisivel))
