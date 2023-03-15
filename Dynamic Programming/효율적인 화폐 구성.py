# 정수 N, M을 입력받기
n, m = map(int, input().split())
# N개의 화폐 단위 정보를 입력받기
array = []
for i in range(n):
    array.append(int(input()))

# DP 테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍 진행(보텀업)
d[0] = 0
for i in range(n): # 각각의 화폐 단위
    for j in range(array[i], m + 1): # 각각의 금액
        # (i - k)원을 만드는 방법이 존재하는 경우
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)

# 최종적으로 M원을 만드는 방법이 없는 경우
if d[m] == 10001:
    print(-1)
else:
    print(d[m])
