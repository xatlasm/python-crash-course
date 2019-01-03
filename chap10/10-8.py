#Cats and Dogs
cats_file = 'pythoncc exercises/chap10/cats.txt'
dogs_file = 'pythoncc exercises/chap10/dogs.txt'


def print_names(filename):
    """Prints names from input file"""
    try:
        with open(filename, 'r') as file_object:
            name_list = file_object.readlines()
    except FileNotFoundError:
        print('The name file ' + filename + ' cannot be found!')    
    else:
        print('Names in file ' + str(filename) + ':')
        for name in name_list:
            print(name.strip())

print_names(cats_file)
print_names(dogs_file)