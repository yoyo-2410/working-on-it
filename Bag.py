# Program: Bag

class Bag:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def count(self, item):
        return self.items.count(item)

bag = Bag()
bag.add(10)
bag.add(20)
bag.add(10)

print("Bag items:", bag.items)
print("Count of 10:", bag.count(10))
