import sys
sys.path.append('.')  # for debugging

from APIs.getCurrentUser import GetCurrentUser
from utils.table import Table
from utils.clear import Clear
from utils.updateProfile import UpdateProfile as update_profile
from utils.genId import GenId
from utils.emailValidator import isEmailValid

def manage_customers():
    # Clearing previous outputs
    Clear()
    print("Managing customers...")
    
    while True:
        Clear()
        # loading customer
        users = Table.loadData('users.txt')
        
        try: # handling no customers
            customers = users.filter('role', 'customer')
        except ValueError: 
            input("No customers found in database (press ENTER to continue)...")
            return
        
        # Printing all customers
        print(customers)
        
        print("""
        Choose an action:
        1. Add customer
        2. Edit customer
        3. Delete customer
        4. Quit
        """)
        
        action = input("Enter the number of the action you want to perform: ").lower()
        
        Clear()  # Clearing previous output
        print(customers)
        
        match action:
            case '1':
                Clear()
                print("Add customer:")
                # Logic for adding a customer
                addDict = {}
                for key in customers.columns:
                    userInput = 'customer' if key == 'role' else input(f"Enter {key}: ")
                    addDict.update({key: userInput})
                
                users.append(addDict)
                Clear()
                input("Customer added successfully (press ENTER to continue)...")
                
            case '2':
                print("Edit customer: ")
                # Logic for editing a customer
                email = input("Enter email of the customer to edit: ")
                Clear()
                
                # validating email
                if email not in customers['email']: 
                    Clear()
                    input("Customer email not found no edits made (Press ENTER to continue)...")
                    continue 
                
                updateIdentifier = {'email': email}
                updateData = {}
                
                for key in customers.columns:
                    if key == 'role': continue # skipping role
                    
                    userInput = input(f'Enter new {key} (Enter for no changes): ')
                    if userInput:
                        # validating email
                        if key == 'email' and not isEmailValid(userInput):
                            input("Email provided already exists no changes made (press ENTER to continue)...")
                            return
                            
                        updateData.update({key: userInput})
                
                Clear()
                users.update(updateIdentifier, updateData)
                input("press ENTER to continue...")
                
            case '3':
                print("Delete customer: ")
                # Logic for deleting a customer
                email = input("Enter email of the customer to delete: ")
                
                # validating email
                if email not in customers['email']: 
                    input("Customer email not found no deletion made (Press ENTER to continue)...")
                    continue 
                
                try:
                    users.delete({'email': email})
                    Clear()
                    input("customer deleted successfully (press ENTER to continue)...")
                except ValueError:
                    Clear()
                    input("Customer email not found. Press ENTER to continue...")
                
            case '4':
                Clear()
                # Quit the loop
                break
                
            case _:
                Clear()
                input("Invalid choice. Try again.Press ENTER to continue...")
    
        users.saveData('users.txt')

def manage_menu():
    # Clearing previous outputs
    Clear()
    
    print("Managing menu categories and pricing...")
    menu = Table.loadData('menu.txt')
    
    # Printing all menu items
    print(menu)
    
    while True:
        Clear()  # Clearing previous output
        
        print("""
        Choose an action:
        1. Add menu item
        2. Edit menu item
        3. Delete menu item
        4. Quit
        """)
        
        action = input("Enter the number of the action you want to perform: ").lower()
        
        Clear()  # Clearing previous output
        print(menu)
        
        match action:
            case '1':
                Clear() 
                print("Add menu item:")
                # Logic for adding a menu item
                addDict = {}
                for key in menu.columns:
                    userInput = str(GenId(menu['id'])) if key == 'id' else input(f"Enter {key}: ")
                    addDict.update({key: userInput})
                
                menu.append(addDict)
                Clear()
                input("Menu item added successfully (ENTER to continue)...")
                
            case '2':
                print("Edit menu item: ")
                # Logic for editing a menu item
                item_id = input("Enter the item ID of the menu item to edit: ")
                updateIdentifier = {'id': item_id}
                updateData = {}
                
                for key in menu.columns:
                    if key == 'id': continue # skipping id and role
                    
                    userInput = input(f'Enter new {key} (Enter for no changes): ')
                    if userInput:
                        updateData.update({key: userInput})
                
                Clear()
                menu.update(updateIdentifier, updateData)
                input("press ENTER to continue")
                
            case '3':
                print("Delete menu item: ")
                # Logic for deleting a menu item
                item_id = input("Enter the item ID of the menu item to delete: ")
                
                try:
                    Clear()
                    menu.delete({'id': item_id})
                    input("ENTER to continue...")
                except ValueError:
                    input("Menu item ID not found. Press ENTER to continue...")
                
            case '4':
                Clear()
                # Quit the loop
                break
                
            case _:
                Clear()
                input("Invalid choice. Try again. (ENTER to continue)...")
    
        menu.saveData('menu.txt')

def view_ingredients():
    print("Viewing ingredients list requested by chef...")
    
    # loading ingredients data
    ingredients = Table.loadData('ingredientsRequest.txt')

    # displaying ingredient requests
    print(ingredients)
    
    # holding the output
    input('Press ENTER to continue...')


def main():
    actions = {
        "1": manage_customers,
        "2": manage_menu,
        "3": view_ingredients,
        "4": update_profile,  
        "5": exit
    }

    # looping until user chooses a valid action
    while True:
        Clear() # clearing output from previous loop 
        
        # printing user instructions
        print("""
        Choose an action:
        1. Manage customers
        2. Manage menu categories and pricing
        3. View ingredients list requested by chef
        4. Update profile
        5. Exit
        """)

        # getting user choice
        choice = input("Enter the number of the action you want to perform: ")

        # getting corresponding action according to choice
        if action := actions.get(choice, None):
            Clear()  
            action()

        # if choice is not valid
        else:
            Clear()  
            input("Invalid choice press ENTER to try again...")

if __name__ == "__main__":
    main()
