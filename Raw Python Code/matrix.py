# words = ["Hello","Alaska","Dad","Peace"]
# r1 = set("qwertyuiop")
# r2 = set("asdfghjkl")
# r3 = set("zxcvbnm")
# res, cnt1, cnt2, cnt3 = [], 0, 0, 0
# for i in range(len(words)):
#     print(set(words[i].lower()))
#     if (set(words[i].lower()) in r3):
#         res.append(words[i])
# print(res)
# i = "jdsoijs"
# print(i.startswith("l"))    

# Output: ["Alaska","Dad"]

# string_number = "0000"

# try:
#     integer_number = int(string_number)
#     print(integer_number)
# except ValueError:
#     print("Conversion to integer failed. The string contains non-numeric characters.")

l1 = [1,2,3,4,5]
l2 = l1.copy()
l2.pop()
print(l1,l2,end='\n')