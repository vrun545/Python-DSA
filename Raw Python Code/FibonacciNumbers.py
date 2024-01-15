def fibonacci(num):
    global fibo, count
    if (num <= len(fibo)-1):
        return fibo[num]
    else:
        fibo.append(fibonacci(num-1)+fibonacci(num-2))
        return fibo[num]   
fibo = []
fibo.append(0)
fibo.append(1)
count = 1
n = 6
print(n,"th fibonacci number:",fibonacci(n))