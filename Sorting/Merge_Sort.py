def mergesort(arr, low, high):
    if low < high:
        mid = ( low + high ) // 2
        mergesort(arr, low, mid)
        mergesort(arr, mid+1, high)
        merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    i, j, k = low, mid+1, low
    arr2 = [0 for _ in range(len(arr))]

    while i <= mid and j <= high:

        if arr[i] <= arr[j]:
            arr2[k] = arr[i]
            i += 1
            k += 1
        else:
            arr2[k] = arr[j]
            j += 1
            k += 1

    if i > mid:
        while j <= high:
            arr2[k] = arr[j]
            j += 1
            k += 1
    else:
        while i <= mid:
            arr2[k] = arr[i]
            i += 1
            k += 1

    for p in range(low, high+1):
        arr[p] = arr2[p]
       

if __name__ == "__main__":
    arr = [3,2,7,6,9,1,5,4,10,8]
    print("Before Sorting = ", arr)
    mergesort(arr, 0, len(arr)-1)
    print("After Sorting = ", arr)
