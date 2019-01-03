#Hello users
usernames = ['admin', 'bob', 'dave', 'joe', 'sam']
if usernames:
    for user in usernames:
        if user == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello ' + user.title() + ', and welcome back.')
else:
    print('We need to find some users!')