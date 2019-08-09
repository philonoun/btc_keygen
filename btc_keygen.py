from bitcoin import *

#generates random private key
my_private_key = random_key()

#associates a public key from private key
my_public_key = privtopub(my_private_key)

#creates a public address from public key
my_bitcoin_address = pubtoaddr(my_public_key)

#prints bitcoin address
print(my_bitcoin_address)
