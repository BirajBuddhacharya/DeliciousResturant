def GetCurrentUser(): 
    with open('Cookies/user.txt', 'r') as file: 
        line = file.readline()
        
    line = line.split(',')
    name, email, role = line
        
    return name, email, role
    