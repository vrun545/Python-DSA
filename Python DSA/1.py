s = "tERxtbok"
mid = len(s)//2
vowels = ['a','e','i','o','u']
l1 = list(s[0:mid].lower())
l2 = list(s[mid:].lower())
d1, d2  = {}, {}
for i in range(len(l1)):
    if l1[i] in vowels and l1[i] not in d1:
        d1[l1[i]] = 1
    elif l1[i] in vowels and l1[i] in d1:
        d1[l1[i]] += 1
for i in range(len(l2)):
    if l2[i] in vowels and l2[i] not in d2:
        d2[l2[i]] = 1
    elif l2[i] in vowels and l2[i] in d2:
        d2[l2[i]] += 1
        
result = sorted(d1.items()) == sorted(d2.items())
print(result)
