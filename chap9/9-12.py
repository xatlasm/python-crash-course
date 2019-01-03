#Multiple Modules

from user import User
from admin import Admin, Privileges

me = Admin('mitchell', 'atlas', 28, 'male',['can create', 'can read', 
            'can update', 'can delete'])
me.privileges.show_privileges()
me.describe_user()