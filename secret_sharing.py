from decimal import *
from random import *


getcontext().prec = 10000


class Encoder:
	def __init__(self, message: str, keys: int):
		self._message = Converter().string_to_int(message)
		self._keys = keys
		self._coefficients = [0]
		for i in range(1, keys):
			self._coefficients.append(randint(0, self._message))

	def get_key(self, key=None):
		if key is None:
			key = randint(0, self._message)
		encrypted = 0
		for i in range(self._keys):
			encrypted += (key ** i) * self._coefficients[i]
		return key, encrypted + self._message


class Decoder:
	def __init__(self, key_list: list):
		self._key_list = key_list

	def decrypt(self):
		decrypted = 0
		for i in range(len(self._key_list)):
			temp_result = Decimal(1)
			for j in range(len(self._key_list)):
				if i != j:
					temp_result *= Decimal(self._key_list[j][0]) / (Decimal(self._key_list[j][0]) - Decimal(self._key_list[i][0]))
			decrypted += temp_result * Decimal(self._key_list[i][1])
		return Converter().int_to_string(int(decrypted))




class Converter:
	"""
	>>> c = Converter()
	>>> c.int_to_string(c.string_to_int('abcdefghijklnmopqrstuvwxyz'))
	'abcdefghijklnmopqrstuvwxyz'
	"""

	def __init__(self, seed = 1024):
		self.seed = seed

	def string_to_int(self, string: str):
		i = 0
		for char in string:
			i *= self.seed
			i += ord(char)
		return i

	def int_to_string(self, number: int):
		string = ""
		while number:
			string += chr(number % self.seed)
			number //= self.seed
		return string[::-1]


e = Encoder('ffkjnbkdjfnbvkdfjnklwjfbnlkwdjfvnlkwfjvnwlkfjvnwkljdfvnkwjfvnkwjfnvlkwjfvnlwjkfdbvjwhbcvh,wgvcwhsdgcvhwdsbvjsbjkwsdbv,jwsdbvhjdwsbvh', 3)
l = [e.get_key() for _ in range(3)]
for i in l:
	print(i)
print(Decoder(l).decrypt())
print(Converter().string_to_int('ffkjnbkdjfnbvkdfjnklwjfbnlkwdjfvnlkwfjvnwlkfjvnwkljdfvnkwjfvnkwjfnvlkwjfvnlwjkfdbvjwhbcvh,wgvcwhsdgcvhwdsbvjsbjkwsdbv,jwsdbvhjdwsbvh'))