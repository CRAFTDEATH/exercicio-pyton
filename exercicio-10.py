# 10. Leia nome, salário e categoria de um funcionário, se a categoria for igual a “m”
# de mensalista, conceder 10% de aumento, se for igual a “h” de horista, conceder
# 20% de aumento, se não for “m” nem “h”, exibir a mensagem categoria inválida.

nome = str(input('Digite seu nome:'))
salario = float(input('Digite o salario:'))
categoria = str(input('Digite a categoria'))

if categoria == "m":
    calculo = ((salario * 10) / 100)
    total = salario + calculo
    print("O valor com aumento sera: %.2f" % total)

elif categoria == "h":
    calculo = ((salario * 20) / 100)
    total = salario + calculo
    print("O valor com aumento sera: %.2f" % total)
else:
    print('categoria inválida');
