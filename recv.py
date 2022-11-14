import socket 
import encrypt
import utils

LISTEN_HOST = '0.0.0.0'
LISTEN_PORT = 9999
LISTEN_ADDR = (LISTEN_HOST, LISTEN_PORT)

CRYPT_KEY = 'secretmessage'

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	listen_socket.bind(LISTEN_ADDR)
	listen_socket.listen()
	chat_socket, address = listen_socket.accept()
	print(f'Connection from {address}')
	socket_file = chat_socket.makefile('r')
	try:
		# Receive padlock packet
		data_in = utils.decode_data(socket_file.readline())
		# Add own lock and return packet
		data_out = encrypt.encrypt(CRYPT_KEY, data_in)
		chat_socket.sendall(utils.encode_data(data_out))
		# Received packet
		data_in = utils.decode_data(socket_file.readline())
		# Remove own padlock
		payload = encrypt.encrypt(CRYPT_KEY, data_in)
		print(f'Received {payload.decode()}!')
	finally:
		socket_file.close()
finally:
	listen_socket.close()