# PERMUTATIONS OF LISTS OF NUMBERS

def permute(arr, index, ans):
    # Base Case
    if index >= len(arr):
        ans.append(arr[:])
        return 
    
    # Proceesing
    for i in range(index, len(arr)):
        arr[i], arr[index] = arr[index], arr[i]
        permute(arr, index+1, ans)
        arr[i], arr[index] = arr[index], arr[i]


if __name__ == "__main__":
    arr = [1,2,3]
    index = 0
    ans = []
    permute(arr, index, ans)
    print(ans)