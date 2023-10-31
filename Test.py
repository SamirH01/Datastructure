def sequential_search(elements, e):
    for i in range(len(elements)):
        if elements[i] == e:
            return i 
    return -1

list = [1, 2, 5, 6, 7, 8]

print(sequential_search(list, 8))

def binary_search(elements, e):
    low = 0
    high = len(elements)-1
    while(low <= high):
        mid = (low+high)//2
        if (elements[mid] > e):
            high = mid-1
        elif (elements[mid] < e):
            low = mid+1
        else: 
            return mid
    return -1

print(binary_search(list, 8))