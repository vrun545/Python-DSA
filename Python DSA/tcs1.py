# def fact(n):
#     res = 1
#     l1 = [1]
#     for i in range(2,n+1):
#         res *= i
#     return res

# n = int(input())
# ans = ((n)*(fact(n-1))) - (n-1)*(n-1)
# print(ans)
# from math import factorial

# n = int(input())

# def numberOfWays(n):

#    finalRes = (factorial(n) - ((n-1)**2))
#    return finalRes



n = int(input())
num = input().split(" ")[0]
num = int(num)
forces = list(map(int, input().split(' ')))

def solve(forces, num, i):
	if i == len(forces) or num<0: 
		return False
	if num == 0:
		return True
	return solve(forces, num, i+1) or solve(forces, num-forces[i], i+1)

def numberOfWays(num, forces):
	if solve(forces, num, 0):
		print("Possible")
	else: 
		print("Not Possible")
	for i in range(num):
		return
numberOfWays(num, forces)