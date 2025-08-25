#Implementation of Deque by using doubly linked list class
from DLL import *

class Deque:
    def __init__(self):
        self.items=DLL()
        self.count=0
    def is_empty(self):
        return self.items.isEmpty()
    def insert_front(self,data):
        pass