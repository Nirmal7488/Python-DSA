class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next


class Queue:
    def __init__(self,Start=None):
        self.Start=Start
        self.count=0
    def isEmpty(self):
        return self.Start==None
    def enqueue(self,data):
        if self.Start is not None:
            temp=self.Start
            while True:
                if temp.next==None:
                    break
                temp=temp.next
            temp.next=Node(data,None)
        else:
            self.Start=Node(data,None)
        self.count+=1
    def dequeue(self):
        if not self.isEmpty():
            self.Start=self.Start.next
            self.count-=1
        else:
            raise IndexError("Queue is Empty")
    
    def get_front(self):
        return self.Start.item
    def get_rear(self):
        if not self.isEmpty():
            temp=self.Start
            while True:
                if temp.next==None:
                    return temp.item
                temp=temp.next
        else:
            pass
    def size(self):
        return self.count
    
q1=Queue()
q1.enqueue(7)
q1.enqueue(9)
q1.enqueue(1)
q1.enqueue(5)
q1.dequeue()
print("Front : ",q1.get_front())
print("Rear : ",q1.get_rear())
print("size : ",q1.size())

