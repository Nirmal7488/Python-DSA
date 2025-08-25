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
