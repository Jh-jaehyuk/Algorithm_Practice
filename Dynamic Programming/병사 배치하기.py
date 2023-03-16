# 가장 긴 증가하는 부분 수열. (Longest Increasing Subsequence, LIS)
# D[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
# 모든 0 <= j < i 에 대하여, D[i] = max(D[i], D[j] + 1) if array[j] < array[i]

n = int(input())
array = list(map(int, input().split()))
# 순서를 뒤집어 '최장 증가 부분 수열' 문제로 변환
array.reverse()
# 1차원 DP 테이블 초기화
dp = [1] * n
# LIS 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)
# 열외해야 하는 병사의 최소 수를 출력
print(n - max(dp))
