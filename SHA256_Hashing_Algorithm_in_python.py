from hashlib import sha256
# Output is a 256 bits long sequence (message digest)
# This is the hash Bitcoin uses
# The result is a 64 character long hexadecimal sequence
# 1 hexadecimal character can be stored on 4 bits

s1 = 'My name is Malik.'
s2 = 'My name is Malik'
result1 = sha256(s1.encode())
print(result1.hexdigest())
# We can see because of the avalanche effect, these two hashes are completly different even though the difference is just a point
result2 = sha256(s2.encode())
print(result2.hexdigest())