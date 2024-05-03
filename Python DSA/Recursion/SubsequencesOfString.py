def solve(l1, index, output, ans):
    if index >= len(l1):
        ans.append(output[:])
        return

    # include
    output.append(l1[index])
    solve(l1, index+1, output, ans)
    output.pop()
    
    # Exclude
    solve(l1, index+1, output, ans)

def subsequence(l1, ans):
    index = 0
    output = []
    solve(l1, index, output,  ans)
    return ans

if __name__ == "__main__":
    str1 = "abc"
    l1 = list(str1)
    ans = []
    subsequence(l1, ans)
    print("All subsequences are: ", sorted(ans))