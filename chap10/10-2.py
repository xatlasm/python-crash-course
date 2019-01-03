#Learning C

filename = 'pythoncc exercises/chap10/learning_python.txt'

with open(filename) as file_object:
    learning_list = file_object.readlines()

for learning in learning_list:
    modlearning = learning.replace('Python','C')
    print(modlearning.strip())