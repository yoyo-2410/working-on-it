class Stack:
    def __init__(self): self.s=[]
    def push(self,x): self.s.append(x)
    def pop(self): return self.s.pop() if self.s else ''
    def peek(self): return self.s[-1] if self.s else ''
    def empty(self): return not self.s

prec = lambda op: {'+':1,'-':1,'*':2,'/':2,'^':3}.get(op,0)
isop = lambda ch: ch.isalnum()

def infix_to_postfix(expr):
    s, out = Stack(), ''
    for ch in expr:
        if isop(ch): out+=ch
        elif ch=='(': s.push(ch)
        elif ch==')':
            while s.peek()!='(': out+=s.pop()
            s.pop()
        else:
            while not s.empty() and prec(ch)<=prec(s.peek()): out+=s.pop()
            s.push(ch)
    while not s.empty(): out+=s.pop()
    return out

print("Postfix:", infix_to_postfix(input("Enter infix: ")))
