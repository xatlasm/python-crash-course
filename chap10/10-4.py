# Guest book
filename = 'pythoncc exercises/chap10/guest_book.txt'

with open(filename, 'a') as file_object:
    while True:
        name = input('Enter name (q to quit): ')
        if name == 'q':
            break
        print('Thank you for visiting, ' + name + '!\n')
        file_object.write(name + '\n')