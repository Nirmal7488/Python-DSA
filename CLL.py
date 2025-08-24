#Circular Linked List

class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class CLL:
    def __init__(self,Last=None):
        self.Last=Last
    
    def isEmpty(self):
        return self.Last==None
    
    def traverse(self):
        if self.Last is not None:
            temp=self.Last.next
            while True:
                print(temp.item,end=" ")
                temp=temp.next
                if temp==self.Last.next:
                    break
    
    def addAtBeg(self,data):
        if self.Last is not None:
            n=Node(data,self.Last.next)
            self.Last.next=n      
        else:
            self.Last=Node(data)
            self.Last.next=self.Last

    def addAtEnd(self,data):
        if self.Last is not None:
            n=Node(data,self.Last.next)
            self.Last.next=n
            self.Last=n
        else:
            self.Last=Node(data)
            self.Last.next=self.Last

    def search(self,data):
        if self.Last is not None:
            temp=self.Last.next
            while True:
                if temp.item==data:
                    return temp
                temp=temp.next
                if temp==self.Last.next:
                    break
            return None

    def addAfter(self,temp,data):
        if self.Last is not None:
            if temp is not None:
                n=Node(data,temp.next)
                temp.next=n
                if temp==self.Last:
                    self.Last=n
                
                
                



    

obj=CLL()
obj.addAtBeg(6)
obj.addAtBeg(8)
obj.addAtEnd(3)
obj.addAtBeg(4)
obj.addAfter(obj.search(4),5)
obj.addAfter(obj.search(3),9)
obj.addAfter(obj.search(6),7)

obj.traverse()