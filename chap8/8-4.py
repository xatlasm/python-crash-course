#Large Shirt
def make_shirt(size = 'large', message = 'I love Python'):
    """Creates a T-shirt with a message"""
    size = str(size)
    message = str(message)
    print('A ' + size + ' size shirt with the message: ' + message)
    
make_shirt('large')
make_shirt('medium')
make_shirt('small', 'You suck!')