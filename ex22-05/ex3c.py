meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

mes_input = input("Digite o número ou nome do seu mês de nascimento: ")

if mes_input.isdigit():
    mes_numerico = int(mes_input)
    if mes_numerico >= 1 and mes_numerico <= 12:
        mes_nome = meses[mes_numerico - 1]
        print("O mês de nascimento é:", mes_nome)
    else:
        print("Mês inválido")
else:
    mes_input = mes_input.capitalize()
    if mes_input in meses:
        print("O mês de nascimento é:", mes_input)
    else:
        print("Mês inválido")






