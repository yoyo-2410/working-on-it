def dfs(graph, node, visited=None):
    if visited is None: visited = []
    visited.append(node)
    for n in graph.get(node, []):
        if n not in visited:
            dfs(graph, n, visited)
    return visited

graph = {
    "A":["B","C"], "B":["D"], "C":["E","F"],
    "D":[], "E":["G"], "F":[], "G":[]
}

print("\nDFS Traversal:", dfs(graph, "A"))
