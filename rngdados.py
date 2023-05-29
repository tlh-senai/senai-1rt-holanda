import random

while True:
	s = 0
	t = "p"
	
	q = (input("\nQuantos dados serão rolados?\n> "))
	if q == "":
		q = 1
	else:
		q = int(q)
	if q == 0:
		esc = input("Deseja encerrar o programa? (s/n)\n> ")
		if esc == "s" or esc == "S":
			break


	d = (input("Quantos lados deve ter o dado?\n> "))
	if d == "":
		num = [4,6,8,10,12,20,100]
		d = random.choice(num)
	else:
		d = int(d)
	if d < 2:
		esc = input("Deseja encerrar o programa? (s/n)\n> ")
		if esc == "s" or esc == "S":
			break
	
	if q > 1:
		t = input("Lista ordenada somada ou rolagens separadas? (L/S)\n> ")
	
	mais = (input("Insira o valor a ser somado a rolagem ou 0\n> "))
	if mais == "":
		mais = 0
	else:
		mais = int(mais)
	s += mais
	
	
	if t == "L" or t == "l":
		r = []
		for i in range(0,q):
			r += [random.randint(1,d)]
		r.sort(reverse=True)
		print ("{}d{}+{} \n\n{} = {} [{}]".format(q,d,s,r,sum(r),sum(r)+s))
	
	elif t == "S" or t == "s":
		print ("{}#d{}+{}\n".format(q,d,s))
		for i in range(0,q):
			rand = random.randint(1,d)
			print("d{}+{} = {} [{}]".format(d,s,rand,rand+s))
	elif t == "p":
			rand = random.randint(1,d)
			print("1d{}+{}\n\n{} [{}]".format(d,s,rand,rand+s))
			
	else:
		print ("Opção inválida // '{}'".format(t))