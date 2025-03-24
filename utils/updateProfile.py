import sys; sys.path.append('.')
from APIs.getCurrentUser import GetCurrentUser
from utils.table import Table
from utils.saveCurrentUser import SaveCurrentUser
from utils.clear import Clear

def UpdateProfile(): 
    Clear() # clearing all previous outputs
    
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
    
    Clear()
    input("Email updated successfully (press ENTER to continue)...")
    Clear()

if __name__  == '__main__': 
    UpdateProfile()