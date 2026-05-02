# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None 

# class Stack:
#     def __init__(self):
#         self.top = None
#         self.size = 0
    
#     def __len__(self):
#         return self.size
    
#     def __repr__(self):
#         items = []
#         current = self.top

#         while current is not None:
#             items.append(str(current.value))
#             current = current.next

#         return "Stack(top -> " + " -> ".join(items) + ")"



#     def push(self, value):
#         new_node = Node(value)
#         new_node.next = self.top
#         self.top = new_node
#         self.size +=1
#         return self.top.value

#     def pop(self, value):
#         if self.top is None:
#             raise IndexError("Stack is empty --Stack Underflow")
#         value_returned = self.top.value
#         self.top = self.top.next

#         self.size -=1 
#         return value_returned

#     def peek(self):
#         if self.top is None:
#             raise ValueError("Stack is empty --Stack Underflow")
#         return self.top.value

#     def is_empty(self):
#         return self.top is None


# if __name__ == "__main__":
#     stack = Stack()
#     stack.push(10)
#     stack.push(20)
#     stack.push(30)
#     stack.push(40)
#     stack.push(50)
#     stack.push(60)
#     print(stack.peek())
#     print(stack)

class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1

    def is_full(self):
        return self.top == self.capacity - 1

    def is_empty(self):
        return self.top == -1

    def push(self, item):
        if self.is_full():
            raise ValueError("Stack Overflow")
        self.top += 1
        self.stack[self.top] = item

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack Underflow")
        # Removed unreachable 'return None' after raise
        item = self.stack[self.top]
        self.stack[self.top] = None 
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[self.top]
    
    def __repr__(self):
        # FIX: Reverse the range so we start from the 'top' index and go down to 0
        items = [str(self.stack[i]) for i in range(self.top, -1, -1)]
        return "ArrayStack(Top -> " + " -> ".join(items) + ")"

if __name__ == "__main__":
    stack = ArrayStack(5)
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    
    # After pushing 10, 20, 30, 40:
    # Top is at 40.
    
    # stack.pop() # Removes 40
    # stack.pop() # Removes 30
    
    print(stack) # Should display: ArrayStack(Top -> 20 -> 10)
    print(f"Current Peek: {stack.peek()}")