import threading
import socket

host = '127.0.0.1' #local host
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()

            nickname = nicknames[index]
            broadcast(f'{nickname} has left the chat'.encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f'connected with {str(address)}')

        client.send('buyorsell'.encode('ascii'))
        buyorsell = client.recv(1024).decode('ascii')

        if buyorsell == 'b':
            client.send('NICKNAME'.encode('ascii'))
            nickname = client.recv(1024).decode('ascii')
            nicknames.append(nickname)
            clients.append(client)

            print(f'Nickname of the client is {nickname}')
            broadcast(f'-> {nickname} has joined the chat to buy'.encode('ascii'))

            client.send('connected to the server'.encode('ascii'))

            thread = threading.Thread(target=handle, args=(client,))
            thread.start()
        else:
            client.send('NICKNAME'.encode('ascii'))
            nickname = client.recv(1024).decode('ascii')
            nicknames.append(nickname)
            clients.append(client)

            client.send('CAR NAME'.encode('ascii'))
            car_name = client.recv(1024).decode('ascii')

            client.send('CAR TYPE'.encode('ascii'))
            car_type = client.recv(1024).decode('ascii')

            client.send('KMS RUNNED'.encode('ascii'))
            kms = client.recv(1024).decode('ascii')

            client.send('YEARS RUNNED'.encode('ascii'))
            years = client.recv(1024).decode('ascii')

            client.send('PRICE'.encode('ascii'))
            price = client.recv(1024).decode('ascii')

            client.send('CONTACT'.encode('ascii'))
            contact = client.recv(1024).decode('ascii')

            client.send('ADDITIONAL INFORMATION'.encode('ascii'))
            addinfo = client.recv(1024).decode('ascii')

            print(f'Nickname of the client is {nickname}')

            broadcast(f'-> {nickname} has joined the chat with car {car_name} which is of type {car_type}'.encode('ascii'))
            broadcast(f'-> {nickname} s car has runned {kms} kilometers for {years} years'.encode('ascii'))
            broadcast(f'-> {nickname} is willing to sell his/her car for {price} bucks'.encode('ascii'))
            broadcast(f'-> Here are some additional information about {nickname} s car is below: '.encode('ascii'))
            broadcast(f'-> {addinfo}'.encode('ascii'))
            broadcast(f'-> Whoever is willing to buy {nickname} s car can contact this number {contact}\n'.encode('ascii'))

            client.send('connected to the server'.encode('ascii'))

            thread = threading.Thread(target=handle, args=(client,))
            thread.start()


print('......server is listening......')
receive()
