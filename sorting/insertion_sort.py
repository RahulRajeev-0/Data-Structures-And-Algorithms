'''
insertion sort 

also divides the array into sorted and unsorted part 
assumes the first of element of the array is already sorted 
compare the next element with previous element and swap it

----- main thing to remember about the algorithm -----

first we store the key 
then we compare if the key is less than the previous number
if the key is less than the previous number then we swap the we make the arr[index_key] = arr[index_of_key - 1] 
===> now the key and index of key element become the large and also the previous one then 
we already store the value of key in a temp and change the previous element to key



if in the wrong position .

---- complexity ----
best case when the array is already sorted O(n)
average case O(n^2)
worst case O(n^2)

space complexity  O(1)

stable sorting algorithm

'''

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i] 
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key 
l = [2,3,1,3,7,755,32]

insertion_sort(l)
print(l)

