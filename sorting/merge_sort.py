'''
------merge sort-------

uses two function 

first one for comparing and arranging 
second one for dividing the array into small parts 

uses divide and conquer method 

merge function takes left and right arrays 
and compare them and add them on sorted order to an extra array named merged and return it

merge_sort function is responsible for dividing the array into small parts 
and calling the merge function (helper) 

-> stable sorting algorithm 
-> average case complexity O(n log n )
-> worst case complexity O (n log n)
-> space complexity O(n)




'''

def merge (left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index] :
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
    
    return merged

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)

    merged = merge(left_arr, right_arr)
    return merged


l = [2,3,1,3,7,755,32]

print(merge_sort(l))


