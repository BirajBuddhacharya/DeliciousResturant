import os

def update_profile(email, new_data):
    file_path = os.path.join(os.path.dirname(__file__), '../Databases/users.txt')
    
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        updated_lines = []
        for line in lines:
            if line.startswith(email):
                updated_line = f"{email},{new_data}\n"
                updated_lines.append(updated_line)
            else:
                updated_lines.append(line)
        
        with open(file_path, 'w') as file:
            file.writelines(updated_lines)
        
        print("Profile updated successfully.")
    except FileNotFoundError:
        print("The users file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
update_profile('user@example.com', 'new_data')
    
    