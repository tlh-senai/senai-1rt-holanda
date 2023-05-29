nome=input("Insira seu nome: ")
dia=input("Insira o dia de seu nascimento: ")
mes=input("Insira o mês de seu nascimento: ")
ano=input("Insira o ano de seu nascimento: ")

if mes=="1":
    mes="Janeiro"
if mes=="2":
    mes="Fevereiro"
if mes=="3":
    mes="Março"
if mes=="4":
    mes="Abril"
if mes=="5":
    mes="Maio"
if mes=="6":
    mes="Junho"
if mes=="7":
    mes="Julho"
if mes=="8":
    mes="Agosto"
if mes=="9":
    mes="Setembro"
if mes=="10":
    mes="Outubro"
if mes=="11":
    mes="Novembro"
if mes=="12":
    mes="Dezembro"

print("Olá",nome+", você nasceu no dia",dia,"de",mes,"de",ano+".")