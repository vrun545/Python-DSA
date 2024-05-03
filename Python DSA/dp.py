# # # import math
# # # def goodsplits(arr,n):
# # #     dp = [0]*len(n+1)
# # #     for i in range(n-1,-1,-1):
# # #         dp[i] = 1 + dp[i-1]
# # #         for j in range(i+1,n):
# # #             if math.gcd(arr[i],arr[j])>1:
# # #                 dp[i] = min(dp[i], 1+dp[j+1])
# # #     return dp[0]

# # # if __name__ == "__main__":
# # #     arr = [2,3,5,2,1,68,9,7]
# # #     n = len(arr)
# # #     result = goodsplits(arr,n)
# # #     print(result) 
# # # def discount(arr, n):
# # #     stack =[]
# # #     nser = []

# # #     return result


# # # if __name__ == "__main__":
# # #     arr = [2,3,1,2,4,2]
# # #     n = len(arr)
# # #     result = discount(arr,n)
# # #     print(result)
# # from heapq import *
# # arr = [5,2,3,7,1]
# # heapify(arr)
# # arr.append(0)
# # heapify(arr)
# # print(arr)

# from typing import *
# def performOperations(a: List[int], n: int, k: int)-> List[int]:
# 	b = [0]*len(a)
# 	while k>0:
# 		max1 = max(a)
# 		for i in range(0,len(a)):
# 			b[i] = max1-a[i]
# 		a[:] = b[:]
# 		k -= 1
# 	return a

# if __name__ == "__main__":
#     n = 4,
#     a = [4,2,1,3] 
#     k = 2
#     performOperations(a,n,k)
#     print(a)

# 1 -7 0
# 2 3 -3 1
a = [2,9,-7,1,4,7]
b = []
cnt = 0
c = []
if len(a)<=1:
	print(0)
for i in range(0,len(a)-1,2):
	b.append(a[i]+a[i+1])
	cnt += 1
print(b)
c = b[::-1]
if b[:]==c[:]:
	 print(cnt)
else:
	print(0) 