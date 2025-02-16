from APIs.updateProfile import UpdateProfile
from APIs.getCurrentUser import GetCurrentUser
from utils.table import Table
from utils.clear import Clear

def manage_staff():
    print("Managing staff...")
    users = Table().loadData('Databases/users.txt')
    
    # printing all users
    print(users)
    
    while True:
        print("""
        Choose an action:
        a. Add staff
        e. Edit staff
        d. Delete staff
        q. Quit
        """)
        
        action = input("Enter the letter of the action you want to perform: ").lower()
        
        Clear() # clearing previous outputs
        match action:
            case 'a':
                # Logic for adding staff
                name = input("Enter name of the new staff: ")
                password = input("Enter password of the new staff: ")
                email = input("Enter email of the new staff: ")
                role = input("Enter role of the new staff: ")
                users.append(name, password, email, role)
                print(f"Added new staff: {name}, Role: {role}")
            case 'e':
                # Logic for editing staff
                name = input("Enter name of the staff to edit: ")
                for user in users:
                    if user["name"] == name:
                        new_name = input("Enter new name: ")
                        new_role = input("Enter new role: ")
                        user["name"] = new_name
                        user["role"] = new_role
                        Table().saveData('users.txt', users)
                        print(f"Updated staff: {new_name}, Role: {new_role}")
                        break
                else:
                    print("Staff not found.")
            case 'd':
                # Logic for deleting staff
                name = input("Enter name of the staff to delete: ")
                users = [user for user in users if user["name"] != name]
                Table().saveData('users.txt', users)
                print(f"Deleted staff: {name}")
            case 'q':
                # Quit the loop
                break
            case _:
                Clear()
                print("Invalid choice. Try again.")
    

def view_sales_report():
    print("Viewing sales report...")
    
    salesReport= Table().loadData("salesReport.txt")
    
    print(salesReport)

def view_feedback():
    # making table object
    table = Table()
    
    # loading feedback table
    table.loadData('feedbacks.txt')
    
    # displaying feedbacks
    print("Viewing feedback...")
    print(table)

def update_profile():
    # geting current user mail from cookie
    _, email, _ = GetCurrentUser()
    
    # Presenting the user with options to update profile
    print("""
    Choose an option to update:
    1. Change name
    2. Change email
    3. Change password
    """)

    # Getting user choice
    choice = input("Enter the number of the option you want to update: ")

    # Initializing updatekwargs dictionary
    updatekwargs = {}

    match choice:
        case "1":
            new_name = input("Enter new name: ")
            updatekwargs["updateName"] = new_name
        case "2":
            new_email = input("Enter new email: ")
            updatekwargs["updateEmail"] = new_email
        case "3":
            new_password = input("Enter new password: ")
            updatekwargs["updatePassword"] = new_password
        case _:
            Clear()
            print("Invalid choice. No updates made.")
            return

    # Calling UpdateProfile with email and updatekwargs
    UpdateProfile(email, **updatekwargs)
    
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
            print("Invalid choice try again")
        


# for unit testing
if __name__ == "__main__":
    view_feedback()