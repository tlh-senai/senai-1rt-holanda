do=True
while do == True:
    num1=float(input("Insira o primeiro valor > "))
    num2=float(input("Insira o segundo valor > "))

    op=str(input("Escolha a operação a ser realizada (+, -, *, /, **) > "))
    if op == "+":
        print ("{} + {} = {}".format(num1,num2,num1+num2))
    elif op == "-":
        print ("{} - {} = {}".format(num1,num2,num1-num2))
    elif op == "*":
        print ("{} * {} = {}".format(num1,num2,num1*num2))
    elif op == "/":
        print ("{} / {} = {}".format(num1,num2,num1/num2))
    elif op == "**":
        print ("{} ** {} = {}".format(num1,num2,num1**num2))
    do = str(input("Novamente? (s/n) > "))
    if do == "s" or do == "S":
        do = True
    else:
        do = False