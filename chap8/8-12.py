#Sandwiches
def sandwich(*ingredients):
    """Makes a sandwich"""
    print('Making a sandwich with: ')
    for ingredient in ingredients:
        print('-' + ingredient)

sandwich('ham', 'cheese', 'mayo')