def heapify (arr, n, i):
    largest = i
    left = i * 2 + 1
    right = i * 2 + 2


    if left < n and arr[left] > arr[i]: largest = left
    if right < n and arr[right] > arr[largest]: largest = right

    if largest != i :
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    

def heapSort(arr):
    n = len(arr)

    # for buiding a maxHeap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1 , 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
print("Sorted array is:", arr)


