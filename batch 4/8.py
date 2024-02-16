def partition(li, low, high):
    pivot = li[high]
    i = low - 1
    for j in range(low, high):
        if li[j] <= pivot:
            i += 1
            li[i], li[j] = li[j], li[i]
    li[i+1], li[high] = li[high], li[i+1]
    return i + 1

def quicksort(li, low, high):
    if low < high:
        pi = patition(li, low, high)
        quicksort(li, low, pi- 1)
        quicksort(li, pi + 1, high)
