#Polling
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

poll_people = ['bob', 'phil', 'james', 'mary','sarah']

for person in poll_people:
    if person in favorite_languages.keys():
        print(person.title() + ', thanks for taking the poll.')
    else:
        print(person.title() + ', please take the poll!')