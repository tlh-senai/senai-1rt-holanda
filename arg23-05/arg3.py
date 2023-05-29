nota1=float(input("Insira a primeira nota: "))
nota2=float(input("Insira a segunda nota: "))
nota3=float(input("Insira a terceira nota: "))

def media(a,b,c):
    return((a+b+c)/3)

print ("Média = {}".format(round(media(nota1,nota2,nota3), 1)))
if media(nota1,nota2,nota3) < 6:
    print("Nota abaixo da média.")
elif media(nota1,nota2,nota3) >= 6:
    print("Parabéns! Nota acima da média.")