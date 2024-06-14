# array already need to be sorted

# recursive binary search 

def binary_search_recursive(arr, left, right, target):
    if left > right:
        return -1
    mid = left + (right - left) // 2
    if arr[mid] == target: return mid
    if arr[mid] > target:
       return binary_search_recursive(arr, left, mid - 1, target)
    else:
       return binary_search_recursive(arr, mid + 1, right, target)
        
      

l = [1,2,3,4,5,6,7]
# print(binary_search_recursive(l, 0, len(l), 2))




# iterative 

def binary_search_iterative(arr, left, right, target):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target: 
            return mid
        if arr[mid] < target:
            left = mid + 1
        else :
            right = mid - 1
    return -1

print(binary_search_iterative(l, 0, len(l) , 3))
print(binary_search_recursive(l, 0, len(l) - 1, 5))
