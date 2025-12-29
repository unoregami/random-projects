import random

class Node():
    def __init__(self, data):
        self.head = self
        self.data = data
        self.next = None
        self.back = None
        self.tail = None

    def seeHead(self):
        try:
            return self.head.data
        except:
            return self.head

    def seeTail(self):
        try:
            return self.tail.data
        except:
            return self.tail

    def push(self, next):
        if self.tail == None:
            next.back = self
            self.next = next
            self.tail = next
        else:
            self.next.push(next)
            self.tail = next

    def shift(self):
        if self.head == None or self.head.next == None:
            self.head = None
            self.data = None
            self.tail = None
            print("Node is Empty!")
        else:
            self.head = self.head.next
            self.head.back = None

    def pop(self):
        if self.head == None or self.tail.back == None:
            self.head = None
            self.data = None
            self.tail = None
            print("Node is Empty!")
        else:
            self.tail = self.tail.back
            self.tail.next = None


a = Node(0)

for i in range(1,10):
    a.push(Node(i))

for i in range(11):
    print(a.seeTail())
    a.pop()

