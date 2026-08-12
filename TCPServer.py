import socket

host = "www.google" #input any website here to test
port = 80

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(host,port)

client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n".encode())

resposta = cliente.recv(4096)

print(resposta.decode())
