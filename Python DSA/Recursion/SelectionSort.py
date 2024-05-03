# SELECTION SORT RECURSIVE APPROACH
def selection_sort(l1,n):
    # Base Case
    if n==0 or n == 1:
        return 

    # Processing
    max1 = float("-inf")
    max_index = -1
    for i in range(n):
        if max1 < l1[i]:
            max1 = l1[i]
            max_index = i
    if max_index != -1:
        l1[n-1], l1[max_index] = l1[max_index], l1[n-1]

    # Recursive Relation
    selection_sort(l1,n-1)

if __name__ == "__main__":
    l1 = [4,3,2,1,74,321,4,325,5233,3423]
    selection_sort(l1,len(l1))
    print(l1)
