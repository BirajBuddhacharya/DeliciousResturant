import sys; sys.path.append('.')
from utils.clear import Clear
from utils.table import Table
from APIs.getCurrentUser import GetCurrentUser
from utils.genId import GenId
from utils.updateProfile import UpdateProfile as update_profile

def place_orders(): 
    # loading menu and orders table
    menu = Table.loadData('menu.txt')
    orders = Table.loadData('orders.txt')
    
    # creating unique order id
    order_id = str(GenId(orders.tableData['order_id']))
    
    # retriving current customer data to place order
    name, email, _ = GetCurrentUser()
    
    while True: 
        # clearing output from previous loop
        Clear()
        
        # printing menu 
        print(menu)
        
        # getting user order
        food_id = input("Enter id of food you want to order (q for quit):")
        
        # loop break condition
        if food_id == 'q':
            break
        
        # validating food_id 
        if food_id not in menu.tableData['id']: 
            input('Incorrect food id press enter to continue again: ')
            continue
        
        # retriving food name according to id 
        food_name = menu.tableData['name'][menu.search({'id':food_id})]
        
        # getting quantity
        quantity = input("Enter the quantity: ")
        
        # appending order data
        orderData = {
            'id': order_id, 
            'customer_email': email,
            'customer_name': name,
            'food_id': food_id,
            'food_name': food_name,
            'quantity': quantity
        }
        orders.append(orderData)
        
    # saving orders
    orders.saveData("orders.txt")
    print("Your order has been successfully placed")
    
def manage_orders():
    print("Managing orders...")
    orders = Table.loadData('orders.txt')
    
    # printing all users
    print(orders)
    
    while True:
        print("""
        Choose an action:
        e. Edit order
        d. Delete order
        q. Quit
        """)
        
        action = input("Enter the letter of the action you want to perform: ").lower()
        
        Clear() # clearing previous outputs
        print(orders)
        match action:
            case 'e':
                # Logic for editing staff
                order_id = input("Enter order id of order to edit: ")
                updateIdentifier = {'id': order_id}
                updateData = {}
                
                for key in orders.tableData: 
                    userInput = input(f'Enter new {key} (Enter for no changes): ')
                    if userInput: 
                        updateData.update({key: userInput})
                
                orders.update(updateIdentifier, updateData)
            case 'd':
                # Logic for deleting staff
                order_id = input("Enter id of order you want to delete: ")
                orders.delete({'id': order_id})
            case 'q':
                # Quit the loop
                break
            case _:
                Clear()
                print("Invalid choice. Try again.")
    
    orders.saveData('users.txt')
    
def view_order_status():
    pass

def send_feedback(): 
    # loading feedbacks
    feedbacks = Table.loadData('feedbacks.txt')
    
    # loading current user information 
    name, email, role = GetCurrentUser()
    
    # asking feedback
    feedback = input("Write your feedback: ")
    
    # constructing save data
    saveData = {
        'id': str(GenId(feedbacks.tableData['id'])), # randomly generates id 
        'customer_email': email, 
        'customer_name': name, 
        'feedback': feedback
    }
    
    # appending to feedback table
    feedbacks.append(saveData)
    
    # saving feedbacks
    feedbacks.saveData('feedbacks.txt')
    print("We got your feedback ;)")
    
    pass

def main(): 
    """
    4. Customer
        - View & order food (Add, Edit, Delete) and pay to confirm.
        - View order status.
        - Send feedback to the administrator.
        - Update own profile.
    args: 
    """   
    # Mapping actions to corresponing action number
    actions = {
        "1": place_orders,
        "2": manage_orders,
        "3": view_order_status,
        "4": send_feedback,
        "5": update_profile,
        "6": exit
    }

    # looping until user chooses a valid action
    while True:      
        # printing user instructions
        print("""
        Choose an action:
        1. Place orders
        2. Manage orders
        3. View order status
        4. send feedback
        5. Update profile
        6. Exit
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
            
if __name__ == '__main__': 
    update_profile()