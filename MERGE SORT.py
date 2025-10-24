def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a)//2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left, right)

def merge(L, R):
    res, i, j = [], 0, 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            res.append(L[i]); i += 1
        else:
            res.append(R[j]); j += 1
    res += L[i:] + R[j:]
    return res

print("MERGE SORT METHOD\n")
data = [int(x) for x in input("Enter elements separated by space: ").split()]
print("\nUnsorted Array:", data)
sorted_data = merge_sort(data)
print("\nSorted Array using Merge Sort:", sorted_data)
