import sys; sys.path.append('.')
from utils.clear import Clear
from utils.table import Table
from APIs.getCurrentUser import GetCurrentUser
from utils.genId import GenId
from utils.updateProfile import UpdateProfile as update_profile
from utils.fancyTexts import FancyTexts

def place_orders(): 
    # loading menu and orders table
    menu = Table.loadData('menu.txt')
    orders = Table.loadData('orders.txt')
    
    # creating unique order id
    order_id = str(GenId(orders['id']))
    
    # retriving current customer data to place order
    name, email, _ = GetCurrentUser()
    
    while True: 
        # clearing previous output
        Clear()
        
        print("Place Orders...")
        
        # printing menu 
        print(menu)
        
        # getting user order
        food_id = input("Enter id of food you want to order (q or ENTER to quit):").lower()
        
        # loop break condition
        if food_id == 'q' or not food_id:
            break
        
        # validating food_id 
        if food_id not in menu['id']: 
            input('Incorrect food id press enter to continue again: ')
            continue
        
        # retriving food name according to id 
        food_name = menu.getValue('food_name', int(food_id))
        
        # getting quantity
        quantity = input("Enter the quantity: ")
        
        # appending order data
        orderData = {
            'id': order_id, 
            'customer_email': email,
            'customer_name': name,
            'food_id': food_id,
            'food_name': food_name,
            'quantity': quantity,
            'status': 'pending',
            'payment_status': 'Unpaid'
        }
        orders.append(orderData)
        
        # saving orders
        orders.saveData("orders.txt")
        Clear()
        input("Your order has been successfully placed (press ENTER to continue)...")
    
def manage_orders():
    Clear() # clearing previous outputs
    
    print("Managing orders...")
    orders = Table.loadData('orders.txt')
    
    # gettign current user
    _, email, _ = GetCurrentUser()
    
    try: # handling no orders for corresponding userse
        filtered_orders = orders.filter('customer_email', email)
    except ValueError: 
        input("No orders found (press ENTER to continue)...")
        return 
    # printing all users
    print(filtered_orders)
    
    while True:
        print("""
        Choose an action:
        1. Edit order
        2. Delete order
        3. Quit
        """)
        
        action = input("Enter the number of the action you want to perform: ").lower()
        
        Clear() # clearing previous outputs
        print(filtered_orders)
        match action:
            case '1':
                # Logic for editing staff
                order_id = input("Enter order id of order to edit: ")
                updateIdentifier = {'id': order_id}
                
                # breaking if invalid order id
                if not orders.search(updateIdentifier):
                    input("Order Id not found press ENTER to try again...")
                    break
                    
                updateData = {} 
                
                # displaying menu for changes
                menu = Table.loadData('menu.txt')
                print(menu)
                
                for key in orders.columns: 
                    if key == 'food_id' or key == 'quantity': # only updating food_id and quantity
                        userInput = input(f'Enter new {key} (Enter for no changes): ')
                        
                        # skipping if no changes
                        if not userInput: 
                            continue
                        
                        # updating food_name as well
                        if key == 'food_id': 
                            # validating food_id 
                            if userInput not in menu['id']: 
                                input('Incorrect food id press enter to continue again: ')
                                continue
                            food_name = menu['name'][menu.search({'id':userInput})]
                            
                            # updating food name food_name onto updateData
                            updateData.update({'food_name': food_name})
                            
                        if userInput: 
                            updateData.update({key: userInput})
                                
                Clear()
                orders.update(updateIdentifier, updateData)
                input("press ENTER to continue...")
                
            case '2':
                # Logic for deleting staff
                order_id = input("Enter id of order you want to delete: ")
                
                # clearing previous outputs
                Clear()
                
                # deleting from table 
                try: 
                    orders.delete({'id': order_id})
                    input("press ENTER to continue...")
                    Clear()
                except ValueError: 
                    input("Order id not found press ENTER to continue...")
            case '3':
                # Quit the loop
                break
            case _:
                Clear()
                input("Invalid choice. Try again. (press ENTER to continue)...")
                Clear()
    
        orders.saveData('users.txt')
    
def view_order_status():
    Clear() # clearing previous outputs
    
    print("viewing orders...")
    orders = Table.loadData('orders.txt')
    
    # gettign current user
    _, email, _ = GetCurrentUser()
    
    # getting only orders of logedin user
    try: 
        filtered_orders = orders.filter('customer_email', email)
    except ValueError: 
        input("No orders found (press ENTER to continue...)")
        
    # printing all users
    print(filtered_orders)
    
    input('press ENTER to continue...')

def send_feedback(): 
    Clear() # clearing previous outputs
    
    print("sending feedbacks...")
    
    # loading feedbacks
    feedbacks = Table.loadData('feedbacks.txt')
    
    # loading current user information 
    name, email, role = GetCurrentUser()
    
    # asking feedback
    feedback = input("Write your feedback: ")
    
    # constructing save data
    saveData = {
        'id': str(GenId(feedbacks['id'])), # randomly generates id 
        'customer_email': email, 
        'customer_name': name, 
        'feedback': feedback
    }
    
    # appending to feedback table
    feedbacks.append(saveData)
    
    # saving feedbacks
    feedbacks.saveData('feedbacks.txt')
    Clear()
    print(FancyTexts['thank you'])
    print("Your feedbacks are safe with our team ;)")
    input("press ENTER to continue...")
    
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
        # clearing previous loop outputs
        Clear()
        
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
            action()
                        
        
        # if choice is not valid
        else: 
            Clear() # clearing previous outputs
            input("Invalid choice press ENTER to try again...")
            
if __name__ == '__main__': 
    main()