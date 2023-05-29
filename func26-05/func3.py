def maior(a,b,c):
    l = [a,b,c]
    return max(l)

n1 = float(input("Primeiro número\n> "))
n2 = float(input("Segundo número\n> "))
n3 = float(input("Terceiro número\n> "))

print("Maior número:\n>> "+str(maior(n1,n2,n3)))