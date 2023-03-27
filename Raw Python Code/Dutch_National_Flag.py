
# DUTCH NATIONAL FLAG ALGORITHM

def sortArr(arr, n):
    beg, mid, end = 0, 0, n-1
    while mid <= end:
        if arr[mid] == 0:
            arr[beg], arr[mid] = arr[mid], arr[beg]
            beg += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[end] = arr[end], arr[mid]
            end -= 1

# DRIVER PROGRAM    
if __name__ == "__main__":
    arr = [1, 0, 1, 0, 1, 2, 2, 1, 1, 0, 1, 2, 2, 1, 0, 1, 2, 0, 0, 0, 1]
    n = len(arr)
    sortArr(arr, n)
    print(arr)