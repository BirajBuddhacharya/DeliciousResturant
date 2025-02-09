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
    def __init__(self): 
        self.tableData = {'header': [], 'body': []} # table data storage
        
    def addHeader(self, *headers): 
        self.tableData['header'] = headers
        
        # assigning no of columns
        self.columnsLen =  len(headers)
        
    def addRow(self, *data): 
        # checking if row data matches the number of header
        if len(data) != self.columnsLen: 
            print("No of data must match column. No data added")
            return 
        
        self.tableData['body'].append(data)
    
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
                self.addHeader(*line)
            # handling table body
            else: 
                self.addRow(*line)
    
    def saveData(self, fileName): 
        saveStr = ''
        
        # saving head
        saveStr += ','.join(self.tableData['header'])
        # adding line break 
        saveStr += '\n'
        
        for data in self.tableData['body']: 
            saveStr += ','.join(data)
            # line break 
            saveStr += '\n'
            
        # saving into file 
        with open(fileName, 'w') as fp:
            fp.write(saveStr) 
            
    def __str__(self):  
        if not self.tableData['header'] or not self.tableData['body']:
            return "Table is empty."

        # Determine column widths dynamically
        col_widths = [max(len(str(row[i])) for row in [self.tableData['header']] + self.tableData['body']) for i in range(len(self.tableData['header']))]

        # Create formatted row function
        def format_row(row):
            return "| " + " | ".join(f"{str(row[i]):<{col_widths[i]}}" for i in range(len(row))) + " |"

        # Generate separator
        separator = "+-" + "-+-".join("-" * col_widths[i] for i in range(len(col_widths))) + "-+"

        # Construct table
        return_str = f"{separator}\n{format_row(self.tableData['header'])}\n{separator}\n"
        return_str += "\n".join(format_row(row) for row in self.tableData['body'])
        return_str += f"\n{separator}"

        return return_str
    
    def append(self, *appendargs):
        if len(appendargs) != self.columnsLen: 
            print("args and columns len doesn't match. No change done") 
            return 
        
        self.tableData['body'].append(appendargs)
        
     
# unit testing
if __name__ == "__main__": 
    table = Table()
    table.loadData('users.txt')
    print(table)
    table.saveData('usersTest.txt')

