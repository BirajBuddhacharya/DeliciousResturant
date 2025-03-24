from utils.clear import Clear
from utils.fancyTexts import FancyTexts
from utils.table import Table
from utils.login import Login
from utils.register import Register

def main(): 
    # clearing all previous outputs
    Clear()
    
    print(f"{'-' * 30} {FancyTexts['welcome']} {'-' * 30}")
    
    # making action map of corresponding function 
    actions = {
        '1': Login, 
        '2': Register,
    }

    while True: 
        print("""
            choose an action:
            1. Login
            2. Register 
        """)
        id = input("Enter the number of action you want to perform: ")
        
        if action := actions.get(id, None): 
            Clear()
            action()
            break
        else: 
            input("invalid option try again (press ENTER to continue)")
            Clear()
                
main()