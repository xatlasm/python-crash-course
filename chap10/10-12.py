#Favorite Number Remembered

import json

filename = 'pythoncc exercises/chap10/fav_num.json'

def get_fav_num():

    fav_num = input('What is your favorite number? ')

    with open(filename, 'w') as f_obj:
        json.dump(fav_num,f_obj)

def read_fav_num():
    """Reads user's favorite number from JSON"""

    with open(filename, 'r') as f_obj:
        fav_num = json.load(f_obj)

    print('I know your favorite number! It\'s ' + str(fav_num))


try:
    read_fav_num()
except FileNotFoundError:
    get_fav_num()