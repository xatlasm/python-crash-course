#T-Shirt
def make_shirt(size, message):
    """Creates a T-shirt with a message"""
    size = str(size)
    message = str(message)
    print('A ' + size + ' size shirt with the message: ' + message)
    
make_shirt('large', 'hello world!')