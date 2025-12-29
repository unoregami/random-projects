class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class List:
    def __init__(self):
        self.top = None
        
    def push(self):
        x = Node(int(input("Input: ")))
        if self.top is None:
            self.top = x
            self.top.next = None
            return
        x.next = self.top
        self.top = x
        
    def display(self):
        temp = self.top
        while temp:
            print(f"[{temp.data}] ", end = "")
            temp = temp.next
        

sample = List()
sample.push()
sample.push()
sample.push()
sample.push()
sample.push()
sample.display()
