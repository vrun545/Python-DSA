# BUBBLE SORT RECURSIVE APPROACH
def bubble_sort(l1,n):
    if n==0 or n==1:
        return
    
    for i in range(n-1):
        if l1[i] > l1[i+1]:
            l1[i], l1[i+1] = l1[i+1], l1[i]
    
    bubble_sort(l1,n-1)

if __name__ == "__main__":
    l1 = [1,0,6,4,3,7,9,2,5,8]
    bubble_sort(l1,len(l1))
    print(l1)