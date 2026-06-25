# with statement is used to wrap the execution block within the context manager
import json
file_path = "hello.json"
try: 
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content["greatone"])
except FileNotFoundError:  # Changed 'expect' to 'except'
    print("hero kya baat hai")  # Indented this line
except PermissionError:
    print("you dont have the permission to read thsi file")