while True:
    n = int(input("Insira um número > "))
    if n < 0:
        break
    if n % 2 == 0:
        print ("Número par.")
    else:
        print ("Número impar.")
print ("\n\nFINALIZADO\n\n")