# Function to swap two characters in a character array
def swap(ch, i, j):
    temp = ch[i]
    ch[i] = ch[j]
    ch[j] = temp
 
# Recursive function to generate all permutations of a string
def permutations(ch, curr_index=0):
    if curr_index == len(ch) - 1:
        l1.append(''.join(ch))
        return

    for i in range(curr_index, len(ch)):
        # including characters
        swap(ch, curr_index, i)
        # recursive relation
        permutations(ch, curr_index + 1)
        # backtracking
        swap(ch, curr_index, i)
    return l1
 

if __name__ == '__main__':
    l1 = []
    s = 'ABC'
    l1 = permutations(list(s))
    print(l1)