'''
------- quick sort ------

-> uses divide and conquer principle

works by selection of the pivot and find the correct position of pivot 
by partitioning the other two element into two sub array
then are sorted recurcively 

complexity 
time woast case time complixity O(n^2)  {when the pivot is selected is not good}
time best case time complixity O(n log n)
space complexity O(log n)

'''

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [i for i in arr[1:] if i <= pivot ]
    right = [i for i in arr[1:] if i > pivot ]
    return quick_sort(left) + [pivot] + quick_sort(right)

l = [2,3,1,3,7,755,32]

print(quick_sort(l))


