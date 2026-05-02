class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def __repr__(self):
        items = []
        current = self.top

        while current is not None:
            items.append(str(current.value))
            current = current.next

        return "Stack(top -> " + " -> ".join(items) + ")"



    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size +=1
        return self.top.value

    def pop(self, value):
        if self.top is None:
            raise IndexError("Stack is empty --Stack Underflow")
        value_returned = self.top.value
        self.top = self.top.next

        self.size -=1 
        return value_returned

    def peek(self):
        if self.top is None:
            raise ValueError("Stack is empty --Stack Underflow")
        return self.top.value

    def is_empty(self):
        return self.top is None


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(50)
    stack.push(60)
    print(stack.peek())
    print(stack)