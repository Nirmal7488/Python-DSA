
from DLL import *

class Deque(DLL):
    def __init__(self):
        self.count=0
        super().__init__()
    def is_empty(self):
        return self.isEmpty()
    def insert_front(self,data):
        self.addAtBeg(data)
        self.count+=1
    def insert_rear(self,data):
        self.addAtEnd(data)
        self.count+=1
    def delete_front(self):
        if not self.is_empty():
            self.delAtBeg()
            self.count-=1
        else:
            raise IndexError("Deque Underflow")
    def delete_rear(self):
        if not self.is_empty():
            self.delAtEnd()
            self.count-=1
        else:
            raise IndexError("Deque Underflow")
    def get_front(self):
        if not self.is_empty():
            return self.Start.item
        else:
            raise IndexError("Deque Underflow")
    def get_rear(self):
        if not self.is_empty():
            temp=self.Start
            while temp.next is not None:
                temp=temp.next
            return temp.item
        else:
            raise IndexError("Deque Underflow")
    def size(self):
        return self.count
    
d1=Deque()
d1.insert_front(5)
d1.insert_front(7)
d1.insert_rear(1)
d1.insert_rear(9)
d1.delete_front()
d1.delete_rear()

print("front:",d1.get_front())
print("rear:",d1.get_rear())