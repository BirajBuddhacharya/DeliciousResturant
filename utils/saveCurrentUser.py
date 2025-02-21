def SaveCurrentUser(name:str, email:str, role:str): 
    """
        saves currently loged in user in cookie/user.txt file (acts as session variable)
    """
    data = [name, email, role]
    with open('Cookies/user.txt', 'w') as file: 
        file.write(';'.join(data))
        

# unit testing
if __name__ == '__main__': 
    pass