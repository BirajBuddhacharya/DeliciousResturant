from APIs.getUser import GetUser
from Users.admin import main as admin
from Users.chef import main as chef
from Users.customer import main as customer
from Users.manager import main as manager


def handleRole(role): 
    """
        executes corresponding function accoding to the role
        args: 
            role -> role of the logedin user
        returns: 
            none
    """
    match role: 
        case 'admin': 
            admin()
        case 'chef': 
            chef()
        case 'customer': 
            customer()
        case 'manager': 
            manager() 
        case _: # default case (executes if none of the above role is found)
            print("Role not found")
        
def main(): 
    # attempt counter
    attemptCount = 1
    
    # for 3 password tries
    while attemptCount <= 3: 
        # getting email and password from the user
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        
        # getting user Data according to email from Users.csv
        userData = GetUser(email)
        
        # if user data is found in Users.csv
        if userData: 
            # depackaging user data
            name, correctPassword, role = userData
            
            # if password matches
            if password == correctPassword: 
                print("Welcome", name)
                print("You are loged in as", role)
                handleRole(role)
                break
               
            # if password doesn't match with passowrd in Users.csv 
            else: 
                print("Incorrect password")
        
        # if user data not found                
        else: 
            print("Email could not be found")
            
        # incrementing attempt count (for only 3 attempts feature)
        attemptCount += 1   
    
    # handling too many attempts
    if attemptCount == 4: 
        print("To many attempts program exiting")

main()