from secret_sharing import *

getcontext().prec = 1000

# Encode the message and get 3 keys
e = Encoder('This is an Epic TestMessage!', keys=3)
keys = [e.get_key() for _ in range(3)]

# Decode the message using 3 keys
d = Decoder(keys)
print(d.decrypt())  # 'This is an Epic TestMessage!'
