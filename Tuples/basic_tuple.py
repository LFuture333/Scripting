# array with numbers 
L = [4,5,5,5,6,7]

res= []

# basic for loop
for index, element in enumerate(L):
    res.append((element, index))

print("List of tuples")
print(res)
