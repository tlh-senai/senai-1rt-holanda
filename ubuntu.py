hostname="ubuntuholanda"
systemon = True
users=["holanda", "root"]
senha="Senai@134"
print("Ubuntu 16.04 LTS ubuntu tty\n")
senhac = False
mkdird=[]
comandos=["pwd","ls","lsblk","poweroff","mkdir","","ls /","sudo su","exit"]
while senhac == False:
	systemon = True
	login=input("{} login: ".format(hostname))
	if login in users:
		loginsenha=input("Password: ")
		if loginsenha == senha:
			senhac = True
			print("Last Login: Thu May 25 14:16:25 BRT 2023 on tty \nWelcome to Ubuntu 16.04 LTS (GNU/Linux 4.4.0-21-generic x64_64) \n")
		else:
			print ("Incorrect login")
			senhac = False
	else:
		print ("Incorrect login")
while systemon == True:
	if login == "holanda":
		linhadecomando=input("{}@{}:~$ ".format(login,hostname))
		if linhadecomando in comandos:
			if linhadecomando == "pwd":
				print("/home/holanda/")
			if linhadecomando == "ls":
				print (mkdird)
			if linhadecomando == "mkdir":
				mkdird=mkdird + [input()]
			if linhadecomando == "rm -r *":
				mkdird=[]
			if linhadecomando == "lsblk":
				print("sda\n└sda1\n└sda2")
			if linhadecomando == "poweroff":
				systemon = False
			if linhadecomando == "ls /":
				print ("/bin /boot /cdrom /dev /etc \n/home /lib /lib64 /media /mnt \n/opt /proc /root /run /sbin \n/srv /sys /tmp /usr /var")
			if linhadecomando == "sudo su":
				loginsenha = input("Password: ")
				if loginsenha == senha:
					login = "root"
				else:
					print("Incorrect login")
			if linhadecomando == "exit":
				systemon = False
		else:
			print("bash: {}: not found".format(linhadecomando))
	if login == "root":
		linhadecomando=input("{}@{}:~# ".format(login,"localhost"))
		if linhadecomando in comandos:
			if linhadecomando == "pwd":
				print("/root/")
			if linhadecomando == "ls":
				print (mkdird)
			if linhadecomando == "mkdir":
				mkdird=mkdird + [input()]
			if linhadecomando == "rm -r *":
				mkdird=[]
			if linhadecomando == "lsblk":
				print("sda\n└sda1\n└sda2")
			if linhadecomando == "ls /":
				print ("/bin /boot /cdrom /dev \n/etc /home /lib /lib64 \n/media /mnt /opt /proc \n/root /run /sbin /srv \n/sys /tmp /usr /var")
			if linhadecomando == "poweroff":
				systemon = False
			if linhadecomando == "exit":
				login = "holanda"
		else:
			print("bash: {}: not found".format(linhadecomando))