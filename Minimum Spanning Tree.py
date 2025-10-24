V = 5
G = [
    [0, 4, 0, 5, 2],
    [4, 0, 1, 3, 0],
    [0, 1, 0, 8, 0],
    [5, 3, 8, 0, 2],
    [2, 0, 0, 2, 0]
]

selected = [0]*V
selected[0] = 1
edges = 0
print("\nEdge : Weight")

while edges < V-1:
    min_w, x, y = 9999, 0, 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if not selected[j] and G[i][j]:
                    if G[i][j] < min_w:
                        min_w, x, y = G[i][j], i, j
    print(f"{x}-{y}: {G[x][y]}")
    selected[y] = 1
    edges += 1
