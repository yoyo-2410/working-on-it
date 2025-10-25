def dfs(g,n,v=None):
    v=v or []; v+=[n]
    for x in g.get(n,[]):
        if x not in v: dfs(g,x,v)
    return v

g={"A":["B","C"],"B":["D"],"C":["E","F"],"D":[],"E":["G"],"F":[],"G":[]}
print("DFS Traversal:",dfs(g,"A"))
