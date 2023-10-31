sorted_list = [2, 5, 6, 8, 23, 65]
list = [5, 54, 81, 567, 3, 8]

def sequential_search(elements, e):  #also called linear search
    for i in range(len(elements)):
        if elements[i] == e:
            return i 
    return -1

print(sequential_search(list, 8))

def binary_search(elements, e): #works for a sorted list
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

print(binary_search(sorted_list, 23))

def swap(elements, pos1, pos2):
    tmp = elements[pos1]
    elements[pos1] = elements[pos2]
    elements[pos2] = tmp

def insertion_sort(elements):  # use when array is nearly sorted or when the array is small
    for i in range(len(elements)):
        j = i
        while j > 0 and elements[j] < elements[j-1]:
            swap(elements, j, j-1)
            j-=1
    return elements


print(insertion_sort(list))

