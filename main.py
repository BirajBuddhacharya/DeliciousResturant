from utils.handleRole import HandleRole
from utils.login import Authenticate
from utils.clear import Clear
from utils.fancyTexts import FancyTexts
from utils.table import Table

def login(): 
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
        print("\nThank you for your time")
        print("Program is now exiting")
        exit()

def register(): 
    print("Register...")
    users = Table.loadData('users.txt')
    
    # Logic for adding user
    addDict = {}
    for key in users.columns:
        if key == 'role': 
            addDict.update({'role': 'customer'})
            continue
        userInput = input(f"Enter {key}:")
        addDict.update({key: userInput})
    
    users.append(addDict)
    users.saveData('users.txt')
    Clear()
    input("Registered Succesfully (press ENTER to continue)")
    
    # logging user in 
    Authenticate(addDict['email'], addDict['password'])
    HandleRole('customer')

def main(): 
    # clearing all previous outputs
    Clear()
    
    print(f"{'-' * 30} {FancyTexts['welcome']} {'-' * 30}")
    
    # making action map of corresponding function 
    actions = {
        '1': login, 
        '2': register,
    }

    while True: 
        print("""
            choose an action:
            1. Login
            2. Register 
        """)
        id = input("Enter the number of action you want to perform: ")
        
        if action := actions.get(id, None): 
            Clear()
            action()
            break
        else: 
            input("invalid option try again (press ENTER to continue)")
            Clear()
                
main()