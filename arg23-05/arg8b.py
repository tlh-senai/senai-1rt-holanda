dec=(str(input("Aperte 1 para inserir o valor do dólar ou 2 para inserir o valor do real: ")))
if dec == "1":
    dolar = float(input("Insira o valor em dólares: "))
    real = dolar * 4.97
    print ("${} = R${}".format(round(dolar, 2),round(real, 2)))
elif dec == "2":
    real = float(input("Insira o valor em reais: "))
    dolar = real / 4.97
    print ("R${} = ${}".format(round(real, 2),round(dolar, 2)))