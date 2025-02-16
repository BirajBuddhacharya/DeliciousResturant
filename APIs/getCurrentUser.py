def GetCurrentUser(): 
    '''
        gets current user saved in cookie 
        args -> none
        returns ->
            name -> name of logged in user
            email -> email of logged in user
            role -> role of logged in user
    '''
    with open('Cookies/user.txt', 'r') as file: 
        line = file.readline()
        
    line = line.split(',')
    name, email, role = line
        
    return name, email, role
    