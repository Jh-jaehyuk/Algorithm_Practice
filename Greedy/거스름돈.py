def solution(n): # 시간복잡도는 총 금액과 관계없이 동전 종류에 영향을 받음.
    answer = 0
    coins = [500, 100, 50, 10]

    for coin in coins:
        answer += n // coin
        n %= coin
    return answer

print(solution(1260))
