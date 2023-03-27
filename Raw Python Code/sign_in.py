l1 = ["12 30 sign-in","30 58 sign-out","12 38 sign-out","67 90 sign-in","67 100 sign-out"]
max_span = 20
l3 = []
dict1 = {}
for i in l1:
    l2 = []
    j=0
    l2 = l1[j].split(" ")
    dict1[l2[j]] = l2[j+1]
    if(l2[j+2]=="sing-in"):
        dict1[j][j+1] += 1
    else:
        dict1[j][j+1] -= 1
    j+=1
for i in dict1:
    if(dict[i]==0 and max_span<=20):
        l3.append(dict1.key(i))
print(l3.sorted())



operatiosn = ["push 3","pop","push 10","push 8","push 2","pop","inc 2 3","pop","push 15","inc 3 1","push 1"]



# def smart_divide(func):
    # def inner(a,b):
        # print("I am going to divide",a,"and",b)
        # if b == a:
            # print("Whoops!! Can't divide")
