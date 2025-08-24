#Implementation of Queue inheriting linkedList class
from linkedList import *

class Queue(SLL):
    def __init__(self):
        self.count=0
        super().__init__()
    def isEmpty(self):
        return super().isEmpty()
    def enqueue(self,data):
        self.insertAtEnd(data)
        self.count+=1
    def dequeue(self):
        if not self.isEmpty():
            self.delAtBeg()
            self.count-=1
        else:
            raise IndexError("Queue is Empty")
    def get_front(self):
        if not self.isEmpty():
            return self.Start.item
        else:
            raise IndexError("Queue is Empty")
    def get_rear(self):
        if not self.isEmpty():
            temp=self.Start
            while True:
                if temp.next is None:
                    return temp.item
                temp=temp.next
        else:
            raise IndexError("Queue is Empty")
    def size(self):
        return self.count
    
q1=Queue()
q1.enqueue(8)
q1.enqueue(3)
q1.enqueue(9)
q1.enqueue(2)
q1.dequeue()
print("Front : ",q1.get_front())
print("Rear : ",q1.get_rear())
print("size : ",q1.size())
    