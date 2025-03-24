import sys; sys.path.append('.')
from utils.table import Table 

def isEmailValid(email: str) -> bool: 
    users = Table.loadData('users.txt')
    validity = email not in users['email']
    
    return validity

if __name__ == '__main__': 
    print(isEmailValid('sd@gmail.com'))