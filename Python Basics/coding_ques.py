# Section B: Coding Problems (Solve Any 5)
# 1. Write a program to remove vowels from a string.
# 2. Write a program to remove duplicate elements from a list.
# 3. Write a program to find the largest number in a list.
# 4. Write a program to count how many times each character appears in a string.
# 5. Write a program to reverse a string without using slicing

# 1.
my_string = "Baseball"
vowels = "aeiouAEIOU"
line = [char for char in my_string if char not in vowels]
result = "".join(line)
print(result)

# 2.
my_list = [1,4,2,5,2,6,2,7,2,2]
print (list (dict.fromkeys(my_list)))
# 3.

a_list = [1,5,2,7,4,9,1,5,3]
print(max(a_list))

# 4.
s = "sarthak"
counter = {}
for ch in s:
    if ch in counter:
        counter[ch] += 1
    else:
        counter[ch] = 1
print(counter)




# 5.

string_1 = "Python"
revv= "".join(reversed(string_1))
print(str(revv))
rev = ""
for charr in string_1:
    rev = charr + rev
print(rev)

# Section C: Debugging & Error Finding
#
#
# 1. Identify and fix the error:
nums = [1, 2, 3]
print(nums[2])
# bug was nums[3] as it is out of range or bound

# 2. Identify the error:
# name = "Python"
# name[0] = "J"
# strings are immutable so nums[0] = "j" is a error here.

# 3. Find the bug:
x = 10
if x == 5:
    print("Equal")
# == not equals



