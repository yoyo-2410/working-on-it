class Stack:
    def __init__(self): self.s=[]
    def push(self,x): self.s.append(x)
    def pop(self): return self.s.pop() if self.s else ''
    def top(self): return self.s[-1] if self.s else ''
    def empty(self): return not self.s

def infix_to_postfix(exp):
    p, st, out = {'+':1,'-':1,'*':2,'/':2,'^':3}, Stack(), ''
    for ch in exp:
        if ch.isalnum(): out += ch
        elif ch=='(': st.push(ch)
        elif ch==')':
            while st.top()!='(': out+=st.pop()
            st.pop()
        else:
            while not st.empty() and p.get(ch,0)<=p.get(st.top(),0): out+=st.pop()
            st.push(ch)
    while not st.empty(): out+=st.pop()
    return out

print("Postfix:", infix_to_postfix(input("Enter infix: ")))
