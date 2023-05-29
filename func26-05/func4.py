while True:
    def ver_par(a):
        if a % 2 == 0:
            par = True
        else:
            par = False
        return par

    n = int(input("Insira um número:\n> "))
    par = ver_par(n)
    if par == True:
        print (n,"é um número par.\n")
    else:
        print (n,"é um número ímpar.\n")