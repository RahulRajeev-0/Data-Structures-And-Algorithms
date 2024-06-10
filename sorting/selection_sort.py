'''
Divide the array into two part 
find the smallest element from the unsorted part
swap it to the sorted postion

--- complexity ----
complext (all best , worst, avarage) = O(n^2)

space complexity = O(1)

not a stable sorting algorithm 

'''

def selection_sort(arr) :
    for i in range(len(arr)):
        min_ele = min(arr[i:])
        min_index = arr.index(min_ele)
        if arr[i] != arr[min_index]: arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

l = [2,3,1,3,7,755,32]
selection_sort(l)
print(l)

