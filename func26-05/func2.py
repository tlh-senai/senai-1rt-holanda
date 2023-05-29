from time import sleep

def cont_reg(a):
    while a > -1:
        print (a)
        a -= 1
        sleep(1)

n = int(input("Insira um número:\n> "))
print(cont_reg(n))