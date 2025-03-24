import sys; sys.path.append('.') # for debugging
from APIs.getCurrentUser import GetCurrentUser
from utils.table import Table
from utils.clear import Clear
from utils.updateProfile import UpdateProfile as update_profile
from utils.emailValidator import isEmailValid

def manage_staff():
    # clearing previous outputs 
    Clear()
    
    print("Managing staff...")
    users = Table.loadData('users.txt')
    
    # printing all users
    print(users)
    
    while True:
        Clear() # clearing previous output
        
        print("""
        Choose an action:
        1. Add staff
        2. Edit staff
        3. Delete staff
        4. Quit
        """)
        
        action = input("Enter the number of the action you want to perform: ").lower()
        
        Clear() # clearing previous outputs
        print(users)
        match action:
            case '1':
                print("Add staff:")
                # Logic for adding staff
                addDict = {}
                for key in users.columns:
                    userInput = input(f"Enter {key}:")
                    
                    # validating email
                    if key == 'email': 
                        if not isEmailValid(userInput): 
                            Clear()
                            input("Email already exists no updates made (press ENTER to continue)...")
                            break
                        
                    addDict.update({key: userInput})
                
                Clear()
                users.append(addDict)
                input("User added succesfully (press ENTER to continue)...")
                
            case '2':
                print("Edit staff: ")
                # Logic for editing staff
                email = input("Enter email of the staff to edit: ")
                updateIdentifier = {'email': email}
                updateData = {}
                
                for key in users.columns: 
                    userInput = input(f'Enter new {key} (Enter for no changes): ')
                    if userInput: 
                        # validating email
                        if key == 'email': 
                            if not isEmailValid(userInput) and userInput != email: 
                                Clear()
                                input("Email not valid no edit made (Press ENTER to continue)...")
                                break
                        updateData.update({key: userInput})
                
                users.update(updateIdentifier, updateData)
                Clear()
                input("staff edited successfully (press ENTER to continue)...")
                
            case '3':
                print("Delete Staff: ")
                # Logic for deleting staff
                email = input("Enter email of the staff to delete: ")
                
                try: 
                    users.delete({'email': email})
                    Clear()
                    input("Staff account deleted successfully (press ENTER to continue)...")
                    Clear()
                except ValueError: 
                    input("staff email not found press ENTER to continue...")
            case '4':
                Clear()
                # Quit the loop
                break
            case _:
                Clear()
                input("Invalid choice. Try again. ( press ENTER to try again)...")
    
        users.saveData('users.txt')
    
def view_sales_report():
    print("Viewing sales report...")
    
    try: 
        salesReport= Table.loadData("salesReport.txt")
    except ValueError: 
        print("No sales report")
        return 

    print(salesReport)
    input("press Enter to continue...")
    Clear()

def view_feedback():
    # loading feedback data
    try: 
        table = Table.loadData('feedbacks.txt')
    except ValueError: 
        print("No feedback report")
        return 
    
    # displaying feedbacks
    print("Viewing feedback...")
    print(table)
    input("Press ENTER to continue...")
    Clear()
  
def main(): 
    # Start writing your code here
    """
    1. Administrator
        - Manage staff - Manager, Chef (Add, Edit, Delete)
        - View sales report based on month, chef etc.
        - View feedback sent by customers.
        - Update own profile.
    """
    
    # Mapping actions to corresponing action number
    actions = {
        "1": manage_staff,
        "2": view_sales_report,
        "3": view_feedback,
        "4": update_profile,
        "5": exit
    }

    # looping until user chooses a valid action
    while True:      
        # printing user instructions
        print("""
        Choose an action:
        1. Manage staff
        2. View sales report
        3. View feedback
        4. Update profile
        5. Exit
        """)

        # getting user choice
        choice = input("Enter the number of the action you want to perform: ")

        # getting corresponing action according to choice 
        if action := actions.get(choice, None):
            Clear() # clearing previous outputs
            action()
            
        
        # if choice is not valid
        else: 
            Clear() # clearing previous outputs
            input("Invalid choice press ENTER to try again...")
        

# for unit testing
if __name__ == "__main__":
    main()