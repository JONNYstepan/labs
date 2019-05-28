import socket

client = socket.socket()
client.connect(("127.0.0.1", 8000))
out_data_ = input("Введите значения матрицы 2 х 2: ")
client.send(bytes(out_data_, 'UTF-8'))

while True:
	in_data = client.recv(1024)
	print(in_data.decode())
	out_data = input("Введите значения матрицы 2 х 2: ")
	client.send((bytes(out_data, 'UTF-8')))
	if not out_data:
		break

client.close()