
file = open('lines.txt', 'r')
lines = file.readlines()
file.close()

print(lines[2], lines[-1])

file = open('lines.txt', 'a')
file.write("\nHey !!\n there what's going on \n welcome")
file.close()

file = open("lines.txt", "r")
print(file.read())
file.close()