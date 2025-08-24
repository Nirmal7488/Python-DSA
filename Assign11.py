from linkedList import *
class Stack(SLL):
    def isEmpty(self):
        return super().isEmpty()
    def push(self,data):
        self.insertAtBeg(data)
    def pop(self):
        if not self.isEmpty():
            self.delAtBeg()
        else:
            raise IndexError("Stack is Empty")
    def peek(self):
        if not self.isEmpty():
            return self.Start.item
        else:
            raise IndexError("Stack is Empty")
    
s1=Stack()
s1.push(6)
s1.push(3)
s1.push(5)
s1.pop()
s1.pop()
print(s1.peek())
