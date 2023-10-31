def sequential_search(elements, e):
    for i in range(len(elements)):
        if elements[i] == e:
            return i 
    return -1

list = [1, 2, 5, 6, 7, 8]

print(sequential_search(list, 8))