def solve(arr, index, sum1, target, ans, output):
    # Base Case
    if index == len(arr):
        if sum1 == target:
            ans.append(output[:])
        return
        
    # Exclude 
    solve(arr, index+1, sum1, target, ans, output)
    # Include
    sum1 += arr[index]
    output.append(arr[index])
    solve(arr, index+1, sum1, target, ans, output)
    sum1 -= arr[index]
    output.pop()

def subsequences(arr, target, ans):
    output = []
    index = 0
    sum1 = 0
    solve(arr, index, sum1, target, ans, output)

if __name__ == "__main__":
    arr = [3,2,4,5,1,6]
    target = 6
    ans = []
    subsequences(arr, target, ans)
    print(f"All Subsequences whose sum equal to {target} are: ", ans)