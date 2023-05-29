while True:
    num = int(input("Insira um número (-1 para terminar) > "))
    if num == -1:
        break
    result = 1
    cont = 1
    while cont <= num:
        result *= cont
        cont += 1
    print ("{}! = {}".format(num,result))