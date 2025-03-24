from utils.table import Table 
from utils.clear import Clear
from utils.login import Authenticate
from utils.handleRole import HandleRole

def Register(): 
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