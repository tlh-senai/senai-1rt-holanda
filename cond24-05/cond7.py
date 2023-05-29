nota=int(input("Insira sua nota da Olimpiada do Conhecimento do SENAI São Paulo: "))
if nota <= 50:
    print ("Pela pontuação de {} pontos, você receberá um Certificado de Participação.".format(nota))
elif nota <= 60:
    print ("Pela pontuação de {} pontos, você receberá um Certificado de Menção Honrosa.".format(nota))
elif nota <= 70:
    print ("Pela pontuação de {} pontos, você receberá uma Medalha de Bronze!".format(nota))
elif nota <= 90:
    print ("Pela pontuação de {} pontos, você receberá uma Medalha de Prata!".format(nota))
elif nota > 90:
    print ("Parabéns pela pontuação de {} pontos! Como prêmio, você receberá a Medalha de Ouro!!".format(nota))
