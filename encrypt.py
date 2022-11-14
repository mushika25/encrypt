import random

def get_random_bytes(seed, count):
	R = random.Random(seed)
	return [R.randint(0,225) for i in range(count)]

def encrypt(key, data):
	random_bytes = get_random_bytes(key, len(data))
	return bytes ([data[i] ^ random_bytes[i] for i in range(len(data))])