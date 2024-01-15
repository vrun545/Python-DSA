def reverseString(str1, i, j):
    if i > j:
        return
    str1[i], str1[j] = str1[j], str1[i]
    reverseString(str1, i+1, j-1) 



if __name__ == "__main__":
    l1 = [1,2,3,4,5,6]
    l2 = [1,2,3,4,5]
    reverseString(l1, 0, len(l1)-1)
    reverseString(l2, 0, len(l2)-1)
    print(l1, l2, end="\n")