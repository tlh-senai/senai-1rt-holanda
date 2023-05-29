veloc=int(input("Em qual velocidade você estava? > "))
if veloc > 80:
    valor=(veloc-80)*7
    print("Você estava indo a {}km/h, que é acima do limite de 80km/h.".format(veloc))
    print("Você recebeu uma multa no valor de R${}.".format(valor))
elif veloc == 80:
    print("Quase ein.")
else:
    print("Tudo certo.")
    