import socket 
import encrypt
import utils 

PAYLOAD = 'Golden Jubille'

REMOTE_HOST = '10.10.98.79'
REMOTE_PORT = 9999
REMOTE_ADDR = (REMOTE_HOST, REMOTE_PORT)

CRYPT_KEY = 'plainmessage'

chat_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	chat_socket.connect(REMOTE_ADDR)
	socket_file = chat_socket.makefile('r')
	try:
		#Send encrypted payload
		data_out =encrypt.encrypt(CRYPT_KEY, PAYLOAD.encode())
		chat_socket.sendall(utils.encode_data(data_out))
		#wait for reply, which is double-encrypted payload\
		data_in = utils.decode_data(socket_file.readline())
		#Remove our padlock
		data_out = encrypt.encrypt(CRYPT_KEY, data_in)
		chat_socket.sendall(utils.encode_data(data_out))
	finally:
		socket_file.close()
finally:
	chat_socket.close()



