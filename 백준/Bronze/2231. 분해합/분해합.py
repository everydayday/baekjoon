N = int(input())

for i in range(max(0,N - len(str(N)) * 9), N):  # 최소 탐색 범위 설정
    if sum(map(int, str(i))) + i == N:  # 생성자 판별
        print(i)
        break  # 생성자 찾았으면 반복 종료
else:
    print(0)  # 생성자가 없을 경우 출력
