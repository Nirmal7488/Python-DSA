class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class DLL:
    def __init__(self,Start=None):
        self.Start=Start

    def isEmpty(self):
        return self.Start==None
    
    def traverse(self):
        temp=self.Start
        while temp is not None:
            print(temp.item,end=" ")
            temp=temp.next

    def addAtBeg(self,data):
        if self.Start is not None:
            n=Node(self.Start.prev,data,self.Start)
            self.Start.prev=n
            self.Start=n
        else:
            self.Start=Node(None,data,None)

    
    def addAtEnd(self,data):
        if self.Start is not None:
            temp=self.Start
            while temp.next is not None:
                temp=temp.next
            temp.next=Node(temp,data,temp.next)
        else:
            self.Start=Node(None,data,None)

    def search(self,data):
        if self.Start is not None:
            temp=self.Start
            while temp is not None:
                if temp.item == data:
                    return temp
                temp=temp.next
            return None
    
    def addAfter(self,temp,data):
        if temp is not None:
            n=Node(temp,data,temp.next)
            if temp.next is not None:
                temp.next.prev=n
            temp.next=n

    def delAtBeg(self):
        if self.Start is not None:
            if self.Start.next is not None:
                self.Start = self.Start.next
                self.Start.prev=None
            else:
                self.Start=None

    def delAtEnd(self):
        if self.Start is not None:
            if self.Start.next is not None:
                temp=self.Start
                while True:
                    if temp.next is None:
                        temp.prev.next=None
                        break
                    temp=temp.next
            else:
                self.Start=None
    
    def delItem(self,data):
        if self.Start is not None:
            if self.Start.next is None:
                if self.Start.item == data:
                    self.Start=None
            else:
                temp=self.Start
                while True:
                    if temp.item==data:
                        if temp.prev is None:
                            temp.next.prev=None
                            self.Start=temp.next
                        else:
                            if temp.next is not None:
                                temp.next.prev=temp.prev
                            temp.prev.next=temp.next
                        break
                    temp=temp.next
                    if temp is None:
                        break

    def  __iter__(self):
        if self.Start==None:
            return DLLIterator(None)
        return DLLIterator(self.Start)                      

    
class DLLIterator:
    def __init__(self,Start):
        self.Current=Start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.Current==None:
            raise StopIteration
        data=self.Current.item
        self.Current=self.Current.next
        return data

            



myList = DLL()
myList.addAtBeg(4)
myList.addAtBeg(5)
myList.addAtEnd(2)
myList.addAfter(myList.search(2),8)
myList.addAfter(myList.search(4),7)
# myList.delAtBeg()
# myList.delAtEnd()
# myList.delItem(7)
# myList.delItem(5)
# myList.delItem(25)





# myList.traverse()
for i in myList:
    print(i,end=" ")