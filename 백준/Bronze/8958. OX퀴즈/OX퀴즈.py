N = int(input())

for _ in range(N):
    arr = input()
    sum = 0
    temp = 0
    for i in range(len(arr)):
        if arr[i] == 'O':
            temp += 1
            sum += temp
        elif arr[i] == 'X':
            temp = 0 

    print(sum)

