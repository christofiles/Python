c = 65
n = int(input("Enter number of rows : "))
for i in range (n):
    for j in range(i+1):
        print(chr(c),end = '')
    c = c+1
    print('\n')