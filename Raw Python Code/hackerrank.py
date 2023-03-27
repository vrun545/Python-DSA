# k = 1
# arr = [4, 2, 3, 5, 1]
# def largestPermutation(k, arr):
#     maximum_element = max(arr)
#     maximum_arr = arr[1:]
#     temp_maximum_element = max(maximum_arr)
#     print(temp_maximum_element)
#     idx = arr.index(maximum_element)
#     arr[idx], arr[0] = arr[0], arr[idx]
#     if k <=1: return arr
#     i = 1
#     while i<k:
#         temp_maximum_element = max(arr[1:])
#         idx = arr.index(temp_maximum_element)
#         arr[idx], arr[i] = arr[i], arr[idx]
#         i += 1
#     return arr
# print(largestPermutation(k,arr))

t = int(input())

def consecutive_subsequence(n, k, arr):
    count = 0
    sumation = 0
    sum_temp = []
    sub_temp = []
    
    for i in range(n):
        sumation += arr[i]
        sum_temp.append(sumation)
    
    for i in range(len(sum_temp)-1):
        diff = abs(sum_temp[i+1]-sum_temp[i])
        sub_temp.append(diff)

    print(arr)
    print(sum_temp)
    print(sub_temp)

    for i in range(n):
        if arr[i] % k == 0: count+=1
    for i in range(len(sum_temp)):
        if sum_temp[i] % k == 0: count+=1
    for i in range(len(sub_temp)):
        if sub_temp[i] % k == 0: count+=1
    
    return count

for i in range(t):
    n,k = map(int, input().split(' '))
    arr = list(map(int, input().split(' ')))
    num = consecutive_subsequence(n, k, arr)
    print(num, end = " ")


