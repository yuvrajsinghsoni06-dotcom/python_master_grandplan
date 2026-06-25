# with statement is used to wrap the execution block within the context manager
import csv
file_path = "helo.csv"
try: 
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)       
except FileNotFoundError:  # Changed 'expect' to 'except'
    print("hero kya baat hai")  # Indented this line
except PermissionError:
    print("you dont have the permission to read thsi file")