from APIs.getUser import GetUser
from utils.saveCurrentUser import SaveCurrentUser
   
def Login(email: str, password: str): 
    """
        logs in the user if the email and password are correct
        args: 
            email -> email of the user
            password -> password of the user
        returns: 
            (isAuthenticated, role) -> (True, role) if the user is loged in successfully
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
    
    