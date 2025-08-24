#Implementation of Queue using linkedList class

from linkedList import *
class Queue():
    def __init__(self):
        self.items=SLL()
        self.count=0
    def isEmpty(self):
        return self.items.isEmpty()
    def enqueue(self,data):
        self.items.insertAtEnd(data)
        self.count+=1
    def dequeue(self):
        if not self.isEmpty():
            self.items.delAtBeg()
            self.count-=1
        else:
            raise IndexError("Queue is Empty")
    def get_front(self):
        if not self.isEmpty():
            return self.items.Start.item
        else:
            raise IndexError("Queue is Empty")
    def get_rear(self):
        if not self.isEmpty():
            temp=self.items.Start
            while True:
                if temp.next==None:
                    return temp.item
                temp=temp.next
        else:
            raise IndexError("Queue is Empty")
    def size(self):
        return self.count

q1=Queue()
q1.enqueue(7)
q1.enqueue(3)
q1.enqueue(5)
q1.enqueue(1)
q1.dequeue()
q1.dequeue()
# q1.dequeue()
# q1.dequeue()
print("Front : ",q1.get_front())
print("Rear : ",q1.get_rear())
print("Size : ",q1.size())