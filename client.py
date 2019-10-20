import socket
import threading
def read_sok():
     while 1 :
         data = sor.recv(1024)
         print(data.decode('utf-8'))
server = '25.1.220.6', 5050  # Данные сервера
alias = input("enter your nickname: ") # Вводим наш псевдоним

print(alias+' connect to the server')
sor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sor.bind(('', 0)) # Задаем сокет как клиент
sor.sendto(("[3gs]" + alias).encode(),server)
sor.sendto((alias+' Connect to server').encode('utf-8'), server)# Уведомляем сервер о подключении

potok = threading.Thread(target= read_sok)
potok.daemon = True
potok.start()
while 1 :
	mensahe = input("")
	if mensahe[:5] == "!help":
		print('\n--------------\n!help - show thiis panel\n!nick [nickname] - change nick\n!users - show users\n!snick - show my nickname\n!exit\n--------------\n')
		continue
	if mensahe[:5] == "!nick":
		alias1 = alias
		alias = mensahe[6:]
		sor.sendto((alias1 + ' changed nickname to ' + alias).encode('utf8'),server)
		continue
	if mensahe[:6] == "!snick":
		print("Your nickname: " + alias)
		continue
	if mensahe[:5] == "!exit":
		sor.sendto((alias + " leave the server").encode('utf-8'),server)
		sor.sendto('5kj3hn5j23h523nf'.encode('utf-8'),server)
		sor.close()
		break
	sor.sendto(('['+alias+']'+mensahe).encode('utf-8'), server)
