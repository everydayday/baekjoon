import math

T = int(input())

for _ in range(T):
    H,W,N = map(int,input().split())
    # 층
    floor = N % H 
    # 끝에 층 예외 처리
    if floor == 0:
        floor = H
    # 호수    
    room = math.ceil(N / H)

    if room < 10:
        room = '0' + str(room)

    print(str(floor) + str(room))
