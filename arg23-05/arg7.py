celsius=float(input("Insira a temperatura em C°: "))
def conversao(a):
    return ((a * 9/5)+32)
fahrenreit=conversao(celsius)
print("Temperatura em Celsius: {} C°".format(celsius))
print ("Temperatura em Fahrenreit: {} F°".format(fahrenreit))