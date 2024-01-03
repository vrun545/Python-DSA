def partition(arr, low, high):
    pi = low
    i, j = low, high

    while i < j:

        while i < high and arr[i] <= arr[pi]:
            i += 1
        
        while j > 0 and arr[j] > arr[pi]:
            j -= 1

        # if collision happens then perform swap operation
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[pi], arr[j] = arr[j], arr[pi]

    # returning pivot element's correct position in array
    return j

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)

if __name__ == "__main__":
    arr = [3,2,1,5,4,9,7,8,6]
    print("Before Sorting = ", arr)
    quicksort(arr, 0, len(arr)-1)
    print("After Sorting = ", arr)
