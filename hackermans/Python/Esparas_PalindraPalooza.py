class Node:     #Node class
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:        #stack class
    def __init__(self, sen):
        self.top = None     #Top node of stack list
        self.sen = sen      #original input

    def push(self, new):
        x = Node(new)
        if self.top is None:    #if top is empty, pushes input to top
            self.top = x
            self.top.next = None    #makes address/space for the next node
        else:
            x.next = self.top   #stores the top node to new node's next, and replace top node with new node
            self.top = x

    def display(self):      #displays original, cleaned, and is a palindrome. if empty stack, displays "Empty Stack."
        if self.top is None:
            return print("Empty Stack")
        palin = self.stack()
        print(f"Original Sentence: {self.sen}\nCleaned Sentence: {palin}\nIs a Palindrome?: {self.compare()}")

    def stack(self):    #stacks the data in Nodes to a single variable for later use
        store = ""
        if self.top is None:
            return None
        else:
            temp = self.top
            while temp:
                store += temp.data
                temp = temp.next
        return store
    
    #Comparison of original sentence to stacked variable
    def compare(self):
        palin = self.stack()
        orig = ""
        for i in self.sen:
            if i.isalpha():
                orig += i.lower()
        if palin == orig:
            return True
        else:
            return False


while True: #unlimited usability
    sample = input("Input: ")   #accepts user's input
    console = Stack(sample)
    sample = sample.lower()     #makes user's input to lowercase
    for i in sample:    #stores chars in stack list
        if i.isalpha():     #if char is a letter, pushes it to stack. If not, ignores it.
            console.push(i)

    console.display()
    if console.stack() is None: #if input is not a letter, or empty, ends the program
        break
