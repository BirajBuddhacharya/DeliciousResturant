import os 
import platform

def Clear(): 
    exec = 'cls' if platform.system() == 'Windows' else 'clear'
    
    os.system(exec)
        
# unit testing 
if __name__ == '__main__': 
    print("test")
    Clear()
    print('success')