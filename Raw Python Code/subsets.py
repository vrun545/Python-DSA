def solve(arr, index, output, ans):
    # Base Case
    if index >= len(arr):
        ans.append(output[:])
        return

    # include
    element = arr[index]
    output.append(element)
    solve(arr, index+1, output, ans)
    output.pop()

    # exclude
    solve(arr, index+1, output, ans)

def subsets(arr, n):
    output = []
    ans = []
    index = 0
    solve(arr, index, output, ans)
    return ans

if __name__ == "__main__":
    arr = [1, 2, 3]
    power_set = []
    power_set = subsets(arr, len(arr))
    print(power_set)

