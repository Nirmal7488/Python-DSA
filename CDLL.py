class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class CDLL:
    def __init__(self,Start=None):
        self.Start=Start
    
    def isEmpty(self):
        return self.Start==None

    def traverse(self):
        if self.Start is not None:
            temp=self.Start
            while True:
                print(temp.item,end=" ")
                temp=temp.next
                if temp==self.Start:
                    break
    
    def addAtBeg(self,data):
        if self.Start is not None:
            temp=self.Start
            n=Node(temp.prev,data,temp)
            temp.prev.next=n
            temp.prev=n
            self.Start=n
        else:
            self.Start=Node(None,data,None)
            self.Start.prev=self.Start
            self.Start.next=self.Start

    def addAtEnd(self,data):
        if self.Start is not None:
            temp=self.Start
            n=Node(temp.prev,data,temp)
            temp.prev.next=n
            temp.prev=n
        else:
            self.Start = Node(None,data,None)
            self.Start.prev=self.Start
            self.Start.next=self.Start
    
    def search(self,data):
        if self.Start is not None:
            temp=self.Start
            while True:
                if temp.item==data:
                    return temp
                temp=temp.next
                if temp==self.Start:
                    break
            return None

    def addAfter(self,temp,data):
        if self.Start is not None:
            if temp is not None:
                n=Node(temp,data,temp.next)
                temp.next=n
                temp.next.prev=n
    
    def delAtBeg(self):
        if self.Start is not None:
            if self.Start.next==self.Start:
                self.Start = None
            else:
                temp=self.Start
                temp=temp.next
                temp.prev=self.Start.prev
                self.Start.prev.next=temp
                self.Start=temp

    def delAtEnd(self):
        if self.Start is not None:
            if self.Start.next==self.Start:
                self.Start = None
            else:
                temp=self.Start
                temp=temp.prev
                temp.prev.next=temp.next
                self.Start.prev=temp.prev

    def deleteItem(self,data):
        if self.Start is not None:
            if self.Start.next==self.Start:
                if self.Start.item==data:
                    self.Start=None
            else:
                temp=self.Start
                while True:
                    if temp.item==data:
                        temp.prev.next=temp.next
                        temp.next.prev=temp.prev
                        if temp==self.Start:
                            self.Start=temp.next
                        return
                    temp=temp.next
                    if temp==self.Start:
                        break



obj=CDLL()
obj.addAtBeg(3)
obj.addAtBeg(7)
obj.addAtBeg(8)
obj.addAtBeg(4)
obj.addAtEnd(6)
obj.addAtEnd(3)
obj.addAtEnd(1)
obj.addAtEnd(9)
obj.addAfter(obj.search(4),2)
obj.delAtBeg()
obj.delAtBeg()
obj.delAtEnd()
obj.delAtEnd()
obj.deleteItem(3)
obj.deleteItem(3)
obj.deleteItem(8)
obj.deleteItem(7)
obj.deleteItem(6)

obj.traverse()