#Implementation of Queue Using List
class Queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return len(self.items)==0
    def enqueue(self,data):
        self.items.append(data)
    def dequeue(self):
        if not self.isEmpty():
            self.items.pop(0)
        else:
            raise IndexError("Queue is Empty")
    def get_front(self):
        if not self.isEmpty():
            return self.items[0]
        else:
            raise IndexError("Queue is Empty","Hello")
    def get_rear(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise IndexError("Queue is Empty")
    def size(self):
        return len(self.items)


q1=Queue()
try:
    print(q1.get_front())
except IndexError as e:
    print(e.args[1])

q1.enqueue(5)
q1.enqueue(8)
q1.enqueue(1)
q1.enqueue(7)
q1.dequeue()
# q1.dequeue()
# q1.dequeue()
# q1.dequeue()
print("Front : ",q1.get_front())
print("Rear : ",q1.get_rear())
print("Size : ",q1.size())
    
    