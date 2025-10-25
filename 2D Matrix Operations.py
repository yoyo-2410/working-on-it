import numpy as np

r1, c1 = map(int, input("Enter rows, cols of Matrix 1: ").split())
r2, c2 = map(int, input("Enter rows, cols of Matrix 2: ").split())

A = np.array([list(map(float, input("Row: ").split())) for _ in range(r1)])
B = np.array([list(map(float, input("Row: ").split())) for _ in range(r2)])

if r1 == r2 and c1 == c2:
    print("\nAddition:\n", A + B)
    print("Subtraction:\n", A - B)
else:
    print("\nAddition/Subtraction not possible.")

if c1 == r2: print("\nMultiplication:\n", A @ B)
else: print("\nMultiplication not possible.")

s = float(input("\nEnter scalar: "))
print("\nScaling:\n", A * s)
