from utils.updateProfile import UpdateProfile
from utils.clear import Clear
from utils.table import Table
from APIs.getCurrentUser import GetCurrentUser

def view_orders(): 
    print("viewing orders.....")
    orders = Table.loadData('orders.txt')
    print(orders)

def update_order_status(): 
    print("Updating order status....")
    
    # loading orders
    orders = Table.loadData("orders.txt")

    # printing available orders
    print(orders)
    
    # incomplete
    
    
    
    
def request_ingredients():
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
    print("Ingredient has been requested")

def main(): 
    """
        - View orders placed by customers.
        - Update orders as "In Progress" or "Completed.”
        - Request ingredients (Add, Edit, Delete).
        - Update own profile.
    """
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
            print("Invalid choice try again")
            