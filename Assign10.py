from linkedList import *
class Stack:
    def __init__(self):
        self.items=SLL()
    def isEmpty(self):
        return self.items.isEmpty()
    def push(self,data):
        self.items.insertAtBeg(data)
    def pop(self):
        if not self.isEmpty():
            self.items.delAtBeg()
        else:
            raise IndexError("Stack is empty")
    def peek(self):
        if not self.isEmpty():
            return self.items.Start.item
        else:
            raise IndexError("Stack is empty")
        
s1=Stack()
s1.push(9)
s1.push(5)
s1.pop()
print(s1.peek())