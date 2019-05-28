import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 8000))
sock.listen(5)
print("Server started")
print("Waiting for client request..")

clientConnection,adress = sock.accept()

while True:
	in_data = clientConnection.recv(1024)
	msg = in_data.decode()
	if msg == '':
		break
	out_data = [int(num) for num in msg.split()]
	det = out_data[0]*out_data[3]-out_data[2]*out_data[1]
	change_out_data = (i * det for i in out_data)
	str_out_data = ' '.join(str(i) for i in change_out_data)
	clientConnection.send(bytes(str_out_data, 'UTF-8'))

clientConnection.close()
sock.close()