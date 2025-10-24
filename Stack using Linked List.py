# Stack using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new = Node(data)
        new.next = self.top
        self.top = new

    def pop(self):
        if self.top is None:
            print("Stack Empty")
        else:
            print("Popped:", self.top.data)
            self.top = self.top.next

    def display(self):
        temp = self.top
        if not temp:
            print("Stack Empty")
            return
        while temp:
            print(temp.data, end=" -> " if temp.next else "\n")
            temp = temp.next

# Driver Code
s = Stack()
while True:
    ch = int(input("\n1.Push  2.Pop  3.Display  4.Exit\nEnter choice: "))
    if ch == 1:
        s.push(int(input("Enter element: ")))
    elif ch == 2:
        s.pop()
    elif ch == 3:
        s.display()
    else:
        break
