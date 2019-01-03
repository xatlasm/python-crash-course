#Deli
sandwich_orders = ['ham and cheese', 'turkey avocado', 'BLT']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('Making a ' + sandwich + ' sandwich...')
    finished_sandwiches.append(sandwich)
    
print('I have finished making these sandwiches:')
for sandwich in finished_sandwiches:
    print(sandwich + ' sandwich')