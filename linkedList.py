class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self,Start=None):
        self.Start = Start

    def isEmpty(self):
        return self.Start==None
    
    def traverse(self):
        temp=self.Start
        while temp is not None:
            print(temp.item,end=" ")
            temp=temp.next
      
    def insertAtBeg(self,data):
        n=Node(data,self.Start)
        self.Start=n
    
    def insertAtEnd(self,data):
        n=Node(data)
        if not self.isEmpty():
            temp=self.Start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.Start=n

    def search(self,data):
        temp=self.Start
        while temp is not None:
            if temp.item == data:
                return temp
            else:
                temp=temp.next
        return None

    def insertAfter(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n

    def delAtBeg(self):
        if self.Start is not None:
            self.Start=self.Start.next
        
    def delAtEnd(self):
        if self.Start is None:
            pass
        elif self.Start.next is None:
            self.Start=None
        else:
            temp=self.Start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
    
    def delItem(self,data):
        if self.Start is None:
            pass
        elif self.Start.next is None:
            if self.Start.item == data:
                self.Start=None
        else:
            temp=self.Start
            if temp.item == data:
                self.Start=temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next
                    
    def __iter__(self):
        return SLLIterator(self.Start)

            
class SLLIterator:
    def __init__(self,start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data

    


