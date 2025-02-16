import os 
import platform

def Clear(): 
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
        
# unit testing 
if __name__ == '__main__': 
    print("test")
    Clear()
    print('success')