Age = int(input("What is your age: "))

drive = input("Do you have a licence: press (y/n)")
if Age < 18:
    print("You are a kid ")
elif Age <= 60:
    print("You are an adult ")

else:
    print("You are old aged ")
if drive == "y":
    drive = True
elif drive == "n":
    print("but")
    drive = False
else:
    print("Wrong Input")
if drive and Age > 18:
    print("you can drive!")
else:
    print("You cannot drive as you do not have a licence")
