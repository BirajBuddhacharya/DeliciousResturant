import os

class Table:   
    """
        A class to represent a table structure with headers and rows of data.
            Attributes
                -> tableData : dict
                    A dictionary to store table headers and body data.
                    structure: 
                        self.tableData = {
                            'header': (header1, header2), 
                            'body': [(data1, data2), (data3, data4)]
                        }
                -> columnsLen : int
                    The number of columns in the table. (Dynamically added on self.addHeader())
            Methods
                -> __init__():
                    Initializes the table with empty headers and body.
                -> addHeader(*headers):
                    Adds headers to the table.
                -> addRow(*data):
                    Adds a row of data to the table.
                -> loadData(tableName):
                    Loads table data from a file.
                -> __str__():
                    Returns a string representation of the table.
                    
    """
    def __init__(self, data = None): 
        # validating data
        if data: 
            previous = len(data[data.keys()[0]]) # getting length of first element 
            for _, item in data.items(): 
                current = len(item)
                if current != previous: 
                    raise ValueError('the length of dict data must match')
            
        self.tableData = data if data else {} # table data storage
    
    def loadData(self, tableName): 
        fullPath = os.path.join('Databases', tableName)
        
        # reading file
        try: 
            with open(fullPath, 'r') as file: 
                lines = file.readlines()
            
        # handling wrong file
        except FileNotFoundError: 
            print("The given file path doesn't exist no data loaded")
            return 
        
        # loading data into self.tableData
        for index, line in enumerate(lines): 
            line = line.replace('\n', '').split(',')   # removing any newline and spliting data into list
            
            # handling header
            if index == 0: 
                for header in line: 
                    self.tableData[header] = []
                    
            # handling table body
            else: 
                # handling inproper csv format
                if len(line) != len(self.tableData): 
                    raise ValueError("Bad CSV: data length doesn't match with header")
                
                for key, data in zip(self.tableData.keys(), line): 
                    self.tableData[key].append(data)
    
    def saveData(self, fileName): 
        saveStr = ''
        
        # formating self.tableData into rows and columns
        columns = [[header, *item] for header, item in self.tableData.items()]
        rows = zip(columns)
        
        saveStr = ''
        for row in rows:
            saveStr += ','.join(row) + '\n'
            
        # saving into file 
        with open(fileName, 'w') as fp:
            fp.write(saveStr) 
            
    def __str__(self):  
        if not self.tableData:
            return "Table is empty."

        # formating columns
        columns = [[header, *item] for header, item in self.tableData.items()]
        
        # Determine column widths dynamically
        col_widths = max(
            [ len(str(element)) for element in column ]
            for column in columns
        )
        

        # Create formatted row function
        def format_row(row):
            return "| " + " | ".join(f"{str(element):<{col_widths[i]}}" for i, element in enumerate(row)) + " |"

        # Generate separator
        separator = "+-" + "-+-".join("-" * col_widths[i] for i in range(len(col_widths))) + "-+"

        # Construct table
        rows = zip(columns) # zips corresponding column element into list (row)
        rows_iter = iter(rows)
        
        # debugging 
        for row in rows: 
            print(row)
            
        # # constructing header
        # return_str = f"{separator}\n{format_row(next(rows_iter))}\n{separator}\n"
        # return_str += "\n".join(format_row(row) for row in rows_iter)
        # return_str += f"\n{separator}"

        # return return_str
    
     
# unit testing
if __name__ == "__main__": 
    table = Table()
    table.loadData('users.txt')
    print(table)

