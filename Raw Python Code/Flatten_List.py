
# FLATTEN LIST
###################################################################################
l2=[]
def listing(l1):
    for i in l1:
        if type(i)==list:
            listing(i)
        else:
            l2.append(i)

l1 = [1,2,3,[4,5,[[6,[16,[17,[18]]],7]]],[[[[8]]],9,[]],[[10,11],[12]],[13,14],[15]]
listing(l1)
print(sorted(l2))