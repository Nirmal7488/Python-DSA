#Implementation of Deque Using List
class Deque:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def insert_front(self,data):
        self.items.insert(0,data)
    def insert_rear(self,data):
        self.items.append(data)
    def delete_front(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError("Queue Underflow")
    def delete_rear(self):
        if not self.is_empty():
            self.items.pop(-1)
        else:
            raise IndexError("Queue Underflow")
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue Underflow")
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Queue Underflow")
    def size(self):
        return len(self.items)
    
d1=Deque()
d1.insert_front(7)
d1.insert_front(4)
d1.insert_rear(2)
d1.insert_rear(9)
d1.delete_front()
d1.delete_rear()

print("Front :",d1.get_front()," Rear :",d1.get_rear())
print("Size :",d1.size())