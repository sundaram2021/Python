# Selection sort in Python
# time complexity O(n*n)
#sorting by finding min_index
def selectionSort(array, size):
    
    for i in range(size):
        min_index = i
 
        for j in range(i + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (array[i], array[min_index]) = (array[min_index], array[i])
 
arr = [-4, 23, 0, 10, -19,99,-12,-2,77]
size = len(arr)
selectionSort(arr, size)
print('The array after selection sort is: ')
print(arr)
