def som(a,b):
    return (a+b)
def mult(a,b):
    return (a*b)
def maior(a,b):
    l = [a,b]
    return max(l)
def menor(a,b):
    l = [a,b]
    return min(l)

while True:
    n1 = float(input("Insira o primeiro valor:\n> "))
    n2 = float(input("Insira o segundo valor:\n> "))

    op = str(input("Qual operação realizar?\na. Soma\nb. Multiplicação\nc. Maior número\nd. Menor número\nq. Encerrar\n\n>> "))
    if op == "a" or op == "A":
        print ("A soma de {} e {} é igual a {}\n".format(n1,n2,som(n1,n2)))
    elif op == "b" or op == "B":
        print ("A multiplicação de {} e {} é igual a {}\n".format(n1,n2,mult(n1,n2)))
    elif op == "c" or op == "C":
        print ("O maior número entre {} e {} é {}\n".format(n1,n2,maior(n1,n2)))
    elif op == "d" or op == "D":
        print ("O menor número entre {} e {} é {}\n".format(n1,n2,menor(n1,n2)))
    elif op == "q" or op == "Q":
        print ("Programa encerrado")
        break
    else:
        print ("Operação invalida!\n")