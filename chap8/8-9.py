#Magicians
def show_magicians(magicians):
    """prints the name of each magician in the list"""
    for magician in magicians:
        print(magician.title())
magicians = ['alice','bob','charlie']
show_magicians(magicians)