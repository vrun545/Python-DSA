l1 = list(map(int , input().split()))
l2 = list(map(int , input().split()))
n1 = len(l1)
n2 = len(l2)
i, j = 0, 0
l3 = []

while(i < n1 and j < n2):
    if l1[i]<l2[j]:
        l3.append(l1[i])
        i += 1
    else:
        l3.append(l2[j])
        j += 1

while i<n1:
    l3.append(l1[i])
    i += 1
    
while j<n2:
    l3.append(l2[j])
    j += 1

print(l3)