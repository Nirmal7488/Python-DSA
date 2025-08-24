#Implementation of Queue inheriting list class

class Queue(list):
    def isEmpty(self):
        return len(self)==0
    def enqueue(self,data):
        self.append(data)
    def dequeue(self):
        if not self.isEmpty():
            self.pop(0)
        else:
            pass
    def get_front(self):
        if not self.isEmpty():
            return self[0]
        else:
            pass
    def get_rear(self):
        if not self.isEmpty():
            return self[-1]
        else:
            pass
    def size(self):
        return len(self)
    
q=Queue()
q.enqueue(8)
q.enqueue(5)
q.enqueue(3)
q.enqueue(7)
q.dequeue()
q.dequeue()
# q.dequeue()
# q.dequeue()
print("Front: ",q.get_front())
print("Rear: ",q.get_rear())
print("size = ",q.size())