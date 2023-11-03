import numpy as np
import base64

x = np.array([0, 0.6, 65, 2, 5])

y = np.array([0, 0, 0, 45, 56])




point = (x,y)

#Encryption

byte_data = str(point).encode('utf-8')
encoded_data = base64.b64encode(byte_data)

print(encoded_data)

decode_data = base64.b64decode(encoded_data)

data = decode_data.decode('utf-8')


print(data)
