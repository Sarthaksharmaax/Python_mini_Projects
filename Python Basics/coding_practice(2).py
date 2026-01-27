# Section B: Coding Problems (Solve All)
# 1. Write a program to count the number of vowels in a string.
# 2. Write a program to find the sum of all elements in a list.
# 3. Write a program to check whether a number is even or odd.
# 4. Write a program to find the smallest element in a list.
# 5. Write a program to replace all spaces in a string with underscores (_).

# 1.
my_string = "Johnny Jackson"
vowels = "aeiouAEIOU"
non_vowels = [char for char in my_string if char in vowels]
result = "".join(non_vowels)
print(f"There are {len(result)} vowels in the string.")

# 2.

my_list= [1,2,4,3,5,6,7]
sum = 0
for num in my_list:
    sum += num
print(f"The sum of all the elements in the list is {sum}.")

# 3.

numberr = int(input("Enter a number: "))
if numberr%2 == 0:
    print("Number is even!")
else:
    print("Number is odd!")

# 4.

list_1 =[1,7,4,2,9,5,0,11,16,3,19]
minimum = min(list_1)
print(f"{minimum} is the smallest element in the list.")

# 5.

string_my = "hello my name is sarthak"
new_str = string_my.replace(' ','_')
print(new_str)


# Section C: Debugging & Error Finding

# 1. Identify and fix the error:
nums = [1, 2, 3]
nums.append(4)
print(nums)
# 2. Identify the error:
for i in range(5):
    print(i)
# 3. Find the bug:
x = 10
y = 5
print(x + y)
# all errors are resolved.


