n=float(input("Insira um valor em R$: "))
def conversao(a):
    return (a/4.98)
ndl=round(conversao(n), 2)

print ("Real brasileiro: R${}".format(round(n, 2)))
print ("Dólar americano: ${}".format(ndl))