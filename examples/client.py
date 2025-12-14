import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 2222))

a = 0
while a < 10:
    client_socket.sendall(b'Hello, World!')
    a += 1
    response = client_socket.recv(1024)
    print(f"Получен ответ: {response}")

client_socket.close()