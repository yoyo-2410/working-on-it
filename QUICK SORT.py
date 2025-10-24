def quick_sort(a, low, high):
    if low < high:
        p = partition(a, low, high)
        quick_sort(a, low, p - 1)
        quick_sort(a, p + 1, high)

def partition(a, low, high):
    pivot = a[low]
    i, j = low + 1, high
    while True:
        while i <= j and a[i] <= pivot: i += 1
        while i <= j and a[j] >= pivot: j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
        else:
            break
    a[low], a[j] = a[j], a[low]
    return j

print("QUICK SORT METHOD\n")
arr = [int(x) for x in input("Enter elements separated by space: ").split()]
print("\nUnsorted Array:", arr)
quick_sort(arr, 0, len(arr) - 1)
print("\nSorted Array using Quick Sort:", arr)
