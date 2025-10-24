def merge_sort(a):
    if len(a) <= 1: return a
    mid = len(a)//2
    L, R = merge_sort(a[:mid]), merge_sort(a[mid:])
    res, i, j = [], 0, 0
    while i < len(L) and j < len(R):
        res.append(L[i] if L[i] < R[j] else R[j])
        if L[i] < R[j]: i += 1
        else: j += 1
    return res + L[i:] + R[j:]

print("MERGE SORT METHOD\n")
a = list(map(int, input("Enter elements separated by space: ").split()))
print("\nUnsorted:", a)
print("Sorted:", merge_sort(a))
