import numpy as np

r1,c1 = map(int,input().split())
r2,c2 = map(int,input().split())

A = np.array([list(map(float,input().split())) for _ in range(r1)])
B = np.array([list(map(float,input().split())) for _ in range(r2)])

if r1==r2 and c1==c2: print("Add:\n",A+B,"\nSub:\n",A-B)
else: print("Add/Sub not possible")

if c1==r2: print("Mul:\n",A.dot(B))
else: print("Mul not possible")

s = float(input()); print("Scaled:\n",A*s)
