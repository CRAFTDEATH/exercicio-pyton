# 6. Faça o algoritmo que leia o valor de uma conta de luz (CL) e, caso o valor seja
# maior que R$ 150,00, apresente a mensagem: “Você está gastando muito”. Caso
# contrário exiba a mensagem: “Seu gasto foi normal”.

conta = float(input('Digite o valor da conta de força:'))

if conta > 150:
    print("Você está gastando muito")
else:
    print("Seu gasto foi normal")