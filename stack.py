# peek, pop, push, to_string, size, is_empty

class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return self.size() == 0
    
    def peek(self):
        if self.is_empty():
            return None
        
        return self.items[-1]
    
    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()
    
    def to_string(self):
        if self.is_empty():
            return 'Stack is empty'
        
        result = ""
        
        for item in reversed(self.items):
            result += str(item) + '\n'

        return result.strip()


    
stack = Stack()

stack.push('book 1')
stack.push('book 2')
stack.push('book 3')

# print(stack.size())
# print(stack.peek())
print(stack.to_string())

stack.pop()
# print(stack.size())
# print(stack.peek())
print(stack.to_string())

