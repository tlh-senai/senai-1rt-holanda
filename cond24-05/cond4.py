km=float(input("Qual a distância da viagem em km? > "))
if km <= 200:
    print("Essa viagem é de {}km. O preço da passagem sairá por R${}.".format(km,km*0.5))
else:
    print("Essa viagem é de {}km. O preço da passagem sairá por R${}.".format(km,km*0.45))