def GetUser(email, ):
    """
        args: 
            email -> email of the user
        returns: 
            if in Users database:
                (name, password, role) -> (name of user, password of user, role of user)
            if not in Users database: 
                None
    """
    with open('Database/users.txt', 'r') as file: 
        for lineCount, line in enumerate(file): 
            # skipping the header of the table
            if lineCount == 0: 
                continue
            
            row = line.split(',') # seperates the string by commas and returns a list
            if row[2] == email: 
                return (row[0], row[1], row[3])
        
        # if the user is not found
        return None
   
# unit testing the api         
if __name__ == '__main__': 
    userData = GetUser("anushmaharjan@gmail.com")
    if userData: 
        name, password, role = userData
        print(name, password, role)