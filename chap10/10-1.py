#Learning Python

filename = 'pythoncc exercises/chap10/learning_python.txt'

#Read entire file
with open(filename) as file_object:
    learning = file_object.read()
    print(learning)
    print()

#Loop over object
with open(filename) as file_object:
    for learning in file_object:
        print(learning.strip())
    print()

#Store as list
with open(filename) as file_object:
    learning_list = file_object.readlines()

for learning in learning_list:
    print(learning.strip())