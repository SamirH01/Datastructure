sorted_list = [2, 5, 6, 8, 23, 65]
list = [5, 54, 81, 567, 3, 8]

def sequential_search(elements, e):  #also called linear search
    for i in range(len(elements)):
        if elements[i] == e:
            return i 
    return -1

print(sequential_search(list, 8))

#----------------------------------------------------------------------------------------------------

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

#------------------------------------------------------------------------------------------------------

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

#----------------------------------------------------------------------------------------------------

def selection_sort(elements):    #Good to use when the cost of swap is a lot (swap=n-1)
    for i in range(len(elements)-1):
        bigIndex = 0
        for j in range(1, (len(elements)-i)):
            if elements[j] > elements[bigIndex]:
                bigIndex = j
        swap(elements, (len(elements)-1-i), bigIndex,)
    return elements

print(selection_sort(list))

#----------------------------------------------------------------------------------------------------

list2 = [43, 2, 3, 6, 98, 12, 23]

def merge(L1, L2):                           #a reasonably fast algorithm with a good worst case cost
    answer = []                              #specially good for linked-list
    while len(L1) > 0 and len(L2) > 0:       #linked-list = A linked list is a collection of “nodes” connected together via links. 
        x = L1[0]                            #These nodes consist of the data to be stored and a pointer to the address of the next node within the linked list.
        y = L2[0]
        if x <= y:
            answer.append(x)
            L1.remove(x)
        else: 
            answer.append(y)
            L2.remove(y)
    answer += L1
    answer += L2
    return answer

def mergesort(elements):
    if len(elements) <= 1:
        return elements
    L1 = elements[:(len(elements)//2)]
    L2 = elements[len(elements)//2:]
    return merge(mergesort(L1), mergesort(L2))

print(mergesort(list2))

list3 = [43, 2, 3, 6, 98, 12, 23]

def mergesort2(A, temp, left, right):
    if left == right:                 # List has one record
        return
    mid = (left + right) // 2         # Select midpoint
    mergesort2(A, temp, left, mid)     # Mergesort first half
    mergesort2(A, temp, mid+1, right)  # Mergesort second half
    for i in range(left, right+1):    # Copy subarray to temp
        temp[i] = A[i]
    # Do the merge operation back to A
    i1 = left
    i2 = mid + 1
    for curr in range(left, right+1):
        if i1 == mid+1:               # Left sublist exhausted
            A[curr] = temp[i2]
            i2 += 1
        elif i2 > right:              # Right sublist exhausted
            A[curr] = temp[i1]
            i1 += 1
        elif temp[i1] <= temp[i2]:    # Get smaller value
            A[curr] = temp[i1]
            i1 += 1
        else:
            A[curr] = temp[i2]
            i2 += 1
    return A

temp = [0] * len(list3) 

print(mergesort2(list3, temp, 0, len(list3)-1))

#------------------------------------------------------------------------------------------------------
