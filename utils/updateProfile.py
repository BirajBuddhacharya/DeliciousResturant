from APIs.getCurrentUser import GetCurrentUser
from utils.table import Table
from utils.saveCurrentUser import SaveCurrentUser

def UpdateProfile(): 
        # geting current user mail from cookie
    name, email, role = GetCurrentUser()
    users = Table.loadData('users.txt')
    
    updateData = {
        'name': name,
        'email': email,
        'role': role
    }
                
    for key in users.columns: 
        # skipping role 
        if key == 'role': 
            continue
        
        userInput = input(f'Enter new {key} (Enter for no changes): ')
        if userInput: 
            updateData.update({key: userInput})
            
    users.update({'email': email}, updateData)
    users.saveData('users.txt')
    
    # updating cookies
    SaveCurrentUser(updateData['name'], updateData['email'], updateData['role'])