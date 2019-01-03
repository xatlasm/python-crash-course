#Addition Calculator

print("Give me two numbers, and I'll add them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        int(first_number)
    except ValueError:
        print('Your first number is not a number!')    
    else:
        try:
            int(second_number)
        except ValueError:
            print('Your second number is not a number!')
        else:
            answer = int(first_number) + int(second_number)
            print(answer)