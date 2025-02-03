def UpdateProfile(email, **updatekwargs): 
    AttributesPositions = {
        'updateName': 1, 
        'updatePassword': 2,
        'updateEmail': 3
    }
    # exiting early if the updatekwargs doesn't meet the requirements
    for key in updatekwargs: 
        if key not in AttributesPositions: 
            print("Invalid key")
            return
        
    # reading file
    with open("Databases/users.txt", 'r') as file: 
        lines = file.readlines()
    
    # finding the mentioned email and replacing with updated data
    for index, line in enumerate(lines): 
        line = line.split(',')
        if line[AttributesPositions['updateEmail']] == email: 
            for key, value in updatekwargs.items():
                line[AttributesPositions[key]] = value

            # exiting loop early after email if found
            line = ','.join(line)
                            
            # saving the updated line
            lines[index] = line
            break
        
    # if email is not found
    else: 
        print("Email not found")
        return

    # saving the updated user file
    with open('Databases/users.txt', 'w') as file: 
        for line in lines: 
            file.write(line)
    

# for unit api testing
if __name__ == "__main__": 
    UpdateProfile("alice.brown@example.com", updateEmail = 'anush@gmail.com')