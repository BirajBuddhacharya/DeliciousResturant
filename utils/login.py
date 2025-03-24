from APIs.getUser import GetUser
from utils.saveCurrentUser import SaveCurrentUser
from utils.handleRole import HandleRole
from utils.clear import Clear
from utils.fancyTexts import FancyTexts

def Login(): 
    # attempt counter
    attemptCount = 1
    
    # for 3 password tries
    try:
        while attemptCount <= 3: 
            # getting email and password from the user
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            
            isAuthenticated, role = Authenticate(email, password)
            
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
        
    # handling exit behaviour        
    except KeyboardInterrupt:
        print(f'\n{FancyTexts['thank you']}')
        print("\nThank you for your time")
        print("Program is now exiting")
        exit()
        
def Authenticate(email: str, password: str): 
    """
        logs in the user if the email and password are correct
        args: 
            email -> email of the user
            password -> password of the user
        returns: 
            (isAuthenticated, role) -> 
                (True, role) if the user is loged in successfully
                (False, None) if the user is not loged in successfully
    """
   # getting user Data according to email from Users.csv
    userData = GetUser(email)
    
    # if user data is found in Users.csv
    if userData: 
        # depackaging user data
        name, correctPassword, role = userData
        
        # if password matches
        if password == correctPassword: 
            SaveCurrentUser(name, email, role)
            return (True, role)
            
        # if password doesn't match with passowrd in Users.csv 
        else: 
            print("Incorrect password")
            return (False, None)
    
    # if user data not found                
    else: 
        print("Email could not be found")
        return (False, None)
    
    