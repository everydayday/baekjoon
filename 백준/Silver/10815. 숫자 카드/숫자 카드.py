
N = int(input())
arr1 = list(map(int,input().split()))
dct = {}
for a in arr1:
    dct[a] = 1

M = int(input())
arr2 = list(map(int,input().split()))
for b in arr2:
    try :
        if dct[b] == 1 :
            print(1 , end = " ")
    except :
        print(0, end = " ")