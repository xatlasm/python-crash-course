#Movie tickets
age = ""
while age != 0:
    age = input('What is your age? (Enter 0 to quit)')
    age = int(age)
    if age == 0:
        break
    if age < 3:
        print('Your ticket is free.')
    elif age >= 3 and age <= 12:
        print('Your ticket costs $10.')
    elif age > 12:
        print('Your ticket costs $15.')