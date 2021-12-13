import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = '192.168.0.133'
PORT = 12333
listener.bind((IP, PORT))
listener.listen(5)
connection, address = listener.accept()
connection.send("Connected".encode('utf8'))

alfavit_zifri = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

while True:
    data = connection.recv(1024).decode('utf8')
    print(data)
    print('----------------------')

    zbilshenya = int(input('key:'))
    message = input("Message:")
    widpovid = ''
    for a in message:
        old_bukva = alfavit_zifri.find(a)
        new_bukva = old_bukva + zbilshenya
        if a in alfavit_zifri:
            widpovid += alfavit_zifri[new_bukva]
        else:
            widpovid += a
        
    connection.send(widpovid.encode('utf8'))
    
    
    if not data: 
        continue