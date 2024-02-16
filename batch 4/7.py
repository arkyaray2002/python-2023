def bin_search(li, item):
    li.sort()
    high = len(li) - 1
    low = 0
    while(low <= high):
        mid = (low + high) //2
        if li[mid] == item:
            return mid
        elif li[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return -2

print(f"Index : {bin_search([1,2,3,4,5,6,7,8], 10) + 1}")
