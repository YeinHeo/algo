import hashlib

s = input()

data = s.encode()
hash_object = hashlib.sha256()
hash_object.update(data)
print(hash_object.hexdigest())
