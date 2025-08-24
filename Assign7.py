#Implementation of Stack using List

class Stack:
    def __init__(self):
        self.item=[]
    
    def isEmpty(self):
        return len(self.item)==0
    
    def push(self,data):
        self.item.append(data)

    def pop(self):
        if not self.isEmpty():
            self.item.pop()
        else:
            raise IndexError("Stack is Empty")
    
    def peek(self):
        if not self.isEmpty():
            return self.item[-1]
        else:
            raise IndexError("Stack is Empty")
        
    def size(self):
        return len(self.item)
        
        


obj=Stack()
obj.push(5)
obj.push(1)
obj.push(2)
obj.pop()
obj.pop()
obj.pop()
obj.pop()
print(obj.peek())

