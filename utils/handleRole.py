from Users.admin import main as admin
from Users.chef import main as chef
from Users.customer import main as customer
from Users.manager import main as manager
from utils.clear import Clear
from APIs.getCurrentUser import GetCurrentUser

def HandleRole(role): 
    """
        executes corresponding function accoding to the role
        args: 
            role -> role of the logedin user
        returns: 
            none
    """
    # clearing previous outputs
    Clear()
    
    # maping corresponding action to the role
    roles = {
        'admin': admin,
        'chef': chef,
        'customer': customer,
        'manager': manager
    }
    # formating role
    role = "".join(role.split()) # removing any linen breaks and white spaces
    
    # if the role is found
    if action := roles.get(role, None):
        # welcome message
        name, email, role = GetCurrentUser()
        print(f"Welcome {name} you are logged in as {role}")
        print("-" * 60)
        action()
        
    # if the role is not found
    else: 
        print("Role not found")
        

