class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class Stack:
    def __init__(self,Tos=None):
        self.Tos=Tos
    
    def isEmpty(self):
        return self.Tos==None
    
    def push(self,data):
        n=Node(data,self.Tos)
        self.Tos=n
    
    def pop(self):
        if self.Tos is not None:
            val=self.Tos.item
            self.Tos=self.Tos.next
        else:
            raise IndexError("Stack is Empty(Underflow)")
    
    def peek(self):
        if self.Tos is not None:
            return self.Tos.item
        else:
            raise IndexError("Stack is Empty(Underflow)")
    

s1=Stack()
s1.push(4)
s1.push(7)
s1.push(2)
s1.pop()

print(s1.peek())

            