words = ['hello', 'world', 'this', 'is', 'great']
line =(" ".join(words))
print(line)
print(len(line))

s = {1,2,3}
s.add(4)
print(s)
l = [1,2,3]
l.append(4)
print(l)
print(len(s) == len(l))

a = ["hello"]
b = ["world"]
add = a+b
print(" ".join(add))
print(type(add))
