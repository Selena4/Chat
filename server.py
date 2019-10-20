import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind (('25.1.220.6',5050))
names = {}
nnames = []
client = [] # Массив где храним адреса клиентов
print ('Start Server')
while 1 :
    try:
        data , adress = sock.recvfrom(1024)
        com = str(data)
        if "!users" in com:
            sock.sendto("\n-Users online:".encode(),adress)
            ips = []
            for i in client:
                if i[0] in ips:
                    continue
                else:
                    ips.append(i[0])
            for _ in ips:
                sock.sendto((_ + " ("+names[_] + ")").encode(),adress)
            sock.sendto("--------------\n".encode(),adress)
        if com == '5kj3hn5j23h523nf':
            client.remove(adress)
        if com[2:7] == "[3gs]":
            names[str(adress[0])] = com[7:-1]
            continue
        print (adress[0] + ' send message (' + data.decode('utf-8')+ ')')
        if  adress not in client :
            client.append(adress)# Если такова клиента нету , то добавить
        for clients in client :
            if clients == adress : 
                continue # Не отправлять данные клиенту который их прислал
            sock.sendto(data,clients)
    except:
        print('ERROR')
