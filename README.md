# secret sharing

A simple python mini librairy to encrypt strings using [Shamir's secret sharing scheme](https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing#Mathematical_definition).

## usage

A basic example of how to use the code

```python
from secret_sharing import *

getcontext().prec = 1000

# Encode the message and get 3 keys
e = Encoder('This is an Epic TestMessage!', keys=3)
keys = [e.get_key() for _ in range(3)]

# Decode the message using 3 keys
d = Decoder(keys)
print(d.decrypt())  # 'This is an Epic TestMessage!'
```

I am using the decimal module, so to begin I have to set.

```python
getcontext().prec = 1000
```

This sets the precicion of the Decimals used. This must be set, if you don't you will suffer severe performance issues. A value of 1000 is a good start value. If you notice your secrets are not decoded correctly you can try to increase this value. The longer the message the higher the precision should be.

### Encryption

To encrypt your message you can make a `Encoder` object and this has 2 parameters:

+ message = (str) The message to be encoded.
+ keys = (int) The number of keys that should be enough to decrypt the message.

Then you can use `get_key()` to fetch a key.

### Decryption

To decrypt the message you should make a `Decoder` object which you have to provide a list of keys. It will assume the number of keys in the list is the number needed to decrypt the message. Then call decrypt() to decrypt the message.

## Notes

+ During the decoding you might nitice that the last character of the message can be different compared to the beginning, the rest of the message should be the same.
