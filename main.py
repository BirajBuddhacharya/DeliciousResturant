from utils.handleRole import HandleRole
from utils.login import Login

def main(): 
    # attempt counter
    attemptCount = 1
    
    # for 3 password tries
    while attemptCount <= 3: 
        # getting email and password from the user
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        
        isAuthenticated, role = Login(email, password)
        
        if isAuthenticated: 
            HandleRole(role)
            break
        
        # incrementing attempt count (for only 3 attempts feature)
        attemptCount += 1   
    
    # warning too many attempts
    else: 
        print("To many attempts program exiting")

main()