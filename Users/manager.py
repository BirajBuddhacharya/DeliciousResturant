import sys
sys.path.append('.')  # for debugging

from APIs.getCurrentUser import GetCurrentUser
from utils.table import Table
from utils.clear import Clear
from utils.updateProfile import UpdateProfile as update_profile

def manage_customers():
    Clear()

    print("Managing customers...")
    customers = Table.loadData('customers.txt')  # Assume customers data is stored in 'customers.txt'

    # printing all customers
    print(customers)

    while True:
        Clear()  # clearing previous output

        print("""
        Choose an action:
        a. Add customer
        e. Edit customer
        d. Delete customer
        q. Quit
        """)

        action = input("Enter the letter of the action you want to perform: ").lower()

        Clear()  
        print(customers)

        match action:
            case 'a':
                print("Add customer:")
                # Logic for adding a customer
                addDict = {}
                for key in customers.tableData:
                    userInput = input(f"Enter {key}:")
                    addDict.update({key: userInput})

                customers.append(addDict)
                print("Customer added successfully")

            case 'e':
                print("Edit customer: ")
                # Logic for editing a customer
                email = input("Enter email of the customer to edit: ")
                identifierUpdate = {'email': email}
                updateData = {}

                for key in customers.tableData:
                    userInput = input(f'Enter new {key} (Enter for no changes): ')
                    if userInput:
                        updateData.update({key: userInput})

                customers.update(identifierUpdate, updateData)
                print("Customer details updated successfully")

            case 'd':
                print("Delete Customer: ")
                # Logic for deleting a customer
                email = input("Enter email of the customer to delete: ")
                customers.delete({'email': email})
                print("Customer deleted successfully")

            case 'q':
                # Quit the loop
                break

            case _:
                Clear()
                print("Invalid choice. Try again.")

    customers.saveData('customers.txt')


def manage_menu():
    Clear()

    print("Managing menu categories and pricing...")
    menu = Table.loadData('menu.txt')  

    # printing all menu items
    print(menu)

    while True:
        Clear()  # clearing previous output

        print("""
        Choose an action:
        a. Add menu item
        e. Edit menu item
        d. Delete menu item
        q. Quit
        """)

        action = input("Enter the letter of the action you want to perform: ").lower()

        Clear()  
        print(menu)

        match action:
            case 'a':
                print("Add menu item:")
                # Logic for adding a menu item
                addDict = {}
                for key in menu.tableData:
                    userInput = input(f"Enter {key}:")
                    addDict.update({key: userInput})

                menu.append(addDict)
                print("Menu item added successfully")

            case 'e':
                print("Edit menu item: ")
                # Logic for editing a menu item
                item_id = input("Enter the item ID of the menu item to edit: ")
                identifierUpdate = {'id': item_id}
                updateData = {}

                for key in menu.tableData:
                    userInput = input(f'Enter new {key} (Enter for no changes): ')
                    if userInput:
                        updateData.update({key: userInput})

                menu.update(identifierUpdate, updateData)
                print("Menu item updated successfully")

            case 'd':
                print("Delete Menu Item: ")
                # deleting a menu item
                item_id = input("Enter the item ID of the menu item to delete: ")
                menu.delete({'id': item_id})
                print("Menu item deleted successfully")

            case 'q':
                
                break

            case _:
                Clear()
                print("Invalid choice. Try again.")

    menu.saveData('menu.txt')

def view_ingredients():
    print("Viewing ingredients list requested by chef...")
    
    # loading ingredients data
    ingredients = Table.loadData('ingredientsRequest.txt')

    # displaying ingredient requests
    print(ingredients)


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
    manage_menu()
