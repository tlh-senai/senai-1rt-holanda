import random

def soma(a,b):
    return (a+b)

n1 = random.randint(1,100)
n2 = random.randint(1,100)

print ("{} + {}\n---------\n>> {} <<\n---------\nCONCLUÍDO".format(n1,n2,soma(n1,n2)))