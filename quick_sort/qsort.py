def exchange(array, i, j):
    temp = array[i-1]
    array[i-1] = array[j-1]
    array[j-1] = temp
    
def partition(array, begin, end):
    x = array[end-1]
    middle = begin - 1
    for i in range(begin, end):
        if array[i-1] <= x:
            middle = middle + 1
            exchange(array, i, middle)
    exchange(array, middle+1, end)
    return middle+1

def quick_sort(array, begin, end):
    if begin < end:
        middle = partition(array, begin, end)
        quick_sort(array, begin, middle-1)
        quick_sort(array, middle+1, end)


