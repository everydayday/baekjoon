N = input()
n = 0
arr = map(int,input().split())
for a in arr:
    flag = True
    if a == 1:
        flag = False
    for i in range(2,a):
        if a % i == 0 :
            flag = False
    if flag == True:
        n += 1
print(n)