class Node:
    def __init__(self,d): self.d=d; self.l=self.r=None

def inorder(t):  if t: inorder(t.l); print(t.d,end=' '); inorder(t.r)
def preorder(t): if t: print(t.d,end=' '); preorder(t.l); preorder(t.r)
def postorder(t):if t: postorder(t.l); postorder(t.r); print(t.d,end=' ')

r=Node('A'); r.l=Node('B'); r.r=Node('C')
r.l.l=Node('D'); r.l.r=Node('E'); r.r.r=Node('F')

print("Inorder:"); inorder(r)
print("\nPreorder:"); preorder(r)
print("\nPostorder:"); postorder(r)
