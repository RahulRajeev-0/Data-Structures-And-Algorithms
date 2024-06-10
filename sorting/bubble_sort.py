"""
The main part of bubble sort is it compares the adjacent element
and swap it if it is in the woring position 

complexity of O(n**2)

bubble sort is stable sorting alogrithm 

not efficent for large data set 

usually not used because of complexity 
"""



def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]: arr[i], arr[j] = arr[j], arr[i]
    return arr
l = [2,3,1,3,7,755,32]
bubble_sort(l)
print(l)


