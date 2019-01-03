#No Pastrami
sandwich_orders = ['ham and cheese', 'turkey avocado', 'BLT', 'pastrami',
                    'pastrami', 'pastrami']
finished_sandwiches = []

print('We are out of pastrami!')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('Making a ' + sandwich + ' sandwich...')
    finished_sandwiches.append(sandwich)

print('I have finished making these sandwiches:')
for sandwich in finished_sandwiches:
    print(sandwich + ' sandwich')