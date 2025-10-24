class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, data):
        new = Node(data)
        if not self.rear:
            self.front = self.rear = new
        else:
            self.rear.next = new
            self.rear = new

    def dequeue(self):
        if not self.front:
            print("Queue Empty")
        else:
            print("Deleted:", self.front.data)
            self.front = self.front.next
            if not self.front:
                self.rear = None

    def display(self):
        if not self.front:
            print("Queue Empty")
            return
        temp = self.front
        while temp:
            print(temp.data, end=" -> " if temp.next else "\n")
            temp = temp.next

# Driver Code
q = Queue()
while True:
    ch = int(input("\n1.Enqueue 2.Dequeue 3.Display 4.Exit\nEnter choice: "))
    if ch == 1:
        q.enqueue(int(input("Enter element: ")))
    elif ch == 2:
        q.dequeue()
    elif ch == 3:
        q.display()
    else:
        break
