
dict1 = {1:200, 2:400, 3:600, 6:100, 5:700, 6:400, 7:50}

l1 = dict(sorted(dict1.items(), key = lambda item : item[0], reverse=True))
print(l1)