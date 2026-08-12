import socket

host = "127.0.0.1"
port = 4444

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cliente.sendto("AAAAAAAAAAAAAA".encode(),(host, port))

dados, endereço = cliente.recvfrom(4096)
print(dados.decode())
