import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 2222))
server_socket.listen(1)

print("Сервер запущен")

client_socket, client_address = server_socket.accept()
print(f"Подключение установлено с {client_address}")

a = 0
while a < 10:
    data = client_socket.recv(1024)
    print(f"Получены данные: {data}")

    client_socket.sendall(b'Hello!')
    print("Ответ отправлен")

client_socket.close()
server_socket.close()