from base64 import b64decode, b64encode

def decode_data(data):
	if isinstance(data, str):
		data = data.encode()
	if data == b'':
		raise ValueError('Disconneted')
	return b64decode(data.rstrip(b'\n\r'))

def encode_data(data):
	if isinstance(data, str):
		data = data.encode()
	return b64encode(data) + b'\n'