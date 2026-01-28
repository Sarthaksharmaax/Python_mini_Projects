user1 = {
    "name": "sarthak sharma",
    "age" : 20
}
print( "age" in user1)
# in is used to check whether particular key is in the dict or not.
print( user1.keys())
# to check all keys in dict.
print(user1.values())
# to check all values in dict.
items= user1.items()
print(user1.items())
print(type(items))

print(user1.update({"age" : 33}))
print(user1.values())
print(user1.update({"age":22}))
print(user1)


