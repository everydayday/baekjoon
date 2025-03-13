N = int(input())
flag = False
for i in range(N):
    sum = 0
    n = i
    while(n != 0):
        sum += n % 10
        n = n // 10
    sum += i
    if sum == N :
        flag = True
        print(i); break
    
if not flag :
    print(0)
