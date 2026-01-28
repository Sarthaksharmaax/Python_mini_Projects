a= -1234.66
print(abs(a))
# abs() for changing negative int to a positive int
print(round(a))
# round() is for rounding off a float
print(len('HELLO WORLD'))

word = "sarthak sharma"
print(word[len(word)::-1])
list = [1,2,3,4,5]
for i in list:
    if(i>1):
        print(all(list))
#         print true value if the condition is true = all().


integer = 207
print(bin(integer))
# convert an integer number to a binary string prefixed with “0b”. The result is a valid Python expression.
print(bool(4<2))
# bool print true or false acc to condition.
uppper_case= 'ABHINAV is a boy'
print(uppper_case.lower())
print(uppper_case.upper())
# to lower or upper the string cases.
name = input("Enter your name: ")
age = input("Enter  your age :")
print("your name is {}. your age is {}".format('abhi',age).capitalize().upper())
line = ' hello my man and man is the alpha and woman is the beta so man is good.'
print(line.find('man'))
# to find word in a phrase
print(line.replace('man','woman'))
# to replace a word with a new word
print(line)

