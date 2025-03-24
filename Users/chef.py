import sys; sys.path.append('.')
from utils.updateProfile import UpdateProfile
from utils.clear import Clear
from utils.table import Table
from APIs.getCurrentUser import GetCurrentUser

def view_orders(): 
    Clear()
    print("viewing orders.....")
    orders = Table.loadData('orders.txt')
    print(orders)
    input("Press Enter to continue...")
    Clear()

def update_order_status(): 
    Clear() # clearing previous outputs
    print("Updating order status....")
    
    # loading orders
    orders = Table.loadData("orders.txt")

    # printing available orders
    print(orders)
    
    order_id = input("Enter order id of order to update: ")
    # validatin order id 
    if order_id not in orders['id']: 
        Clear()
        input("order id not in orders table (press ENTER to continue)...")
        return
    
    Clear()
    # getting order status
    order_statuses = {
        "1": "Pending",
        "2": "Ongoing",
        "3": "Completed"
    }
    # printing available statuses
    print("Order statuses:")
    for status_id, status in order_statuses.items():
        print(f"{status_id}. {status}")

    # getting status id from user
    status_id = input("Enter status id: ")
    
    # storing order status in a variable
    order_status = order_statuses.get(status_id, None)
    if not order_status: # validating order status 
        Clear()
        input("invalid status id (press ENTER to continue)")
        return 
    
    # updating orders
    orders.update({'id': order_id}, {'status': order_status})
    
    # saving updated orders
    orders.saveData('orders.txt')
    
    Clear()
    input("Order status updated successfully press ENTER to continue...")
    
def request_ingredients():
    Clear() # clearing previous outputs
    print("requesting ingredients...")
    
    ingredients = Table.loadData('ingredientsRequest.txt')
    
    # inputing ingredient name and quantity from user
    ingredient_name = input("Enter name of ingredient: ")
    quantity = input("Enter quantity: ")
    
    # getting email of chef from GetCurrentUser api
    _, chef_email, _ = GetCurrentUser()
    
    # appending ingredent to ingredient object 
    ingredients.append({'chef_email': chef_email, 'ingredient_name': ingredient_name, 'quantity': quantity})
    
    # saving ingredients
    ingredients.saveData("ingredientsRequest.txt")
    
    Clear()
    input("Ingredient has been requested press ENTER to continue...")

def main(): 
    """
        - View orders placed by customers.
        - Update orders as "In Progress" or "Completed.”
        - Request ingredients (Add, Edit, Delete).
        - Update own profile.
    """
    Clear() # clearing previous outputs
    
     # Mapping actions to corresponing action number
    actions = {
        "1": view_orders,
        "2": update_order_status,
        "3": request_ingredients,
        "4": UpdateProfile,
        "5": exit
    }

    # looping until user chooses a valid action
    while True:      
        Clear() # clearing output of previous loop 
        
        # printing user instructions
        print("""
        Choose an action:
        1. View orders
        2. Update order status
        3. Request ingredients
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
            

# unit testing
if __name__ == "__main__": 
    main()