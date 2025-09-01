#Implementation of Priority Queue using list
class PQueue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(self,priority,data):
        if not self.is_empty():
            for i in range(len(self.items)):
                if self.items[i][0]<priority:
                    return self.items.insert(i,[priority,data])
        self.items.append([priority,data])
    def pop(self):
        self.items.pop(0)
    def get_front(self):
        if not self.is_empty():
            return self.items[0][1]
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1][1]
    def size(self):
        return len(self.items)
    
    def traverse(self):
        for i in self.items:
            print(i)

pq=PQueue() 
pq.push(2,6)
pq.push(2,7)
pq.push(1,9)
pq.push(3,2)
pq.push(0,8)
pq.pop()

print("front:",pq.get_front())
print("rear:",pq.get_rear())

pq.traverse()


