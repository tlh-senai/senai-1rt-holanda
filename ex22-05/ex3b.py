nome=input("Seu nome: ")
dia=input("Dia de nascimento: ")
escext=input("Digite '1' para escrever o mês por extenso ou '2' para escrever númericamente")
if escext=="1":
    mes1=input("Escreva o mês por extenso: ")
elif escext=="2":
    mes2=input("Escreva o mês númericamente: ")
ano=input("Ano de nascimento: ")

if escext=="1":
    print("Olá",nome+", você nasceu no dia",dia,"de",mes1,"de",ano+".")
elif escext=="2":
    print("Olá",nome+", você nasceu em",dia + "/" + mes2 + "/" + ano + ".")