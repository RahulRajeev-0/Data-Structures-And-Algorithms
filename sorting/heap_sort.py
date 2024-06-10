# heap sort 
# use heapify function (max)
# first make the array a max heap 
# then swap the first element to the last while iteration 


# heapfiy function takes 3 arguements => they are array, endpoint , starting root index  
# 

def heapify (arr, n, i):
    largest = i
    left_child = i * 2 + 1
    right_child = i * 2 + 2

    if left_child < n and arr[left_child] > arr[i]: largest = left_child
    if right_child < n and arr[right_child] > arr[largest] : largest = right_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

# making a max heap
    for i in range(n // 2 - 1, -1, -1): # iterating backwords from the middle
        heapify(arr, n, i)

    for i in range(n - 1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Sorted array is:", arr)



