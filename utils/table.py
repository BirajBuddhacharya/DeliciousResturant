import os

class Table: 
    """

    """
    def __init__(self): 
        self.tableData = {'header': [], 'body': []} # table data storage
        
    def addHeader(self, *headers): 
        self.tableData['header'] = headers
        self.columnsLen =  len(headers)
        
    def addRow(self, *data): 
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
     
# unit testing
if __name__ == "__main__": 
    table = Table()
    table.loadData('users.txt')
    print(table)

