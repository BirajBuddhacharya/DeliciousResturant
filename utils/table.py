import os

class Table:   
    """
    A class to represent a table structure with headers and rows of data.
    
    Attributes:
        tableData (dict): A dictionary to store table headers and body data.
            Structure: 
                self.tableData = {
                    'heading1': ['data1', 'data2', 'data3'], 
                    'heading2': ['data1', 'data2', 'data3']
                }
        colLen (int): Number of columns in the table.
    
    Methods:
        __init__(data):
            Initializes the table with the provided data.
        
        __search(searchItem: dict):
            Searches for an element in the table using the given key-value pair.
        
        loadData(filename):
            Loads table data from a CSV file and returns an instance of the class with the loaded data.
        
        append(data: dict):
            Appends data to the table object (will not be saved in file).
        
        update(updateIdentifier: dict, updateData: dict):
            Updates data in the table based on the given identifier.
        
        delete(deleteIdentifier: dict):
            Deletes data from the table based on the given identifier.
        
        saveData(fileName):
            Saves the current table data to a CSV file.
        
        __str__():
            Returns a string representation of the table.
    """
    def __init__(self, data: dict): 
        # validating data
        previous = len(data[next(iter(data))]) # getting length of first element 
        for _, item in data.items(): 
            current = len(item)
            if current != previous: 
                raise ValueError('the length of dict data must match')
            previous = current
            
        self.tableData = data  # table data storage
        self.colLen = len(self.tableData)
        
    def search(self, searchItem: dict): 
        """
        Searches for an element in the table using the given key-value pair.
        
        Args:
            searchItem (dict): A dictionary containing a single key-value pair to search for.
                Structure:
                Note: The length of the dictionary must be 1.
        
        Returns:
            int: The index of the element in the table if found.
            None: If the element is not found or if an error occurs.
        
        Example: 
            index = self.__search({'name': 'x'})
        """
        # only supports dict with 1 item
        if len(searchItem) > 1 or len(searchItem) == 0: 
            print("bad parameter given len must be 1")
        
        key, value = [(key, value) for key, value in searchItem.items()][0]
        for i, element in enumerate(self.tableData[key]): 
            if element == value: 
                return i

        # if value not found
        raise IndexError("value not found")   
     
    
    @classmethod
    def loadData(cls, filename): 
        """
        Loads data from a CSV file in the database and returns an instance of the class with the loaded data.
        
        Args:
            filename (str): The name of the file to load.
        
        Returns:
            cls: An instance of the class with the loaded data.
        
        Raises:
            FileNotFoundError: If the specified file does not exist.
            ValueError: If the CSV file format is incorrect (i.e., the number of columns does not match the header).
        
        Example:
            table_instance = Table.loadData('example.csv')
        """
        # making dict to store loaded data
        tableData = {}
        
        fullPath = os.path.join('Database', filename)
        
        # reading file
        try: 
            with open(fullPath, 'r') as file: 
                lines = file.readlines()
            
        # handling wrong file
        except FileNotFoundError: 
            print("The given file path doesn't exist no data loaded")
            return 
        
        # returning if file is empty
        if not lines: 
            raise ValueError("The file is empty")
        
        # loading data into self.tableData
        for index, line in enumerate(lines): 
            line = line.replace('\n', '').split(';')   # removing any newline and spliting data into list
            
            # handling header
            if index == 0: 
                for header in line: 
                    tableData[header] = []
                    
            # handling table body
            else: 
                # handling inproper csv format
                if len(line) != len(tableData): 
                    raise ValueError("Bad CSV: data length doesn't match with header")
                
                for key, data in zip(tableData.keys(), line): 
                    tableData[key].append(data)
        
        return cls(tableData)
    
    def append(self, data: dict): 
        """
        Appends data to the table object (will not be saved in file).
        
        Args: 
            data (dict): A dictionary of data to append (must match the structure of the table).
        Example: 
            instance.append({'appendkey1': 'value', 'appendkey2': 'value'})
        """
        # validating data
        if type(data) != dict: 
            print("parameter must me of type dict")
            return 
        if any(key not in self.tableData for key in data) or len(data) != self.colLen: 
            print('bad append data: data must having matching key as tableData no data appended')
            return 
        
        for key, item in data.items(): 
            self.tableData[key].append(item)
    
    def update(self, updateIdentifier:dict, updateData:dict):
        """
        Updates data in the table based on the given identifier.
        
        Args:
            updateIdentifier (dict): A dictionary containing a single key-value pair to identify the row to update.
            updateData (dict): BirajBuddhacharya/testingRepoA dictionary containing the data to update.
        """
        # validating data 
        if any((key not in self.tableData) for key in updateIdentifier): 
            print("given data is not valid: all key must match the key in table")
            return 
        
        index = self.search(updateIdentifier)
        
        for key, value in updateData.items(): 
            self.tableData[key][index] = value
        
        print("Data updated Successfully")
        return 
            

    def delete(self, deleteIdentifier: dict):
        """
        Deletes data from the table based on the given identifier.
        
        Args:
            deleteIdentifier (dict): A dictionary containing a single key-value pair to identify the row to delete.
        """
        index = self.search(deleteIdentifier)
        
        for _, value in self.tableData.items(): 
            del value[index]
        
        print("Data deleted successfully")
            
    def saveData(self, fileName):
        """
        Saves the current table data to a CSV file.
        
        Args:
            fileName (str): The name of the file to save the data to.
        """
        fullPath = os.path.join('Database', fileName) 
        saveStr = ''
        
        # formating self.tableData into rows and columns
        columns = [[header, *item] for header, item in self.tableData.items()]
        rows = zip(*columns)
        
        saveStr = ''
        for row in rows:
            saveStr += ';'.join(row) + '\n'
            
        # saving into file 
        with open(fullPath, 'w') as fp:
            fp.write(saveStr) 
    
            
    def __str__(self):  
        """
        Returns a string representation of the table.
        
        Returns:
            str: A formatted string representation of the table.
        """
        if not self.tableData:
            return "Table is empty."

        # formating columns
        columns = [[header, *item] for header, item in self.tableData.items()]
        
        # Determine column widths dynamically
        col_widths = [
            max(len(str(element)) for element in column)
            for column in columns
        ]
        
        # Create formatted row function
        def format_row(row):
            return "| " + " | ".join(f"{str(element):<{col_widths[i]}}" for i, element in enumerate(row)) + " |"

        # Generate separator
        separator = "+-" + "-+-".join("-" * col_widths[i] for i in range(len(col_widths))) + "-+"

        # Construct table
        rows = zip(*columns) # zips corresponding column element into list (row)
        rows_iter = iter(rows)
        
        # constructing header
        return_str = f"{separator}\n{format_row(next(rows_iter))}\n{separator}\n"
        return_str += "\n".join(format_row(row) for row in rows_iter)
        return_str += f"\n{separator}"

        return return_str
    
    def __iter__(self): 
        columns = [item for _, item in self.tableData.items()]
        rows = zip(*columns) # zips corresponding column element into list (row)
        
        return iter(rows)
    
    def __getitem__(self, index): 
        if isinstance(index, list): 
            return Table({key: self.tableData[key] for key in index})
        
        return Table(self.tableData[index])
    
    def getRow(self, index): 
        # handling list index
        if isinstance(index, list): 
            row = {key: [value[i] for i in index] for key, value in self.tableData.items()}
        else: 
            row = {key: value[index] for key, value in self.tableData.items()}
            
        return Table(row)
     
    def filter(self, searchColumn, searchValue):
        if column := self.tableData.get(searchColumn, None): 
            index_list = []
            
            for i, value in enumerate(column): 
                if value == searchValue: 
                    index_list.append(i)
            
            # if not data found
            if len(index_list) == 0: 
                print("No data found")
                return
            
            return self.getRow(index_list)
        
        # if search column not found
        print("search column not found")
    
    def unique(self, key): 
        seen = set()
        display_index = []
        
        if column := self.tableData.get(key, None): 
            for i, value in enumerate(column): 
                if value not in seen:   
                    display_index.append(i)
                    seen.add(value)                
            
            return self.getRow(display_index)
        
        # if key not found
        print("key not found")
    
# unit testing
if __name__ == "__main__":
    table = Table.loadData('users.txt')
    print(table.filter('email', 'test@gmail.com'))
