# MAJORITY ELEMENT

def majorityElement(self, A, N):
        #Your code here
        d = {}
        for i in A:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        max1 = N//2
        for i in d:
            if d[i] > max1:
                max1 = i 
                break
        return max1