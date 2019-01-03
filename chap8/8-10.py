#Great Magicians
def show_magicians(magicians):
    """prints the name of each magician in the list"""
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    """Make Magicians Great Again"""
    great_magicians=[]
    for magician in magicians:
        great_magicians.append(magician + ' the Great')
    return great_magicians
magicians = ['alice','bob','charlie']
great_magicians = make_great(magicians)
show_magicians(great_magicians)