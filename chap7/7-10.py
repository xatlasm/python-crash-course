#Dream Vacation
responses = {}

polling_active = True

while polling_active:
    name = input('Name? ')
    place = input('Where would you like to go? ')

    responses[name] = place

    repeat = input('Another vote? (y/n)')
    if repeat == 'n':
        polling_active = False

print('\n--- Results ---')
for name, place in responses.items():
    print(name + " would like to go to " + place + ".")