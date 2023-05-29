#Definindo as váriaveis. A variável "salario" é float, pois possui casas decimais, enquanto a variável "porc" é inteira, por não precisar de casas decimais.
salario=float(input("Insira seu salário: "))
porc=int(input("Qual a porcentagem do aumento (não incluir sinal de porcentagem): "))

#Aqui eu defini a varíavel "aumento" como o valor do salario + o salario vezes a porcentagem. 
aumento=salario+(salario*(porc/100))

#Primeiro exibi o salário, só pelo visual mesmo :D
print("Seu salário é de R${}".format(salario))

#Aqui eu usei o format pra inserir a porcentagem e o salário com aumento nas chaves
#.format(PORCENTAGEM , AUMENTO)
#Usei o round pra exibir só duas casas decimais também.
#round(AUMENTO , <NUMERO DE CASAS DECIMAIS>)
print("Com {}% de aumento, seu salário é de: R${}".format(porc,round(aumento, 2)))
