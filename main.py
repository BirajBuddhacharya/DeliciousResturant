from utils.handleRole import HandleRole
from utils.login import Login
from utils.clear import Clear

def main(): 
    # clearing all previous outputs
    Clear()
    
    print(f"{'-' * 40} Welcome {'-' * 40}")
    
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
            
            # for going back to login page
            attemptCount = 0
        else: 
            Clear()
            print("Incorrect email or password")
        
        # incrementing attempt count (for only 3 attempts feature)
        print(f"{3-attemptCount} attempts left")
        attemptCount += 1   
    
    # warning too many attempts
    else: 
        print("To many attempts program exiting")

main()