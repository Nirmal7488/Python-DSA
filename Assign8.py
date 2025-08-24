class Stack(list):
    def is_Empty(self):
        return len(self)==0
    def push(self,data):
        self.append(data)
    def pop(self):
        if not self.is_Empty():
            return super().pop()
        else:
            raise IndexError("Stack is Empty")
    def peek(self):
        if not self.is_Empty():
            return self[-1]
        else:
            raise IndexError("Stack is Empty")
    def size(self):
        return len(self)

    def insert(self,index,data):
        raise AttributeError("No attribute 'insert' in stack.")


obj = Stack()
obj.push(8)
obj.insert(1,9)

obj.pop()
    
    
