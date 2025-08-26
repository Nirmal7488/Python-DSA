#Implementation of Deque by extending list class

class Deque(list):
    def is_empty(self):
        return len(self)==0
    def insert_front(self,data):
        self.insert(0,data)
    def insert_rear(self,data):
        self.append(data)
    def delete_front(self):
        if not self.is_empty():
            self.pop(0)
        else:
            raise IndexError("Deque Underflow")
    def delete_rear(self):
        if not self.is_empty():
            self.pop(-1)
        else:
            raise IndexError("Deque Underflow")
    def get_front(self):
        if not self.is_empty():
            return self[0]
        else:
            raise IndexError("Deque Underflow")
    def get_rear(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Deque Underflow")
    def size(self):
        return len(self)

d1=Deque()
d1.insert_front(6)
d1.insert_front(8)
d1.insert_rear(3)
d1.insert_rear(4)
d1.delete_front()
d1.delete_rear()
print(d1.get_front())
print(d1.get_rear())
print(d1.size())