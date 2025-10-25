class Bag:
    def __init__(self): self.items = []
    def add(self, i): self.items.append(i)
    def contains(self, v): return v in self.items

b = Bag()
for _ in range(int(input("Enter number of items: "))):
    b.add(input("Enter item: "))

v = input("Enter value to search: ")
print("Found!" if b.contains(v) else "Not Found!")
