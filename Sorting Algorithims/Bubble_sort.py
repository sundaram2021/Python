def bubble_sort(Lists):
    n = len(Lists)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if Lists[j] > Lists[j + 1]:
                swapped = True
                Lists[j], Lists[j + 1] = Lists[j + 1], Lists[j]
         
        if not swapped:
            return

array = []
array_length = int(
    input("Enter the number of elements of array or enter the length of array : ")
)
for i in range(array_length):
    value = int(input("Enter the value in the array : "))
    array.append(value)

bubble_sort(array)
print(array)
