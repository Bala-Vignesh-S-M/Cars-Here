import socket
import threading


buyorsell = input("buy or sell(b/s)")

if buyorsell == 's':
    nickname = input("Choose a nickname : ")
    car_name = input("Enter the name of your car : ")
    car_type = input("Enter the type of your car : ")
    kms = input("Enter kilometers your car runned : ")
    years = input("Enter the number of years your car has been used : ")
    price = input("Enter your price to sell your car : ")
    contact = input("Enter your contact Details : ")
    addinfo = input("Enter the Additional informations about your car : ")
else:
    nickname = input("Choose a nickname : ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'buyorsell':
                client.send(buyorsell.encode('ascii'))
            elif message == 'NICKNAME':
                client.send(nickname.encode('ascii'))
            elif message == 'CAR NAME':
                client.send(car_name.encode('ascii'))
            elif message == 'CAR TYPE':
                client.send(car_type.encode('ascii'))
            elif message == 'KMS RUNNED':
                client.send(kms.encode('ascii'))
            elif message == 'YEARS RUNNED':
                client.send(years.encode('ascii'))
            elif message == 'PRICE':
                client.send(price.encode('ascii'))
            elif message == 'CONTACT':
                client.send(contact.encode('ascii'))
            elif message == 'ADDITIONAL INFORMATION':
                client.send(addinfo.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()