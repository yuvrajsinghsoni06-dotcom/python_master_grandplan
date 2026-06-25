# with statement is used to wrap the execution block within the context manager

file_path = "C:/Users/1000/OneDrive/Documents/python_master_grandplan/file I-o/hello.txt"
try: 
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:  # Changed 'expect' to 'except'
    print("hero kya baat hai")  # Indented this line
except PermissionError:
    print("you dont have the permission to read thsi file")