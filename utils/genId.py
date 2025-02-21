import random

def GenId(checkList: list) -> int: 
    """
        generates random id which is not in a given list 
        args: 
            checkList (list) -> list of item which will not be included in randomNum
        returns: 
            randomNum (int)
    """
    
    while True: 
        randomNum = random.randint(0, 999999)
        if randomNum not in checkList:
            return randomNum