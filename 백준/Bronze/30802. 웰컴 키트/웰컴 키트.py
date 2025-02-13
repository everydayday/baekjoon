N = int(input())
arr = list(map(int,input().split()))
T, P = map(int,(input().split()))

Tans = 0
for i in range(len(arr)):
    if arr[i] == 0 :
        pass
    if arr[i] % T == 0 :
        Tans += arr[i] // T
    else :
        Tans += arr[i] // T + 1

Psum = sum(arr)
Pans0 = Psum // P
Pans1 = Psum % P

print(Tans)
print(Pans0,Pans1)


