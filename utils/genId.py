import random
from utils.table import Table

def GenId(checkList: list | Table) -> int: 
    """
        generates random id which is not in a given list 
        args: 
            checkList (list | Table) -> list of item which will not be included in randomNum
        returns: 
            randomNum (int)
    """
    
    while True: 
        randomNum = random.randint(0, 9999)
        if randomNum not in checkList:
            return randomNum
    
