#Implementation of Priority Queue Using Linked List

class Node:
    def __init__(self,priority=None,item=None,next=None):
        self.priority=priority
        self.item=item
        self.next=next

class PriorityQueue:
    def __init__(self,Start=None):
        self.Start=Start
    def is_empty(self):
        return self.Start==None
    def push(self,priority,data):
        if not self.is_empty():
            temp=self.Start
            if temp.next is None:
                if priority < temp.priority:
                    n=Node(priority,data,temp)
                    self.Start=n
                else:
                    temp.next=Node(priority,data,temp.next)
            elif priority < temp.priority:
                n=Node(priority,data,temp)
                self.Start=n
            else:
                while temp.next is not None:
                    back=temp
                    temp=temp.next
                    if priority < temp.priority:
                        back.next=Node(priority,data,temp)
                        return
                temp.next=Node(priority,data,temp.next)
        else:
            self.Start=Node(priority,data,None)
    
    def pop(self):
        if not self.is_empty():
            self.Start=self.Start.next

    def get_front(self):
        if not self.is_empty():
            return self.Start.item
        
    def get_rear(self):
        if not self.is_empty():
            temp=self.Start
            while temp.next is not None:
                temp=temp.next
            return temp.item
    
p=PriorityQueue()
p.push(1,8)
p.push(3,4)
p.push(5,13)
p.push(2,34)
p.push(4,10)
p.push(0,70)
p.push(1,55)

print("front : ",p.get_front())
print("rear : ",p.get_rear())

                


