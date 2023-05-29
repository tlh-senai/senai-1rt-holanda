print ("\n> CALCULADORA DE ÁREA <\n")

while True:
    def area(a,b):
        return(a*b)
   
    largura=float(input("Insira a largura.\n> "))
    comprimento=float(input("Insira o comprimento.\n> "))
    r = area(largura,comprimento)

    print("Largura = {}\nComprimento = {}\n\nÁrea = {} * {} = {:.2f}m²\n({}m²)\n".format(largura,comprimento,largura,comprimento,r,r))