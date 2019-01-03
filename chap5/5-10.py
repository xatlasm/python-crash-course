#Checking usernames
current_users = ['admin', 'bob', 'dave', 'joe', 'sam']
new_users = ['bob', 'Dave', 'jim', 'sue', 'pam']
for new_user in new_users:
    if new_user.lower() in current_users:
        print('Please choose a different username')
    else:
        print('That username is available.')