veloc=int(input("Em qual velocidade você estava? > "))
if veloc > 80:
    print("Você estava indo a {}km/h, que é acima do limite de 80km/k.".format(veloc))
    print("Você recebeu uma multa.")
elif veloc == 80:
    print("Quase ein.")
else:
    print("Tudo certo.")