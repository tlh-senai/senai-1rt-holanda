n=int(input("Informe um número > "))

print  (n)
if n == 2:
    print ("Seu número é primo!")
elif n % n == 0 and n % 2 != 0:
    print ("Seu número é primo!")
else:
    print ("Seu número não é primo.")