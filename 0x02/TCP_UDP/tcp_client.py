import socket

target_host = "0.0.0.0"
target_port = 9999

# criar um objeto socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# conectar o cliente
client.connect((target_host, target_port))

# enviar alguns dados
client.send(b"ABCDEF\r\n\r\n")

# receber alguns dados
response = client.recv(4096)

print(response.decode())
client.close()