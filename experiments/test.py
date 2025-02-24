file = open('Database/users.txt', 'r')
lines = file.readlines()

for line in lines: 
    line = line.split(';')
    for i in line: 
        print(i, end='\t')