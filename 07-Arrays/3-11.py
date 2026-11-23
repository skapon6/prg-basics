def bubblesort(array):
    for i in range(len(array)):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            
    return array
print(bubblesort([4,5,2,9,1]))