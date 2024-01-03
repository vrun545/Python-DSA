def count_str(strings):
    cnt = 0
    for i in range(len(strings)):
        for j in range(len(strings[i])):
            if not(((strings[i][j] >= 'a' and strings[i][j] <='z') or (strings[i][j] >= 'A' and strings[i][j] <= 'Z'))):
                cnt += 1
                break
    return cnt


if __name__ == "__main__":
    t = int(input())
    l1 = []
    while t > 0:
        string = input()
        l1.append(string)
        t -= 1
    print(l1)
    answer = count_str(l1)
    print("Total Invalid Strings = ", answer)
    print("Total Valid Strings = ", (len(l1)-answer))