#Multiples of 10
num = input("Please input a number:")
num = int(num)
if num % 10 == 0:
    print("\n The number " + str(num) + " is divisible by 10")
else:
    print("\n The number " + str(num) + " is not divisible by 10")