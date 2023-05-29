nota1=float(input("Insira a primeira nota: "))
nota2=float(input("Insira a segunda nota: "))
nota3=float(input("Insira a terceira nota: "))

media = (nota1+nota2+nota3)/3

print ("Média = {:.2f}".format(media))
if media < 5:
    print("Nota abaixo da média.")
elif media < 6:
    print("Foi pra recuperação.")
else:
    print("Parabéns! Nota acima da média.")