arr = []
for _ in range(9):
    temp = list(map(int,input().split()))
    arr.append(temp)

a = arr[0][0]
i = 1
j = 1

for m in range(9):
    for n in range(9):
        t = arr[m][n]
        if t > a :
            a = t
            i = m + 1
            j = n + 1

print(a)
print(i, j)